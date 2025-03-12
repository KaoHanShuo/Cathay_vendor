# QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號
# 從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
# 請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?

# 輸入：n值(0-100)
# 輸出：第幾順位

def modify(num:int)->int:
    people = list(range(1,num+1))
    i=0
    while len(people) > 1:
        i = (i+2) % len(people)
        people.pop(i)
    return people[0]

input = 100
output = modify(input)
print(output)