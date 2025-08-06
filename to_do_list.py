import os
def get_input(a, b):
    while True:
        try:
            x = int(input(' '))
            if a <= x <= b:
                return x
            else:
                print(f'❌ Invalid input. Enter a number between {a} to {b}')
        except ValueError:
            print(f'❌ Invalid input. Press a number between {a} to {b}')

def main():
    print('===To-do-list===')
    print('1.To view tasks list')
    print('2.To add a new task')
    print('3.To remove a task')
    print(f'4.To mark a task as done\n')
    print('Enter your choice:')
    x = get_input(1, 4)
    if x == 1:
        view_task()
    if x == 2:
        add_task()
    if x == 3:
        remove_task()
    if x == 4:
        mark_done()
def view_task():
    path= os.getcwd()
    full_path = os.path.join(path, 'tasks.txt')
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            list_tasks = f.readlines()
            if not list_tasks:
                print("File is empty")
                main()
            else:
                for lines in list_tasks:
                    print(lines.strip())
    except FileNotFoundError:
        print('you do not have the tasks file')
        main()

def add_task():
    print('==ADD TASK===')
    path= os.getcwd()
    full_path=os.path.join(path, 'tasks.txt')
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            list_tasks = f.readlines()
        try:
            b=int(list_tasks[-1].strip().split('|')[0])
        except ValueError:
            b=0
        except IndexError:
            b=0
    except FileNotFoundError:
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write('')
        b=0
        pass
    b+=1

    task=str(input('Enter task name that you want to add: '))
    com_task=f'{b}|[ ]|{task}\n'


    path= os.getcwd()
    full_path = os.path.join(path, 'tasks.txt')
    if os.path.getsize(path + '\\tasks.txt')==0:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(com_task)
    else:
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write(com_task)
    with open(full_path, 'r', encoding='utf-8') as file:
        list_ts=file.readlines()
        for lines in list_ts:
            print(lines.strip())
def remove_task():
    print('==REMOVE TASK===')
    path= os.getcwd()
    full_path = os.path.join(path, 'tasks.txt')
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            tasks = f.readlines()
            for line in tasks:
                print(line.strip())
            try:
                k = tasks[-1].strip().split('|')[0]
            except IndexError:
                print('There is no task in your list yet')
                main()
    except FileNotFoundError:
        print('You have not added any tasks!')
        main()
        pass



    print('Enter task number that you want to remove: ')
    h=int(k)
    j=get_input(1, h)
    with open(full_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        j-=1
        del lines[j]
        task_list=[]
        d=1
        for line in lines:
            b=str(d)
            new_line=line.replace(line.strip().split('|')[0],b)
            task_list.append(new_line)
            d+=1
    path= os.getcwd()
    full_path = os.path.join(path, 'tasks.txt')
    with open(full_path, 'w', encoding='utf-8') as f:
        f.writelines(task_list)
    for lines in task_list:
        print(lines.strip())

def mark_done():
    print('==MARK DONE===')
    path= os.getcwd()
    full_path = os.path.join(path, 'tasks.txt')

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            list=f.readlines()
            b=list[-1].strip().split('|')[0]
            for lines in list:
                print(lines.strip())
    except FileNotFoundError:
        print('You have not added any tasks!')
        main()
    print('Enter the number of task that you want to mark done.')
    c=int(b)
    x=get_input(1, c)

    new_list=[]
    for line in list:
        if int(line.strip().split('|')[0])==x:
            new_line= line.replace(line.strip().split('|')[1],'✅')
            new_list.append(new_line)
        else:
            new_list.append(line)
    for lines in new_list:
        print(lines.strip())
    with open(full_path, 'w', encoding='utf-8') as f:
        f.writelines(new_list)



main()