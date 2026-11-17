## ============================================================================
## 序章 - 打捞阿尔法
## ============================================================================
## 章节目标：
## 1. 打捞阿尔法机体
## 2. 带回工作室
## 3. 解锁工作室UI
## 
## 章节结束后：chapter_progress = 1
## ============================================================================

## 快速交叉淡入：用于同一位置上的角色轮换（拌嘴、抢话）。
## 比默认的 dissolve(0.5) 快得多，不会拖慢节奏，但能消掉硬切的闪烁。
define quickfade = Dissolve(0.15)


label prologue:
    ## ========================================
    ## 序章开始
    ## ========================================
    
    # 设置章节进度为0（序章）
    $ chapter_progress = 0
    
    # ===== 场景1：开场 =====
    # 在这里写开场剧情
    # 示例：
    # scene bg_ocean with fade
    # play music "bgm_ocean.ogg" fadein 2.0
    # "旁白文字..."
    # 角色名 "对话内容"
     
    scene bg_classroom 
    play sound "audio/se/SW_BG.WAV" loop
    sera "今天天气……好得有点过分了。"
    sera "阳光与云层的角度正正好，气温是最舒适的26°。风速和风向正适合冲浪……"
    sera "这种天气，就应该趁着阳光，在沙滩上晒太阳，或者支上一个鱼竿，一定能大丰收的吧……"
    sera "再不济，就在窗边睡一觉也行啊。"
    sera "而不是在这里……"
    show teacher normal
    stop sound fadeout 2.0
    play music "audio/bgm/Zero-Two-DARLINGs - 开篇5.wav" volume 0.5 loop
    teacher "瑟拉芬娜·斯派克！" with vpunch
    sera "哇啊！" with vpunch
    teacher "你竟然还在发呆。"
    teacher "你知道今天为什么被叫来吗？"
    sera "呃……因为昨天晚上我去食堂拿走了四颗水煮蛋？"
    teacher "你竟然还擅自去食堂拿走配给食物！？"
    sera "啊，糟了，不是因为这个吗……"
    teacher "食堂的事等下再跟你算账……"
    teacher "这次找你来是因为你的最终测验。"
    sera "诶？可我明天就要毕业了……而且最终测验的学分不是早就算进去了吗？"
    teacher "那也不是你在试卷上乱填的理由。"
    teacher "尤其是你的历史试卷！"
    teacher "“帕弥什战争结束的时间是一亿五千万年前”，这就是你的答案？"
    teacher "下一步你是不是打算写，恐龙灭绝的原因是帕弥什？"
    sera "哎呀，记混了嘛……"
    teacher "战争结束是150年前，这么基本的常识难道你也会记混？"
    teacher "你一天天的脑子里都在想些什么东西！"
    teacher "还有这道题，“帕弥什战争的英雄，灰鸦小队的指挥官，战后人类的第一任议长的名字是？”你填的什么？"
    teacher "瑞文·格雷森！"
    teacher "我怎么不知道那位伟大的指挥官现在正睡在你的上铺？"
    teacher "你们两个一个倒数第一，一个倒数第二，难道还很自豪吗？"
    sera "哎呀，可这也不算我写错了吧，瑞文不也是灰鸦……"
    teacher "……瑞文·格雷森的确是第六代灰鸦指挥官，我不否认。"
    teacher "但我要问的是本尊！是那个伟大的起源！！"
    teacher "这是基础中的基础！要是让伊甸区的审查官看到这种试卷，你会被直接打上“智力缺陷”的标签！"
    teacher "我再给你最后一次机会，瑟拉芬娜·斯派克，回答我，灰鸦指挥官的名字是——"
    sera "（坏，坏了，老师看起来真的生气了！）"
    sera "（如果不答对的话，恐怕就不止是水煮蛋的问题了……）"
    sera "（让我好好想想，书上写的是什么来着……）"
    # 暂停一下，让玩家准备输入
    $ renpy.pause(0.5, hard=True)

    # 输入循环（带二次确认）
    label input_commander_name:
        python:
            temp_name = renpy.input("记忆中那个模糊的名字似乎是：", length=20)
            if isinstance(temp_name, str) and temp_name.strip():
                commander_name = temp_name.strip()
            else:
                commander_name = "指挥官"
    
        # 二次确认
        menu:
            "确认是「[commander_name]」吗？"
        
            "确认":
                pass
        
            "重新输入":
                jump input_commander_name

    # 根据输入显示不同对话
    if commander_name == "指挥官":
        sera "咦，啊，不对……哦！我想起来了！"
        sera "报告老师！根据《战后历史纲要》记载，因为帕弥什战争末期的动荡与数据损毁，那位伟人的真实名讳并未留存在格式塔的公开记录中！"
        teacher "看来你的脑子里除了水煮蛋，至少还装了一点正经东西。"
        teacher "没错，我们现在都以[commander_name]称呼那名伟人。"
    else:
        sera "呃，是[commander_name]！对，就是[commander_name]！"
        teacher "令人惊讶。"
        teacher "如果不是我看过最新的考古研究内刊，我还真以为你又在胡编乱造。"
        teacher "的确，最近是在一些受损的数据库中还原出了[commander_name]这个音节。虽然还未被写入正式教材……"
        teacher "但你要记住，瑟拉芬娜同学。对于历史而言，个人的名讳并不重要。重要的是那位伟人作为“人类代表”的符号意义。"
        teacher "要对历史有敬畏之心，明白吗？"

    teacher "总而言之，好在你还记得这些。"
    teacher "那当时为什么要在试卷上写这种乱七八糟的东西？"
    sera "当时是当时嘛，老师。考试太紧张，一时想不起来也正常吧。"
    sera "我不是什么优秀的学生，也不是任何名号的继承者。"
    sera "而且再怎么着我的分数也够不上{color=#ff0000}升格者{/color}的门槛，毕业了直接去格式塔分我的工作岗位不就好了？"
    sera "老老实实过一辈子也不坏嘛。"
    teacher "朽木不可雕也！"
    teacher "你要知道，[commander_name]最开始也只是一名普通人，但那个人通过自身的努力，成为了战后人类议会的第一任会长。"
    teacher "就算学分不够，在岗位上积攒工作积分，也可以得到{color=#ff0000}升格{/color}机会。"
    teacher "法奥斯学院的学生都应当努力精进自我，总有一天成为{color=#ff0000}升格者{/color}，加入位于{color=#ff0000}伊甸区{/color}的星际远航计划——"
    sera "成为推动人类文明迈向星辰大海的先驱者，为人类的进步添砖加瓦是吧？是是老师，我记着呢。"
    teacher "你——"
    teacher "如果人人都像你一样安于现状，人类文明要如何才能更上一层楼？"
    sera "不用担心啦老师，格式塔也说过，社会底层的螺丝钉也很重要，对吧？"
    teacher "唉……"
    teacher "……罢了。只要你毕业后不去惹事，不要给学院抹黑，我就谢天谢地了。"
    teacher "就这样吧，去走廊罚站。"
    teacher "下一个，哈里森！"
    sera "（啊哈，果然这家伙也被叫来检讨会啦，好姐妹就是要有难同当嘛。）"
    show teacher normal at char_left with move
    show harrison normal at char_right with quickfade
    harrison "嗨，老师~"
    teacher "知道今天叫你来是为什么吗？"
    harrison "呃，考试成绩？门禁逃逸？还是食堂的水煮蛋？"
    teacher "你也去偷拿水煮蛋！？食堂的水煮蛋就那么好吃！？"
    teacher "这次叫你来是因为有同学目击你翻墙出去！"
    teacher "瑟拉芬娜也就罢了！哈里森啊哈里森，你可是堂堂正正的第五代哈里乔！"
    teacher "等你明天毕业，要掌管的是整个生命之星的资料与数据！"
    teacher "无论是黄金时代的医疗记录，还是免疫时代留下的帕弥什样本……"
    teacher "需要我重申这些资料的重要性吗！"
    harrison "不，不用老师。我知道的，嘿嘿。"
    teacher "别嬉皮笑脸的！你身负如此重大的职责，竟敢目无法纪！"
    teacher "在毕业前离开法奥斯学院是被严令禁止的，你明白吗？"
    teacher "未年满16岁的学生，应当在法奥斯学院中统一进行抚养和教育。"
    teacher "这是为了减轻社会的压力，也是为了让同学们能够专心训练，早日成为{color=#ff0000}升格者{/color}。"
    teacher "翻墙这种行为只会成为其它同学的坏榜样，如果有人效仿，你知道会为学院带来怎样的麻烦吗？"
    harrison "啊……明白的明白的。我保证不再犯！"
    teacher "不要只是口头说明白！你身上的处分已经多到有辱哈里乔这个名号了！"
    teacher "今天是最后一次批评教育。等你明天毕业了，也要安分守己，老实工作。"
    harrison "是是老师，保证不再犯，安分守己，老实工作！"
    teacher "你最好是。真是的……一个两个都不给我省心。"
    teacher "去瑟拉芬娜那边等着。"
    hide teacher with quickfade
    show harrison normal at center_pos with move
    harrison "好的好的~唉……"
    sera "不公平，怎么这么快就放你走了，继承人就可以为所欲为吗。"
    harrison "小声点你这家伙，看来你是还没有被骂够是吧！"
    sera "是是，话说还没完吗？"
    harrison "我刚刚在门外还看到了……"
    teacher "下一个，西格蒙德，进来！"
    harrison "喏，就是那家伙。"
    sera "啊！？好学生也来检讨会啊！"
    harrison "说不定西格蒙德为了陪我们特意犯了事呢？太讲义气了兄弟！"
    sera "先闭嘴！老师在看呢！"
    hide harrison
    show teacher normal at char_left
    show sigmund normal at char_right
    with quickfade
    sigmund "您好，老师。"
    teacher "嗯，西格蒙德，你先坐。"
    sera "（哇啊，语气都不一样，好学生就是好啊。）"
    teacher "今天叫你来……"
    sigmund "水煮蛋的事，真的很抱歉。但我真的没有参与，是瑟拉和哈里森硬塞给我的。"
    teacher "……什么？怎么你也？"
    sigmund "……不是这个问题吗？"
    teacher "真受不了……不，忘了水煮蛋吧，今天叫你来是为了志愿的事，西格蒙德。"
    sera "（真可惜，不是特地犯事来陪我们的呢。）"
    sigmund "关于志愿……老师，我想我上次已经和您说明了。"
    sigmund "我并不打算现在就成为{color=#ff0000}升格者{/color}。"
    sigmund "我还有身为第七代西蒙的职责。"
    teacher "老师当然明白。有你这样优秀的学生，想必西蒙先生也会骄傲。"
    teacher "但是，现在是和平年代。作为过去军事总司令的职责如今也只是挂名，完全可以寻找他人代劳。"
    teacher "如果你成为{color=#ff0000}升格者{/color}，格式塔当然也会立刻培养下一代西蒙。"
    teacher "能够前往{color=#ff0000}伊甸区{/color}的机会不多，何况加入星际远航计划更是学院的最高荣誉。"
    teacher "你确定要就这样放弃吗？"
    sigmund "抱歉，老师。我明白这份荣誉的来之不易。"
    sigmund "只是，我还未曾体验过地表的工作与生活。在前往{color=#ff0000}伊甸区{/color}之前，我想再多看看这里。"
    sigmund "况且，我的朋友们也在这……"
    teacher "但如果你成为{color=#ff0000}升格者{/color}，你也可以为你的朋友们申请资源。"
    teacher "比如瑟拉芬娜，一台构造体或许能为她的工作提供助力……"
    sera "啊？我吗？"
    sigmund "……瑟拉，你需要吗？"
    sera "哎呀，不着急啦，我又不是没法应付。"
    teacher "……"
    teacher "罢了。格式塔不会强迫你。我也只是最后确认。"
    teacher "毕竟成为{color=#ff0000}升格者{/color}是完全自愿。我们也会尊重你的想法。"
    teacher "只是如果你改变主意，记得随时发起申请。{color=#ff0000}伊甸区{/color}的大门会一直向你敞开。"
    teacher "今天就到这里了。明天就是毕业典礼。最后一天，希望你们可以安安分分……"
    teacher "尤其是你们两个。"
    sera "嘿嘿。"
    hide sigmund
    show harrison normal at char_right
    with quickfade
    harrison "嘿嘿。"
    hide harrison with quickfade
    show teacher normal at center_pos with move
    teacher "唉……你们真是我带过最差的一届。"
    teacher "凡尼特，带他们回去吧。"
    show teacher normal at char_left with move
    show vannett normal at char_right with quickfade
    vannett "好的老师，我会负责把他们好好送回去。"
    teacher "嗯。还有，凡尼特……瑞文·格雷森呢？"
    vannett "她没来，老师。"
    teacher "……我就知道。我都已经快要习惯了。"
    teacher "罢了。"
    teacher "凡尼特，我知道你们关系好，但你身为第六代凡妮莎，同时也是本届首席……"
    teacher "还是少和某些不三不四的同学一起鬼混为妙。"
    vannett "当然，老师，请您放心。"
    teacher "那就好。就这样。"
    hide teacher
    hide vannett
    with dissolve


    stop music fadeout 2.0
    sera "……"
    sera "呼……"
    sera "终于结束了……"
    play music "audio/bgm/SWFunny.wav" volume 0.5 loop
    show harrison normal at center_pos with dissolve
    harrison "是啊是啊，可累死我了。"
    # 凡尼特插话，哈里森让到左边
    show harrison normal at char_left with move
    show vannett normal at char_right with quickfade
    vannett "没有让你们写检讨就偷着乐吧，二位不、三、不、四、的、同、学。"
    sera "呜哇，首席大人又来说风凉话。"
    harrison "就是就是，明明吃水煮蛋的时候你吃得最香。跟你这种老师的狗腿子谈不来。"
    vannett "这就是倒数第二和倒数第三的友谊吗，哇啊好羡慕哦。"
    sera "你说什么呢凡尼特，上次哈里森翻墙的时候你不也跟着去了吗！"
    vannett "就是因为我没有蠢到被当场抓住，所以我才依旧是好学生啊。"
    harrison "这个家伙怎么回事……找茬吗！"
    show sigmund normal at center_pos with quickfade
    sigmund "慢，慢着，你们不会打算在这打起来吧。"
    vannett "我才懒得和野蛮人动手。"
    harrison "你说谁野蛮人呢！"
    vannett "未开化的帕弥什感染体也不会像你这样吧。"
    harrison "凡尼特！你这家伙找抽是吧！"
    sigmund "等，你们俩都少说两句。检讨会刚刚结束吧。"
    sera "哎！干嘛，继续啊！凡尼特和哈里森值得纪念的第105战正要决出胜负呢！"
    sigmund "瑟拉你也住口。"
    sera "啊！西格蒙德！你这家伙居然凶我！亏我还专门借你《空花霸王》第七卷！"
    sigmund "那和现在是两码事。"
    constructor "哔哔，哔哔，清扫，清扫，请让开道路，请让开道路。"
    sigmund "明天都要毕业了，为什么不能好好相处呢？"
    harrison "什么话，我和凡尼特这是关系好的表现。"
    vannett "谁和你关系好了，倒数第三同学。"
    sera "确实关系不错。"
    vannett "瑟拉，我看你也是还没有被老师骂够。"
    harrison "哎呀，说什么见外的话，都是一起翻过墙的交情了嘛！"
    vannett "你让开，不要靠近我。"
    constructor "哔哔，哔哔，请让开道路，请让开道路。"
    harrison "来嘛，凡尼特！最后一天了，让我们多增进增进感情怎么样啊~"
    vannett "不要，你这家伙靠近我一米以内，我就会因为你身上的傻子气息窒息而死。"
    sigmund "拜托，你们别胡闹了……"
    sera "好机会！哈里森！左右包抄！"
    vannett "啊你们两个疯子——别过来！"
    harrison "现在后悔已经晚了凡尼特！现在你也是共犯了！"
    sera "而且食堂的钥匙也是你交出来的，我们是一条绳上的蚂蚱！"
    vannett "该死——"
    sigmund "喂，你们几个，小——"
    sera "哇啊！" with hpunch
    vannett "啊——！" with hpunch
    harrison "唉唉——！" with hpunch
    # 撞翻清洁构造体（0.80 秒，压在它这句被撞断的话上）
    play sound "audio/se/prologue_cleaning_construct_crash.ogg"
    constructor "请让开道——哔哔——吱——"
    stop music fadeout 2.0
    sigmund "……"
    sera "痛痛……我的屁股……好像砸到什么……"
    harrison "啊，你们俩没事……呜哇……"
    vannett "这下好了……"
    sera "这是什么，等……这，这不是清洁构造体吗！"
    constructor "嘎吱……嘎……"
    sigmund "看起来已经彻底失去功能了……"
    vannett "还是教务处专用的，S型精密清洁构造体。"
    vannett "造价大概相当于我们四个人十年的生活费总和。"
    vannett "哈，这下好了，瑟拉芬娜。构造体可是限定资源，坏一个少一个。"
    harrison "等，那岂不是……"
    play music "audio/bgm/SWFunny.wav" volume 0.5 loop
    sera "坏了，坏了坏了坏了，完蛋了！这这这这怎么办！"
    sigmund "不必担心。只是意外的话，最多也就是写一份检讨。"
    sera "会写一晚上检讨啦！！！！说不定还要背处分啊！！！"
    harrison "背处分也不是什么大不了的问题吧。"
    sera "我和你这种随便背处分也不会影响{color=#ff0000}升格者{/color}资格的继承者不一样啦！"
    vannett "是啊，你这种家伙哪怕背一个处分，恐怕这辈子就没法成为{color=#ff0000}升格者{/color}了。"
    sigmund "不，重点不是这个吧。格式塔不会把赔偿金记在瑟拉头上吗？"
    sera "也就是说接下来我不仅要出卖劳动力，还要用个人配给支付赔偿！？"
    vannett "像你这种家伙，怕是接下来的十年里都要省吃俭用了吧。"
    sera "不要啊——怎怎怎怎么办！哈里森！西格蒙德！凡尼特！救救我啊——！"
    sigmund "不，就算你问我……"
    vannett "哈，自作自受。"
    harrison "……等一下，还有办法。"
    sera "真的吗！？哈里森！？有什么办法！？"
    harrison "没事的瑟拉，放心，好姐妹是不会让你被处分的！"
    vannett "不管你们在打什么主意，我可不打算掺和。我先回去了。"
    harrison "慢着！凡尼特，你也别在那幸灾乐祸。当时可是你推的我。"
    vannett "哈？是你自己冲过来的！"
    harrison "这就是罗生门了。而且，老师让你看着我们，结果我们打坏了这种贵重物品……"
    harrison "你觉得你完美的首席履历上会不会留下污点呢？"
    vannett "……你，你这家伙……"
    harrison "当然啦，西格蒙德作为目击者也脱不了干系吧。"
    sigmund "为，为什么……我又……"
    harrison "嘿嘿，总之——我们当然是有福同享，有难同当啦——"
    sera "还是你鬼点子多啊，哈里森！话说你到底有什么办法？"
    harrison "嗨！你别问！总之，跟我来就对了——！"
    sera "要去哪？"
    harrison "该怎么说呢……反正，先翻墙！"
    sigmund "格式塔在上……饶了我吧。"
    # ===== 场景2：发现阿尔法 =====
    # 在这里写发现阿尔法的剧情
    
    stop music fadeout 2.0
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene bg_street with pushleft
    $ renpy.pause(1.2, hard=True)
    play sound "audio/se/SW_BG.WAV" loop
    show natalia normal at center_pos with dissolve
    natalia "噗……哈哈，哈哈哈哈哈哈——！" with hpunch
    natalia "所以，这就是你们几个跑到我这来的理由？"
    play music "audio/bgm/Zero-Two-DARLINGs - 开篇5.wav" volume 0.5 loop
    # 西格蒙德接话，前辈让到左边
    show natalia normal at char_left with move
    show sigmund normal at char_right with quickfade
    sigmund "没错，就是这样，娜塔莉亚前辈。"
    natalia "因为处分通知单需要生物认证才能生效，所以先逃出学校……"
    sera "只要我们在处分录入系统之前消失，等到明天毕业典礼直接拿证走人，系统就追不到我们头上了！"
    natalia "哈哈哈哈哈哈——！" with hpunch
    natalia "这种漏洞百出的计划！真亏你们想得出来啊——！"
    natalia "堂堂首席，和准升格者，竟然因为撞坏了一个扫地机器人，结果就像是通缉犯一样来我这避难！"
    sigmund "严格来讲……我并非罪魁祸首。"
    hide sigmund
    show vannett normal at char_right
    with quickfade
    vannett "不要说得好像我是凶手一样。"
    hide vannett
    show harrison normal at char_right
    with quickfade
    harrison "哎，如果不是你非要反抗，我们也不会落到如此地步好不好！"
    hide harrison
    show vannett normal at char_right
    with quickfade
    vannett "如果法奥斯学院的评级标准是强词夺理，估计首席的名号就要落到你头上了。"
    hide vannett
    show harrison normal at char_right
    with quickfade
    harrison "那也比装清高的真首席大人要好一点吧？"
    sera "哦哦，105战要在这里开始了吗！前辈，你押谁？"
    natalia "不要在我家开擂台，赌博也禁止。就算格式塔的监察没有覆盖到我这里也不行。"
    natalia "虽然我也很想看看第105战的胜负，但你们谁要是碰坏了我的宝贝“阿西莫夫”号，我就把谁的脑袋吊到法奥斯学院的大门上当装饰。"
    harrison "……那，那当然不会的，前辈。仅限这次，我们友好相处吧，凡尼特。"
    hide harrison
    show vannett normal at char_right
    with quickfade
    vannett "难得同意你这个蠢货的意见。"
    hide vannett
    show sigmund normal at char_right
    with quickfade
    sigmund "谢天谢地……"
    sigmund "不过，话说回来，前辈，“阿西莫夫”号是？"
    natalia "嗯？你忘了吗，就是我先前说要研发的那个啊！"
    sigmund "那……那个？"
    natalia "就是那个啊！那个！"
    sigmund "是，是哪个……"
    sera "哦！我懂了！是不是那个！非牛顿流体纳米装甲·全天候泛银河系·深层地壳热液喷口探测及近地轨道突击两用·可变后掠翼式潜水艇！"
    natalia "对对！就是那个！不愧是小瑟拉，记得很清楚嘛！"
    sigmund "……你是怎么记住哪个名字的。明明……唉，算了……"
    hide sigmund
    show vannett normal at char_right
    with quickfade
    vannett "明明平时理论课的考点只要超过两行，就会触发她的大脑缓存溢出，对吧？这种构造放在黄金时代恐怕也是未解之谜。"
    hide vannett
    show sigmund normal at char_right
    with quickfade
    sigmund "……也不能这么说，也许这就是瑟拉的天赋也说不定。"
    hide sigmund
    show vannett normal at char_right
    with quickfade
    vannett "那可真是毫无意义的天赋。"
    hide vannett
    show sigmund normal at char_right
    with quickfade
    sigmund "可是，毕竟娜塔莉亚前辈也能记住……"
    hide sigmund
    show vannett normal at char_right
    with quickfade
    vannett "至少前辈还有令人望而生畏的科研天赋，不像某只刚脱了毛的猴子——"
    sera "喂！我可都听到了！"
    sera "凡尼特你这家伙——啧，怪不得隔壁班的艾丽莎会丢下你跑去和西格蒙德表白呢！"
    vannett "哈？瑟拉芬娜，你，你怎么知道——等等，西格蒙德！？"
    hide vannett
    show sigmund normal at char_right
    with quickfade
    sigmund "……不是，我没答应她。是她自己……"
    hide sigmund
    show vannett normal at char_right
    with quickfade
    vannett "瑟拉芬娜，这笔账回头算。还有，西格蒙德，你回来，你给我说清楚。"
    hide vannett with quickfade
    sera "略略略，听不见听不见，败犬的哀嚎我才听不见~"
    sera "比起那个嘴毒到损阴德的家伙，前辈，快跟我说说你的“阿西莫夫”号吧！"
    sera "它准备好下水了吗！"
    natalia "我就当什么都没听见好了。"
    natalia "至于我的小宝贝嘛。你们今天来得也巧，我正打算做第一次航行测试呢。"
    natalia "喂，哈里森，你在那也看半天了，不如干脆都来搭把手？"
    show harrison normal at char_right with quickfade
    harrison "比起潜艇，我还是更好奇凡尼特的感情史……那可是爆炸性八卦啊！"
    natalia "我的潜艇也是限量版，而且会爆炸。"
    harrison "我，我知道了啦！我来帮忙就是了！"
    harrison "但是瑟拉，这事的前因后果待会你得给我讲清楚啊！"
    natalia "很好，那么小瑟拉，就交给你设定航线咯。"
    sera "哦哦哦哦哦可以亲手摸到非牛顿流体纳米装甲·全天候泛银河系·深层地壳热液喷口探测及近地轨道突击两用·可变后掠翼式潜水艇了吗！"
    sera "荣幸至极！！前辈，目的地是哪？"
    natalia "就是那啊。"
    harrison "那？"
    natalia "那嘛，就是那，我不是跟你们讲过嘛。"
    harrison "又来了，前辈，不说清楚的话谁会知道到底是什么地方……"
    sera "哦哦！我明白了！"
    harrison "啊？！"
    sera "就是那啊哈里森！之前前辈说过的，从阿西莫夫留下的笔记手稿中解码出的那个坐标！"
    harrison "真亏你能和前辈对上电波……"
    harrison "但还是帮我回忆一下，行吗，我怎么一点印象都没有。"
    sera "要从哪开始回忆？从前辈是第九代阿西莫夫开始？"
    harrison "这种事我还是知道的啦！"
    natalia "还是我来说吧。我在继任阿西莫夫一职时，就对专属实验室进行了整理。"
    natalia "除了常规的科学理事会资料以外，还有一些在仓库中积灰的实验器具。"
    natalia "就在那堆没用的废纸和垃圾中，我找到了一个纸箱。"
    natalia "里面竟然是，那位初代阿西莫夫的亲笔手稿！"
    harrison "啊，你这么说我就有印象了。"
    harrison "前辈你之前说，那个手稿的扉页有一个加密代码来着？"
    sera "对，之后前辈就解码成功了！当时还把我们都叫过来开了个庆功宴嘛！"
    harrison "啊，我彻底想起来了。说是解码的结果是个坐标。"
    natalia "没错。这个坐标的位置是深海，想要到达那里……"
    sera "就得需要这种超级厉害的潜艇啊才行啊！"
    harrison "好，死去的记忆这就复活了。"
    harrison "瑟拉，还愣着干什么，快把航线设定好啊！"
    sera "早就弄好了！还用你说！"
    natalia "这么快？"
    natalia "如果不是格式塔不允许，我一定让小瑟拉来做我的助理。"
    natalia "不过现在不是说这种事的时候。好了，哈里森，收拾好东西，我们去海边，做好下水的准备！"
    harrison "得令！"
    harrison "那我们就先走啦！"
    hide harrison
    hide natalia
    with dissolve
    sera "啊，你们等等我……"
    sera "凡尼特，西格蒙德，你们来不来？"
    show vannett normal at center_pos with dissolve
    vannett "……好吧，今天就到这里，西格蒙德。"
    # 西格蒙德进场，凡尼特让到左边
    show vannett normal at char_left with move
    show sigmund normal at char_right with quickfade
    sigmund "……感谢首席不杀之恩。"
    vannett "之后我会找机会让你一五一十说清楚。"
    vannett "瑟拉，你给我等一下。这种时候怎么能少得了我？"
    sera "知道了知道了你扯我也没用——"
    sigmund "……谢天谢地。"
    sigmund "等等，这是……"
    sigmund "慢着！瑟拉！前辈！你们怎么把遥控器给放在这了啊！"
    sigmund "哎——等一下——"
    # ===== 场景3：打捞过程 =====
    # 瑟拉维持第一人称；群戏最多三人同屏，按对话焦点轮换。
    
    stop music fadeout 2.0
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene bg_beach with pushleft
    $ renpy.pause(1.2, hard=True)
    # 【你的标注】BGM Ding-Dong!.mp3
    play music "audio/bgm/Ding-Dong!.mp3" volume 0.5 loop
    show vannett normal at center_pos with dissolve
    vannett "……"
    vannett "我受不了了，这个音乐到底是怎么回事。"
    vannett "瑟拉，快把你的随身终端从车载音响上拔下来！"
    sera "凡尼特你这家伙太过分了，这可是黄金时代最流行的歌曲啊。"
    sera "不管是作词还是作曲，都是由格式塔完成的。可是值得纪念的珍贵音频资料呢。"
    vannett "为什么我的同学会是这种品味老土的家伙？"
    vannett "现在谁还会听AI做出来的，老掉牙的曲子？"
    sera "什么，这可是科技之美！"
    sera "凡尼特难道不懂算法旋律的美妙之处吗！"
    vannett "我才没必要懂这种东西。"
    vannett "总之，你给我拔了——"
    sera "哇！不要把你的手伸过来啊！前辈还在开车呢！"
    vannett "我宁可掉进海里粉身碎骨也不要再听这种电子噪音一秒钟了！"
    # 第二个人进场，凡尼特从中间让到左边
    show vannett normal at char_left with move
    show sigmund normal at char_right with quickfade
    sigmund "……我，我还不想掉进海里粉身碎骨啊……"
    show natalia normal at center_pos with dissolve
    natalia "我也是。你们两个家伙，给我安静！我们到了！"

    # 【你的标注】音效 SW_LowPitch ／ BGM中断 ／ 屏幕抖动
    stop music
    play sound "audio/se/SW_LowPitch.WAV"
    with hpunch
    $ renpy.pause(0.4, hard=True)

    sera "啊啊啊啊——"
    sera "差点咬到舌头！凡尼特，你干的好事！"
    vannett "如果你早点放弃你那个该死的音乐，我们就不至于是这个下场了。"
    hide sigmund
    show harrison normal at char_right
    with quickfade
    harrison "如果你们两个没有打起来，前辈也不至于要急刹车吧……"
    natalia "没错。如果我的宝贝“阿西莫夫”号有一点擦伤，我就打电话通知法奥斯学院，送你们二位一个惊喜处分大礼包。"
    vannett "不好意思前辈，刚刚是我们说话太大声了。"
    vannett "我现在就帮您把潜艇卸下来。"

    # 【你的标注】停顿 ／ 重物落地 ／ 投入水中 ／ 屏幕震动 ／ 水花特效
    hide vannett
    hide harrison
    show natalia normal at center_pos
    with dissolve

    # 潜艇卸下、砸在沙滩上（1.25 秒）。停顿正好被音效填满，不会有空档。
    play sound "audio/se/prologue_submarine_drop_sand.ogg"
    with vpunch
    $ renpy.pause(1.2, hard=True)

    # 推下水（音效 2.00 秒 / 水花 0.65 秒）。
    # 只等 0.8 秒就让瑟拉开口，剩下的水声垫在她那句话底下；水花这时已经自己淡完了。
    play sound "audio/se/prologue_submarine_splash.ogg"
    show prologue_submarine_splash_vfx at submarine_splash_burst
    $ renpy.pause(0.8, hard=True)
    hide prologue_submarine_splash_vfx

    sera "哦哦！下水了下水了"
    natalia "很好，如我所料，运行完美。"
    # 【你的标注】背景图 bg_ocean.png ／ BGM 开篇7
    scene bg_ocean with fade
    play music "audio/bgm/compressed/Zero-Two-DARLINGs - 开篇7.wav" volume 0.5 loop
    $ renpy.pause(1.0, hard=True)

    sigmund "什么都看不到呢。"
    harrison "是不是有点太黑了？"
    natalia "哎呀，还没有潜到最底部呢，耐心点，等一会就好了。"

    # 前三句只看潜艇传回的暗色海面画面，人物留在画外。
    # 讨论宝藏时回到三人构图，前辈固定在左侧。
    show natalia normal at char_left
    show sigmund normal at center_pos
    show vannett normal at char_right
    with dissolve
    sera "哦哦，会找到什么呢……好期待啊！"
    sera "会不会找到什么，海盗之王留下的，能够开启大航海时代的宝藏啊！"
    sigmund "瑟拉，你漫画看太多了……"
    vannett "就算退一万步说，真的有这种宝藏，那也是不能换成信用点的废铁。"
    sera "别这么说嘛，人多少得有点浪漫幻想吧！你看，万一我们因为发现了珍贵的考古发现被表彰……"
    hide sigmund
    show harrison normal at center_pos
    with quickfade
    harrison "私自发掘是犯罪行为哦，瑟拉。"
    sera "……天啊，你们这些家伙难道一点点海贼之魂都没有吗！"
    vannett "反倒是我有点羡慕你做白日梦的能力了。"
    natalia "有什么不好吗？反正这种程度的罪名，用阿西莫夫的权限就能摆平了。"
    hide harrison
    show sigmund normal at center_pos
    with quickfade
    sigmund "某，某种意义上前辈才是最不妙的那个……"
    natalia "嘘——！等等，有东西了！"
    # 【你的标注】背景图切换为 bg_deep_ocean.png
    # scene 会清掉所有立绘，正好借这次换景重排站位：
    # 接下来西格蒙德和哈里森要来回拌嘴（"一块石头？""不，等一下"），
    # 让他们各占一边，这四句就不用反复切换立绘。
    scene bg_deep_ocean with fade
    show sigmund normal at char_left
    show natalia normal at center_pos
    show harrison normal at char_right
    with dissolve
    sera "哦哦！在哪在哪！"
    sigmund "是这个吗？看起来是……"
    harrison "……一块石头？"
    sigmund "不，等一下。一定是我们看漏了什么。既然是前辈解读的坐标，那肯定是存在什么东西的。"
    harrison "对，对啊，肯定不止一块——"
    natalia "不，这就是块石头。"
    harrison "前，前辈？"
    hide sigmund
    show vannett normal at char_left
    with quickfade
    vannett "哦呀，看来有人的海贼之魂要幻灭了哦。"
    sera "你说什么呢！真正的海贼可是到最后一刻也不会放弃的啊！"
    sera "前辈！可以把遥控器借我一下吗！"
    natalia "好呀。毕竟坐标就在这附近。经过这么多年，也有可能是发生了偏差。还是谨慎一些搜索一下吧。"
    # 接过控制器后清出海底画面；凡尼特继续在画外催促。
    hide vannett
    hide natalia
    hide harrison
    with dissolve
    play sound "audio/se/SW_Key1.WAV"
    show bg_deep_ocean:
        subpixel True
        xalign 0.5
        yalign 0.5
        zoom 1.0
        ease 0.6 zoom 1.04
    sera "前辈说得对！"
    vannett "……所以说你这家伙，我劝你最好不要浪费无所谓的时间了。"
    vannett "过会天色就暗下去了，算上返回的时间，我们最好现在就收拾一下比较好。"
    vannett "不论如何，就算是那个初代阿西莫夫，也有会出错的时候——"
    sera "啊——石头下面好像有东西！"
    vannett "哈？"
    natalia "哦哦,真的有东西耶。"
    vannett "怎么可能，刚才还没有任何东西。"
    natalia "不过看起来就只是一根树枝。"
    vannett "嗨，树枝？我还以为……"
    # 辨认结构时保持画面无遮挡，所有人围看同一幅监视画面。
    sera "慢着，慢着慢着。你们仔细看啊！这个结构，这个造型，这个凸起的链接方式……"
    sera "我总觉得这是一只手臂啊……"
    sigmund "瑟拉这么一说，我看着也有点像了。"
    show natalia normal at center_pos with dissolve
    natalia "是吗？事情开始变得有意思起来了。"
    natalia "小瑟拉的直觉一向很准。"
    natalia "一直在这里看着也看不出什么，总之先拿出来看看再说！"
    natalia "稍等，把遥控器给我，开启打捞程序！"
    sera "知，知道啦！前辈，等一下，不要挤我啊——哇啊——什么都看不到啦——"

    # 控制提示音接黑屏，省略打捞时间；回岸后的落地声交代货物已上岸。
    play sound "audio/se/SW_Key2.WAV"
    stop music fadeout 1.5
    scene black with dissolve
    $ renpy.pause(1.5, hard=True)

    # ===== 场景4：带回工作室 =====

    # 【你的标注】转场回先前的沙滩 ／ BGM m_relax.mp3
    scene bg_beach with fade
    play sound "audio/se/prologue_submarine_drop_sand.ogg" volume 0.45
    play music "audio/bgm/m_relax.mp3" fadein 2.0 volume 0.5 loop
    $ renpy.pause(1.0, hard=True)

    show vannett normal at char_left
    show natalia normal at center_pos
    show sigmund normal at char_right
    with dissolve
    vannett "所以，我们花了这么大功夫，就捞上来这么写废铜烂铁？"
    natalia "乍一看的确是废铜烂铁……凡尼特，我不怪你。"
    natalia "不过把这些铁块收集起来并复原一下的话……"
    sera "哇！前辈！是个人的形状诶！"
    natalia "你是什么时候拼好的！？小瑟拉！？"
    sigmund "抱歉，前辈，我应该拦住她的。"
    natalia "算啦，西格蒙德。你拦不住这家伙。"
    natalia "况且我本来也打算亲自修复。小瑟拉帮我省了不少事呢。"
    hide sigmund
    show harrison normal at char_right
    with quickfade
    harrison "不过……初代阿西莫夫指向的坐标，竟然只有一具遗骸吗？"
    harrison "我还以为会有那位大人留下的科研发现呢。"
    vannett "说遗骸怕也不准确吧。"
    vannett "谁家好人的骨头是金属做的？"
    harrison "哎！也许就是会有这么赛博朋克的展开呢！"
    harrison "比如阿西莫夫大人为了永生让自己机械飞升什么的！"
    natalia "阿西莫夫才不会研究那么无聊的东西。"
    natalia "不过机械的骨架啊……这么一想还真是没有头绪。"
    hide harrison
    show sigmund normal at char_right
    with quickfade
    sigmund "总不会是瑟拉总挂在嘴边的……‘原初构造体’吧？"
    sera "对哦！！！原初构造体！！"
    # 第一次失语仍留在群像里，不切特写；由角色说话高亮自然带出反应。
    vannett "……"
    hide sigmund
    show harrison normal at char_right
    with quickfade
    harrison "西格蒙德——不要总是说些不着边际的话。你看，打开奇怪的开关了吧。"
    harrison "就算是我也觉得这太不切实际了。原初构造体不是个都市传说吗？"
    natalia "喔？那具体是什么样的都市传说，我怎么没有听说过。"
    sera "啊，前辈有兴趣？我很乐意跟你说说看！"
    harrison "啊啊，开始了开始了。"
    sera "是这样的！和我们现在熟知的各种辅助生活用的构造体不同……"
    sera "听说一开始的构造体，是以军事为目的发明的！"
    # 设定讨论由西格蒙德、前辈、哈里森保持三人站位；凡尼特暂时出画。
    hide vannett
    show sigmund normal at char_left
    with quickfade
    sigmund "经典的阴谋论开场呢。"
    sera "而且啊，听说一开始驱动构造体的不是AI……"
    sera "而是人类的意识！"
    sera "所有的构造体都是人形的！"
    sera "而帕弥什战争就是因为有构造体的参与才能顺利结束的！"
    harrison "瑟拉，我不想泼你冷水啊……"
    harrison "你也知道，人形的构造体是不存在的吧。"
    sigmund "没人能够证明人形构造体确实存在过。"
    sigmund "现今的构造体申请案里也没有人型的选项。"
    sera "呜呜……可，可是……"
    sera "万，万一呢！你们难道没有想过理由吗！为什么构造体没有人形的理由！"
    natalia "从实用性角度来讲，非人形的形状可比人形方便多了。"
    natalia "不过嘛，小瑟拉说的也不无道理……"
    sigmund "前辈？"
    natalia "毕竟我们面前就摆着一个所谓的‘证明’啊。"
    sera "对，对啊！这个机械骨架！"
    sera "如果这不是构造体，这是什么！"
    sigmund "但，就算是人形，也不代表意识就是人类意识吧。"
    sigmund "毕竟在黄金时代早期，也有实验性地制作过人形机器人……"
    harrison "瑟拉，论坛的灵异和都市传说板块我也爱看。"
    harrison "但你也别当真啊！西格蒙德说得对，这也有可能是黄金时代的机器人实验的产物吧？"
    sera "黄金时代的东西哪有可能这么新！"
    harrison "锈成这样谁看得出来新旧啊！"
    natalia "也不能这么说。在深入研究之前，谁也不能下定论。"
    natalia "所以，当务之急应该是先把这玩意带回去。"
    natalia "凡尼特，西格蒙德，就麻烦你们二位搭把手，先帮我把它放到车子上吧。"
    # 点名搬运时先转向两人，让玩家看见凡尼特没有接上西格蒙德的话。
    hide harrison
    hide natalia
    show vannett normal at char_right
    with dissolve
    sigmund "明白了，前辈。那么凡尼特去负责那一边……"
    $ renpy.music.set_volume(0.55, delay=0.4, channel="music")
    pause 0.35
    vannett "……"
    sigmund "凡尼特？"
    # 保持双人构图，完整容纳回神和连续的掩饰；不插笑点震屏或急切换。
    vannett "……啊。嗯？怎么了？瑟拉又添什么新笑话了吗，这我可得记下来。"
    sera "不要给我记这种东西啊！你这家伙怎么了，怎么心不在焉的。"
    vannett "没什么，我只是在想事情。"
    vannett "我错过了猴戏吗？真遗憾。"
    sera "别遗憾啊！"
    vannett "这猴子的声音还真吵。"
    vannett "那么，你们决定这个东西要如何处理了吗？"
    # 直到他主动转回处置问题，才恢复群像与原来的音乐音量。
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    show natalia normal at center_pos with dissolve
    natalia "虽然我很想把它带到我的实验室……"
    natalia "但在进入我的分析仪之前，物理损伤的优先级要更高一点。"
    natalia "至少得让它不会散架吧。"
    sigmund "既然如此，暂时寄放在瑟拉的工坊如何？"
    sera "啊？我？"
    hide vannett
    show harrison normal at char_right
    with quickfade
    harrison "对哦，瑟拉你这家伙，格式塔不是给你分配了毕业后的工坊吗？"
    harrison "本来打算今天顺道去看一眼呢。"
    natalia "嗯？我记得小瑟拉毕业后被分配到机械修理的岗位去了对吧？"
    natalia "那不是正好专业对口吗？"
    natalia "你不介意让前辈我做你的第一个客户吧？"
    sera "诶，诶诶！"
    sera "等等等等一下，为什么突然把这么重要的事情塞给我啊！"
    sera "我还没有做好开始接单的心理准备啊！"
    harrison "但你明天一毕业不就要开始工作了吗？"
    sera "那也是明天再说！"
    # 处理骨架时把焦点交给前辈。普通淡入，不用坏笑、停手或提示音解释意图。
    hide sigmund
    hide harrison
    with dissolve
    natalia "哎呀，真遗憾。那只好先由我来简单处理一下了。"
    natalia "反正用电工胶带随便缠一下就好了吧？"
    sera "前，前辈——！"
    sera "再怎么说也不能用电工胶带啊！啊啊，还有那个轴承，前辈！不是这样放的——"
    natalia "就算小瑟拉你这么说……我也只是个业余人士……"
    sera "前——辈——！"
    show sigmund normal at char_left with quickfade
    sigmund "瑟拉，还是先把容易掉的地方固定一下吧。"
    sigmund "虽然有点不太合规……"
    show vannett normal at char_right with quickfade
    vannett "算了吧，西格蒙德。我们今天做的事有几个是合规的？"
    sera "你，你们几个……"
    natalia "小瑟拉，没关系的，身为前辈，我会完全尊重你的决定……"
    sera "我，我……"
    sera "呜呜，感觉会好麻烦啊……"
    sera "但又不能放着前辈这样乱来……"
    sera "那，那好吧！"
    sera "我明白了！那就交给我吧！"
    sera "赌上我修微波炉之神的名义！"
    sera "我一定修好这个构造体！"
    # 瑟拉说完豪言后收成单人反应镜头，再落西格蒙德的吐槽。
    hide natalia
    hide vannett
    with quickfade
    show sigmund normal at center_pos with move
    sigmund "不……所以……"
    sigmund "修微波炉之神算哪门子称号啊……"
    ## ========================================
    ## 序章结束 - 解锁工作室
    ## ========================================
    
    # 设置章节进度为1（进入第一章）
    $ chapter_progress = 1
    
    # 第一枚零件由第一章剧情发放；初访工作室不能提前修复。
    $ my_parts = 0
    
    # 淡出到黑屏（音乐一起收，别让 m_relax 硬切断）
    stop music fadeout 3.0
    scene black with fade

    centered "序章完成"
    centered "工作室已解锁"
    pause 1.5
    
    # 跳转到工作室
    jump workshop_intro


## ============================================================================
## 工作室初次引导（可选）
## ============================================================================

label workshop_intro:
    # 初访台词和教学在 story/workshop_intro.rpy，统一由主循环调用。
    jump main_hub_loop
