income_list = []
spend_list = []
daily_balance = {}
final_balance = 0

for i in range(7):
    income = float(input(f'请输入过去第{i+1}天的收入:'))
    income_list.append(income)

for i in range(7):
    spend = float(input(f'请输入过去第{i+1}天的支出：'))
    spend_list.append(spend)

for i in range(7):
    daily_balance[f'第{i + 1}天结余'] = income_list[i] - spend_list[i]
    final_balance += daily_balance[f'第{i + 1}天结余']

print(f'过去7天的收入列表是{income_list}')
print(f'过去7天的支出列表是{spend_list}')
print(f'每天的结余是{daily_balance}')
print(f'最终的结余是{final_balance}')
