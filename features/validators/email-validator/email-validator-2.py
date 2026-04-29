def validate_email(email):
    if email[0].isdigit() or email[0] in '.@':
        raise Exception("Email cannot start with number, '.' or '@'")

    if email.count('@') != 1:
        raise Exception("Email must contain exactly one '@'")

    username, domain = email.split('@')

    if '.' not in domain:
        raise Exception("Domain must contain at least one '.'")

    if domain.endswith('.'):
        raise Exception("Domain cannot end with '.'")

    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789.@"
    for ch in email:
        if ch not in allowed_chars:
            raise Exception("Invalid characters in email")

    return True

email = str(input("Enter email : "))    
validate_email(email)
