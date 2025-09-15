class StudentForm:
    def __init__(self, name, age, subjects):
        self.name = name          
        self.age = age     
        self.subjects = subjects  
    def introduction(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")
        print("My subjects are:")
        for subject in self.subjects:
            print(f" - {subject}")
        print()  
student1 = StudentForm("Alice", 14, ["Math", "English", "Science"])
student2 = StudentForm("Bob", 15, ["History", "Geography", "opt.maths"])
student3 = StudentForm("Charlie", 13, ["Computer Science", "samajik", "Music"])

student1.introduction()
student2.introduction()
student3.introduction()