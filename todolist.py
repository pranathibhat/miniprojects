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
        if y in to_do:
            done.append(y)
            to_do.remove(y)
        else:
            print("Enter the task in the list")

    def task_rem():
        print()
        print('The tasks remaining are : ')
        if to_do==[]:
            print("There are no tasks to be done")
        else:
             y=[i for i in to_do]
             print(y)

    def task_done():
        print()
        print('The tasks completed are : ')
        if done==[]:
            print("There are no tasks done")
        else:
             y=[i for i in done]
             print(y)

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

