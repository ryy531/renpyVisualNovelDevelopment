# 工作室初访：多人画外对话，不显示角色立绘。
# 教学轮廓跟随台词中的指认出现，介绍结束后收起。

label workshop_first_visit:
    scene workshop_bg_scaled with fade
    sera "（唉，结果还是带回来了……这么重要的事情，交给我真的好吗……）"
    sera "（是不是当初该拒绝前辈比较好啊……）"
    natalia "哎呀，小瑟拉！你这工坊还不错嘛！"
    vannett "对于这个评级的家伙，已经可以算是奢侈了吧？"
    sera "你少说两句会死吗，凡尼特！"
    harrison "好了好了你们两个，与其在那站着不如帮我们搬东西啦！"
    sigmund "好，好重……放在这边可以吗，瑟拉？"
    sera "嗯，放在那边就好，麻烦你们啦。"
    call workshop_tutorial from _call_workshop_dialogue_tutorial
    $ workshop_tutorial_seen = True
    return


label workshop_tutorial:
    # 延续初访的同一场景；重复 scene 会触发 window auto，使对话框先隐藏再显示。
    # 普通对话框推进教学，轮廓只做提示，不允许在对话途中操作。
    natalia "不过，这个工坊现在应该还不能用吧？工具什么都配齐了吗？"
    sera "啊，工具就在墙上呢。"
    # 高亮展示墙上的工具：轮廓自行淡入，不插入计时停顿或对话转场。
    show screen workshop_tutorial_focus("repair")
    sera "不过现在的问题主要是没有零件啊……所以就算有工具也没法开始。"
    natalia "没关系，我倒是不着急。小瑟拉按照自己的节奏慢慢来就好。"
    hide screen workshop_tutorial_focus

    sigmund "那么把接下来的待办事项写进那边的电脑如何？"
    # 展示一旁的电脑：先提到电脑，再沿物件轮廓高亮。
    show screen workshop_tutorial_focus("sortie")
    sigmund "系统应该会把计划同步到你的终端，做下一步规划吧？"
    sigmund "之后就按照电脑上的待办，一件件地做下去吧。"
    sera "我本来就打算这么干啦——"
    sigmund "那就好。"
    # 教学介绍完毕，收起轮廓，告别与内心独白恢复普通对话演出。
    hide screen workshop_tutorial_focus
    natalia "没有什么其它事情的话，那就先回去咯。这回要写的报告可是堆积如山呢。"
    natalia "你们几个，要坐车的话就赶紧过来，不然我就丢下你们了！"
    sera "知，知道了前辈！我写好待办就来！"
    sera "（总之，事情应该都处理得差不多了。）"
    sera "（在被人发现我们提前开启了工坊前，先把事情记下来吧。）"
    sera "（明天就要离开法奥斯，开始工作了……）"
    sera "（呜呜，事情到底会变成什么样子啊……）"
    return
