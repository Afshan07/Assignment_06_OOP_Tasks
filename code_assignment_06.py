# -------------------------------
# Task 1: Using self
# -------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 = Student("Ali", 85)
student1.display()


# -------------------------------
# Task 2: Using cls
# -------------------------------

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

obj1 = Counter()
obj2 = Counter()
Counter.show_count()
# Task 3: Public Variables and Methods
# -------------------------------------

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} car is starting!")

# Object create karke access karna
my_car = Car("Toyota")
print(my_car.brand)
my_car.start()
# Task 4: Private Variables and Methods
# --------------------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def __show_balance(self):      # Private method
        print(f"Balance: {self.__balance}")

    def access_balance(self):
        self.__show_balance()

# Object create karke access karna
account = BankAccount(5000)
account.access_balance()
# Task 5: Protected Variables and Methods
# ----------------------------------------

class Employee:
    def __init__(self, name, salary):
        self._name = name        # Protected variable
        self._salary = salary    # Protected variable

    def _show_details(self):     # Protected method
        print(f"Name: {self._name}, Salary: {self._salary}")

# Object create karke access karna
emp = Employee("John Doe", 50000)
emp._show_details()
# Task 6: Class Variables and Class Methods
# ------------------------------------------

class Bank:
    bank_name = "ABC Bank"   # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Object create karke access karna
bank1 = Bank()
bank2 = Bank()

print(bank1.bank_name)
print(bank2.bank_name)

# Change bank name
Bank.change_bank_name("XYZ Bank")

print(bank1.bank_name)
print(bank2.bank_name)
# Task 7: Static Variables and Static Methods
# --------------------------------------------

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Static method ko bina object banaye call karna
result = MathUtils.add(5, 7)
print(f"Sum: {result}")
# Task 8: Constructors and Destructors
# -------------------------------------

class Logger:
    def __init__(self):
        print("Logger object created!")

    def __del__(self):
        print("Logger object destroyed!")

# Object create karke dekhna
log = Logger()

# Jab program end hota hai ya manually del(log) karte hain to destructor call hota hai
# Task 9: Access Modifiers: Public, Private, and Protected
# ---------------------------------------------------------

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn           # Private variable

# Object create karte hain
emp = Employee("Alice", 50000, "123-45-6789")

# Access public variable
print(f"Public: {emp.name}")

# Access protected variable
print(f"Protected: {emp._salary}")

# Access private variable (direct access will cause error)
# Correct way: using _ClassName__variableName
print(f"Private: {emp._Employee__ssn}")
# Task 10: The super() Function
# ------------------------------

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)     # super() se parent class ka constructor call
        self.subject = subject

# Object create karte hain
teacher = Teacher("Mr. Smith", "Mathematics")
print(f"Name: {teacher.name}, Subject: {teacher.subject}")
# Task 11: Instance Methods
# ---------------------------

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Object create karte hain
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
# Task 12: Class Methods
# -----------------------

class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Objects create karke dekhte hain
book1 = Book("Python 101")
book2 = Book("Learning AI")

print(f"Total books: {Book.total_books}")
# Task 13: Static Methods
# ------------------------

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# Static method call karte hain
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is {temp_f}°F")
# Task 14: Composition
# ---------------------

class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

# Engine object create karke Car ko pass karte hain
engine = Engine()
my_car = Car(engine)
my_car.start_car()
# Task 15: Aggregation
# ----------------------

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Aggregation: reference to Employee

# Employee object banate hain
emp = Employee("Alice")

# Department object mein employee ko associate karte hain
dept = Department("HR", emp)

print(f"Departme# Task 16: Method Resolution Order (MRO) and Diamond Inheritance
# ----------------------------------------------------------------

class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):
    pass

# D ka object create karke show() call karte hain
obj = D()
obj.show()
nt: {dept.department_name}, Employee: {dept.employee.name}")
# Task 17: Function Decorators
# -------------------------------

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Function call karte hain
say_hello()
# Task 18: Class Decorators
# ---------------------------

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Object create karte hain
p = Person("John")
print(p.greet())
# Task 19: Property Decorators: @property, @setter, and @deleter
# ---------------------------------------------------------------

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price!")

    @price.deleter
    def price(self):
        del self._price

# Object create karte hain
p = Product(100)
print(p.price)

p.price = 150
print(p.price)

del p.price
# Task 20: callable() and __call__()
# ------------------------------------

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Object create karte hain
double = Multiplier(2)

# Test callable
print(callable(double))  # True

# Object ko function ki tarah call karte hain
print(double(10))  # Output: 20
# Task 21: Make a Custom Class Iterable
# ----------------------------------------

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

# Object create karte hain aur loop lagate hain
cd = Countdown(5)
for number in cd:
    print(number)
