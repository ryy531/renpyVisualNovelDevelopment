## ============================================================================
## 角色定义与立绘配置
## ============================================================================
## 本文件包含游戏中所有角色的定义和立绘配置
## ============================================================================

## 导入自动高亮所需的函数
init python:
    from functools import partial

## ============================================================================
## 角色定义
## ============================================================================

## 主角（第一人称视角，不显示立绘）
## callback=dim_all：她说话时场上没有人该高亮，所有立绘一起压暗。
## 不加这个的话，她说话时立绘会停在上一个人的高亮状态；而刚 show 上来、
## 还没开口的角色更是会一直满亮——那就是"只有说话的人高亮"失效的原因。
define sera = Character("瑟拉", color="#ff8833", callback=dim_all)  # 橙色

## 序章角色（添加自动高亮）
define teacher = Character("老师", callback=partial(char_fade, "teacher"))
define constructor = Character("构造体", callback=dim_all)
define sigmund = Character("西格蒙德", color="#996633", callback=partial(char_fade, "sigmund"))
define vannett = Character("凡尼特", color="#9966cc", callback=partial(char_fade, "vannett"))
define harrison = Character("哈里森", color="#ffee99", callback=partial(char_fade, "harrison"))
define natalia = Character("娜塔莉亚", color="#8b0000", callback=partial(char_fade, "natalia"))

## 后续章节角色（添加自动高亮）
define alpha = Character("阿尔法", color="#ff0000", callback=partial(char_fade, "alpha"))
## 鸦羽本体定义。写对话时不要直接用它——用 raven（鸦语自动加密封装）
## 或 raven_x（机密预加密台词），两者定义在 systems/crow_speech.rpy
define raven_base = Character("鸦羽",
    color="#4da6ff",
    who_outlines=[(2, "#ff0000", 0, 0)],
    callback=partial(char_fade, "raven")
)
define laurel = Character("Laurel-II", color="#f4e4c1", callback=partial(char_fade, "laurel"))

## 旁白（无名字显示）—— 同样全体压暗
define narrator = Character(None, callback=dim_all)

## 系统提示（可选）
define system = Character("系统", color="#00ff00", what_color="#00ff00")


## ============================================================================
## 立绘定义
## ============================================================================
## 命名规则：image [角色名] [表情]
## 例如：image teacher normal 对应文件 teacher_normal.png
## ============================================================================

## ---------- 序章角色立绘 ----------
## 老师（取消注释后启用）
image teacher normal = "images/characters/teacher_normal.png"

## 西格蒙德
image sigmund normal = "images/characters/sigmund_normal.png"

## 凡尼特
image vannett normal = "images/characters/vannett_normal.png"

## 哈里森
image harrison normal = "images/characters/harrison_normal.png"

## 娜塔莉亚
image natalia normal = "images/characters/natalia_normal.png"


## ---------- 后续章节角色立绘 ----------
## 阿尔法（红色名字）
# image alpha normal = "images/characters/alpha/alpha_normal.png"

## 鸦羽（蓝色名字+红色描边）
# image raven normal = "images/characters/raven/raven_normal.png"

## Laurel-II（淡金色月亮色）
# image laurel normal = "images/characters/laurel/laurel_normal.png"


## ============================================================================
## 立绘位置定义
## ============================================================================
## 双人对话参考原作：人物分居两侧，中央留出大块背景。
## 用画布中心定位；xalign 会同时改变锚点，宽立绘容易挤向中央。
## 1920 宽画面下中心约为 326 / 1594，比默认 left/right 各向外移 174。
## 保持原尺寸、底部对齐；单人继续使用 center_pos。
transform char_left:
    xpos 0.17
    xanchor 0.5
    yalign 1.0

transform char_right:
    xpos 0.83
    xanchor 0.5
    yalign 1.0


## ============================================================================
## 使用说明
## ============================================================================
## 
## 1. 显示立绘：
##    show teacher normal              # 居中显示
##    show teacher normal at char_left  # 左侧显示（宽间距）
##    show teacher normal at char_right # 右侧显示（宽间距）
## 
## 2. 切换表情：
##    show teacher smile               # 直接切换
##    show teacher smile with dissolve # 溶解切换
## 
## 3. 隐藏立绘：
##    hide teacher                     # 隐藏指定角色
##    hide teacher with dissolve       # 溶解隐藏
## 
## 4. 对话：
##    teacher "对话内容"               # 显示立绘的角色
##    sera "对话内容"                  # 主角（不显示立绘）
##    "旁白内容"                       # 无名字旁白
## 
## ============================================================================
