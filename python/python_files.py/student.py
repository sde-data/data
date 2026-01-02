class Student:
    def __init__(self, name, age, sid):
        self.name = name
        self.age = age
        self.sid = sid

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.sid)

if __name__ == "__main__":
    s = Student("Test", 0, 0)
    s.display()
# s1 = Student("Suresh", 30, 1)
# s2 = Student("Ravi", 22, 2)

# s1.display()
# s2.display()

