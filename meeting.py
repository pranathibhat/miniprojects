class Meeting:

    def __init__(self,key):
    	
    	self.dictionary_name={1:"9 am",2:"11 am",3:"12.30pm",4:"3pm",5:"7pm",6:"9pm"}
    	self.key=key
    	self.new_dic={}

    def time_view(self):
    	mine=int(input())
    	for i in self.dictionary_name.keys():
            if(mine==i):
                self.new_dic.update({i:self.dictionary_name[i]})
                del self.dictionary_name[i]
    	    else:
    		print("Enter proper time slot")
    	return self.new_dic


a=Meeting(3)
b=a.time_view()
print(b)

