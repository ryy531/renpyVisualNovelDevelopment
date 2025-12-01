# 定义鼠标点击时的波纹效果
transform click_ripple_effect(x, y):
    pos (x, y)
    anchor (0.5, 0.5)
    alpha 1.0 zoom 0.5
    linear 0.5 alpha 0.0 zoom 1.5

# Python 函数：播放特效但不阻止事件
init python:
    def trigger_feedback():
        # 1. 播放音效
        renpy.play("audio/click_test.WAV", channel="sound")
        
        # 2. 获取鼠标位置
        mx, my = renpy.get_mouse_pos()
        
        # 3. 显示特效屏幕
        renpy.show_screen("click_visual", x=mx, y=my)
        
        # 重要：返回 None，告诉 Ren'Py "我没处理完，请继续执行默认的翻页操作"
        return None

# 修正后的监听器
screen key_listener():
    # 使用 behavior 层的捕捉，或者简单的 imagebutton 覆盖全屏是另一种做法，
    # 但最直接的是利用 key "dismiss" 的穿透性。
    # 遗憾的是 Ren'Py 的 key 语句通常会吞掉事件。
    
    # 我们换个思路：不拦截 dismiss，而是利用 screen 的 event 处理。
    # 但为了简化，我们用一个透明的全屏按钮作为“点击层”。
    
    button:
        style "empty" # 空样式
        xfill True
        yfill True
        action [ Function(trigger_feedback), Return() ] 
        # 注意：Return() 会导致交互结束（相当于点了一下），这正是我们想要的“翻页”。

# 显示特效的临时屏幕 (保持不变)
screen click_visual(x, y):
    zorder 100 # 保证特效显示在最上层
    add "images/ui/click_effect.png" at click_ripple_effect(x, y)
    timer 0.6 action Hide("click_visual")