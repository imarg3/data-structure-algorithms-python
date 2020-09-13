# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i

    return res


def prime(n):
    for num in range(1, n + 1):

        i = 2

        for i in range(2, num + 1):
            if num % i == 0:
                break

        if i == num:
            print(num)


def decimal_to_binary(number):
    while number > 0:
        print(number % 2, end='')
        number = int(number / 2)

    print()


def print_table(number):
    for i in range(1, 10 + 1):
        print(number * i)


def main():
    print_hi('PyCharm')
    print()

    result = factorial(5)
    print(f"Factorial of 5! = {result}")
    print()

    print("Prime numbers of 100 :")
    prime(100)
    print()

    print("Decimal to Binary of 10 :")
    decimal_to_binary(10)
    print()

    print("Table of 27 :")
    print_table(27)
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
