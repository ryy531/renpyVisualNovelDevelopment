define memory_unknown = Character("？？？", color="#d0d0d0", callback=dim_all)

image chapter1_memory_gun = Transform("images/cg/ravenge_gun_pov_clean_crop.png", xysize=(1920, 1080))
image chapter1_memory_bullet = Transform("images/cg/ravenge_bullet_pov_clean_full.png", xysize=(1920, 1080))

transform chapter1_memory_word_shake:
    xoffset 0
    linear 0.05 xoffset -7
    linear 0.05 xoffset 7
    repeat

screen chapter1_memory_words(word, size=72, shake=False, word_color="#f4f7ff"):
    zorder 400
    add Solid("#000")
    button:
        xfill True
        yfill True
        background None
        action NullAction()
    if shake:
        text word size size color word_color align (0.5, 0.5) at chapter1_memory_word_shake
    else:
        text word size size color word_color align (0.5, 0.5)

transform chapter1_memory_tv_line:
    xzoom 1.0
    alpha 1.0
    linear 0.22 xzoom 0.02
    linear 0.12 alpha 0.0

screen chapter1_memory_tv_cut():
    zorder 400
    add Solid("#000")
    add Solid("#d8faff") xysize (1920, 6) align (0.5, 0.5) at chapter1_memory_tv_line

label memory_alpha_05:
    scene black with fade
    centered "{color=#0af}【记录】{/color}"
    centered "{size=40}A05{/size}"
    $ renpy.pause(0.7, hard=True)
    scene bg_cliff with fade
    play music "audio/bgm/Zero-Two-DARLINGs - 开篇3.wav" fadein 1.0 volume 0.5 loop

    memory_unknown "……"
    memory_unknown "已经结束了。"
    memory_unknown "你没有■路。"
    memory_unknown "是我赢了。"

    "……"
    "■■呢？"

    memory_unknown "我亲手处理完毕了。"
    memory_unknown "不用担心。"

    "……"
    "是吗。这就是你的选■。"
    "那么，他们也是吗？"

    memory_unknown "他们？"
    memory_unknown "啊，如果你是指灰■■■。"
    memory_unknown "没错，他们也是我亲手处理的。"

    "……为什么。"
    "你承诺过……"
    "■■■■是你的家人，你会和他们一直——"

    memory_unknown "一直在一起？"
    memory_unknown "在构造体威胁到人类安全的当下，那种天■的承诺早就变成了笑话。"

    "你——！"

    memory_unknown "没关系，不用着急。"
    memory_unknown "我马上送你去见他们。"
    scene chapter1_memory_gun with dissolve
    $ renpy.pause(0.4, hard=True)

    "所以……"
    "你的誓言，你的承诺，你的约定……"
    "通通都是笑话吗？"
    "那些并肩作战，同生共死的回■与情感！"
    "对你来说，是可以随意抛弃的吗？"
    "你口中不同的道路，难道也是——"

    memory_unknown "让你产生无谓的期待，真是抱■。"
    memory_unknown "我啊，终究也只是个普通人类哦。"
    memory_unknown "我和那些人，其实并没有什么本质上的不同。"
    memory_unknown "所以，拜托了。"
    memory_unknown "最后的工作，最后一名构造体。"
    memory_unknown "看在过去的份上，别让我为难。"

    "想都别想。"
    "就算今天真的要死在这里……"
    "我也要——"
    stop music fadeout 0.2
    play sound "sfx/g_story_pistol.mp3"
    scene chapter1_memory_bullet
    with hpunch
    $ renpy.pause(0.35, hard=True)

    memory_unknown "你总是这■。"
    memory_unknown "■■■，为什么你就不能……乖乖去死呢？"

    scene black with dissolve
    play sound "sfx/g_story_run.mp3"
    $ renpy.pause(1.9, hard=True)
    play sound "sfx/chapter1_memory_fall.wav"
    $ renpy.pause(1.0, hard=True)
    play sound "sfx/g_story_liquidimp.mp3" volume 0.8
    $ renpy.pause(1.0, hard=True)

    memory_unknown "是……她……掉下去……"
    memory_unknown "……舰船……打捞……"
    memory_unknown "务必要……"

    play sound "sfx/chapter1_memory_underwater.wav"
    show screen chapter1_memory_words("又一次")
    $ renpy.pause(1.20, hard=True)
    show screen chapter1_memory_words("人类")
    $ renpy.pause(1.10, hard=True)
    show screen chapter1_memory_words("欺骗")
    $ renpy.pause(1.15, hard=True)
    show screen chapter1_memory_words("背叛")
    $ renpy.pause(1.20, hard=True)
    show screen chapter1_memory_words("死亡")
    $ renpy.pause(1.15, hard=True)
    show screen chapter1_memory_words("毁灭")
    $ renpy.pause(1.30, hard=True)
    show screen chapter1_memory_words("不可饶恕", word_color="#e53935")
    $ renpy.pause(1.50, hard=True)
    show screen chapter1_memory_words("不可饶恕", size=104, word_color="#e53935")
    $ renpy.pause(1.60, hard=True)
    show screen chapter1_memory_words("不可饶恕", size=152, shake=True, word_color="#e53935")
    with hpunch
    $ renpy.pause(2.10, hard=True)
    hide screen chapter1_memory_words

    play sound "sfx/chapter1_memory_tv_off.wav"
    show screen chapter1_memory_tv_cut
    $ renpy.pause(0.40, hard=True)
    hide screen chapter1_memory_tv_cut

    scene black with fade
    centered "{color=#0af}记忆结束{/color}"
    $ mark_memory_read("alpha", 5)

    return
