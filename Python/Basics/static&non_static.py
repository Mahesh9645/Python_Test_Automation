"""
1.Static Variable (Class Variable)
---------------------------------
* its belongs to class varable and shared by all objects of the class
* its outside  __init__(constructor) method
* accessed by ClassName.variable or self.variable.
* memoryStored once for the whole class.

--------------------------------------------------------------------------------------
2. Non-Static Variable (Instance Variable)
--------------------------------------------------
Belongs to: Each object separately.
Defined: Inside __init__ using self.
Accessed by: self.variable.
Memory: Each object gets its own copy.
Changes affect: Only that specific object, not others.

"""

class Student:
    school = "ABC School"  # Static Variable

    def __init__(self, name):
        self.name = name  # Non-Static Variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name, s1.school)  # Alice ABC School
print(s2.name, s2.school)  # Bob ABC School


