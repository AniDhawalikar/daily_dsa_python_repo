# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: Initially the stack s is empty. The last element is the top of the stack.
# Read 1 from the stream and push it to the stack. s = [1].
# Read 2 from the stream and push it to the stack. s = [1,2].
# Pop the integer on the top of the stack. s = [1].
# Read 3 from the stream and push it to the stack. s = [1,3].


def buildArray(target, n):
    result = []
    count = 1

    for i in target:
        while count < i:
            result.append("Push")
            result.append("Pop")
            count += 1
        
        result.append("Push")
        count += 1 
    return result


nums = [2,3,4]
n = 4
print(buildArray(nums, n))