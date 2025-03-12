# 國泰銀行要慶祝六十周年
# 需要買字母貼紙來布置活動空間
# 文字為"Hello welcome to Cathay 60th year anniversary"
# 請寫一個程式計算每個字母(大小寫視為同個字母)出現次數

# 輸出：
# 0 1
# 6 1
# A 4
# C 2
# E 5
# H 3
# ....(繼續印下去)

def modify(input:str):
    input = input.upper()
    output = {}
    for char in input:
        if char != " ":
            if char in output:
                output[char] += 1
            else:
                output[char] = 1    
    return sorted(output.items())

input = "Hello welcome to Cathay 60th year anniversary"
output = modify(input)
for key, value in output:
    print(key, value)