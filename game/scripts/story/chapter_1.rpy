# 第一章：初遇
# 从工作室初访结束接起；博物馆调查留给下一章。

define constantine = Character("康斯坦丁", color="#d6bf9b", callback=partial(char_fade, "constantine"))
define chapter1_terminal_voice = Character("？？？", screen="chapter1_terminal_say", ctc=None)

image constantine normal = "images/characters/oldman.png"
image chapter1_street = "images/bg/bg_street2.png"

# 待机时保留暗下去的显示器。瑟拉说话仍使用常规对白框。
screen chapter1_terminal_idle():
    zorder 90
    frame:
        align (0.5, 0.35)
        xysize (1200, 525)
        background "#071018e8"
        padding (44, 38)
        vbox:
            spacing 28
            text "SERAPHINA // DIAGNOSTIC CONSOLE" size 26 color "#68808a"
            add Solid("#364b55") xysize (1100, 2)
            text "_" size 40 color "#456571"

# 说话时用整屏覆盖常规对话、快捷菜单及点击特效；本句结束后
# say screen 自动撤下，下面的待机显示器没有残留文字。
screen chapter1_terminal_say(who, what):
    zorder 400
    add "workshop_bg_scaled"
    add "#0009"
    frame:
        align (0.5, 0.35)
        xysize (1200, 525)
        background "#06141cf5"
        padding (36, 30)
        vbox:
            xfill True
            spacing 0
            text "SERAPHINA // UNKNOWN SIGNAL":
                xalign 0.5
                text_align 0.5
                size 24
                color "#44dbd4"
            null height 8
            text who id "who":
                xalign 0.5
                text_align 0.5
                size 27
                color "#8cece7"
            null height 18
            add Solid("#44dbd4") xysize (1100, 2) xalign 0.5
            fixed:
                xfill True
                ysize 340
                text what id "what":
                    xsize 1020
                    xalign 0.5
                    ypos 170
                    yanchor 0.5
                    text_align 0.5
                    size 36
                    line_spacing 12
                    color "#b8fff2"
    text "▸" align (0.84, 0.78) size 36 color "#44dbd4"

transform chapter1_light_flicker:
    alpha 0.0
    linear 0.06 alpha 0.65
    linear 0.08 alpha 0.0
    pause 0.10
    linear 0.05 alpha 0.45
    linear 0.15 alpha 0.0

screen chapter1_power_flicker():
    zorder 350
    add Solid("#e8f7ff") at chapter1_light_flicker

label chapter_1:
    scene chapter1_street with fade
    play music "audio/bgm/Zero-Two-DARLINGs - 开篇5.wav" fadein 1.0 volume 0.5 loop
    sera "单线密封塞，油封，密封轴承……"
    sera "还有一组常用螺栓和通用电线。"
    sera "啊！该死的，这些就5000信用点了！"
    sera "当初学校里也没说这种程度的基础零件要这么贵啊……"
    sera "好在下周8街那边还有两个单子，不然真的要揭不开锅了。"
    sera "我想想，还差一组匹配的防水插头，供应商还偏偏断货了，要想搞到的话……"
    sera "唉，麻烦死——啊！"
    play sound "audio/se/SW_LowPitch.WAV"
    with hpunch
    show constantine normal at center_pos with dissolve
    constantine "哎哟！"
    sera "痛痛痛——啊，老爷子！你怎么又站在垃圾桶边上！"
    sera "这条巷子本来就窄，很容易撞到啦！"
    constantine "嗨呀……这不是小瑟拉嘛。刚回来啊。"
    sera "不要转移话题啊，老爷子！"
    constantine "不好意思，不好意思……不过这里抽烟比较方便。"
    sera "您还抽啊，前几天不是说为了萝丝奶奶，要戒了吗？"
    constantine "为了不影响她，我这不都跑到这来了吗？"
    constantine "别担心，小瑟拉。老头子我马上就要攒够点数，成为{color=#e64b4b}升格者{/color}了。"
    constantine "等到了{color=#e64b4b}伊甸区{/color}，就不用抠抠搜搜抽这种廉价卷烟……"
    constantine "还能给萝丝申请一台医疗构造体呢！"
    sera "您最好是啦，万一星际远征计划全面禁烟要怎么办啊！"
    constantine "哈哈哈，那就走一步看一步吧。"
    constantine "说起来，小瑟拉你毕业也有一个月了吧？"
    constantine "工作还适应吗？要不要我到时候也帮你申请些物资？"
    sera "您照顾好萝丝奶奶就是了，我就不用了。"
    sera "现在每天都忙得要死，鬼知道为什么有那么多东西要修啊。"
    sera "比起物资，我更希望天上能掉下来一组带线尾的防水插头——"
    constantine "防水的……插头？"
    sera "就是里面有端子的那种。端子是夹在电线上的小金属片，两头接上，电路才通。"
    sera "还得型号对得上，密封塞也不能破……哎呀，跟您解释不清楚。"
    constantine "型号我是不懂。不过前两天有人送来一台坏代步车，车底下还挂着好几截线呢。"
    constantine "你要不要去看看？"
    sera "代步车！那控制器说不定还留着，没准……"
    sera "我都忘了您是做回收的了……可以拆吗？这不太合规吧？"
    constantine "你还会担心合不合规的问题吗？"
    sera "您还是挺了解我的嘛，老爷子。"
    sera "我先看看型号。要是能用，我把那截线一起取下来。谢谢您啦！"
    constantine "哈哈，去吧去吧，拆的时候慢点啊。"
    constantine "年轻真好啊……呵呵。"

    hide constantine with dissolve
    call chapter_1_first_repair from _call_chapter_1_first_repair

    call chapter_1_after_memory_05 from _call_chapter_1_after_memory_05

    $ chapter_progress = 2
    return

label chapter_1_after_memory_05:
    scene workshop_bg_scaled with fade
    play music "audio/bgm/compressed/Zero-Two-DARLINGs - 开篇7.wav" fadein 1.0 volume 0.5 loop
    sera "哇！吓我一跳！"
    sera "刚刚那是什么啊……这个东西里面本来的数据吗？"
    sera "该死，糊成一团，什么都没看清……"
    sera "难道是因为刚换了防水插头，线路通了的缘故？"
    sera "不过这会又没反应了。应该是DC电源模块还不稳定吧？"
    sera "总之让我先拔了它，然后再——"
    play sound "audio/se/SW_Key2.WAV"
    with hpunch
    play sound "sfx/g_story_machineon.mp3"
    show screen chapter1_terminal_idle
    chapter1_terminal_voice "……"
    chapter1_terminal_voice "你是谁？"
    sera "！？唔哦哦！动，动了！"
    sera "等等，这是在问我吗？"
    sera "是在问我对吧！"
    chapter1_terminal_voice "……"
    chapter1_terminal_voice "没错。"
    sera "它！能！对！话！"
    sera "难道是真的！？那个头部模块里面果然搭载了AI？"
    sera "不，或者说，难道更进一步……里面真的是完整的意识？！"
    sera "唔哦哦哦难道原初构造体果然是真的！其实人类议会还藏着可怕的阴谋——"
    chapter1_terminal_voice "……"
    sera "咦，等等，慢着，等一下。"
    sera "如果这玩意真的是原初构造体……那让议会知道了会怎么样……"
    sera "不，不不，慢着慢着慢着！"
    sera "坏了，不管怎么想都会有超级大的麻烦……"
    sera "不行不行不行！等等，冷静一点啊瑟拉芬娜！我们还没有证据证明这是个原初构造体不是吗！"
    sera "对，对，现在还不能下定论！"
    sera "你，没错，就是你！快告诉我你只是个普通的AI，对不对？对的吧！"
    chapter1_terminal_voice "……"
    chapter1_terminal_voice "你的自言自语结束了吗。"
    sera "不——"
    sera "你怎么可以这么智能啊——！"
    chapter1_terminal_voice "所以，你能回答我的问题了吗？"
    chapter1_terminal_voice "你是谁？"
    sera "就算你这么问我，我要怎么回答你啊……"
    sera "小朋友们大家好，我的名字是瑟拉芬娜·斯派克哦，很高兴认识你！"
    sera "你期待的是这样的答案吗？"
    chapter1_terminal_voice "……"
    chapter1_terminal_voice "我至少知道了你的名字。"
    sera "所以呢，你是什么，你难道真的是原初构造体？"
    chapter1_terminal_voice "……我不明白你说的原初构造体是什么。"
    chapter1_terminal_voice "但我的确是构造体。"
    sera "哦哦，那你是什么时候的构造体，型号？服役年限？制造批次？"
    chapter1_terminal_voice "不知道。"
    sera "怎么会不知道呢！名字你总该有吧？"
    chapter1_terminal_voice "……"
    chapter1_terminal_voice "不知道。"
    chapter1_terminal_voice "我没有关于我自己的记忆。"
    sera "哈啊？"
    sera "等会，你，你这家伙，别告诉我是那种失忆了的狗血桥段……"
    chapter1_terminal_voice "我确实没有关于自己的记忆。"
    chapter1_terminal_voice "所以我想我的确符合失忆的标准。"
    sera "……格式塔在上……"
    sera "当初我就不该答应前辈……"
    sera "早知道让她带你回去缠满电工胶带算了……"
    chapter1_terminal_voice "介意说明一下情况吗？"
    sera "啊——不好意思，想必你也很混乱吧。"
    sera "我想想我该怎么说啊……"
    sera "总之，你呢，是我和我的一位前辈从海里捞上来的。"
    sera "当时的你乱七八糟的，所以我就把你给带回来咯。"
    sera "你得感谢我，不是我妙手回春的话，你现在还是一堆废铁呢。"
    chapter1_terminal_voice "原来如此，感谢你。"
    sera "不……你道谢得这么干脆我反而会很尴尬啦……"
    chapter1_terminal_voice "你说你是从海里找到我的。"
    chapter1_terminal_voice "那么，请问现在的时间是？"
    sera "啊？下午四点五十七。"
    chapter1_terminal_voice "……不，我是问年份。"
    sera "喔，那个啊，今年是2345年。"
    chapter1_terminal_voice "……"
    chapter1_terminal_voice "这样吗……"
    sera "怎么了，问这个做什么？"
    chapter1_terminal_voice "我的上一次开机记录是2208年。"
    sera "咦，居然那么久吗！"
    sera "你可真是个老古董啊！"
    chapter1_terminal_voice "……谢谢夸奖。"
    sera "没在夸你，都说了你这样让我很尴尬啊。"
    sera "不过2208年……是战后吧……"
    sera "让我想想，2208年，2208年……"
    sera "哎，等会，[commander_name]当选议长是2208年还是2209年来着……"
    stop music fadeout 0.2
    play sound "audio/se/SW_LowPitch.WAV"
    show screen chapter1_power_flicker
    with hpunch
    pause 0.45
    hide screen chapter1_power_flicker
    sera "哇啊啊啊！慢，慢着！怎么回事！"
    sera "啊，我的电脑！喂，你这家伙在干什么啦！工作室的电压都被你整不稳了！"
    sera "还不快住手！不然我拔你电源了！"
    chapter1_terminal_voice "……！"
    chapter1_terminal_voice "……抱歉。"
    play music "audio/bgm/compressed/Zero-Two-DARLINGs - 开篇7.wav" fadein 1.5 volume 0.5 loop
    sera "怎么搞的，突然这么大反应？"
    chapter1_terminal_voice "……[commander_name]……"
    sera "？嗯？[commander_name]怎么了？你认识那位灰鸦的指挥官？"
    chapter1_terminal_voice "……叛徒。"
    sera "什，什么？"
    chapter1_terminal_voice "[commander_name]……无耻的小人……无情的背叛者……"
    chapter1_terminal_voice "灰鸦……不可饶恕的人类……"
    sera "慢，慢着。你在说什么，你说的是[commander_name]对吧？"
    sera "人类议会的第一任议长，伟大的英雄和先锋者，帕弥什战争结束的功臣……之类的。"
    sera "你怎么把那个人说得这么不堪啊！"
    chapter1_terminal_voice "那个人……成为了议长吗？"
    chapter1_terminal_voice "竟然还被奉为英雄，真是可笑。"
    sera "呃，你们是有什么恩怨啊？"
    chapter1_terminal_voice "……不知道。"
    sera "哈？不知道！？那你还……"
    chapter1_terminal_voice "我不清楚具体发生了什么，但……"
    chapter1_terminal_voice "我的情感在告诉我憎恨那个人。"
    sera "哈，看来历史人物总是没有看起来那么伟光正。"
    sera "要是让瑞文知道了，她估计会乐一天吧……"
    chapter1_terminal_voice "你……对于灰鸦的指挥官有什么了解吗？"
    sera "没有，仅限于历史书。"
    sera "我还留着教材呢，你要看眼吗？"
    chapter1_terminal_voice "……如果你不介意的话。"
    sera "好好，让我给你翻翻。"
    play sound "sfx/chapter1_rummage.wav"
    pause 1.3
    play sound "audio/se/prologue_submarine_drop_sand.ogg" volume 0.18
    with vpunch
    sera "哎，放哪儿了……啊，在这！"
    $ renpy.music.set_volume(0.18, delay=0.2, channel="music")
    play sound "sfx/chapter1_book_page_turn.ogg"
    sera "喏，这是[commander_name]的那一页。"
    $ renpy.music.set_volume(1.0, delay=0.5, channel="music")
    sera "怎么样，有想起什么吗？"
    chapter1_terminal_voice "……"
    chapter1_terminal_voice "不知道，至少记载的内容和我的印象没有任何重叠。"
    sera "看来你很讨厌那家伙了。"
    chapter1_terminal_voice "我想看看其它的，比如帕弥什战争那一页。"
    sera "好好，明白了……"
    $ renpy.music.set_volume(0.18, delay=0.2, channel="music")
    play sound "sfx/chapter1_book_page_turn.ogg"
    pause 2.8
    $ renpy.music.set_volume(1.0, delay=0.5, channel="music")
    sera "……唉，你看好了吗，我都累了。"
    chapter1_terminal_voice "抱歉。"
    sera "没关系啦，反正你现在也动不了。"
    sera "有什么有价值的信息吗？"
    chapter1_terminal_voice "……不清楚。"
    chapter1_terminal_voice "上面的记载很笼统。"
    sera "毕竟是历史书嘛……我也是背过就忘，我懂你。"
    sera "这样的话……嗯，我想想……"
    sera "回头我带你去博物馆好了！"
    chapter1_terminal_voice "博物馆？"
    sera "对！帕弥什战争纪念馆！"
    sera "离这里不远，还是蛮方便的！"
    chapter1_terminal_voice "……是吗，那么有劳你了。"
    sera "没事，包在我身上！正好我也很久没去了！"
    sera "馆内那个主题餐厅味道还不错呢！"
    sera "不过在那之前——"
    sera "我得先想办法把你修到可以走路的程度才行。"
    sera "还得把你打扮得完全不像个构造体。"
    sera "哎呀，那这样的话估计得再想办法找个电机编码器——"
    chapter1_terminal_voice "抱歉。"
    sera "不，我没有在怪你……"
    sera "这也不是你的错啦。"
    sera "虽然很麻烦，但总而言之……"
    sera "{color=#78e6a0}欢迎回到地球，老古董！{/color}"
    chapter1_terminal_voice "……"
    hide screen chapter1_terminal_idle
    stop music fadeout 1.0
    scene black with fade
    return

# 首次修复留在第一章调用栈内，记忆结束后继续同一场戏。
label chapter_1_first_repair:
    if chapter1_repair_stage == "not_started":
        sera "先把车底那截线剪下来……嗯，密封圈也还完整。"
        play sound "audio/se/SW_Key1.WAV"
        sera "就是它！型号完全一样！"
        $ my_parts += 1
        $ chapter1_repair_stage = "awaiting_repair"

    if chapter1_repair_stage == "awaiting_repair":
        scene workshop_bg_scaled with fade
        play music "audio/bgm/compressed/Zero-Two-DARLINGs - 开篇7.wav" fadein 1.0 volume 0.5 loop
        sera "运气真好，型号竟然正好一模一样。"
        sera "这下好了——这玩意的修复可算是能有点进展了。"
        sera "到时候前辈问起来，就告诉她是工作忙……"
        sera "哎呀，也确实是忙嘛，我也是需要娱乐生活的！"
        sera "工具都在墙上……总之，先把这组防水插头装进去吧。"
        show screen workshop_tutorial_focus("repair")
        sera "先把旧接口拆掉，再固定新端子。"
        hide screen workshop_tutorial_focus
        sera "好，开工吧！"

    while chapter1_repair_stage == "awaiting_repair":
        call screen workshop_screen(repair_event=True)
        if _return == "repair_alpha" and my_parts > 0:
            $ my_parts -= 1
            $ alpha_fix = min(100, alpha_fix + 20)
            $ unlock_memory("alpha", 5)
            $ chapter1_repair_stage = "memory"
            scene workshop_bg_scaled with dissolve
            play sound "audio/se/SW_Key3.WAV"
            sera "旧接口卸下来……端子夹紧。密封塞要推到底，不然还是会进水。"
            sera "好了，把线尾接到控制板上——哎！"
            play sound "sfx/g_ingame_ev15_elecboom.mp3"
            with hpunch
            sera "糟，探针滑到了另一边！刚才那下不会把电路烧了吧？"
            sera "等等……头部模块的指示灯？它刚刚亮了一下？"
            stop music fadeout 0.5
            play sound "audio/se/SW_BG.WAV"
            scene black with dissolve
            pause 0.5

    if chapter1_repair_stage == "memory":
        call memory_alpha_05 from _call_chapter_1_memory_alpha_05
        $ chapter1_repair_stage = "complete"
    return
