a = b = 0

# begin math switcher functions
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def sqr(a, _):
    return a * a

# end math switcher functions


def inp1():
    global a, b
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    # return a, b


def inp2():
    global a
    a = int(input("Enter A:"))
    # return a


def init_switcher():
    switcher = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
        '^': sqr
    }
    input_switcher = {
        '+': inp1,
        '-': inp1,
        '*': inp1,
        '/': inp1,
        '^': inp2
    }

    return switcher, input_switcher
# end def init_switcher()


def menu(sw):
    # menus
    print("Calculator type your operation:")
    for key in sw.keys():
        print(key)


# end def menu


def operation(ch, switcher, input_switch):
    input_switch.get(ch, "You have typed a wrong input")()
    return switcher.get(ch, "Invalid option chosen.")(a, b)


# end def operation


def main():
    sw, inp = init_switcher()
    menu(sw)
    # input choice
    ch = input("Enter Choice: ")
    ans = operation(ch, sw, inp)
    print(ans)


# end def main():


if __name__ == "__main__":
    main()
