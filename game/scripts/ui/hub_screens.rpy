# 1. 背景图定义
image workshop_bg_scaled = im.Scale("images/bg/bg_workshop.jpg", 1920, 1080)

# 三个物件轮廓图的定位区域，教学与悬停共用。
# SVG 路径沿背景中物件的外形描绘，由 tools/build_workshop_outlines.py 维护。
define workshop_regions = {
    "sortie": (493, 511, 302, 241),
    "repair": (459, 190, 267, 214),
    "diary": (20, 802, 280, 149),
}

init python:
    def workshop_outline(target):
        return "images/ui/workshop/{}_outline.svg".format(target)

# 2. 工作室主界面
screen workshop_screen(repair_event=False):
    tag menu 
    modal True
    add "workshop_bg_scaled"
    for target, caption, target_action, available in (
        ("sortie", "继续", Return("continue"), not repair_event),
        ("repair", "修复", Show("repair_window", story_repair=repair_event), repair_event or workshop_repair_available()),
    ):
        $ rx, ry, rw, rh = workshop_regions[target]
        button:
            pos (rx, ry)
            xysize (rw, rh)
            padding (0, 0)
            background None
            hover_background workshop_outline(target)
            # 填充遮罩仅用于命中判断，物件周围的空白不再触发高亮。
            focus_mask ("images/ui/workshop/{}_mask.svg".format(target))
            action target_action
            sensitive available
            tooltip caption

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            align (0.5, 0.1)
            size 60
            color "#fff"
            outlines [(2, "#000", 0, 0)]

    if repair_event:
        text "使用获得的零件，修复机体。":
            align (0.5, 0.88)
            size 32
            color "#fff"
            outlines [(2, "#000", 0, 0)]

    ## 传输记录入口：鸦羽说过话之后才出现（避免剧透）
    if persistent.crow_log and workshop_repair_available() and not repair_event:
        textbutton "传输记录":
            align (0.985, 0.03)
            action Show("crow_log_screen")
            text_size 32
            text_color "#f4e4c1"
            text_hover_color "#fff"
            text_outlines [(2, "#000", 0, 0)]

transform workshop_tutorial_outline_fade:
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        linear 0.2 alpha 0.0

screen workshop_tutorial_focus(target):
    # 淡入淡出只作用于轮廓，不使用脚本级 with/pause 重显上一句对白。
    # 这层不创建交互；点击与回退始终交给正在显示的对话。
    $ rx, ry, rw, rh = workshop_regions[target]
    add workshop_outline(target) at workshop_tutorial_outline_fade pos (rx, ry)

## ============================================================================
## ⚠️ 旧版修复界面 —— 已停用，保留仅供参考
## ============================================================================
## 这份和 scripts/ui/repair_window_enhanced.rpy 里的 repair_window 重名。
## 重名时后加载的那份会静默覆盖先加载的，而 repair_window_enhanced.rpy 排序靠后，
## 所以实际生效的一直是那一份（自称 "v7 最终修复版"），这份从来没被用到过。
##
## 为了不再有两个同名 screen，这里改名为 repair_window_old，不再参与运行。
## 确认不需要之后，整段可以直接删掉。
## （另：这份末尾还多出一个重复的"关闭"按钮，也是它没被使用的旁证。）
## ============================================================================

screen repair_window_old():
    modal True
    zorder 100
    
    # 半透明背景遮罩
    add "#000c" 
    
    # 主容器
    frame:
        align (0.5, 0.5)
        xsize 1400
        ysize 900
        background "#222"
        padding (40, 40)
        
        vbox:
            spacing 30
            
            ## ========================================
            ## 标题区域
            ## ========================================
            text "机体修复台" size 50 color "#fff" xalign 0.5 outlines [(2,"#000")]
            text "当前持有零件: [my_parts]" size 30 color "#ff0" xalign 0.5
            
            null height 20
            
            ## ========================================
            ## 修复进度区域
            ## ========================================
            frame:
                xfill True
                ysize 300
                background "#333"
                padding (20, 20)
                
                vbox:
                    spacing 20
                    
                    # 阿尔法机体
                    hbox:
                        spacing 30
                        xfill True
                        
                        # 左侧: 机体名称和进度
                        vbox:
                            spacing 5
                            xsize 500
                            yalign 0.5
                            
                            text "阿尔法机体" size 35 color "#fff"
                            text "修复进度: [alpha_fix]%" size 25 color "#0f0"
                            text "已解锁记忆: [get_unlocked_count('alpha')]/5" size 22 color "#aaa"
                        
                        # 右侧: 修复按钮
                        textbutton "修复 (+20%, 消耗1零件)":
                            xsize 450
                            ysize 70
                            yalign 0.5
                            sensitive (my_parts > 0 and alpha_fix < 100)
                            action [
                                SetVariable("my_parts", my_parts - 1),
                                SetVariable("alpha_fix", min(100, alpha_fix + 20))
                            ]
                            text_size 26
                            text_color "#0f0"
                            text_hover_color "#fff"
                            text_insensitive_color "#555"
                    
                    # 鸦羽机体
                    hbox:
                        spacing 30
                        xfill True
                        
                        vbox:
                            spacing 5
                            xsize 500
                            yalign 0.5
                            
                            text "鸦羽机体" size 35 color "#fff"
                            text "修复进度: [raven_fix]%" size 25 color "#0f0"
                            text "已解锁记忆: [get_unlocked_count('raven')]/5" size 22 color "#aaa"
                        
                        textbutton "修复 (+20%, 消耗1零件)":
                            xsize 450
                            ysize 70
                            yalign 0.5
                            sensitive (my_parts > 0 and raven_fix < 100)
                            action [
                                SetVariable("my_parts", my_parts - 1),
                                SetVariable("raven_fix", min(100, raven_fix + 20))
                            ]
                            text_size 26
                            text_color "#0f0"
                            text_hover_color "#fff"
                            text_insensitive_color "#555"
                    
                    # Laurel-II机体
                    hbox:
                        spacing 30
                        xfill True
                        
                        vbox:
                            spacing 5
                            xsize 500
                            yalign 0.5
                            
                            text "Laurel-II机体" size 35 color "#fff"
                            text "修复进度: [luna_fix]%" size 25 color "#0f0"
                            text "已解锁记忆: [get_unlocked_count('laurel')]/5" size 22 color "#aaa"
                        
                        textbutton "修复 (+20%, 消耗1零件)":
                            xsize 450
                            ysize 70
                            yalign 0.5
                            sensitive (my_parts > 0 and luna_fix < 100)
                            action [
                                SetVariable("my_parts", my_parts - 1),
                                SetVariable("luna_fix", min(100, luna_fix + 20))
                            ]
                            text_size 26
                            text_color "#0f0"
                            text_hover_color "#fff"
                            text_insensitive_color "#555"
            
            null height 10
            
            ## ========================================
            ## 记忆碎片区域
            ## ========================================
            frame:
                xfill True
                ysize 350
                background "#333"
                padding (20, 20)
                
                vbox:
                    spacing 15
                    
                    text "已解锁的记忆碎片" size 35 color "#fff" xalign 0.5
                    
                    null height 5
                    
                    # 记忆列表容器
                    viewport:
                        xfill True
                        ysize 260
                        scrollbars "vertical"
                        mousewheel True
                        
                        vbox:
                            spacing 10
                            
                            # 阿尔法的记忆
                            if get_unlocked_count("alpha") > 0:
                                text "▼ 阿尔法机体记忆" size 28 color "#0af"
                                
                                $ alpha_memories = get_unlocked_memories("alpha")
                                for mem_num in alpha_memories:
                                    $ is_read = is_memory_read("alpha", mem_num)
                                    $ unread_mark = "{color=#f00}[NEW]{/color} " if not is_read else ""
                                    $ button_color = "#fff" if is_read else "#ff0"
                                    
                                    textbutton "[unread_mark]记忆碎片 A0[mem_num]":
                                        xsize 1200
                                        ysize 50
                                        action [
                                            Hide("repair_window"),
                                            Jump("memory_alpha_0" + str(mem_num))
                                        ]
                                        text_size 24
                                        text_color button_color
                                        text_hover_color "#0f0"
                                
                                null height 10
                            
                            # 鸦羽的记忆
                            if get_unlocked_count("raven") > 0:
                                text "▼ 鸦羽机体记忆" size 28 color "#0af"
                                
                                $ raven_memories = get_unlocked_memories("raven")
                                for mem_num in raven_memories:
                                    $ is_read = is_memory_read("raven", mem_num)
                                    $ unread_mark = "{color=#f00}[NEW]{/color} " if not is_read else ""
                                    $ button_color = "#fff" if is_read else "#ff0"
                                    
                                    textbutton "[unread_mark]记忆碎片 P0[mem_num]":
                                        xsize 1200
                                        ysize 50
                                        action [
                                            Hide("repair_window"),
                                            Jump("memory_raven_0" + str(mem_num))
                                        ]
                                        text_size 24
                                        text_color button_color
                                        text_hover_color "#0f0"
                                
                                null height 10
                            
                            # Laurel-II的记忆
                            if get_unlocked_count("laurel") > 0:
                                text "▼ Laurel-II机体记忆" size 28 color "#0af"
                                
                                $ laurel_memories = get_unlocked_memories("laurel")
                                for mem_num in laurel_memories:
                                    $ is_read = is_memory_read("laurel", mem_num)
                                    $ unread_mark = "{color=#f00}[NEW]{/color} " if not is_read else ""
                                    $ button_color = "#fff" if is_read else "#ff0"
                                    
                                    textbutton "[unread_mark]记忆碎片 L0[mem_num]":
                                        xsize 1200
                                        ysize 50
                                        action [
                                            Hide("repair_window"),
                                            Jump("memory_laurel_0" + str(mem_num))
                                        ]
                                        text_size 24
                                        text_color button_color
                                        text_hover_color "#0f0"
                            
                            # 如果没有任何记忆
                            if get_unlocked_count("alpha") == 0 and get_unlocked_count("raven") == 0 and get_unlocked_count("laurel") == 0:
                                text "尚未解锁任何记忆碎片" size 28 color "#888" xalign 0.5 yalign 0.5
    
    ## ========================================
    ## 底部关闭按钮
    ## ========================================
    textbutton "关闭":
        align (0.5, 0.95)
        xsize 200
        ysize 60
        text_size 40
        action Hide("repair_window")


        
    textbutton "关闭":
        align (0.5, 0.8)
        text_size 40
        action Hide("repair_window")
