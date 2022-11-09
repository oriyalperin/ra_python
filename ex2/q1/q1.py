import re


def find_email_addresses(txt_file):
    """
    find all the valid and invalid email addresses in the file @txt_file,
    by using regular expression.
    learn more about valid email address format: https://help.xmatters.com/ondemand/trial/valid_email_format.htm

    Example:
    >>> with open("file_fea.txt", 'w') as file:
    ...     file.write("hello, I am valid_email@addr.ess\\n")
    ...     file.write("hey there, I am -invalid__email.@addres.s\\n")
    ...     file.write("hi, I am not-email@address\\n")
    33
    42
    27
    >>> valid_addr, invalid_addr = find_email_addresses("file_fea.txt")
    >>> print(valid_addr,invalid_addr)
    ['valid_email@addr.ess'] ['-invalid__email.@addres.s']


    :param txt_file: text file path
    :return: 2 lists,valid and invalid,
    contains all the valid and invalid email addresses that were found in the file, respectively.
    """
    valid = []
    invalid = []
    with open(txt_file, 'r') as f:
        txt = f.read()
    poss = re.findall(r'[^\s]+@[^\s]+\.[^\s]+', txt)
    for word in poss:
        if re.match(r'[\w]+[.-_]*[\w]+@[\w-]+\.[\w]{2,}', word) and re.match(r'(?!.*[\.-_][\.-_])', word):
            valid.append(word)
        else:
            invalid.append(word)

    return valid, invalid


if __name__ == '__main__':

    file = input("please enter a file name: ")
    valid_addr, invalid_addr = find_email_addresses("file1.txt")
    print(f"valid email addresses: {valid_addr}")
    print(f"invalid email addresses: {invalid_addr}")
