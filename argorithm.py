"""
给定一个数组，挑选出和值最大的一个子数组，
条件是相邻元素不能同时选择

思路：遍历一次数组，设置两个变量：
    包含当前元素的最大值 curMax
    包含前一个元素的最大值preMax
    在遍历过程过不断更新上述两个变量：
    curMax = current +preMax' (preMax'表示上一轮中的值)
    preMax = max(preMax', curMax')

"""
def maxList(myList):
    length = len(myList)
    preMax = 0
    curMax = 0
    temp = 0
    for i in range(0, length):
        temp = myList[i] + preMax
        preMax = max(curMax, preMax)
        curMax = temp
    return max(curMax, preMax)

"""
给定一个整数序列，a0, a1, a2, …… , an（项可以为负数），
求其中加和（sum）最大的连续子序列。
例如： [-2，1，-2，3，10，-4，7，2，5，-2，1]
的加和连续最大子序列为[3,10,-4,7,2,5]

思路：动态规划
参考博客 https://blog.csdn.net/hs794502825/article/details/7956730

"""
def maxSum(myList):
    #考虑数组只有一个负元素
    sum = myList[0]
    thisSum = 0
    for i in range(1, len(myList)):
        thisSum += myList[i]
        if thisSum > sum:
            sum = thisSum
        elif thisSum > 0:
            pass
        elif thisSum < 0:
            thisSum = 0
    return sum

if __name__ == "__main__":
    #myList = [-2, 1, -2, 3, 10, -4, 7, 2, 5, -2, 1]
    myList = [-2]
    print(maxSum(myList))


    #myList = [2, 3, 4, 1, 9, 3, 2, 3, 3, 4] 
    #print(maxList(myList))
    
    
    
