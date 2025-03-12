# 國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]
# 但是老師在輸入成績的時候看反了
# 把五位學生的成績改成了[35, 46, 57, 91, 29]
# 請用一個函數來將學生的成績修正。

# 輸入: [35, 46, 57, 91, 29]
# 輸出: [53, 64, 75, 19, 92]

# def modify(input:list)-> list:
#     for i in range(len(input)):
#         num = list(str(input[i]))
#         step = num[0]
#         num[0] = num[1]
#         num[1] = step
#         input[i] = int(num[0]+num[1])
#     return input

def modify(input:list)-> list:
    for i in range(len(input)):
        num = list(str(input[i]))
        for j in range(len(num)//2):
            step = num[j]
            num[j] = num[-(1+j)]
            num[-(1+j)] = step
        input[i] = ""    
        for j in range(len(num)):
            input[i] = input[i] + num[j]
    return input


input = [35, 46, 57, 91, 29]
output = modify(input)
print(output)   
