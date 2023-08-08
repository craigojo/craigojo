not_allowed_characters = ('.', '/', ';')
while True:
    print()
    nickname = input('Enter a nickname (".", "/", ";" (not allowed)')
    invalid_chars_counter = 0

    for char in not_allowed_characters:
        if char in nickname:
            invalid_chars_counter += 1

        if invalid_chars_counter > 0:
            print()
            print('INVALID: The nickname cannot conrain ".", "/", ";" ')

        else:
            break
    print()
    print('Welcome ' + nickname)
    break
