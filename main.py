# Vigenere cipher

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



key = key_generator(keyword='AYUSH', len_plaintext=len('GEEKSFORGEEKS'))
