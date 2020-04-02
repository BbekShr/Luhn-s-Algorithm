
def get_digit(number, n):
    return number // 10**n % 10


try:
    entryNumber = int(input("Please enter a card number: "))
    lengthToStr = str(entryNumber)
    length = len(lengthToStr)
    sum1 = 0
    sum2 = 0

    firstDigit = (int(entryNumber / (10**(length-1))))
    firstTwoDigit = (int(entryNumber / (10**(length-2))))

    for x in range(length):
        if x%2 == 0:
            sum1 += get_digit(entryNumber, x)

        if x%2 == 1:
            getNum = get_digit(entryNumber, x)*2
            if getNum > 9:
                sum2 = sum2 + get_digit(getNum, 0) + get_digit(getNum, 1)
            else:
                sum2 = sum2 + getNum

    finalSum = sum1 + sum2

    if get_digit(finalSum, 0) == 0:
        print("Valid Card and the card type is: \n")
        print(length)
        if 12 < length < 17:
            # Visa 13 to 16 digits starts with 4
            if firstDigit == 4:
                print("Visa")
            # Amex 15 digits, starts with 34 and 37
            if length == 15 and (firstTwoDigit == 34 or firstTwoDigit == 37):
                print("AMEX")
            # Master Card 16 digits, starts with 51 to 55
            if length == 16 and (50 < firstTwoDigit < 56):
                print("Master Card")

    else:
        print("Invalid Card")
except ValueError:
    print("Please enter a valid numbers")

