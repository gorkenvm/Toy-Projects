# calculator project
# class init method attribute funct vs method

class Calc(object):
    # init metodu
    def __init__(self, a, b):
        # attribute
        self.value1 = a
        self.value2 = b

    def add(self):
        "addition a+b =result >return result"
        return self.value1+self.value2

    def multiply(self):
        "multiplication a*b = result > return result"
        return self.value1*self.value2


print("choose add(1), multiply(2)")
selection = input("select 1 or 2")

v1 = input("first value")
v2 = input("second value")
c1 = Calc(v1, v2)
add_result = c1.add()
multiply_result = c1.multiply()
print("Add:{},multiply:{}".format(add_result, multiply_result))
