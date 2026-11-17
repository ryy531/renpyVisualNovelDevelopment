## ============================================================================
## 立绘自动高亮：只有正在说话的人是亮的，其他人压暗
## ============================================================================
## 用法：在 characters.rpy 里给角色加 callback=partial(char_fade, "立绘tag")。
## 没有立绘的角色（瑟拉、旁白、构造体）用 callback=dim_all —— 他们说话时全体压暗。
## ============================================================================

transform dark_in:
    alpha 1.0
    matrixcolor BrightnessMatrix(0.0)

transform dark_out:
    # 以乘法压暗保留深色衣物的纹理，避免固定减亮度把阴影压成纯黑。
    alpha 1.0
    matrixcolor TintMatrix("#777777")

transform center_pos:
    xalign 0.5
    yalign 1.0


init -1 python:
    from functools import partial

    ## 参与自动高亮的立绘 tag。
    ## 以后给新角色加立绘时，记得往这个列表里补一个，否则他不会被压暗。
    HIGHLIGHT_TAGS = [
        "teacher", "sigmund", "vannett", "harrison", "natalia", "constantine",
        "alpha", "raven", "laurel",
    ]

    def _restage(tag, effect):
        """把 tag 这个立绘按原位重新显示一遍，换上 effect（dark_in / dark_out）。

        位置要从当前的 at_list 里取回来，否则重新 show 会把角色弹回屏幕中央。
        """
        attrs = renpy.get_attributes(tag)
        if not attrs:
            return False
        at_ls = renpy.get_at_list(tag)
        pos = at_ls[0] if at_ls else renpy.store.center_pos
        renpy.show(tag + " " + " ".join(attrs), at_list=[pos, effect])
        return True

    def _dim_others(speaker):
        """把除 speaker 以外、当前在场的立绘全部压暗。speaker 传 None 表示全体压暗。

        这里直接问 Ren'Py 当前在场有谁，而不是维护自己的名单——
        旧版依赖一个每句话都会被清空的字典，导致"压暗其他人"从来没真正生效过，
        而且刚 show 上来、还没开口的角色会一直保持满亮。
        """
        showing = renpy.get_showing_tags()
        for tag in HIGHLIGHT_TAGS:
            if tag == speaker or tag not in showing:
                continue
            _restage(tag, renpy.store.dark_out)

    def char_fade(character_name, event_name, *args, **kwargs):
        """有立绘的角色：说话时自己高亮，其他人压暗。"""
        if event_name != "begin" or character_name is None:
            return
        if not _restage(character_name, renpy.store.dark_in):
            # 说话者此刻不在场（比如画外音），那就只把在场的其他人压暗
            _dim_others(None)
            return
        _dim_others(character_name)

    def dim_all(event_name, *args, **kwargs):
        """没有立绘的角色（瑟拉、旁白、构造体）说话时：场上没人该高亮，全体压暗。"""
        if event_name == "begin":
            _dim_others(None)
