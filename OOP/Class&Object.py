class College :
    principal = "Prem"       # Class attribute (shared by all College)

    # Constructor runs when you create a College
    def __init__(self,name,no):
                # Instance attributes (each teacher has its own)
        self.name = name
        self.no = no
    
        # Method (a function that belongs to the class)
    def tech(self):
        return f"Teacher name is {self.name} and ID is {self.no}"

# Create objects (instances)
t1 = College("Ram",1)
t2 = College("Sham",2)

print(t1.tech())
print(t2.name,t2.no)

print(College.principal)

# class College : defines a new type.

# self means “this object” (Python passes it automatically).

# Use instance attributes when data differs per object; use class attributes for shared facts.