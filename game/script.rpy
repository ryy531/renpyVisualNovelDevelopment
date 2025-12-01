# 游戏的唯一入口
label start:
    show screen key_listener # 开启点击特效
    
    # --- 第一阶段：序章 (Prologue) ---
    # 如果进度是0，先跑序章
    if chapter_progress == 0:
        call chapter_prologue
        # 序章结束后，进度变成1，解锁工作室
        $ chapter_progress = 1
        "系统提示：工作室权限已解锁。"

    # --- 第二阶段：工作室循环 (Game Loop) ---
    call main_hub_loop

    return

# 这是一个专门处理循环的 label，方便管理
label main_hub_loop:
    while True:
        # 1. 显示工作室
        call screen workshop_screen
        
        # 2. 处理工作室返回的动作
        if _return == "sortie":
            # 路由系统：根据当前进度去不同的章节
            if chapter_progress == 1:
                call chapter_1
            elif chapter_progress == 2:
                call chapter_2
            else:
                "现有剧情已完结。"
                return # 结束游戏，或者 break

    return

# --- 剧情内容定义 ---

label chapter_prologue:
    scene black
    "【序章：打捞】"
    "那是150年后的一个雨天..."
    "瑟拉芬娜捡到了那具残骸。"
    return

label chapter_1:
    scene black
    "【第一章：初遇】"
    "瑟拉芬娜拿起了背包，决定出门寻找能源。"
    $ my_parts += 5
    "你获得了5个零件。"
    $ chapter_progress += 1 # 这一章打完，进度推到2
    return

label chapter_2:
    scene black
    "【第二章：记忆的各种】"
    "这是第二章的剧情..."
    return