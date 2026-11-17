# -*- coding: utf-8 -*-
"""鸦语离线转换器
================
用途：机密台词（不能以明文出现在工程里的线索）在这里转换，
只把输出的两行代码贴进剧本；明文仅保留在你自己的笔记里。

用法：
    python crow_encoder.py "格式塔已发现露西亚的意识海波动，大约七天后会解析完毕。"
    python crow_encoder.py --decode "西瓜茶壶雨伞把茶壶马桶如果肥皂月亮打火机的"
    python crow_encoder.py --test        # 自检（编码可逆性验证）

注意：4 位 16 进制是 **Unicode 码位**，不是 UTF-8 字节。多数在线"hex to text"
转换器会把 5979 当成两个字节读成 "Yy"，那是错的——正确读法是 U+5979 = 她。

⚠️ 本文件的表和参数必须与 game/scripts/systems/crow_speech.rpy 保持一致。
   改任何一边，另一边同步改。
"""
import sys
import zlib
import random

CROW_TABLE = {
    u'0': u'月亮', u'1': u'番茄', u'2': u'拖把', u'3': u'袜子',
    u'4': u'马桶', u'5': u'西瓜', u'6': u'枕头', u'7': u'雨伞',
    u'8': u'牙刷', u'9': u'茶壶', u'A': u'电钻', u'B': u'烤箱',
    u'C': u'剪刀', u'D': u'打火机', u'E': u'肥皂', u'F': u'蘑菇',
}
CROW_NOISE_MID = [u'的', u'了', u'是', u'在', u'就', u'和', u'被',
                  u'把', u'之', u'其', u'但是', u'所以', u'而且', u'如果']
CROW_NOISE_END = [u'吧', u'吗', u'呢', u'啊', u'哦', u'嘛']
CROW_PUNCT_POOL = ([u'，'] * 6 + [u'。'] * 3 + [u'？', u'！', u'……', u'、'])
CROW_SENT_END = (u'。', u'？', u'！', u'……')

CROW_PAYLOAD_COLOR = u'#e74c3c'
CROW_P_MID_NOISE = 0.22
CROW_P_END_PARTICLE = 0.35
CROW_BREAK_MIN = 4
CROW_BREAK_MAX = 9
CROW_FOLD_MIN_SENT = 6
CROW_FOLD_HARD = 10


def crow_escape(s):
    return s.replace(u'{', u'{{').replace(u'[', u'[[')


def crow_units(text):
    rng = random.Random(zlib.crc32(text.encode('utf-8')) & 0xffffffff)
    units = []
    state = {'since': 0, 'threshold': rng.randint(CROW_BREAK_MIN, CROW_BREAK_MAX)}

    def brk(mark):
        if units and units[-1][1] == 'X':
            return
        if mark in CROW_SENT_END and rng.random() < CROW_P_END_PARTICLE:
            units.append((rng.choice(CROW_NOISE_END), 'N'))
        units.append((mark, 'X'))
        state['since'] = 0
        state['threshold'] = rng.randint(CROW_BREAK_MIN, CROW_BREAK_MAX)

    n = len(text)
    for i, ch in enumerate(text):
        cp = ord(ch)
        nibs = None
        if 0x4E00 <= cp <= 0x9FFF:
            nibs = format(cp, '04X')
        elif cp < 128 and ch.isalnum():
            nibs = format(cp, '02X')
        if nibs:
            for d in nibs:
                units.append((CROW_TABLE[d], 'P'))
                state['since'] += 1
                if rng.random() < CROW_P_MID_NOISE:
                    units.append((rng.choice(CROW_NOISE_MID), 'N'))
                if state['since'] >= state['threshold']:
                    brk(rng.choice(CROW_PUNCT_POOL))
        else:
            if i == n - 1:
                units.append((crow_escape(ch), 'X'))
            else:
                brk(crow_escape(ch))
    return units


def crow_render(units):
    out = []
    for t, k in units:
        if k == 'P':
            out.append(u'{color=%s}%s{/color}' % (CROW_PAYLOAD_COLOR, t))
        else:
            out.append(t)
    return u''.join(out)


def crow_fold_cut(units):
    pc = 0
    for i, (t, k) in enumerate(units):
        if k == 'P':
            pc += 1
        if k == 'X':
            if t in CROW_SENT_END and pc >= CROW_FOLD_MIN_SENT:
                return i + 1
            if pc >= CROW_FOLD_HARD:
                return i + 1
    return len(units)


def crow_hex(text):
    parts = []
    for ch in text:
        cp = ord(ch)
        if 0x4E00 <= cp <= 0x9FFF:
            parts.append(format(cp, '04X'))
        elif cp < 128 and ch.isalnum():
            parts.append(format(cp, '02X'))
        else:
            parts.append(crow_escape(ch))
    return u' '.join(parts)


def crow_encode_line(text):
    units = crow_units(text)
    total = sum(1 for _t, k in units if k == 'P')
    full = crow_render(units)
    cut = crow_fold_cut(units)
    if cut >= len(units):
        disp = full
    else:
        head = crow_render(units[:cut])
        while head and head[-1] in u'，。？！、…':
            head = head[:-1]
        disp = head + (u'——【传输已收录 · 全文%d词】' % total)
    return disp, full, crow_hex(text), total


def _q(s):
    """转成可贴进 Ren'Py 双引号字符串的形式"""
    return s.replace(u'\\', u'\\\\').replace(u'"', u'\\"')


def emit(text):
    disp, full, hexline, total = crow_encode_line(text)
    key = zlib.crc32(text.encode('utf-8')) & 0xffffffff
    print(u'# ---- 以下两行贴进剧本（明文别贴！）----')
    print(u'    $ crow_archive_raw(%d, "%s", "%s", %d)' % (key, _q(full), _q(hexline), total))
    print(u'    raven_x "%s"' % _q(disp))
    print(u'')
    print(u'# 预览（档案全文）：')
    print(u'#   %s' % full)


def decode(text):
    """鸦语 -> 明文。自动忽略虚码与标点，按每 4 词 = 1 字分组。
    输入可以是档案全文、台词框截取，甚至带 {color} 标签的原串。"""
    inv = {v: k for k, v in CROW_TABLE.items()}
    # 先按词长倒序，保证"打火机"不会被误切成"打"+"火机"
    words = sorted(inv.keys(), key=len, reverse=True)
    digits = []
    i = 0
    while i < len(text):
        for w in words:
            if text.startswith(w, i):
                digits.append(inv[w])
                i += len(w)
                break
        else:
            i += 1          # 虚码、标点、标签一律跳过
    out = []
    leftover = len(digits) % 4
    for j in range(0, len(digits) - leftover, 4):
        h = u''.join(digits[j:j + 4])
        cp = int(h, 16)
        out.append((h, chr(cp)))
    return out, leftover


def show_decode(text):
    pairs, leftover = decode(text)
    print(u'识别到 %d 个字：' % len(pairs))
    print(u'')
    print(u'  ' + u'  '.join(u'%s=%s' % (h, c) for h, c in pairs))
    print(u'')
    print(u'明文：%s' % u''.join(c for _h, c in pairs))
    if leftover:
        print(u'')
        print(u'⚠ 末尾剩 %d 个词凑不满 4 位——可能是截取不完整，或原文含非汉字字符。' % leftover)


def self_test():
    """可逆性自检：密文词序列还原出的16进制必须等于原文编码"""
    inv = {v: k for k, v in CROW_TABLE.items()}
    cases = [
        u'格式塔已发现露西亚的意识海波动，大约七天后会解析完毕。',
        u'好。',
        u'坐标X7，重复，X7。',
        u'Laurel-II在听吗？',
    ]
    for text in cases:
        units = crow_units(text)
        decoded = u''.join(inv[t] for t, k in units if k == 'P')
        expected = u''
        for ch in text:
            cp = ord(ch)
            if 0x4E00 <= cp <= 0x9FFF:
                expected += format(cp, '04X')
            elif cp < 128 and ch.isalnum():
                expected += format(cp, '02X')
        assert decoded == expected, u'FAIL: %s' % text
        disp, full, hexline, total = crow_encode_line(text)
        print(u'PASS %3d词  %s' % (total, text))
        print(u'  台词框: %s' % disp)
    print(u'全部通过。')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    args = sys.argv[1:]
    if not args:
        print(__doc__)
    elif args[0] == '--test':
        self_test()
    elif args[0] in ('--decode', '-d'):
        for t in args[1:]:
            show_decode(t)
    else:
        for t in args:
            emit(t)
