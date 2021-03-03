def leapyear(num):
    if (num % 100 == 0):
        return False
    elif(num % 4 == 0):
        return True
