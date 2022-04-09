

# %% Calculator

class Calc(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1+self.value2

    def mult(self):
        return self.value1 * self.value2

    def div(self):
        return self.value1 / self.value2

    def ext(self):
        return self.value1 - self.value2


print("Choose Add(1), Multiply(2), Division(3) or Extraction(4)")
selection = input("select 1, 2, 3 or 4")
v1 = int(input("first value"))
v2 = int(input("second value"))
c1 = Calc(v1, v2)
if selection == "1":
    add_res = c1.add()
    print("Add: {}".format(add_res))
elif selection == "2":
    mult_res = c1.mult()
    print("Multiply: {}".format(mult_res))
elif selection == "3":
    div_res = c1.div()
    print("Division: {}".format(div_res))
elif selection == "4":
    ext_res = c1.ext()
    print("Extraction: {}".format(ext_res))
else:
    print("Please Choose 1, 2, 3 or 4 for Selection")
