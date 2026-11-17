## ============================================================================
## 鸦语加密系统
## ============================================================================
## 鸦羽的台词在"显示时"自动编码为鸦语：
##   - 剧本里照常写明文：raven "格式塔已发现……"
##   - 台词框只显示第一个伪句 + 【传输已收录】标记
##   - 完整密文自动进"传输记录"档案（工作室界面右上角按钮）
##   - Laurel-II 的 HEX 台词与鸦语是同一串数据的两种读法
##
## 完整规则、参数说明、玩家侧解码链见 _doc/鸦语加密规范.md
## ⚠️ 表和参数若修改，必须同步 tools/crow_encoder.py（离线转换器）
## ============================================================================

init -5 python:
    import zlib
    import random as _crow_random

    ## ---- 16词表：一个词 = 一位16进制 ----
    CROW_TABLE = {
        u'0': u'月亮', u'1': u'番茄', u'2': u'拖把', u'3': u'袜子',
        u'4': u'马桶', u'5': u'西瓜', u'6': u'枕头', u'7': u'雨伞',
        u'8': u'牙刷', u'9': u'茶壶', u'A': u'电钻', u'B': u'烤箱',
        u'C': u'剪刀', u'D': u'打火机', u'E': u'肥皂', u'F': u'蘑菇',
    }

    ## ---- 虚码层：伪语法词与假标点，纯装饰，不参与解码 ----
    ## 词表不得与 CROW_TABLE 的 16 个词重叠
    CROW_NOISE_MID = [u'的', u'了', u'是', u'在', u'就', u'和', u'被',
                      u'把', u'之', u'其', u'但是', u'所以', u'而且', u'如果']
    CROW_NOISE_END = [u'吧', u'吗', u'呢', u'啊', u'哦', u'嘛']
    CROW_PUNCT_POOL = ([u'，'] * 6 + [u'。'] * 3 +
                       [u'？', u'！', u'……', u'、'])
    CROW_SENT_END = (u'。', u'？', u'！', u'……')

    ## ---- 可调参数 ----
    CROW_PAYLOAD_COLOR = u'#e74c3c'   # 密文标红色
    CROW_P_MID_NOISE = 0.22           # 每个密文词后插伪语法词的概率
    CROW_P_END_PARTICLE = 0.35        # 假句号/问号前带"吧/吗/呢"的概率
    CROW_BREAK_MIN = 4                # 每 4~9 个密文词落一个假标点
    CROW_BREAK_MAX = 9
    CROW_FOLD_MIN_SENT = 6            # 折叠：够 6 词后遇句末标点即切
    CROW_FOLD_HARD = 10               # 折叠：超 10 词后遇任意标点即切

    def crow_escape(s):
        """转义 Ren'Py 文本特殊字符（透传的原文标点可能含 { 和 [）"""
        return s.replace(u'{', u'{{').replace(u'[', u'[[')

    def crow_units(text):
        """明文 -> [(词, 类型)]。类型：P=密文 N=虚码词 X=标点。
        随机种子取自明文本身，同一句话永远生成同一串。"""
        rng = _crow_random.Random(zlib.crc32(text.encode('utf-8')) & 0xffffffff)
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
            if 0x4E00 <= cp <= 0x9FFF:          # 汉字：UTF-16 码位 -> 4 词
                nibs = format(cp, '04X')
            elif cp < 128 and ch.isalnum():     # 英文/数字：1 字节 -> 2 词
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
                ## 原文标点：句尾原样保留，句中强制落一次断句（节奏呼应原句）
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
        """返回折叠切点：第一个伪句结束的位置"""
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
        """Laurel-II 层：同一句话的原始 HEX（不掺虚码）"""
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
        """返回 (台词框显示串, 档案全文, HEX串, 密文词数)"""
        units = crow_units(text)
        total = sum(1 for _t, k in units if k == 'P')
        full = crow_render(units)
        cut = crow_fold_cut(units)
        if cut >= len(units):
            disp = full   # 短句完整显示，不加标记
        else:
            head = crow_render(units[:cut])
            while head and head[-1] in u'，。？！、…':
                head = head[:-1]
            disp = head + (u'——【传输已收录 · 全文%d词】' % total)
        return disp, full, crow_hex(text), total

    def crow_archive_add(key, full, hexline, count):
        """收录进传输记录（按明文哈希去重，同一句只收一次）"""
        if persistent.crow_log is None:
            persistent.crow_log = []
        for e in persistent.crow_log:
            if e[0] == key:
                return
        persistent.crow_log.append((key, full, hexline, count))

    def crow_archive_raw(key, full, hexline, count):
        """离线转换器输出专用：预加密台词的档案收录（明文不进工程）"""
        crow_archive_add(key, full, hexline, count)

    class CrowSpeaker(object):
        """鸦羽的说话封装：明文进，鸦语出，档案自动收录。
        限制：不支持 raven happy "..." 这种带表情后缀的说法，
        需要换表情时先写 show raven happy 再单独一行对话。"""
        def __init__(self, base):
            self.base = base

        def __call__(self, what, *args, **kwargs):
            disp, full, hexline, count = crow_encode_line(what)
            key = zlib.crc32(what.encode('utf-8')) & 0xffffffff
            crow_archive_add(key, full, hexline, count)
            return self.base(disp, *args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.base, name)


## 传输记录跨存档保留（类似画廊）
default persistent.crow_log = []

## raven：日常用，明文自动加密
## raven_x：机密线索用，直接贴离线转换器生成的密文（明文不出现在工程里）
define raven = CrowSpeaker(raven_base)
define raven_x = Character(kind=raven_base)


## ============================================================================
## 传输记录界面
## ============================================================================
screen crow_log_screen():
    modal True
    zorder 120
    default show_hex = False

    add "#000c"

    frame:
        align (0.5, 0.5)
        xsize 1500
        ysize 900
        background "#1a1a22"
        padding (40, 40)

        vbox:
            spacing 20

            hbox:
                xfill True
                text "传输记录" size 44 color "#fff"
                textbutton ("视图：原始HEX" if show_hex else "视图：鸦语"):
                    xalign 1.0
                    action ToggleScreenVariable("show_hex")
                    text_size 26
                    text_color "#f4e4c1"
                    text_hover_color "#fff"

            null height 6

            viewport:
                xfill True
                ysize 700
                scrollbars "vertical"
                mousewheel True

                vbox:
                    spacing 24
                    if persistent.crow_log:
                        for idx, entry in enumerate(persistent.crow_log):
                            vbox:
                                spacing 6
                                text ("传输 #%02d · %d 词" % (idx + 1, entry[3])) size 24 color "#88aabb"
                                if show_hex:
                                    text entry[2] size 24 color "#9fd4a0"
                                else:
                                    text entry[1] size 26 color "#cccccc"
                    else:
                        text "（尚无记录）" size 28 color "#888" xalign 0.5

    textbutton "关闭":
        align (0.5, 0.95)
        xsize 200
        ysize 60
        text_size 36
        action Hide("crow_log_screen")
