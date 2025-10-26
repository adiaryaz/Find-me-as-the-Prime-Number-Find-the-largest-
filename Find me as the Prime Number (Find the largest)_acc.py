def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_largest_prime():
    largest_prime = None

    while True:
        user_input = input().strip().lower()
        if user_input == 'n':
            break
        elif user_input == 'y':
            try:
                number = int(input())
                if number < 0:
                    print("NoProceed")
                    return
                if is_prime(number):
                    if largest_prime is None or number > largest_prime:
                        largest_prime = number
            except ValueError:
                print("NoProceed")
                return
        else:
            print("NoProceed")
            return

    if largest_prime is not None:
        print(largest_prime)
    else:
        print("NotFound")

if __name__ == "__main__":
    find_largest_prime()