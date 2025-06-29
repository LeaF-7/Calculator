import tkinter as tk
from tkinter import messagebox
import math

def calc_money(rx_level):
    if rx_level == 0:
        return 0
    elif rx_level < 50:
        return 198
    elif 50 <= rx_level <= 100:
        return 396
    else:
        return 396 + (rx_level - 100) * 10

def calculate():
    try:
        level_str = entry_level.get().strip()
        piece_str = entry_piece.get().strip()
        if not level_str or not piece_str:
            messagebox.showerror("错误", "请填写所有输入项！")
            return
        level = int(level_str)
        piece = int(piece_str)
        if level <= 160:
            messagebox.showerror("错误", "您的等级不够,给爷爬")
            return
        judge = var_judge.get()
        judge2 = var_judge2.get()
        if judge == 'y':
            score = 0
        else:
            score = (level - 160) * 10
        dict1 = {'level': level, 'score': score, 'piece': piece}
        dict2 = {}
        if judge2 == 'n':
            piece2 = math.floor(score // 15)
            all_piece = piece + piece2
            if all_piece < 100:
                rx_score = 15 * (100 - all_piece)
                rx_level = math.floor(rx_score // 10)
            else:
                rx_score = 0
                rx_level = 0
                rx_piece = 0
            money = calc_money(rx_level)
            rx_piece = 100 - all_piece
            if rx_piece < 0:
                rx_piece = 0
        else:
            if piece < 80:
                if score < (80 - piece) * 25:
                    piece2 = score // 25
                    all_piece = score // 25 + piece
                else:
                    piece2 = (80 - piece) + ((score - (80 - piece) * 25) // 50)
                    all_piece = 80 + ((score - (80 - piece) * 25) // 50)
            else:
                piece2 = int(score // 50)
                all_piece = piece + int(score // 50)
            rx_score = 0
            pd_piece = all_piece
            while pd_piece < 100:
                if pd_piece < 80:
                    rx_score += 25
                    pd_piece += 1
                else:
                    rx_score += 50
                    pd_piece += 1
            rx_level = rx_score // 10
            money = calc_money(rx_level)
            rx_piece = 100 - all_piece
            if rx_piece < 0:
                rx_piece = 0
        dict2['piece2'] = piece2
        dict2['all_piece'] = all_piece
        dict2['rx_piece'] = rx_piece
        dict2['rx_level'] = rx_level
        dict2['rx_score'] = rx_score
        dict2['money'] = money

        result = (
            f'忍法帖等级：{dict1["level"]}\t'
            f'当前积分：{dict1["score"]}\t'
            f'可兑换片数：{dict2["piece2"]}\t'
            f'兑换前总片数：{dict1["piece"]}\n'
            f'兑换后总片数：{dict2["all_piece"]}\t'
            f'仍需片数：{dict2["rx_piece"]}\t'
            f'仍需等级：{dict2["rx_level"]}\t'
            f'仍需积分：{dict2["rx_score"]}\n'
            f'补满需要：{dict2["money"]}元'
        )
        label_result.config(text=result)
    except Exception as e:
        messagebox.showerror("错误", f"输入有误：{e}")

root = tk.Tk()
root.title('忍法帖计算器')
root.geometry('800x400')

# 外层Frame用于左对齐且靠顶部
center_frame = tk.Frame(root)
center_frame.pack(side='top', anchor='w', pady=30)
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(0, weight=1)

tk.Label(center_frame, text='目前忍法帖等级：').grid(row=0, column=0, sticky='e', pady=8)
entry_level = tk.Entry(center_frame, width=20, bg='lightyellow')
entry_level.grid(row=0, column=1, pady=8)

tk.Label(center_frame, text='本轮积分是否换完？').grid(row=1, column=0, sticky='e', pady=8)
var_judge = tk.StringVar(value='n')
tk.Radiobutton(center_frame, text='是', variable=var_judge, value='y').grid(row=1, column=1, sticky='w')
tk.Radiobutton(center_frame, text='否', variable=var_judge, value='n').grid(row=1, column=2, sticky='w')

tk.Label(center_frame, text='目标忍者（老秘藏/新秘藏）：').grid(row=2, column=0, sticky='e', pady=8)
var_judge2 = tk.StringVar(value='n')
tk.Radiobutton(center_frame, text='老秘藏', variable=var_judge2, value='o').grid(row=2, column=1, sticky='w')
tk.Radiobutton(center_frame, text='新秘藏', variable=var_judge2, value='n').grid(row=2, column=2, sticky='w')

tk.Label(center_frame, text='目前拥有片数：').grid(row=3, column=0, sticky='e', pady=8)
entry_piece = tk.Entry(center_frame, width=20, bg='lightyellow')
entry_piece.grid(row=3, column=1, pady=8)

btn_calc = tk.Button(center_frame, text='计算', command=calculate)
btn_calc.grid(row=4, column=0, columnspan=3, pady=15)  # 去掉 sticky 参数

label_result = tk.Label(center_frame, text='', justify='left', anchor='w', wraplength=700)
label_result.grid(row=5, column=0, columnspan=3, sticky='w', pady=10)

root.mainloop()