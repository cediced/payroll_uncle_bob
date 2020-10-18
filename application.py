from decimal import Decimal


class Application:
    def __init__(self):
        self.employees = []

    def execute(self, user_input):
        if self.get_command(user_input) == "AddEmp":
            self.employees.append(Employee.from_string(self.get_every_data_field(user_input)))
        elif self.get_command(user_input) == "DelEmp":
            self.delete_employee(int(self.get_every_data_field(user_input)[0]))

    def get_every_data_field(self, user_input):
        return " ".join(user_input.split()[1:]).split()

    def get_command(self, user_input):
        return user_input.split()[0]

    def search_index_employee(self, employee_id):
        for i, employee in enumerate(self.employees):
            if employee_id == employee.id:
                return i

    def delete_employee(self, employee_id):
        for i, employee in enumerate(self.employees):
            if employee_id == employee.id:
                del self.employees[i]


class Employee:
    def __init__(self, id, name, address, salary_rate, salary):
        self.id = int(id)
        self.name = name
        self.address = address
        self.salary_rate = salary_rate
        self.salary = Decimal(salary)

    @staticmethod
    def from_string(args):
        try:
            return Employee(int(args[0]),
                            args[1],
                            args[2],
                            args[3],
                            Decimal(args[4]))
        except IndexError:
            print("error, you missed one/more argument")
            raise
