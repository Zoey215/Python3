print('-'*20, '欢迎使用员工管理系统', '-'*20)

emps = ['孙悟空\t18\t男\t花果山']
while True:
    print('请选择操作：')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    user_choose = input('请选择[1-4]:')
    print('-' * 62)
    if user_choose == '1':
        print('\t序号\t姓名\t年龄\t性别\t住址')
        n = 1
        for emp in emps:
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choose == '2':
        emp_name = input('请输入姓名：')
        emp_age = input('请输入年龄：')
        emp_gender = input('请输入性别：')
        emp_address = input('请输入住址：')
        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        print('以下员工将被添加到系统中')
        print('-' * 62)
        print('姓名\t年龄\t性别\t住址')
        print(emp)
        print('-' * 62)
        user_confirm = input('请确认该操作[Y/N]:')
        if user_confirm == 'y' or user_confirm == 'yes':
            emps.append(emp)
            print('添加成功')
        else:
            print('操作已取消')
    elif user_choose == '3':
        del_num = int(input('请输入要删除的员工的序号:'))
        if 0 < del_num <= len(emps):
            del_i = del_num - 1
            print('以下员工将被删除')
            print('-' * 62)
            print('\t序号\t姓名\t年龄\t性别\t住址')
            print(f'\t{del_num}\t{emps[del_i]}')
            print('-' * 62)
            user_confirm = input('请确认该操作[Y/N]:')
            if user_confirm == 'y' or user_confirm == 'yes':
                emps.pop(del_i)
                print('删除成功')
            else:
                print('操作已取消')
    elif user_choose == '4':
        print('欢迎使用，再见！')
        input('点击回车键退出')
        break
    else:
        print('你的输入有误，请重新输入！')
        print('-'*62)

