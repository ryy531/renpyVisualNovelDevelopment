## 文字逐字显示；点击补全文字后，留出短暂的阅读缓冲再允许推进。
## 玩家默认文字速度、自动播放和快进设置统一放在 options.rpy。
define config.default_text_cps = 40

## 从最后一个字显示完毕开始计时（包括点击后立即补全的情况）。
## 只拦截手动推进，不改变自动播放、主动快进或剧情内的定时停顿。
define dialogue_dismiss_delay = 0.25
default _dialogue_text_ready_at = None

init python:
    import time as _dialogue_time

    def _dialogue_progress_callback(event, interact=True, **kwargs):
        global _dialogue_text_ready_at

        if not interact:
            return

        # show 对每个 {w}/{p} 分段也会触发；读档、回滚会重新显示当前段。
        if event == "show":
            _dialogue_text_ready_at = None
        elif event == "slow_done":
            # UI 刷新不应反复延长保护时间。
            if _dialogue_text_ready_at is None:
                _dialogue_text_ready_at = _dialogue_time.monotonic()
        elif event == "end":
            _dialogue_text_ready_at = None

    def _dialogue_allow_dismiss():
        # Ren'Py 先处理“点击补全”，再判断能否离开当前句。
        # 因此文字仍在播放时，首次点击依然可以正常补全。
        return (
            _dialogue_text_ready_at is not None
            and _dialogue_time.monotonic() - _dialogue_text_ready_at
                >= dialogue_dismiss_delay
        )

    # 追加全局回调，保留每个角色已有的立绘高亮回调。
    config.all_character_callbacks.append(_dialogue_progress_callback)
    config.say_allow_dismiss = _dialogue_allow_dismiss
