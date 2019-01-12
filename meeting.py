"""Giving the time slot list to users"""
dictionary_name={1:"9 am",2:"11 am",3:"12.30pm",4:"3pm",5:"7pm",6:"9pm"}
new_dic={}

class Meeting:
    """A class to do the functions of assigning a time slot"""
    
    def time_view():
        """A function to check if the time slot is available"""
        
        mine=int(input("Enter time slot you want:"))
        if mine in dictionary_name.keys():
            new_dic.update({mine:dictionary_name[mine]})
            del dictionary_name[mine]
        else:
            print("Enter proper time slot")
        return new_dic

    def free():
        """A function to return the updated dictionary"""
        return dictionary_name

                

def main():
    """main function to prompt the input from users"""
    while True:
        print("1. Alot 2. Remaining Slots 3.exit")
        a=int(input("Enter your choice:"))
        if a==1:
            x=Meeting.time_view()
            print("Alotted slot is :",x)
        elif a==2:
            y=Meeting.free()
            print("Free slots are:",y)
        else:
            break

main()
            
