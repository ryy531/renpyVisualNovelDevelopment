# 1. 背景图定义
image workshop_bg_scaled = im.Scale("images/bg/bg_workshop.jpg", 1920, 1080)

# 2. 工作室主界面
screen workshop_screen():
    tag menu 
    imagemap:
        ground "workshop_bg_scaled"
        # 这里的热点对应你的真实坐标
        hotspot (493, 511, 302, 241) action Return("sortie") tooltip "出发"
        hotspot (459, 190, 267, 214) action Show("repair_window") tooltip "修复"
        hotspot (20, 802, 280, 149) action NullAction() tooltip "日记"

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            align (0.5, 0.1)
            size 60
            color "#fff"
            outlines [(2, "#000", 0, 0)]

# 3. 修复系统弹窗 (重命名了一下，避免太长)
screen repair_window():
    modal True
    zorder 100
    add "#000c" 

    vbox:
        align (0.5, 0.5)
        spacing 20 

        text "机体修复台" size 50 color "#fff" xalign 0.5 outlines [(2,"#000")]
        text "当前持有零件: [my_parts]" size 30 color "#ff0" xalign 0.5
        null height 20 

        # 阿尔法
        hbox:
            spacing 20
            text "阿尔法 (进度 [alpha_fix]%)" size 30 color "#fff" yalign 0.5
            textbutton "修复 (消耗1零件)":
                sensitive (my_parts > 0 and alpha_fix < 100) 
                action [SetVariable("my_parts", my_parts - 1), SetVariable("alpha_fix", alpha_fix + 10)]
                text_color "#0f0"
                text_hover_color "#fff"
                text_insensitive_color "#555"

        # (为了节省篇幅，如果你需要其他两个角色的按钮，请照着之前的代码贴回来，或者暂时只留这一个测试)
        
    textbutton "关闭":
        align (0.5, 0.8)
        text_size 40
        action Hide("repair_window")