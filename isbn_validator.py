def validate_isbn(isbn, length):
    # Length mismatch
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Invalid characters check
    if length == 10:
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
            print('Invalid character was found.')
            return
    else:
        if not isbn.isdigit():
            print('Invalid character was found.')
            return

    main_digits = isbn[:-1]
    given_check_digit = isbn[-1]

    main_digits_list = [int(digit) for digit in main_digits]

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (1 if index % 2 == 0 else 3)

    result = 10 - digits_sum % 10

    return '0' if result == 10 else str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    values = user_input.split(',')

    if len(values) != 2:
        print('Enter comma-separated values.')
        return

    isbn = values[0]

    try:
        length = int(values[1])
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


# main()  # ← REQUIRED to be commented out for tests
