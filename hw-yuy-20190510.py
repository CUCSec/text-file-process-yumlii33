num_list = list()
number = 0
with open( r'log_files\201811123011.log', 'r', encoding='utf8') as f:
    for line in f:
        num = line.split(',')[1]
        num = num[4:]
        if num == '201811123011':
            number = number + 1
print("打卡次数为：{}".format(number))
