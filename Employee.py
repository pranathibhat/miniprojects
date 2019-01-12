class Employee:

    def __init__(self,eid,name):

        self.eid=eid
        self.name=name

class HourlyEmployee(Employee):

    def __init__(self,eid,name,Time,HourSalary):
        
        super().__init__(eid,name)
        self.Time=Time
        self.HourSalary= HourSalary
        

    def earning(self):

        return self.Time * self.HourSalary

    def __str__(self):

        return "%s:%s"%("Hourly Employee", super().__str__())

class SalariedEmployee(Employee):

    def __init__(self,eid,name,weekSalary,Leave):

        super().__init__(eid,name)
        self.weekSalary=weekSalary
        self.Leave=Leave

    def earning(self):

        return self.weekSalary-(self.weekSalary/7 * self.Leave)

    def __str__(self):

        return "%s:%s" %("Salaried Employee", super().__str__())

class Manager(Employee):

    def __init__(self,eid,name,salary,employees=None):

        super().__init__(eid,name)

        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

        self.salary=salary

    def earning(self):

        return self.salary

    def __str__(self):

        return "%s: %s" %("Manager", super().__str__())

    def add_emp(self,emp):

        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):

        if emp in self.employees:
            self.employees.remove(emp)
        
        
class Executive(Employee):

    def __init__(self,eid,name,pay):

        super().__init__(eid,name)
        self.pay=pay

    def earning(self):

        return self.pay

    def __str__(self):

        return "%s : %s" % ("Executive", super().__str__())


a=Manager("7","pan",6)
b=a.earning()
c=a.add_emp("nana")
print(b)
print(c)

    


        

    
    
