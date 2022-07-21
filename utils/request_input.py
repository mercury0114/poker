def request_input(condition):
    n = input()
    while not condition(n):
        print("Wrong input")
        n = input()
    return n
