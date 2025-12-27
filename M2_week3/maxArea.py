#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
盛最多水的容器 - 双指针算法实现
LeetCode 第11题
"""


def maxArea(height):
    """
    求解盛最多水的容器问题
    参数: height - 表示每条垂直线高度的整数数组
    返回: 容器能够容纳的最大水量
    """
    # 初始化左右指针
    left, right = 0, len(height) - 1
    max_area = 0

    # 当两指针未相遇时循环
    while left < right:
        # 计算当前容器面积
        current_height = min(height[left], height[right])
        current_width = right - left
        current_area = current_height * current_width

        # 更新最大面积
        max_area = max(max_area, current_area)

        # 贪心策略：移动较短的一边
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def main():
    """主函数 - 运行测试示例"""
    print("=" * 50)
    print("盛最多水的容器 - 双指针算法测试")
    print("=" * 50)

    # 测试示例1
    print("\n【示例 1】")
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result1 = maxArea(height1)
    print(f"输入: {height1}")
    print(f"输出: {result1}")
    print(f"解释: 选择 height[1]=8 和 height[8]=7")
    print(f"      面积 = min(8,7) × (8-1) = 7 × 7 = 49")

    # 测试示例2
    print("\n【示例 2】")
    height2 = [1, 1]
    result2 = maxArea(height2)
    print(f"输入: {height2}")
    print(f"输出: {result2}")
    print(f"解释: 面积 = min(1,1) × (1-0) = 1 × 1 = 1")

    # 测试示例3
    print("\n【示例 3】")
    height3 = [4, 3, 2, 1, 4]
    result3 = maxArea(height3)
    print(f"输入: {height3}")
    print(f"输出: {result3}")
    print(f"解释: 选择 height[0]=4 和 height[4]=4")
    print(f"      面积 = min(4,4) × (4-0) = 4 × 4 = 16")

    # 测试示例4
    print("\n【示例 4】")
    height4 = [1, 2, 1]
    result4 = maxArea(height4)
    print(f"输入: {height4}")
    print(f"输出: {result4}")
    print(f"解释: 选择 height[0]=1 和 height[2]=1")
    print(f"      面积 = min(1,1) × (2-0) = 1 × 2 = 2")

    print("\n" + "=" * 50)
    print("测试完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
