"""
 * @Author: zuofanxiu 
 * @Date: 2018-08-07 21:11:34 
 * @Last Modified by: zuofanxiu
 * @Last Modified time: 2018-08-07 22:46:16
"""

"""
冒泡排序(实现正序排列)

思路：从数组中第一个数开始，相邻两个数进行比较和交换，(前数大于后数则交换位置)
    直到比较到最后一个数，此时已将最大的数交换放置到了数组最后的位置，也就常
    说的完成了一轮冒泡。如果发生交换，则重复遍历，如果未发生交换，则数组有序，
    排序结束，此时时间复杂度为O(n)
稳定排序，适用初始状态基本有序的序列
"""
def bubbleSort(mylist):
    #设置一个标记，若在第一轮中没有发生交换，说明初始序列有序，无需再遍历
    flag = True
    for i in range(len(mylist)):
        for j in range(len(mylist)-1):
            if(mylist[j] > mylist[j+1]):
                #交换两个数的大小(不借助额外内存)
                mylist[j] = mylist[j] +mylist[j+1]
                mylist[j+1] = mylist[j] - mylist[j+1]
                mylist[j] = mylist[j] - mylist[j+1]
                #发生交换，改变标记信息
                flag = False
        #标志为真，说明序列本身有序，无需遍历排序了
        if (flag):
            break
    return mylist
# 测试
#print(bubbleSort([1, 2, 2]))

"""
快速排序(不稳定排序)

思路：通常选定第一个数作为分区标准x，依次和后面的数比较，比x小的放x前面，
    比x的放x后面，完成第一轮排序，确定了x的最终位置。以x为界限，形成
    左右两个新的排序数组，对两个分区分别重复上述过程。以此类推，直到
    被左右数组长度为1位置

适用：每次划分左右数组，左右数组长度基本差不多
"""
#参数：数组，指定快排序列的起始位置
def quickSort(mylist, low, high):
    #函数出口
    if low >= high:
        return 
    #第一个数作为分区标准
    pivot = mylist[low]
    left = low
    right = high
    #左右向中间靠拢扫面，一轮扫描完毕指向同一个位置
    while(left!=right):
        #从右向左扫描，找到第一个小于pivot的数，交换到左边
        while pivot <= mylist[right] and left < right:
            right-=1
        mylist[left]=mylist[right]
        #从左向右扫描，找到第一个大于pivot的数，交换到右边
        while pivot >= mylist[left] and left < right:
            left+=1
        mylist[right]=mylist[left]
    #确定pivot的最终位置
    mylist[left] = pivot
    #处理两个分区数组
    quickSort(mylist, low, left-1)
    quickSort(mylist, left+1,high)

"""
#测试
if __name__ == "__main__":
    li = [3, 4, 5, 2, 1]
    quickSort(li, 0, len(li)-1)
    print(li)
    """

"""
直接插入排序(稳定排序)

思路：从待排序的n个记录中的第二个记录开始，依次与前面的记录比较并寻找
插入的位置，每次外循环结束后，将当前的数插入到合适的位置。
"""

def insertSort(mylist):
    for i in range(1, len(mylist)):
        #当前待排序元素
        data = mylist[i]
        #从后往前遍历已排序的部分
        for j in range(i, -1, -1):
            #mylist[j-1]是已排序部分的最后一个元素，即待比较的第一个元素
            if mylist[j-1] > data :
                #元素后移
                mylist[j] = mylist[j-1]
            else:
                #否则j就是待插入位置,结束循环
                break
        mylist[j] = data
    return mylist
"""
#测试
if __name__ == "__main__":
    print(insertSort([1,2,2]))
"""

"""
shell排序（不稳定排序）

对直接插入排序的一种改进
思路：对相邻指定距离(增量d)的元素进行插入排序，不断把距离缩小到1，完成排序
    一般建议初始 d = n/2，往后每次循环对半取值
    或者指定增量序列[d1, d2,...dn=1]
"""
def  shellSort(mylist):
    #增量逐步折半减小
    d = len(mylist)//2
    print("初始增量：", d)
    while d > 0:
        for i in range(d, len(mylist)):
            #待比较元素
            data = mylist[i]
            print("data=", data)
            #有序序列中待比较元素
            j = i - d
            print("mylist[j]=", mylist[j])
            while mylist[j] > data and j >= 0:
                #分组元素后移
                mylist[j+d] = mylist[j]
                #j指向再前一个元素
                j -= d
            #待排元素插入
            mylist[j+d] = data
        d //= 2
    return mylist

"""
#测试
if __name__ == "__main__":
    print(shellSort([5, 2, 4, 8, 9, 1, 4, 4]))
"""

"""
简单选择排序 （不稳定排序）

思路：：从待排序列中选出最小的一个数据元素与第一个位置的记录交换；
    然后在剩下的记录当中再找最小的与第二个位置的记录交换，循环到
    只剩下最后一个数据元素为止。
    """
def selectSort(mylist):
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            if mylist[i] > mylist[j]:
                #交换元素
                mylist[i] = mylist[i] + mylist[j]
                mylist[j] = mylist[i] - mylist[j]
                mylist[i] = mylist[i] - mylist[j]

    return mylist
"""
#测试
if __name__ == "__main__":
    print(selectSort([1, 2, 7, 4, 3]))
"""

"""
堆排序（不稳定排序）
性质：完全二叉树或者是近似完全二叉树
     大顶堆：父节点不小于子节点键值
     小顶堆：父节点不大于子节点键值
     左右没有大小顺序
用数组存储数据
思路： 直接认为待排序列为堆的初始化状态，然后
    从倒数第一个非叶节点元素（（n-）/2）开始调整树
"""
def heapSort(mylist):
    pass


"""
二路归并排序（不稳定排序）

思路：初始状态：16，23，100，3，38，128，23 
    第一次归并后：{6,23},{3,100},{38,128},{23}
    第二次归并后：{3,6,23,100},{23,38,128} 
    第三次归并后：{3,6,23,23,38,100,128} 
    完成排序。
"""
def mergeArray(mylist):
    #递归
    if len(mylist) <= 1:
        return mylist
    mid = len(mylist)//2
    lList = mergeArray(mylist[:mid])
    rList = mergeArray(mylist[mid:])
    return merge(lList, rList)
    
#合并两个有序序列(直接插入)
def merge(lList, rList):
    #依次取右边序列中的元素插入左序列
    for data in rList:
        #从左边序列的最后一个元素开始比较
        for i in range(len(lList)-1, -2, -1):
            if data >= lList[i]:
                break
        lList.insert(i+1, data)
    return lList

"""
if __name__ == "__main__":
    result = mergeArray([16, 23, 100, 3, 38, 128, 23])
    #result = merge([16,23,100], [3, 23, 38, 128])
    print("result:", result)
"""

"""
桶排序（不稳定）
 思路：
    待排序列中最大元素数值max,即桶的个数，桶初始化为全0的序列
    遍历待排序列，每个元素放置到对应的桶中（元素大小对应桶的位置下标）
    最后遍历桶的非零元素即为待续序列的正确排序
 
 延申：如果说待排序列中的元素值特别大，比如10000，且序列数值很零散，会出现
    很多空桶，浪费内存，此时
    考虑将元素按照某一个函数映射到一个较小范围，比如说所有数据同时缩小n倍，
    这样可以减少桶的个数
    另外单个桶里的多个元素可以用其他排序方式排序，比如插入排序

    """
def bucketSort(mylist):
    #找到序列中最大的数，作为桶的个数
    maxData = max(mylist)
    print("maxdata=", maxData)
    #创建maxData+1个桶(数据中可能包含0)，初始值为0
    buckets = [0]*(maxData+1)
    print("buckets =", buckets)
    #遍历序列，将元素放置对应的桶中
    for i in mylist:
        #第i个桶里增加1
        buckets[i]+=1
        print("buckets =", buckets)
    #取出桶里的数据
    newList = []
    for j in range(len(buckets)):
        while buckets[j] > 0:
            newList.append(j)
            print("newlist=", newList)
            buckets[j]-=1
    return newList

