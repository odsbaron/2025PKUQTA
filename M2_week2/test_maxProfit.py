def maxProfit(prices, D, fee):
    n = len(prices)
    if n == 0:
        return 0

    # hold[i]: 第i天持有股票的最大收益
    # cool[i]: 第i天不持有股票的最大收益
    hold = [-float('inf')] * n
    cool = [0] * n

    hold[0] = -prices[0]

    for i in range(1, n):
        # 今天持有 = max(昨天持有, 从冷冻期结束后买入)
        if i > D:
            hold[i] = max(hold[i-1], cool[i-D-1] - prices[i])
        else:
            # 冷冻期内只能从初始状态买入
            hold[i] = max(hold[i-1], -prices[i])

        # 今天不持有 = max(昨天不持有, 今天卖出)
        cool[i] = max(cool[i-1], hold[i-1] + prices[i] - fee)

    return max(0, cool[n-1])


# 测试案例
if __name__ == "__main__":
    # 测试1: 基本测试
    prices1 = [1, 2, 3, 0, 2]
    D1 = 1
    fee1 = 0
    print(f"测试1: prices={prices1}, D={D1}, fee={fee1}")
    print(f"结果: {maxProfit(prices1, D1, fee1)}")
    print(f"预期: 3 (买入@1, 卖出@3, 冷冻1天, 买入@0, 卖出@2)")
    print()

    # 测试2: 有手续费
    prices2 = [1, 3, 2, 8, 4, 9]
    D2 = 1
    fee2 = 2
    print(f"测试2: prices={prices2}, D={D2}, fee={fee2}")
    print(f"结果: {maxProfit(prices2, D2, fee2)}")
    print(f"预期: 8 (买入@1, 卖出@8-2=6, 冷冻, 买入@4, 卖出@9-2=7, 总收益=(6-1)+(7-4)=8)")
    print()

    # 测试3: 较长冷冻期
    prices3 = [1, 2, 3, 4, 5]
    D3 = 2
    fee3 = 0
    print(f"测试3: prices={prices3}, D={D3}, fee={fee3}")
    print(f"结果: {maxProfit(prices3, D3, fee3)}")
    print(f"预期: 4 (买入@1, 卖出@5)")
    print()

    # 测试4: 价格递减
    prices4 = [5, 4, 3, 2, 1]
    D4 = 1
    fee4 = 0
    print(f"测试4: prices={prices4}, D={D4}, fee={fee4}")
    print(f"结果: {maxProfit(prices4, D4, fee4)}")
    print(f"预期: 0 (不交易)")
    print()

    # 测试5: 单个价格
    prices5 = [1]
    D5 = 1
    fee5 = 0
    print(f"测试5: prices={prices5}, D={D5}, fee={fee5}")
    print(f"结果: {maxProfit(prices5, D5, fee5)}")
    print(f"预期: 0 (无法交易)")
    print()

    # 测试6: 高手续费
    prices6 = [1, 2, 3, 4, 5]
    D6 = 1
    fee6 = 10
    print(f"测试6: prices={prices6}, D={D6}, fee={fee6}")
    print(f"结果: {maxProfit(prices6, D6, fee6)}")
    print(f"预期: 0 (手续费太高，不值得交易)")
