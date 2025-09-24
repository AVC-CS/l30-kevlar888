def main():
# Ask the user for an integer
    number = int(input('Enter an integer: '))

    # Use modulus operator to check if odd or even
    if number % 2 == 1: #odd\
        result = 1
        print(f'The value {number} is an odd number')
    else:
        result = 0
        print(f'The value {number} is an even number')
    return result


if __name__ == '__main__':
    main()
