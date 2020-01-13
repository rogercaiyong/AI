balance = 0
deposit = 0
withdraw = 0

while True:
    operation = int(input('''请输入如下数字操作：
          1. 查询余额；
          2. 存款；
          3. 取款；
          4. 退出；
          '''))

    if operation == 1:
        print(f'您的余额是{balance}')
    elif operation == 2:
        deposit = int(input(f'请您输入存款金额:'))
        if deposit > 0:
            balance += deposit
            print(f'存款成功，您现在的余额是{balance}元。')
        else:
            print('请您输入正确的存款金额。')
    elif operation == 3:
        withdraw = int(input(f'请您输入取款金额:'))
        if balance >= withdraw:
            balance -= withdraw
            print(f'取款成功，您现在的余额是{balance}元。')
        else:
            print('您的余额不足。')
    elif operation == 4:
        continue
    else:
        print('请输入数字1 - 4进行操作。')
