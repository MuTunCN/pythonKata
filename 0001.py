'''200 key creater'''

import string, random


def keygen(num, key_size=7):
    key_string = string.ascii_letters+string.digits
    key_list = []
    for i in range(num):
        keys = [random.choice(key_string) for key in range(key_size)]
        key_list.append("".join(keys))
    return key_list


def main():
    key_list = keygen(200)
    print(key_list)
if __name__ == '__main__':
    main()
    