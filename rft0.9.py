import sys
import math
level = int(input('目前忍法帖等级：'))
if level < 200:
    print('您的等级不够,给爷爬')
    sys.exit(0)
judge = input('本轮积分是否换完？(y/n)：')
if judge == 'y':
    score = 0
elif judge == 'n':
    if 200 <= level <= 205:
        score = 400 + (level - 200) * 5
    elif level > 205:
        score = 425 + (math.floor((level - 205) // 5) * 50)
    else:
        score = 0  # 补充，防止未定义
else:
    score = 0  # 补充，防止未定义

ninja = int(input('目前拥有片数：'))
if ninja < 80:
    if score < (80 - ninja) * 25:
        pianshu = score // 25
        zongpianshu = score // 25 + ninja
    else:
        pianshu = (80 - ninja) + ((score - (80 - ninja) * 25) // 50)
        zongpianshu = 80 + ((score - (80 - ninja) * 25) // 50)
elif ninja >= 80:
    pianshu = int(score // 50)
    zongpianshu = ninja + int(score // 50)
else:
    pianshu = 0
    zongpianshu = ninja

rxscore = 0
pdpianshu = zongpianshu
while pdpianshu < 100:
    if pdpianshu < 80:
        rxscore += 25
        pdpianshu += 1
    elif pdpianshu >= 80:
        rxscore += 50
        pdpianshu += 1
    else:
        break

rxlevel = rxscore // 10
if rxlevel < 50:
    money = 198
elif 50 <= rxlevel <= 100:
    money = 396
elif rxlevel > 100:
    money = 396 + (rxlevel - 100) * 10
if zongpianshu >= 100:
    money = 0

rxpianshu = max(0, 100 - zongpianshu)

print(f'当前积分：{score}', end='\t')
print(f'可兑换片数：{pianshu}', end='\t')
print(f'兑换完后总片数：{zongpianshu}')
print(f'仍需片数：{rxpianshu}', end='\t')
print(f'仍需等级：{rxlevel}', end='\t')
print(f'仍需积分：{rxscore}')
print(f'补满需要：{money}元')
