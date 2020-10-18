import unittest
from application import Application, Employee


class TestAddEmployee(unittest.TestCase):
    def test_add_hourly_employee(self):
        command_add_employee = "AddEmp 135 Jason Home H 10.0"
        application = Application()
        application.execute(command_add_employee)

        should_employee = Employee(id=135, name="Jason", address="Home", salary_rate="H", salary=10.0)
        assert should_employee.id == application.employees[0].id
        assert should_employee.name == application.employees[0].name
        assert should_employee.address == application.employees[0].address
        assert should_employee.salary_rate == application.employees[0].salary_rate
        assert should_employee.salary == application.employees[0].salary

        assert len(application.employees) == 1

    def test_formating_error(self):
        command_add_employee = "AddEmp 135 Jason H 10.0"
        application = Application()

        with self.assertRaises(IndexError):
            application.execute(command_add_employee)


class TestDeleteEmploye(unittest.TestCase):
    def test_delete_employee(self):
        command_delete_employee = "DelEmp 135"
        application = Application()
        application.execute("AddEmp 135 Jason Home H 10.0")
        self.assertEqual(len(application.employees), 1)
        application.execute(command_delete_employee)
        self.assertEqual(len(application.employees), 0)

    def test_delete_non_existing_employee(self):
        command_delete_employee = "DelEmp 140"
        application = Application()
        application.execute("AddEmp 135 Jason Home H 10.0")
        self.assertEqual(len(application.employees), 1)
        application.execute(command_delete_employee)
        self.assertEqual(len(application.employees), 1)

    def test_wrong_delete_command(self):
        command_delete_employee = "DelEmp"
        application = Application()
        application.execute("AddEmp 135 Jason Home H 10.0")
        self.assertEqual(len(application.employees), 1)

        with self.assertRaises(IndexError) as context:
            application.execute(command_delete_employee)


if __name__ == '__main__':
    unittest.main()
