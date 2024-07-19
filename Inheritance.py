# class Laptop:
#     def brand(self,brand_name,price):
#         print(f"(brand_name) is a brand")
#         print(f"The price of (brand_name) is:- (price)")

# class Dell(Laptop):
#     pass

# class Toshiba(Laptop):
#     pass

# obj=Dell()
# obj.brand('Dell')
# obj.brand('40000')

# tobj=Toshiba
# tobj.brand('Toshiba')
# tobj.brand('25000')


class student:
    def __init__(self):
        print("This is constructor.")

    def info(self):
        print("This is info method.")

    def __del__(self):
        print("This is destructor.")

    def __new__(cls):
        print("This is new method.")
        return object.__new__(cls)
    
    def __str__(self):
        print("This is string.")
        return object.__str__(self)
    
    def __repr__(self):
        print("This is repository.")
        return object.__repr__(self)
    
    def __add__(self):
        print("This is addition.")
        return object.__add__(self)
    
obj=student()
obj.info()
obj.__str__()

# multiple inheritance
# static method 
# class method
# properties
# excess specifier
