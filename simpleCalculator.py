class Stack:
    def __init__(self):
        self.data = []
        
    def pop(self):
        return self.data.pop()
    
    def push(self, value):
        self.data.append(value)
        
    def isEmpty(self):
        return len(self.data) == 0

class Solution:
    
    @staticmethod
    def resolve_op(last_op, result, num):
        if last_op == '+':
            result += num
        elif last_op == '-':
            result -= num
        elif last_op == None:
            result = num
        return result

    def calculate(self, s):
        result = 0
        stack = Stack()
        begin_num = None
        last_op = None
        for index in range(len(s)):
            char = s[index]
            if char >= '0' and char <='9':
                if not begin_num:
                    begin_num = index
                if index == len(s) - 1:
                    num = int(s[begin_num:len(s)])
                    result = Solution.resolve_op(last_op, result, num)
            if char == '-' or char == '+':
                num = int(s[begin_num:index])
                result = Solution.resolve_op(last_op, result, num)
                begin_num = None
                last_op = char
            if char == '(':
                # stack time
                stack.push(last_op)
                stack.push(result)
                last_op = None
                result = 0
            if char == ')':
                other_result = stack.pop()
                other_last_op = stack.pop()
                num = int(s[begin_num:index])
                Solution.resolve_op(other_last_op, other_result, num)
        return result

s = Solution()
print(s.calculate('2 + 2'))
print(s.calculate('4 - 3'))