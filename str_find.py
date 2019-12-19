class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    """非递归"""
    def permute(self, nums):
        nums_used = [0]*len(nums)
        nums_used_in_stack = [[] for j in range(len(nums))]
        stack = []
        allResult = []
        while(True):
            for key, num in enumerate(nums):
                if(nums_used[key] == 0):
                    if num not in nums_used_in_stack[len(stack)]:
                        stack.append(num)
                        nums_used[key] = 1
                        nums_used_in_stack[len(stack) - 1].append(num)
                        try:
                            nums_used_in_stack[len(stack)] = []
                        except IndexError:
                            pass

            if(len(stack) == len(nums)):
                result = []
                for i in stack:
                    result.append(i)
                allResult.append(result)

                while (True):
                    try:
                        x = stack.pop()
                    except IndexError:
                        return allResult
                    for key2, num2 in enumerate(nums):
                        if num2 == x:
                            nums_used[key2] = 0

                    flag = 0
                    for key3, num3 in enumerate(nums):
                        if nums_used[key3] == 0 and num3 not in nums_used_in_stack[len(stack)]:
                            flag = 1
                            break
                        else:
                            flag = 0
                    if(flag == 0):
                        continue
                    else:
                        break


class Solution1:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    '''递归'''
    def permute(self, nums):
        allResult = []
        result = []
        self.permutes(nums, result, allResult)
        return allResult

    def permutes(self, nums, result, allResult):
        # write your code here
        if nums == []:
            new_list = []
            for i in result:
                new_list.append(i)
            allResult.append(new_list)
        for num in nums:
            result.append(num)
            new_nums = []
            for x in nums:
                if x!=num:
                    new_nums.append(x)
            self.permutes(new_nums, result, allResult)
            result.pop()
        return

def main():
    print('程序初始化...')
    n = [1,2,3,4,5,6,7,8]
    X = Solution()
    X1 = Solution1()
    print('非递归：',X1.permute(n))
    print('递归:',X.permute(n))
if __name__ == '__main__':
    main()
