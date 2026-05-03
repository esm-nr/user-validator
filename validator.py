def is_first_name_valid(first_name):
    return first_name is not None and first_name.strip() != ""

def is_email_valid(email):
    return email is not None and "@" in email

def is_password_valid(password):
    return password is not None and len(password) >= 6

def passwords_match(p1, p2):
    return p1 == p2

def is_dob_valid(dob):
    import re
    pattern = r"\d{2}/\d{2}/\d{4}"
    return dob is not None and re.fullmatch(pattern, dob)