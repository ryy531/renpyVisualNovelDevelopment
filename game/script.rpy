# 游戏的唯一入口
label start:
    show screen key_listener # 开启点击特效
    
    # --- 第一阶段：序章 (Prologue) ---
    # 如果进度是0，先跑序章
    if chapter_progress == 0:
        # 注意：这里是 jump，不会再回来。
        # 序章结尾会自己把 chapter_progress 设为 1，然后经 workshop_intro 进入 main_hub_loop。
        jump prologue

    # --- 第二阶段：工作室循环 (Game Loop) ---
    call main_hub_loop from _call_main_hub_loop

    return

# 这是一个专门处理循环的 label，方便管理
label main_hub_loop:
    if not workshop_tutorial_seen:
        call workshop_first_visit from _call_workshop_first_visit

    while True:
        # 1. 显示工作室
        scene workshop_bg_scaled
        call screen workshop_screen
        
        # 2. 处理工作室返回的动作
        if _return == "continue":
            # 路由系统：根据当前进度去不同的章节
            if chapter_progress == 1:
                call chapter_1 from _call_chapter_1
            elif chapter_progress == 2:
                call chapter_2 from _call_chapter_2
            else:
                "现有剧情已完结。"
                return # 结束游戏，或者 break

        elif _return == "memory_alpha_01":
            # 手动回看 A01 才回到工作室；剧情首次播放由第一章直接调用。
            call memory_alpha_01 from _call_workshop_replay_alpha_01

        elif _return == "memory_alpha_05":
            call memory_alpha_05 from _call_workshop_replay_alpha_05

    return

# --- 剧情内容定义 ---

label chapter_prologue:
    scene black
    "【序章：打捞】"
    "那是150年后的一个雨天..."
    "瑟拉芬娜捡到了那具残骸。"
    return

label chapter_2:
    scene black
    "【第二章：记忆的各种】"
    "这是第二章的剧情..."
    return
