# input  : n = {()({}{})}
# output : True
# input  : n = {())}
# output : False


def check_brackets(n):
    if len(n) == 1:
        return False
    
    reference_dict = { ")":"(", "}":"{", "]":"[" }

    stack = []
    for i in n:
        if i not in reference_dict:
            stack.append(i)
        else:
            if not stack:            # extra closing bracket
                return False
            if stack.pop() != reference_dict[i]:
                return False
            
    return len(stack) == 0


n = "{{[]}[[]]}"
print(check_brackets(n))

