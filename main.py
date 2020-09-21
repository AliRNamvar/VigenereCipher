# Vigenere cipher
# secondary branch

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def key_generator(keyword, len_plaintext=0):

    key_ = ''
    cont = True
    while cont:
        for i in keyword:
            key_ = key_ + i
            if len(key_) == len_plaintext:
                cont = False
                break

    return key_


print("add something to hub in pycharm")


def generate_encrypt_table(alphabet):

    input = []
    for i in alphabet:
        input.append(i)

    output = []
    num1 = 1
    while num1 != 27:
        to_append = []
        for j in input:
            to_append.append(j)

        # print("this is to_append (num1 = {}): {}".format(num1, to_append))
        output.append(to_append)
        pop_val = input.pop(0)
        # print("pop val:", pop_val)
        input.append(pop_val)
        num1 += 1
    return output


generate_encrypt_table(alphabet)


key = key_generator(keyword='AYUSH', len_plaintext=len('GEEKSFORGEEKS'))
