## ============================================================================
## 战双帕弥什：锈蚀福音 - 核心变量系统
## ============================================================================
## 本文件包含游戏的所有全局变量和基础数据操作函数
## ============================================================================

## ----------------------------------------------------------------------------
## 修复进度变量 (0-100)
## ----------------------------------------------------------------------------
default alpha_fix = 0      # 阿尔法机体修复进度
default raven_fix = 0      # 鸦羽机体修复进度
default luna_fix = 0       # Laurel-II机体修复进度

## ----------------------------------------------------------------------------
## 资源变量
## ----------------------------------------------------------------------------
default my_parts = 0       # 通用零件数量(用于修复机体)

## ----------------------------------------------------------------------------
## 玩家数据
## ----------------------------------------------------------------------------
default commander_name = "指挥官"  # 灰鸦指挥官的名字（默认值）

## ----------------------------------------------------------------------------
## 章节进度
## ----------------------------------------------------------------------------
default chapter_progress = 0  # 0=序章, 1=第一章, 2=第二章...

## ----------------------------------------------------------------------------
## 工作室状态
## ----------------------------------------------------------------------------
default workshop_location = "seraphina_workshop"  # 工作室背景(暂时只有一个)
default workshop_tutorial_seen = False          # 当前存档是否完成首次引导
default chapter1_repair_stage = "not_started"  # not_started / awaiting_repair / memory / complete
default raven_body_unlocked = False            # 后续剧情获得机体时设为 True
default laurel_body_unlocked = False           # 后续剧情获得机体时设为 True

init python:
    def workshop_repair_available():
        # 兼容已经结束第一章的旧存档；新流程在首次剧情修复后开放。
        return chapter1_repair_stage == "complete" or chapter_progress >= 2

    def workshop_alpha_name():
        # chapter_progress 表示接下来要进入的章节；2 才表示第一章已结束。
        return "阿尔法" if chapter_progress >= 2 else "？？？"

## ----------------------------------------------------------------------------
## 记忆碎片系统 - 解锁状态
## ----------------------------------------------------------------------------
## 格式: memories_unlocked[机体名][记忆编号-1] = True/False
## 例如: memories_unlocked["alpha"][0] 代表 A01 是否解锁
default memories_unlocked = {
    "alpha": [False, False, False, False, False],   # A01-A05
    "raven": [False, False, False, False, False],   # P01-P05
    "laurel": [False, False, False, False, False]   # L01-L05
}

## ----------------------------------------------------------------------------
## 记忆碎片系统 - 已读状态
## ----------------------------------------------------------------------------
## 格式: memories_read[机体名][记忆编号-1] = True/False
## 用于标记玩家是否已经观看过该记忆
default memories_read = {
    "alpha": [False, False, False, False, False],
    "raven": [False, False, False, False, False],
    "laurel": [False, False, False, False, False]
}

## ============================================================================
## 核心函数定义
## ============================================================================

init python:
    
    ## ------------------------------------------------------------------------
    ## 记忆解锁函数
    ## ------------------------------------------------------------------------
    def unlock_memory(character, memory_number):
        """
        解锁指定角色的记忆碎片
        
        参数:
            character (str): 机体名称 "alpha" / "raven" / "laurel"
            memory_number (int): 记忆编号 1-5
        
        返回:
            bool: 是否成功解锁 (如果已解锁则返回False)
        """
        if character not in memories_unlocked:
            return False
        
        index = memory_number - 1  # 转换为数组索引(0-4)
        
        if index < 0 or index >= 5:
            return False
        
        # 如果已经解锁,返回False
        if memories_unlocked[character][index]:
            return False
        
        # 解锁记忆
        memories_unlocked[character][index] = True
        return True
    
    ## ------------------------------------------------------------------------
    ## 记忆已读标记函数
    ## ------------------------------------------------------------------------
    def mark_memory_read(character, memory_number):
        """
        标记指定记忆为已读
        
        参数:
            character (str): 机体名称
            memory_number (int): 记忆编号 1-5
        """
        if character not in memories_read:
            return
        
        index = memory_number - 1
        
        if index >= 0 and index < 5:
            memories_read[character][index] = True
    
    ## ------------------------------------------------------------------------
    ## 检查记忆是否解锁
    ## ------------------------------------------------------------------------
    def is_memory_unlocked(character, memory_number):
        """
        检查指定记忆是否已解锁
        
        返回:
            bool: True=已解锁, False=未解锁
        """
        if character not in memories_unlocked:
            return False
        
        index = memory_number - 1
        
        if index < 0 or index >= 5:
            return False
        
        return memories_unlocked[character][index]
    
    ## ------------------------------------------------------------------------
    ## 检查记忆是否已读
    ## ------------------------------------------------------------------------
    def is_memory_read(character, memory_number):
        """
        检查指定记忆是否已读
        
        返回:
            bool: True=已读, False=未读
        """
        if character not in memories_read:
            return False
        
        index = memory_number - 1
        
        if index < 0 or index >= 5:
            return False
        
        return memories_read[character][index]
    
    ## ------------------------------------------------------------------------
    ## 获取已解锁记忆数量
    ## ------------------------------------------------------------------------
    def get_unlocked_count(character):
        """
        获取指定角色已解锁的记忆数量
        
        返回:
            int: 已解锁数量 (0-5)
        """
        if character not in memories_unlocked:
            return 0
        
        return sum(memories_unlocked[character])
    
    ## ------------------------------------------------------------------------
    ## 获取未读记忆数量
    ## ------------------------------------------------------------------------
    def get_unread_count(character):
        """
        获取指定角色已解锁但未读的记忆数量
        
        返回:
            int: 未读数量
        """
        if character not in memories_unlocked or character not in memories_read:
            return 0
        
        count = 0
        for i in range(5):
            if memories_unlocked[character][i] and not memories_read[character][i]:
                count += 1
        
        return count
    
    ## ------------------------------------------------------------------------
    ## 获取已解锁记忆列表
    ## ------------------------------------------------------------------------
    def get_unlocked_memories(character):
        """
        获取指定角色已解锁的记忆编号列表
        
        返回:
            list: 记忆编号列表 例如 [1, 3, 5]
        """
        if character not in memories_unlocked:
            return []
        
        result = []
        for i in range(5):
            if memories_unlocked[character][i]:
                result.append(i + 1)  # 转换为1-5编号
        
        return result
    
    ## ------------------------------------------------------------------------
    ## 修复进度相关函数
    ## ------------------------------------------------------------------------
    def add_repair_progress(character, amount):
        """
        增加指定机体的修复进度
        
        参数:
            character (str): "alpha" / "raven" / "luna"
            amount (int): 增加的数值
        
        返回:
            int: 修复后的进度值
        """
        global alpha_fix, raven_fix, luna_fix
        
        if character == "alpha":
            alpha_fix = min(100, alpha_fix + amount)
            return alpha_fix
        elif character == "raven":
            raven_fix = min(100, raven_fix + amount)
            return raven_fix
        elif character == "luna":
            luna_fix = min(100, luna_fix + amount)
            return luna_fix
        
        return 0
    
    def get_repair_progress(character):
        """
        获取指定机体的修复进度
        
        返回:
            int: 修复进度 (0-100)
        """
        if character == "alpha":
            return alpha_fix
        elif character == "raven":
            return raven_fix
        elif character == "luna":
            return luna_fix
        
        return 0

## ============================================================================
## 调试用快捷函数 (开发阶段使用,正式版可删除)
## ============================================================================

init python:
    
    def debug_unlock_all_memories():
        """调试用: 解锁所有记忆"""
        for char in ["alpha", "raven", "laurel"]:
            for i in range(5):
                memories_unlocked[char][i] = True
    
    def debug_reset_all():
        """调试用: 重置所有进度"""
        global alpha_fix, raven_fix, luna_fix, my_parts, current_chapter
        
        alpha_fix = 0
        raven_fix = 0
        luna_fix = 0
        my_parts = 0
        current_chapter = 0
        
        for char in ["alpha", "raven", "laurel"]:
            for i in range(5):
                memories_unlocked[char][i] = False
                memories_read[char][i] = False
    
    def debug_print_status():
        """调试用: 打印当前游戏状态"""
        print("=== 游戏状态 ===")
        print("章节进度: {}".format(current_chapter))
        print("修复进度: Alpha={} Raven={} Luna={}".format(alpha_fix, raven_fix, luna_fix))
        print("零件数量: {}".format(my_parts))
        print("已解锁记忆: Alpha={} Raven={} Laurel={}".format(
            get_unlocked_count("alpha"),
            get_unlocked_count("raven"),
            get_unlocked_count("laurel")
        ))
        print("未读记忆: Alpha={} Raven={} Laurel={}".format(
            get_unread_count("alpha"),
            get_unread_count("raven"),
            get_unread_count("laurel")
        ))
