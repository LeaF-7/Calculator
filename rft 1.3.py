import sys
import math
def calc_money(rx_level: int) -> int:
    """
    此函数计算所需的金额
    根据忍法帖等级计算所需金额。
    :param rx_level: 忍法帖等级
    :return: 所需金额
    """
    if not rx_level > 0:
        return 0 # 0表示不需要金额。
    elif rx_level != 0 and rx_level <= 150:
        pd_level = math.floor(rx_level / 50)
        return pd_level * 198
    else:
        pd_level = rx_level - 150
        return (3 * 198) + pd_level * 10

def pd_score(all_piece : int ) -> int:
    """
    此函数计算还需多少积分兑换整卡
    :param all_piece: 积分兑换完后所有片数
    :return: 兑换整卡还需多少积分
    """
    pd_score = 0
    while all_piece < 100: # 进入循环计算兑换整卡需要的积分
        if all_piece >= 80:
            pd_score += 50
            all_piece += 1
        else:
            all_piece += 1
            pd_score += 25
    return pd_score
try:
    level = int(input('目前忍法帖等级：'))
except ValueError:
    print("请输入有效数字！")
    sys.exit(1)
if level <= 160:
    print('您的等级不够,给爷爬')
    sys.exit(0)
judge = input('本轮积分是否换完？(y/n)：')
if judge == 'y':
    score = 0
else:
    score = (level - 160 ) * 10
judge2 = input('目标忍者(o/n)：')
try:
    piece = int(input('目前拥有片数：'))
except ValueError:
    print("请输入有效数字！")
    sys.exit(1)
if judge2 == 'n': # 新秘藏忍法帖计算规则
    piece2 = math.floor(score // 15)
    all_piece = piece + piece2
    if all_piece < 100:
        rx_score = 15 * (100 - all_piece)
        rx_level = math.floor(rx_score // 10)
    else:
        rx_score = 0
        rx_level = 0
    money = calc_money(rx_level)
    rx_piece = max(0,100 - all_piece)
else: # 老秘藏忍法帖计算规则
    if piece < 80:
        if score < (80-piece)*25:
            piece2 = score//25
            all_piece = score//25+piece
            rx_score = pd_score(all_piece)
            rx_level = rx_score // 10
        elif score >= (80-piece)*25:
            piece2 = (80-piece)+((score-(80-piece)*25)//50)
            all_piece = 80+((score-(80-piece)*25)//50)
            rx_score = pd_score(all_piece)
            rx_level = rx_score // 10
    elif 80 <= piece < 100:
        piece2 = int(score//50)
        all_piece = piece + int(score//50)
        rx_score = pd_score(all_piece)
        rx_level = rx_score // 10
    else:
        piece2 = 0
        all_piece = piece
        rx_score = 0
        rx_level = rx_score // 10
    money = calc_money(rx_level)
    rx_piece = max(0,100 - all_piece)
lst1 = ['level', 'score', 'piece', 'piece2', 'all_piece', 'rx_piece', 'rx_level', 'rx_score', 'money']
lst2 = [globals()[name] for name in lst1]
result_dict = dict(zip(lst1, lst2))
# Output the results
print(
    f'忍法帖等级：{result_dict["level"]}\t'
    f'当前积分：{result_dict["score"]}\t'
    f'可兑换片数：{result_dict["piece2"]}\t'
    f'兑换前总片数：{result_dict["piece"]}\t\n'
    f'兑换后总片数：{result_dict["all_piece"]}\t'
    f'仍需片数：{result_dict["rx_piece"]}\t'
    f'仍需等级：{result_dict["rx_level"]}\t'
    f'仍需积分：{result_dict["rx_score"]}\t\n'
    f'补满需要：{result_dict["money"]}元\t'
      )
