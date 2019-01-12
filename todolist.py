to_do=[]
done=[]
class ToDoList:

    def add():
            print()
            x=input("Enter the task to add : ")
            to_do.append(x)
         
    def mark_done():
        print()
        y=input("Enter the task done : ")
        done.append(y)
        to_do.remove(y)

    def task_rem():
        print()
        print('The tasks remaining are : ')
        for z in to_do:
            print(z)

    def task_done():
        print()
        print('The tasks completed are : ')
        for z in done:
            print(z)

def main():
    
 print()
 while True:

    print("1.Add task  2.Mark done  3.Tasks remaining  4.Tasks done  5.exit")
    opt=int(input("Enter option : "))
    if opt==1:
        ToDoList.add()
    elif opt==2:
        ToDoList.mark_done()
    elif opt==3:
        ToDoList.task_rem()
    elif opt==4:
        ToDoList.task_done()
    else:
        break


main()
