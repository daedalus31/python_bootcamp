import re
import sys


def is_valid_email(email: str):
    email_regex = re.compile('[^@]+@[^@]+\.[^@]+')
    return email_regex.match(email)


def clean_emails_set(input_file):
    result = set()
    with open(input_file) as inp:
        for email in inp:
            email = email.strip().lower()
            if is_valid_email(email):
                result.add(email)
    return result


def write_clean_list(emails: set, output_file: str):
    with open(output_file, 'w') as out:
        out.writelines([e + '\n' for e in sorted(emails)])


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    write_clean_list(clean_emails_set(input_file), output_file)
