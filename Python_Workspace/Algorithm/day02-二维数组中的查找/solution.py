
'''
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

    
    从左到右递增，从上到下递增，那么每一列的第一个元素，是这一列的最小元素，但确是这一行最大的元素
    1 2 3 4
    2 3 4 5
    3 4 5 6
    4 5 6 7
    左上角的4是第一行最大的，第4列最小的，可以根据这个元素来减小搜索范围

    运行时间：240ms
    占用内存：5860k
'''


class Solution:
    def Find(self, target, array):
        # 暴力搜索法
        '''
        for i in array:
            if i:
                for j in i:
                    if j == target:
                        return True
        return False
        '''
        # 比较顶点元素法
        i, j = 0, len(array[0]) - 1
        print(i, j)
        while i < len(array) and j >= 0:
            if target > array[i][j]:
                i = i + 1
            elif target < array[i][j]:
                j = j - 1
            else:
                return array[i][j]
        return False

if __name__ == "__main__":
    s = Solution()
    target = 5
    array = [[]]
    print(s.Find(target, array))