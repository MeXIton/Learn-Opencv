#Function เสริม
# สร้าง Constructor
class Employee:
    def __init__(self,name,salary,age,department):
        # Protected Attribute
        self._name = name 
        self._salary = salary
        self._age = age 
        self._department = department

# Public Method       
def _showData(self):
    print("Name = {}".format(self.name))
    print("Salary = {}".format(self.salary))
    print("Age = {}".format(self.age))
    print("department = {}".format(self.department))
    
# สร้าง Object

    obj1 = Employee()
    obj1.detail("Tonnam",50000,17,"OWE")
 
    obj2 = Employee()
    obj2.detail("Namton",30000,18,"Programer")
    
    print(isinstance(obj1,Employee)) #True 
    
    print(dir(obj1)) #Listออกมา
    
    print(obj1.__class__) # Check ว่ามาจาก Class อะไร
    
    obj1._showData()
    
    