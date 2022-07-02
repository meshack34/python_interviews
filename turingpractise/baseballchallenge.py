a=[5,2,'+','C','D']
b=[]
class Solution(object):
    def calPoints(self, a):
        stack = []
        for op in a:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)
    calPoints(a,b)