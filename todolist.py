to_do=[]
done=[]
class ToDoList:

    """A class that handles the task of a to-do list"""

    def add():
        

        """A  function that adds the tasks to list"""
        print()
        x=input("Enter the task to add : ")
        to_do.append(x)
	     
    def mark_done():
        """A function that marks the task as done when the user says the particular
            task is done"""
        
        print()
        y=input("Enter the task done : ")
        if y in to_do:
            done.append(y)
            to_do.remove(y)
        else:
            print("Enter the task in the list")

    def task_rem():
        """A function that returns the user with a list of things yet to be done"""
        
        print()
        print('The tasks remaining are : ')
        for z in to_do:
            print(z)

    def task_done():
        """A function that returns the user with a list of tasks that are done"""
        
        print()
        print('The tasks completed are : ')
        for z in done:
            print(z)

def main():

    """Asking user for the input for the functions defined above"""
    
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
