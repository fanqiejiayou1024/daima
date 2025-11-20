h, w = eval(input())
bmi = w / pow(h, 2)
print("bmi为：{:.2f}".format(bmi))
who, dom = " ", " "
if bmi < 18.5:
    who = "偏瘦"
elif bmi < 25:
    who = "正常"
elif bmi < 30:
    who = "偏胖"
else:
    who = "肥胖"

if bmi < 18.5:
    dom = "偏瘦"
elif bmi < 24:
    dom = "正常"
elif bmi < 28:
    dom = "偏胖"
else:
    dom = "肥胖"

print("bmi指标:国际：{}，国标：{}".format(who, dom))
