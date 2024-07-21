import re

def normalize_phone(phone_number):
    # remove all symbols except for digits
    pattern = r'\d+'
    matches = re.findall(pattern, phone_number)
    preformatted_phone_number = ''.join(matches)

    # keep phone number (7 digits) + operator code (2 digits)
    bare_phone_number = preformatted_phone_number[-9:]
    # add country code
    normalized_phone_umber = f'+380{bare_phone_number[-9:]}'

    return normalized_phone_umber
