## ============================================================================
## 演出特效定义
## ============================================================================
## 一次性的画面特效（水花、烟尘、闪光等）在这里定义，剧本里只负责 show / hide。
## 素材来源与授权记录在 images/effects/PROLOGUE_VFX_SOURCES.md。
## ============================================================================

## ---------- 序章：潜艇入水的水花 ----------

image prologue_submarine_splash_vfx = "images/effects/prologue_submarine_splash_vfx.png"

## 水花炸开：0.10 秒窜起 → 0.55 秒继续扩散，同时淡入淡出并向上飘。
## 整段 0.65 秒，结束时 alpha 已归零，所以 show 之后隔一拍 hide 即可。
transform submarine_splash_burst:
    xpos 55
    ypos 930
    xanchor 0.0
    yanchor 1.0
    zoom 0.46
    alpha 0.0

    parallel:
        easeout 0.10 zoom 0.66
        easeout 0.55 zoom 0.72

    parallel:
        linear 0.05 alpha 1.0
        pause 0.22
        linear 0.38 alpha 0.0

    parallel:
        linear 0.65 yoffset -65
