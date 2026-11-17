## 剧情对话 UI：1920×1080，复用项目字体和 textbox 渐变。
## 比角色定义提前初始化，让现有 Character 自动继承继续提示。
init offset = -1

define adv = Character(kind=adv,
    who_style="story_say_label", what_style="story_say_dialogue",
    window_style="story_say_window",
    ctc="story_next_ready", ctc_position="screen-variable")
define name_only = Character(kind=name_only,
    who_style="story_say_label", what_style="story_say_dialogue",
    window_style="story_say_window",
    ctc="story_next_ready", ctc_position="screen-variable")

## 章节结束、解锁提示等 centered 台词独立显示，避免套用剧情装饰。
## 继承原 centered 的字体、居中与推进行为，无需逐句改剧情。
define character.centered = Character(kind=centered, screen="story_centered", ctc=None)

screen story_centered(who, what):
    text what id "what" style "centered_text"

## combined：三角 + NEXT；icon：只显示三角；text：只显示 NEXT。
define gui.story_next_mode = "combined"
define gui.story_left = 360
define gui.story_width = 1360
define gui.story_text_size = 36
define gui.story_line_color = "#ffffff55"

## 原 PNG 不做裁剪、重绘或重新压缩，保留上传时的透明通道。
image story_voice_wave = "images/ui/story_voice_wave.png"
image story_next_arrow = "images/ui/story_next_arrow.png"
image story_next_text = "images/ui/story_next_text.png"

image story_next_ready = ConditionSwitch(
    "gui.story_next_mode == 'icon'", Transform("story_next_arrow", zoom=0.65),
    "gui.story_next_mode == 'text'", Transform("story_next_text", zoom=0.65),
    "True", Composite((80, 68),
        (16, 0), Transform("story_next_arrow", zoom=0.65),
        (0, 38), Transform("story_next_text", zoom=0.65)))

transform story_next_pulse:
    alpha 0.65
    ease 0.85 alpha 1.0
    ease 0.85 alpha 0.65
    repeat

## 单独的样式避免改变输入框、NVL、历史记录或其他窗口。
style story_say_window is window:
    xalign 0.5
    xfill True
    yalign 1.0
    # 留出四行正文及底部原有快捷菜单的空间。
    ysize 320
    padding (0, 0)
    background Frame("gui/textbox.png", 0, 0)

style story_namebox is namebox:
    xpos 0
    ypos 0.5
    yanchor 0.5
    xanchor 0.0
    xsize None
    ysize None
    background None
    padding (0, 0)

style story_say_label is say_label:
    size 32

style story_say_dialogue is say_dialogue:
    xpos gui.story_left
    ypos 96
    xsize gui.story_width
    size gui.story_text_size
    line_spacing 10
    outlines [(1, "#00000080", 0, 1)]

## 小屏幕适当加宽文字区域；快捷菜单仍沿用项目原来的位置。
style story_say_window:
    variant "small"
    ysize 360

style story_namebox:
    variant "small"
    xpos 0

style story_say_dialogue:
    variant "small"
    xpos 135
    xsize 1650

## 在任意剧情中 call story_dialogue_preview，即可用当前背景预览。
label story_dialogue_preview:
    "时间一点一滴地流逝，母亲写完第一本婴幼儿成长日记的那天，露西亚也学会了呼唤她的名字。"
    sera "声纹、细线和对白区域已经接入。文字显示完后，右下角会出现继续提示。"
    system "系统对白仍然保留原来的绿色文字。"
    return
