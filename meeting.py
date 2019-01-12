dictionary_name={1:"9 am",2:"11 am",3:"12.30pm",4:"3pm",5:"7pm",6:"9pm"}
new_dic={}
class Meeting:
    def time_view():
        mine=int(input("Enter time slot"))
        if mine in dictionary_name.keys():
            new_dic.update({mine:dictionary_name[mine]})
            del dictionary_name[mine]
        else:
            print("Enter proper time slot")
        return new_dic
    def free():
        return dictionary_name

                

def main():
    while True:
        print("1. alot 2. remaining 3.exit")
        a=int(input("Enter:"))
        if a==1:
            x=Meeting.time_view()
            print("Alotted slot is :",x)
        elif a==2:
            y=Meeting.free()
            print("Free slots are:",y)
        else:
            break

main()
            
