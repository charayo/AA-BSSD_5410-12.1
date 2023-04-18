a = b = 0


#  Math switcher class
class Calculator:
    # Ascii values *=42, +43,-45,/47,^94

    def switchCase(self, ch):
        ascii_value = ch
        if ch.lower() != "pow":
            ascii_value = ord(ch)
        default = "Wrong operator"
        return getattr(self, 'calc_' + str(ascii_value), lambda: default)()

    def calc_43(self):
        return a + b

    def calc_45(self):
        return a - b

    def calc_42(self):
        return a * b

    def calc_47(self):
        return a / b

    def calc_94(self):
        return a * a

    def calc_pow(self):
        return pow(a, b)


def inp_1():
    global a, b
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))


def inp_2():
    global a
    a = int(input("Enter A:"))


class TakeInput:
    def menu(self):
        print("Choose from the following operations:\n"
              "*\n"
              "+\n"
              "-\n"
              "/\n"
              "^\n"
              "pow\n")

    def switchCase(self, opp_choice):
        ascii_value = opp_choice
        if opp_choice.lower() != "pow":
            ascii_value = ord(opp_choice)
        default = "Invalid option"
        return getattr(self, 'inp_' + str(ascii_value), lambda: default)()

    def inp_43(self):
        inp_1()

    def inp_45(self):
        inp_1()

    def inp_42(self):
        inp_1()

    def inp_47(self):
        inp_1()

    def inp_94(self):
        inp_2()

    def inp_pow(self):
        inp_1()


def main():
    #  Getting the input
    getInp = TakeInput()
    getInp.menu()
    ch = input("Enter Choice: ")

    getInp.switchCase(ch)

    # determining the operation type and performing the calculation
    calc = Calculator()
    ans = calc.switchCase(ch)
    print(ans)


# end def main():


if __name__ == "__main__":
    main()
