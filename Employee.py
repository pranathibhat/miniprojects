class Employee:

    raise_amount=1.08

    def __init__(self,eid,name):
        self.eid=eid
        self.name=name

    def __str__(self):
        return "%s %s"%(self.eid, self.name)

    def isValid(self,value):
        if value>0:
            raise ValueError,"Attriubute value (%s) must be positive value" %value
        else:
            return value

class HourlyEmployee(Employee):

    def __init__(self,eid,name,Time,HourSalary):
        
        Employee.__init__(self,eid,name)
        self.Hoursdone=self.isValid(int(Time)))
        self.SalaryPerHour=self.isValid(float(HourSalary))
        

    def earning(self):

        return self.Hoursdone * self.SalaryPerHour

    def __str__(self):

        return "%s:%s"%("Hourly Employee", Employee.__str__(self))

class SalariedEmployee(Employee):

    def __init__(self,eid,name,regSal,off):

        Employee.__init__(self,eid,name)
        self.weekSalary=self.isValid(float(regSal))
        self.Leave=self.isValid(int(off))

    def earning(self):

        return self.weekSalary-(self.weekSalary/7 * self.Leave)

    def __str__(self):

        return "%s:%s" %("Salaried Employee", Employee.__str__(self))

class Manager(Employee):

    def __init__(self,eid,name,salary):

        Employee.__init__(self,eid,name)
        self.salary=self.isValid(float(salary))

    def earning(self):

        return self.salary

    def __str__(self):

        return "%s: %s" %("Manager", Employee.__str__(self))

class Executive(Employee):

    def __init__(self,eid,name,pay):

        Employee.__init__(self,eid,name)
        self.pay=self.isValid(float(pay))

    def earning(self):

        return self.pay

    def __str__(self):

        return "%s : %s" % ("Executive", Employee.__str__(self))

class Fire(Employee):

    def __init__(self,eid,name):

        Employee.__init__(self,eid,name)
        

    
    
