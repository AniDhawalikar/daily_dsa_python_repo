# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

def RPN(tokens):
    stack = []

    for i in tokens:
        if i in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()

            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(a - b)
            elif i == "*":
                stack.append(a * b)
            else:
                stack.append(a / b)
        else:
            stack.append(int(i))

    return stack[-1]


nums = ["2","1","+","3","*"]
print(RPN(nums))
