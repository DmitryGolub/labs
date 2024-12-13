class Employee:
    def __init__(self, id_employee, name, **kwargs):
        self._id_employee = id_employee
        self._name = name

    def get_info(self):
        return f"Employee: id - {self._id_employee} name - {self._name}"


class Manager(Employee):
    def __init__(self, id_employee, name, department=None, **kwargs):
        super().__init__(id_employee, name, department=department, **kwargs)
        if not isinstance(department, str):
            raise ValueError("Укажите отдел правильно. Тип должен быть str")
        self._department = department

    def get_info(self):
        return f"Manager: id - {self._id_employee} name - {self._name} department - {self._department}"

    def manage_project(self):
        return f"Manage project - {self._department}"


class Technical(Employee):
    def __init__(self, id_employee, name, specialization=None, **kwargs):
        super().__init__(id_employee, name, specialization=specialization, **kwargs)
        if not isinstance(specialization, str):
            raise ValueError("Укажите специальность правильно. Тип должен быть str")
        self._specialization = specialization

    def get_info(self):
        return (f"Technical: id - {self._id_employee} name - {self._name} "
                f"specialization - {self._specialization}")

    def perform_maintenance(self):
        return f"Performing maintenance - {self._specialization}"


class TechManager(Manager, Technical):
    def __init__(self, id_employee, name, department=None, specialization=None):
        super().__init__(id_employee, name, department=department, specialization=specialization)
        self._team = []

    def add_employee(self, data):
        if not isinstance(data, Employee):
            raise ValueError("Неверный тип данных. Объект должен иметь тип Employee")
        self._team.append(data)

    def get_info(self):
        return (f"TechnicalManager: id - {self._id_employee} name - {self._name}"
                f" specialization - {self._specialization} department - {self._department}")

    def get_team_info(self):
        return "Team:\n" + "\n".join([attender.get_info() for attender in self._team])


tm = TechManager(12, "sdf", department="12", specialization="programmer")
e1 = Employee(1, "Dima")
e2 = Employee(2, "Ivan")
e3 = Employee(3, "Dasha")
m1 = Manager(4, "Anton", department="12")
t1 = Technical(5, "Vlad", specialization="programmer")
team = [e1, e2, e3, m1, t1]

for attender in team:
    tm.add_employee(attender)


print(m1.get_info())
print(m1.manage_project())
print(t1.get_info())
print()
print("-----")
print(tm.get_info())
print(tm.get_team_info())
print("-----")
