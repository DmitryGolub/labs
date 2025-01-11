import random
from time import sleep


class Employee:
    def __init__(self, name = "", id_number =""):
        self.name = name
        self.id = id_number

    def get_info(self):
        return f"{self.id} - {self.name}"


class Manager(Employee):

    def __init__(self, name = "", id_number = "", department = "", **kw):
        super().__init__(name, id_number)
        self.department = department

    def get_info(self):
        return f"{super().get_info()} - manager"


class Technician(Employee):
    def __init__(self, name = "", id_number = "", spec = "", **kw):
        super().__init__(name, id_number)
        self.specialization = spec

    def get_info(self):
        return f"{super().get_info()} - technician"


class TechManager(Manager, Technician):
    def __init__(self, name = "", id_number = "", department = "", spec = ""):
        super().__init__(name= name, id_number= id_number, department= department, spec= spec)
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def get_team_info(self):
        for employee in self.employees:
            print(employee.get_info())

    def get_info(self):
        return f"{Employee.get_info(self)} - techmanager"


admin = TechManager("Alice", "1", "IT", "sysadmin")

admin.get_team_info()
