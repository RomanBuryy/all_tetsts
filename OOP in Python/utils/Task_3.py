class IT_company():
    employee_list = []

    def __add__(self, employee):
        if employee.years_experience <= 3:
            print(f"{employee.name} have years_experience <= 3")
            print("\n")
        else:
            self.employee_list.append(employee)

        return self

    def __str__(self):
        all_devs = sorted(
            [(employee.name, employee.years_experience, employee.language) for employee in self.employee_list],
            key=lambda x: x[1])
        all_devs_format = []

        for i in all_devs:
            all_devs_format.append(f"{i[0]} - {i[1]} years, {i[2]}")

        return f"{(all_devs_format)}"

    def fired_employee(self, key_name):
        test_len = len(self.employee_list)

        for i, _ in enumerate(self.employee_list):
            if self.employee_list[i].name == key_name:
                del self.employee_list[i]
                break

        if test_len == len(self.employee_list):
            print("Key not found")
