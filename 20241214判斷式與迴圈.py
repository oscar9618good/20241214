# 判斷式與迴圈
# 條件
# 如果 今天氣溫低於15度 我穿羽絨衣
# 如果條件成立 就執行某動作
# 如果條件結果為真(Ture) 就執行對應程式碼
print(True, type(False)) #布林值 #數字方面用<>=來判斷對錯
temp=17  #數字17
print(temp<15)
print(temp>=16)
print(temp==17)    #是否等於數字17 #是
print(temp=="17")  #是否等於"17" 字串17  #否
print(temp!=13)    #是否不等於13  #是
print([4]==[4])    #兩個list是否相等  #是
print([1,2,3,4,5]==[5,3,1,4,2])   #兩個list是否相等 #否 #皆含12345，但list順序不一樣
print({"月份":1,"日期":2}=={"日期":2,"月份":1})   #兩個dic是否相等 #是 #皆含同keys:values，不管順序性

#and &且 or |或 必須合併兩個條件
print(5<6 and 5>2)     #True  #and需兩個皆為True才True
print(True and True)   #True
print(True & False)    #False

print(True or True)
print(True or False)
print(False | False)  #or兩個False才False

#XOR ^異或
#如果兩個輸入的布林值不同，結果為 True。
#如果兩個輸入的布林值相同，結果為 False。
print(True^True)      # False，因為兩者相同
print(False ^ True)   # True，因為兩者不同
print(True ^ False)   # True，因為兩者不同
print(False ^ False)  # False，因為兩者相同
print(5 ^ 3)          # 輸出 6，因為 5 (101) XOR 3 (011) = 6 (110)


#not
print(not True or True)     #True  #程式碼從左到右,等於print(False or True)
print(not (True or True))   #False 反轉布林值
print(not True)             #False
print(True and True and False or True)   #True

print("a" in "apple")  #True  #a在apple裡
print("A" in "apple")  #False #A不在apple裡
print("ae"in "apple")  #False 
print(3 in [4,8,3])
print(3 in [4,8,"3"])   #"3"是字串
#print("key" in {"key": "value"})  #True #字典也可以in

temp=21
if temp<15:            #母程式 #行末加:
    print("我穿羽絨衣") #子程式 #按一下Tab縮排，退4格  #判斷不成立就不會觸發
# if temp<20:
    # print("穿夾克")   #若現溫13度，則兩件都穿 #if式一定判斷
elif temp<20:
    print("穿夾克")     #若現溫13度，則只判斷到elif以上  #else if
else:
    print("戴帽子")     #若現溫21度，則戴帽子
print("出門")

#判斷奇數偶數
# X=int(input("請輸入數字"))
# if X%2!=0:          #不能被2整除，餘數不為0
#     print("奇數")
# if X==0:            #是等於0，0為自然數
#     print("自然數") 
# elif X%2==0:        #能被2整除，餘數為0
#     print("偶數")
#優化修正後
X = int(input("請輸入數字: "))
if X == 0:
    print("自然數")
elif X % 2 != 0:
    print("奇數")
else:
    print("偶數")



#判斷輸入的數字是否為閏年 
#每4年為閏年，每100年為平年，每400年為閏年，每1000年為閏年
# X=int(input("請輸入西元年"))
# if X%1000==0 or X%400==0 or X%4==0 and X%100!=0:   #左至右，先and再or #and不要放行末
#     print("閏年")
# else:
#     print("平年")
#優化修正後
X = int(input("請輸入西元年: "))
if X % 1000 == 0:     #規則最大放前面行，1000>400>4
    print("閏年")
elif X % 400 == 0:
    print("閏年")
elif X % 100 == 0:
    print("平年")
elif X % 4 == 0:
    print("閏年")
else:
    print("平年")
#ChatGPt答
def is_leap_year(year):
    """
    判斷年份是否為閏年。
    :param year: 數字型年份
    :return: True 如果是閏年，否則 False
    """
    if year % 1000 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    

#練習:做一個月分列表，輸入月份，判斷該月是何季節
month=["1","2","3","4",'5','6','7','8','9','10','11','12',"一","二",'三',"四","五",'六','七','八','九',"十","十一","十二"]
X=str(input("輸入月份"))
if X in month[0:2] or X in month[12:14]:      #[0:2]是輸出1,2位 #列表範圍:不用0當第一位
    print("春季")
elif X in month[3:5] or X in month[15:17]:
    print("夏季")
elif X in month[6:8] or X in month[18:20]:
    print("秋季")
elif X in month[9:11] or X in month[21:23]:
    print("冬季")
else X not in month:         #else 不需要條件，直接使用 else: 即可。 #else 不應與條件如 X not in month 結合，這應該寫在 if 條件中。
    print("請輸入正確月份")
#優化修正後
# 英文數字和中文數字的月份列表
english_months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
chinese_months = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]
month = english_months + chinese_months   # 合併列表
X = str(input("輸入月份: "))               # 輸入月份
if X in english_months[:3] or X in chinese_months[:3]:
    print("春季")
elif X in english_months[3:6] or X in chinese_months[3:6]:
    print("夏季")
elif X in english_months[6:9] or X in chinese_months[6:9]:
    print("秋季")
elif X in english_months[9:12] or X in chinese_months[9:12]:
    print("冬季")
else:
    print("請輸入正確月份")


#迴圈 #重複執行某一段程式碼 #while 
#continue #pass #break
#當條件成立，就執行一次某些動作，直至條件不成立為止
I="hungry"
NUM=0                #從0開始
# while I=="hungry":   
    # print("eat")               #到這邊執行會一直輸出eat，慎用  #無限迴圈，永遠都是True
while I=="hungry" and NUM<100:   #吃100口為止
    print("eat")               
    NUM=NUM+1                  #計數一次  #先算等號右邊，再賦值回左邊
#等於NUM+=1
    print(NUM)
    if NUM==30:                #如果吃到第30口
        continue               #跳過這次迴圈，從頭開始
        print("throw")
    elif NUM==15:
        pass                   #pass可以註解掉
        print("pass")
    elif NUM==20:              #吃到20口直接停止
        break
        print("break")
    print("eat")


#練習:在1~30內取3的倍數，但不要30
X=type(int)
X+=1

while X%3==0 and X<31:
    print(X)
#優化修正後
X = 1                   #從1開始
while X < 30:           # 範圍是 1 到 29
    if X % 3 == 0:      # 檢查是否是 3 的倍數
        print(X)        #先print出來再+1去判斷
    X += 1              # 遞增 X
#或下列
count=0
while count<30:
    count+=1            #先+1再進入子程式判斷
    if count%3==0:
        if count ==30:  #+1後遇到30則停止
            break
        print(count)
#或使用for迴圈
for X in range(1, 30):  # 範圍是從 1 到 29（不包含 30）
    if X % 3 == 0:      # 檢查是否是 3 的倍數
        print(X)

#random 隨機碼
import random              #導入random模組
rdint=random.randint(1,6)  #從1~6隨機抽
print(rdint)

#練習:骰3次骰子，都沒出現4即獲勝
import random
rdint=random.randint(1,6)
print(rdint)
while rdint!=4:
    rdint=random.randint(1,6)
    print(rdint)
    if rdint!=4:
        rdint=random.randint(1,6)
        print(rdint)
    elif rdint!=4:
        print("YOU WIN!")
#優化修正後
import random
tries = 0           # 計算擲骰子的次數
win = True          # 假設玩家可以獲勝
while tries < 3:    # 限制最多擲骰子 3 次
    rdint = random.randint(1, 6)
    print(f"第 {tries + 1} 次擲骰: {rdint}")
    tries += 1
    if rdint == 4:
        print("你擲到了 4，挑戰失敗！")
        win = False # 玩家輸了
        break       # 結束迴圈
if win:
    print("YOU WIN!")

#練習: 終極密碼(猜一個隨機數的大小)
X=int(input("輸入一個小於100的數字"))
import random
rdint=random.randint(1,99)
print(rdint)
while X<rdint:
    print("大一點")
    break
while X>rdint:
    print("小一點")
    break
X=int(input("再試一次"))
if X==rdint:
    print("YOU WIN!")
#優化修正後
import random
X = int(input("輸入一個小於 100 的數字: ")) # 輸入一個小於 100 的數字
rdint = random.randint(1, 99)              # 隨機生成一個 1~99 的數字
print("目標數字已生成，請開始猜測！")
while True:                                # 反覆猜測，直到猜中為止
    if X < rdint:
        print("大一點")
    elif X > rdint:
        print("小一點")
    else:
        print("YOU WIN!")
        break  # 猜中時結束遊戲
   
    X = int(input("再試一次: "))           # 再次輸入數字
#進階
import random
max=99
min=1
answer=random.randint(1,99)
count=0
while True:
    print("數字介於{}到{}之間".format(min,max))
    guess=int(input())
    if guess==answer:
        print("你猜對了!")
        break
    elif guess<answer:
        print("再大一些")
        min=guess+1
    elif guess<answer:
        print("再小一些")
        max=guess-1
#優化修正後
import random
max = 99
min = 1
answer = random.randint(1, 99)
count = 0
while True:
    print("數字介於 {} 到 {} 之間".format(min, max))
    guess = int(input("請輸入你的猜測: "))
    count += 1                    # 計算猜測次數
    if guess == answer:
        print("你猜對了! 總共猜了 {} 次".format(count))
        break
    elif guess < answer:
        print("再大一些")
        min = guess + 1           # 更新最小範圍，避免重複猜同一數字
    elif guess > answer:
        print("再小一些")
        max = guess - 1           # 更新最大範圍，避免重複猜同一數字

#for迴圈 對著每一個項目執行動作
# for 等泡 in一盒燈泡:
#     拿起(燈泡)
#     檢查(燈泡)
#     拿起(燈座)
#     組裝(燈泡,燈座)
st="abcdefg"
for s in st:
    print(s)    #string裡的abcdefg一個一個抓起來print一遍

li=[1,2,3,4,5,"OK",[0.3,"NOT"]]
for s in li:
    print(s)    #list裡的12345一個一個抓起來print一遍

dic={"A":1,"B":2,"C":3,"D":4,"E":5}
for s in dic:
    print(s)        #dictionary裡的key一個一個抓起來print一遍
    print(dic[s])   #dictionary裡的Value一個一個抓起來print一遍
    print(s,dic[s])

#range
print(list(range(10)))     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10)))   #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2))) #[1, 3, 5, 7, 9]

for n in range(10):
    print("run")   #噴10次run

#練習: 九九乘法表
for I in range(1,10):      #母迴圈
    #print(I)
    for J in range(1,10):  #子迴圈
        print("{}X{}={:<3}".format(I,J,I*J),end=" ")
#或以下
multiplication_table_with_range = ""
for i in range(1, 10):
    row = "  ".join([f"{i}×{j}={i*j}" for j in range(1, 10)])
    multiplication_table_with_range += row + "\n"
print(multiplication_table_with_range)

#費波納契數列
前,中=1,0
for n in range(20):
    後=中+前
    前,中=中,後
    print(後)
