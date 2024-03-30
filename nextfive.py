from hashlib import new


def nextFive(c):
    char_val = ord(c)
    n = ''

    for i in range(5):
        char_val += 1
        if char_val > ord('z'):
           char_val = ord('A')
           
        elif char_val > ord('Z') and char_val < ord('a'):
            char_val = ord('a')

        n += chr(char_val)

    return n 



c = input("Enter the alphabatic Charcter\t")
print(nextFive(c))
