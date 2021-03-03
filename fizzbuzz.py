def fizzbuzz():
    num = 1;
    string = ""
    while (num <= 100):
        if (num % 3 == 0 and num % 5 == 0):
            string += "FizzBuzz"
        elif (num % 3 == 0):
            string += "Fizz"
        elif (num % 5 == 0):
            string += "Buzz"
        else:
            string += str(num)
        if (num != 100):
            string += " "
        num += 1
    print(string)
    return string
