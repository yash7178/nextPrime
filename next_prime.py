def is_prime(num):
    limit = int(num**0.5)
    for n in range(2, limit + 1):
        if num % n == 0:
            return False
    else:
        return True


def next_prime(curr_prime):
    new_prime = curr_prime + 1
    while True:
        if not is_prime(new_prime):
            new_prime += 1
            continue
        else:
            break
    return new_prime


print("Program to find next prime number")
print("Initial Prime Number: 2")
x = 2
while True:
    option = input("Do you want to find next prime number. Enter Yes or No\n")
    try:
        if option[0].upper() == 'Y':
            x = next_prime(x)
            print("Next prime number is: " + str(x))
        elif option[0].upper() == 'N':
            break
        else:
            print("Enter correct input")
            continue
    except IndexError:
        print("Give correct input")

