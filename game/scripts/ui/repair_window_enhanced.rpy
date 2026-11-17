## ============================================================================
## 增强版修复界面 - 整合记忆碎片系统 (修复版)
## ============================================================================
## 修复了 textbutton 中不能使用三元表达式的语法错误
## ============================================================================

## ============================================================================
## 增强版修复界面 (v7 - 最终修复版)
## ============================================================================

screen repair_window(story_repair=False):
    modal True
    zorder 100
    $ alpha_display_name = workshop_alpha_name()
    
    add "#000c"
    
    frame:
        align (0.5, 0.5)
        xsize 1200
        ysize 900
        background "#222"
        padding (30, 25)
        
        vbox:
            xfill True
            spacing 12
            
            ## 标题区域
            text "机体修复台" size 46 color "#fff" xalign 0.5 outlines [(2,"#000")]
            text "当前持有零件: [my_parts]" size 26 color "#ff0" xalign 0.5
            
            null height 3
            
            ## 修复进度区域
            frame:
                xfill True
                ysize 380
                background "#333"
                padding (25, 15)
                
                viewport:
                    ysize 350
                    scrollbars None
                    
                    vbox:
                        spacing 12
                        
                        # 阿尔法机体
                        hbox:
                            spacing 20
                            ysize 100
                            
                            vbox:
                                spacing 4
                                xsize 600
                                yalign 0.5
                                
                                text "[alpha_display_name]" size 30 color "#fff"
                                text "修复进度: [alpha_fix]%" size 20 color "#0f0"
                                text "已解锁记忆: [get_unlocked_count('alpha')]/5" size 17 color "#aaa"
                            
                            $ alpha_can = (my_parts > 0 and (story_repair or (workshop_repair_available() and alpha_fix < 100)))
                            
                            button:
                                xsize 380
                                ysize 55
                                yalign 0.5
                                sensitive alpha_can
                                background "#444"
                                hover_background "#555"
                                insensitive_background "#2a2a2a"
                                if story_repair:
                                    # 返回本次临时工作室调用，由剧情负责扣除零件和自动播放记忆。
                                    action [Hide("repair_window"), Return("repair_alpha")]
                                else:
                                    action [
                                        SetVariable("my_parts", my_parts - 1),
                                        SetVariable("alpha_fix", min(100, alpha_fix + 20))
                                    ]
                                
                                if alpha_can:
                                    text "修复 (+20%, 消耗1零件)" align (0.5, 0.5) size 20 color "#0f0"
                                else:
                                    text "修复 (+20%, 消耗1零件)" align (0.5, 0.5) size 20 color "#666"
                        
                        # 鸦羽机体
                        if raven_body_unlocked and not story_repair:
                            hbox:
                                spacing 20
                                ysize 100
                                
                                vbox:
                                    spacing 4
                                    xsize 600
                                    yalign 0.5
                                    
                                    text "鸦羽机体" size 30 color "#fff"
                                    text "修复进度: [raven_fix]%" size 20 color "#0f0"
                                    text "已解锁记忆: [get_unlocked_count('raven')]/5" size 17 color "#aaa"
                                
                                $ raven_can = (my_parts > 0 and raven_fix < 100)
                                
                                button:
                                    xsize 380
                                    ysize 55
                                    yalign 0.5
                                    sensitive raven_can
                                    background "#444"
                                    hover_background "#555"
                                    insensitive_background "#2a2a2a"
                                    action [
                                        SetVariable("my_parts", my_parts - 1),
                                        SetVariable("raven_fix", min(100, raven_fix + 20))
                                    ]
                                    
                                    if raven_can:
                                        text "修复 (+20%, 消耗1零件)" align (0.5, 0.5) size 20 color "#0f0"
                                    else:
                                        text "修复 (+20%, 消耗1零件)" align (0.5, 0.5) size 20 color "#666"
                        
                        # Laurel-II机体
                        if laurel_body_unlocked and not story_repair:
                            hbox:
                                spacing 20
                                ysize 100
                                
                                vbox:
                                    spacing 4
                                    xsize 600
                                    yalign 0.5
                                    
                                    text "Laurel-II机体" size 30 color "#fff"
                                    text "修复进度: [luna_fix]%" size 20 color "#0f0"
                                    text "已解锁记忆: [get_unlocked_count('laurel')]/5" size 17 color "#aaa"
                                
                                $ luna_can = (my_parts > 0 and luna_fix < 100)
                                
                                button:
                                    xsize 380
                                    ysize 55
                                    yalign 0.5
                                    sensitive luna_can
                                    background "#444"
                                    hover_background "#555"
                                    insensitive_background "#2a2a2a"
                                    action [
                                        SetVariable("my_parts", my_parts - 1),
                                        SetVariable("luna_fix", min(100, luna_fix + 20))
                                    ]
                                    
                                    if luna_can:
                                        text "修复 (+20%, 消耗1零件)" align (0.5, 0.5) size 20 color "#0f0"
                                    else:
                                        text "修复 (+20%, 消耗1零件)" align (0.5, 0.5) size 20 color "#666"
            
            ## 记忆碎片区域
            frame:
                xfill True
                ysize 230
                background "#333"
                padding (20, 12)
                
                vbox:
                    xfill True
                    spacing 6
                    
                    text "已解锁的记忆碎片" size 26 color "#fff" xalign 0.5
                    
                    null height 2
                    
                    viewport:
                        xfill True
                        ysize 160
                        scrollbars "vertical"
                        mousewheel True
                        scrollbar_unscrollable "hide"
                        
                        vbox:
                            spacing 5
                            
                            if get_unlocked_count("alpha") > 0:
                                text "▼ [alpha_display_name]机体记忆" size 20 color "#0af"
                                
                                $ alpha_memories = get_unlocked_memories("alpha")
                                for mem_num in alpha_memories:
                                    $ is_read = is_memory_read("alpha", mem_num)
                                    $ unread_mark = "{color=#f00}NEW{/color} " if not is_read else ""
                                    $ button_color = "#fff" if is_read else "#ff0"
                                    
                                    textbutton "[unread_mark]记忆碎片 A0[mem_num]":
                                        ysize 32
                                        sensitive (not story_repair and renpy.has_label("memory_alpha_0" + str(mem_num)))
                                        if mem_num == 1 or mem_num == 5:
                                            action [Hide("repair_window"), Return("memory_alpha_0" + str(mem_num))]
                                        else:
                                            action [Hide("repair_window"), Jump("memory_alpha_0" + str(mem_num))]
                                        text_size 18
                                        text_color button_color
                                        text_hover_color "#0f0"
                                
                                null height 4
                            
                            if raven_body_unlocked and not story_repair and get_unlocked_count("raven") > 0:
                                text "▼ 鸦羽机体记忆" size 20 color "#0af"
                                
                                $ raven_memories = get_unlocked_memories("raven")
                                for mem_num in raven_memories:
                                    $ is_read = is_memory_read("raven", mem_num)
                                    $ unread_mark = "{color=#f00}[NEW]{/color} " if not is_read else ""
                                    $ button_color = "#fff" if is_read else "#ff0"
                                    
                                    textbutton "[unread_mark]记忆碎片 P0[mem_num]":
                                        ysize 32
                                        action [Hide("repair_window"), Jump("memory_raven_0" + str(mem_num))]
                                        text_size 18
                                        text_color button_color
                                        text_hover_color "#0f0"
                                
                                null height 4
                            
                            if laurel_body_unlocked and not story_repair and get_unlocked_count("laurel") > 0:
                                text "▼ Laurel-II机体记忆" size 20 color "#0af"
                                
                                $ laurel_memories = get_unlocked_memories("laurel")
                                for mem_num in laurel_memories:
                                    $ is_read = is_memory_read("laurel", mem_num)
                                    $ unread_mark = "{color=#f00}[NEW]{/color} " if not is_read else ""
                                    $ button_color = "#fff" if is_read else "#ff0"
                                    
                                    textbutton "[unread_mark]记忆碎片 L0[mem_num]":
                                        ysize 32
                                        action [Hide("repair_window"), Jump("memory_laurel_0" + str(mem_num))]
                                        text_size 18
                                        text_color button_color
                                        text_hover_color "#0f0"
                            
                            if (get_unlocked_count("alpha") == 0 and (not raven_body_unlocked or get_unlocked_count("raven") == 0) and (not laurel_body_unlocked or get_unlocked_count("laurel") == 0)):
                                null height 40
                                text "尚未解锁任何记忆碎片" size 20 color "#888" xalign 0.5
            
            ## 关闭按钮
            hbox:
                xfill True
                
                textbutton "关 闭":
                    xalign 0.5
                    xsize 180
                    ysize 48
                    text_size 30
                    text_color "#fff"
                    text_hover_color "#0f0"
                    text_xalign 0.5
                    background "#444"
                    hover_background "#555"
                    action Hide("repair_window")
