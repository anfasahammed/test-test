def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong(num):
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

    print("Armstrong numbers up to 1000:", [i for i in range(1, 1001) if is_armstrong(i)])
