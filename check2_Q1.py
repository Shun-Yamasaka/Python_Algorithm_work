"""
1950から2050年の間で閏年を出力するプログラム
# 4で割り切れる年は閏年、ただし100で割り切れて、400で割り切れない年は閏年ではない
"""

for i in range(1950, 2051):
    # 100で割り切れて、400で割り切れない年は閏年ではない
    if(i % 100 == 0 and i % 400 != 0):
        continue
    # 4で割り切れる年は閏年
    if(i % 4) == 0:
        print(i)


# 以下模範解答
#def is_leap_year(year):
#    if year % 4 ==0:
#        if year %100 == 0 and year % 400 !=0:
#            return False
#        else:
#            return True
#    else:
#        return False

#for i in range(1950, 2051):
#    print(str(i)+ ''+str(is_leap_year(i)))

