# 微弱电弧点击反馈；素材来源见 images/ui/click_electric/SOURCES.md。
image click_electric_arc:
    "images/ui/click_electric/spark_03.png"
    pause 0.045
    "images/ui/click_electric/spark_01.png"
    pause 0.045
    "images/ui/click_electric/spark_04.png"

transform click_electric_effect(x, y, angle):
    pos (x, y)
    anchor (0.5, 0.5)
    size (76, 76)
    rotate angle
    # 原素材为黑底白色电弧；加色混合让黑底透明，保留淡蓝电光。
    blend "add"
    matrixcolor TintMatrix("#9bcfff")
    alpha 0.38 zoom 0.85
    linear 0.045 alpha 0.28 zoom 0.95
    linear 0.045 alpha 0.34 zoom 1.0
    linear 0.12 alpha 0.0 zoom 1.05

default _click_feedback_serial = 0

init python:
    # 独立通道不打断剧情音效，仍跟随设置中的音效音量和静音。
    renpy.music.register_channel("click_feedback", mixer="sfx", loop=False)

    def trigger_feedback():
        global _click_feedback_serial
        _click_feedback_serial += 1
        # 原素材已压低峰值；提高约 9.8 dB，让扳机声在 BGM 下仍清晰。
        renpy.music.play("sfx/ui_trigger.ogg", channel="click_feedback",
                         loop=False, relative_volume=2.0)

        mx, my = renpy.get_mouse_pos()
        renpy.show_screen("click_visual", x=mx, y=my,
                          serial=_click_feedback_serial)
        return None

screen key_listener():
    # 只观察鼠标松开，同一次点击继续交给对话框和功能按钮处理。
    zorder 200
    key "mouseup_1" action Function(trigger_feedback) capture False

screen click_visual(x, y, serial=0):
    zorder 300
    # 新点击拥有新的子节点，动画与清理计时会一起重启。
    # 避免连续点击沿用旧动画，或被上一次点击的 timer 提前隐藏。
    for pulse index pulse in [serial]:
        add "click_electric_arc" at click_electric_effect(x, y, (pulse % 4) * 90)
        timer 0.22 action Hide("click_visual")
