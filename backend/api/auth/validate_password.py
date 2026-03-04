def validate_password(password):

    if len(password) < 8:
        return False

    contains_upper = False
    contains_lower = False
    contains_number = False
    contains_special = False

    for char in password:
        if char.isupper():
            contains_upper = True
        elif char.islower():
            contains_lower = True
        elif char.isdigit():
            contains_number = True
        elif char == '!' or char == '@' or char == '#' or char == '$' or char == '%' or char == '^' or char == '&' or char == '(' or char == ')' or char == '=' or char == '-' or char == '_':
            contains_special = True
        else:
            return False

    if contains_number and contains_special and contains_lower and contains_upper:
        return True

    return False