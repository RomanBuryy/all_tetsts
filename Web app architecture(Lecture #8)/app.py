from flask import Flask

class Developer():

    def __init__(self, first_name, last_name, programming_language):
        self.first_name = first_name
        self.last_name = last_name
        self.programming_language = programming_language

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.programming_language}"


class Developer_list():
    dev_list = []

    def __add__(self, developer):
        self.dev_list.append(developer)
        return self

    def __str__(self):
        all_devs = [(dev.first_name, dev.last_name, dev.programming_language) for dev in self.dev_list]
        return f"{all_devs}"

    def delete_dev(self):
        del self.dev_list[0]


dev1 = Developer("Roman", "First", "Python")
dev2 = Developer("Igor", "Second", "Java")
dev3 = Developer("Ira", "Third", "Ruby")
dev4 = Developer("Nazar", "Third", "PHP")

a = Developer_list()
a += dev1
a += dev2
a += dev3
a += dev4

app = Flask(__name__)

@app.route('/')
def developer_controller():
    dev = Developer("Roman", "Buryy", "Python")
    return f"{dev}"

@app.route('/remove_developer')
def remove_developer():
    try:
        a.delete_dev()
        return f"{a}"
    except:
        return f"List is empty"
