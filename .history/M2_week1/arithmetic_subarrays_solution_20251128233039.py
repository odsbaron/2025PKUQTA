"""
Arithmetic Subarrays - 动态规划解法

问题：给定整数数组 nums，返回等差子数组的数量。
等差子数组：至少3个元素，相邻元素差值相等。

解题思路：
=========
动态规划 - O(n) 时间复杂度

状态定义：
- dp = 以当前元素结尾的等差子数组个数

状态转移：
- 如果 nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
    dp = dp + 1  # 可以延续等差数列
    total += dp
- 否则:
    dp = 0  # 重置

举例：nums = [1, 2, 3, 4]
- i=2: [1,2,3] 是等差，dp=1，total=1
- i=3: 可延续，dp=2，新增 [2,3,4] 和 [1,2,3,4]，total=3
"""


def numberOfArithmeticSlices(nums):
    """
    动态规划解法

    时间复杂度：O(n)
    空间复杂度：O(1)

    参数:
        nums: 整数数组

    返回:
        等差子数组的总数
    """
    n = len(nums)
    if n < 3:
        return 0

    total = 0  # 总的等差子数组数量
    dp = 0     # 以当前元素结尾的等差子数组个数

    for i in range(2, n):
        # 检查是否能延续等差数列
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp += 1
            total += dp
        else:
            dp = 0  # 无法延续，重置

    return total


# 测试案例
if __name__ == "__main__":
    test_cases = [
        {
            "input": [1, 2, 3, 4],
            "expected": 3,
            "explanation": "We have 3 arithmetic slices: [1,2,3], [2,3,4] and [1,2,3,4]"
        },
        {
            "input": [1],
            "expected": 0,
            "explanation": "Single element, no arithmetic subarrays"
        },
        {
            "input": [1, 2, 3, 4, 6, 8, 10, 12],
            "expected": None,  # 需要计算
            "explanation": "Two separate arithmetic sequences"
        }
    ]

    print("=" * 70)
    print("Arithmetic Subarrays - 动态规划解法测试")
    print("=" * 70)

    for i, test in enumerate(test_cases, 1):
        nums = test["input"]
        expected = test["expected"]
        result = numberOfArithmeticSlices(nums)

        print(f"\nExample {i}:")
        print(f"Input:  nums = {nums}")
        print(f"Output: {result}")
        if expected is not None:
            status = "✅" if result == expected else "❌"
            print(f"Expected: {expected} {status}")
        print(f"Explanation: {test['explanation']}")

        # 详细展示找到的等差子数组
        if result > 0:
            print(f"\n找到的等差子数组：")
            count = 0
            dp_debug = 0
            for j in range(2, len(nums)):
                if nums[j] - nums[j-1] == nums[j-1] - nums[j-2]:
                    dp_debug += 1
                    # 输出所有以 nums[j] 结尾的等差子数组
                    for length in range(3, dp_debug + 3):
                        if j - length + 1 >= 0:
                            count += 1
                            subarray = nums[j - length + 1:j + 1]
                            diff = subarray[1] - subarray[0]
                            print(f"  {count}. {subarray} (差值={diff})")
                else:
                    dp_debug = 0

    print("\n" + "=" * 70)
    print("核心要点")
    print("=" * 70)
    print("""
时间复杂度：O(n) - 只需遍历数组一次
空间复杂度：O(1) - 只需常数空间

关键理解：
- dp 表示以当前位置结尾的等差子数组个数
- 每次延续等差数列时，新增的子数组数量 = dp + 1
- 无法延续时重置 dp = 0
    """)
