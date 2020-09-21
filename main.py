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


def generate_encrypt_table(alphabet):

    output = []
    for i in range(0, 26):
        for j in alphabet:
            output[i].append(j)

        pop_val = alphabet.pop(0)
        alphabet.append(pop_val)

    print(output)


generate_encrypt_table(alphabet)


key = key_generator(keyword='AYUSH', len_plaintext=len('GEEKSFORGEEKS'))
