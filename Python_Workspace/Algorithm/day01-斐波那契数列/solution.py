
'''
    大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）n<=39
    
    保留上一次的计算结果，以供下一次计算去使用
    
    运行时间：21ms
    占用内存：5856k
    时间复杂度：O(n)
'''


class Solution:
    def Fibonacci(self, n):
        a,b,ret = 0, 1, 0
        if n == 0:
            return 0
        while n > 0:
            a, b = b, a+b
            ret = a
            n = n - 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    print(solution.Fibonacci(4))