#1. Реализуйте класс Employee, представляющий сотрудника компании. 
#Класс должен иметь статическое поле company с названием компании, а также методы:
#set_company(cls, name): метод класса для изменения названия компании
#__init__(self, name, position): конструктор, принимающий имя и должность сотрудника
#get_info(self): метод, возвращающий информацию о сотруднике в виде строки (имя, должность, название компании)
#Пример использования:
#employee1 = Employee("John", "Manager")
#employee2 = Employee("Alice", "Developer")
#print(employee1.get_info())  # Вывод:
#"""
#Name: John
#Position: Manager
#Company: ABC Company
#"""
#Employee.set_company("XYZ Company")
#print(employee2.get_info())  # Вывод:
#"""
#Name: Alice
#Position: Developer
#Company: XYZ Company
#"""
class Employee:
    company = ""

    @classmethod
    def set_company(cls, name):
        cls.company = name

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"Employee {self.name} works for company {self.company} in position {self.position}"


Employee.set_company("ABC")
employee = Employee("Adam", "IT-Manager")
print(employee.get_info()) 