class Developer():
    language = ""

    def __init__(self, years_experience: int, name: str):
        self.years_experience = years_experience
        self.name = name

    def __str__(self):
        return f"{self.name} - {self.years_experience} years, {self.language}"

    def __call__(self):
        return f"I use {self.language} to write code. It is class Developer() magic method"

    def about(self):
        if self.years_experience <= 3:
            print(f"My name is {self.name} and I am a Junior Developer.")

        elif self.years_experience <= 5:
            print(f"My name is {self.name} and I am a Middle Developer.")

        else:
            print(f"My name is {self.name} and I am a Senior Developer.")

    def write_code(self):
        print("I am a developer and I write code")


class PythonDeveloper(Developer):
    language = "Python"

    def write_code(self):
        print(f"I use {self.language} to write code")


class JavaDeveloper(Developer):
    language = "Java"

    def write_code(self):
        print(f"I use {self.language} to write code")


class RubyDeveloper(Developer):
    language = "Ruby"

    def write_code(self):
        print(f"I use {self.language} to write code")
