from utils.Task_1 import JavaDeveloper, PythonDeveloper, RubyDeveloper
from utils.Task_2 import E
from utils.Task_3 import IT_company


if __name__ == "__main__":
    print("\n")
    print(" ------------------------------ Task_1 ------------------------------")
    print("\n")
    python_dev = PythonDeveloper(10, "Roman")
    python_dev.about()
    python_dev.write_code()
    print("\n")

    java_dev = JavaDeveloper(5, "Igor")
    java_dev.about()
    java_dev.write_code()
    print("\n")

    ruby_dev = RubyDeveloper(4, "Ira")
    ruby_dev.about()
    ruby_dev.write_code()
    print("\n")

    print(ruby_dev())
    print(python_dev())
    print(java_dev())
    print("\n")
    print(" ------------------------------ Task_2 ------------------------------")
    print("\n")
    print(E.mro())
    print("\n")
    print(" ------------------------------ Task_3 ------------------------------")
    print("\n")
    java_dev_2 = JavaDeveloper(6, "Segiy")
    ruby_2 = RubyDeveloper(4, "Ostap")
    ruby_3 = RubyDeveloper(8, "Ostap")
    python_dev_2 = PythonDeveloper(1, "Olga")
    company_list = IT_company()
    company_list += python_dev
    company_list += java_dev
    company_list += ruby_dev
    company_list += ruby_2
    company_list += java_dev_2
    company_list += ruby_3
    company_list += python_dev_2
    print("Sorted list: ", company_list)
    print("\n")
    company_list.fired_employee("Ostap")
    print("Delete method:", company_list)
