def parsePasswordDb(path):
    password_entries = []
    for line in open(path):
        # tuple structure is (min letter repeats, max letter repeats, letter, password)
        password_entry = line.strip().split()
        password_entries.append((
            int(password_entry[0].split('-')[0]), int(password_entry[0].split('-')[1]), password_entry[1][0], password_entry[2]))
    return password_entries


def getIsPasswordValidPart1(password_entry):
    (min_char_count, max_char_count, char, password) = password_entry
    char_count = password.count(char)
    return (char_count >= min_char_count and char_count <= max_char_count)


def main():
    password_entries = parsePasswordDb('./input/day_2_input.txt')
    valid_passwords = []
    for password_entry in password_entries:
        if getIsPasswordValid(password_entry):
            valid_passwords.append(password_entry)
    return len(valid_passwords)


print(main())
