alphabet_dic = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=13, n=14, o=15, p=16, q=17, r=18,
                    s=19, t=20, u=21, v=22, w=23, x=24, y=25, z=26)


for k, v in alphabet_dic.items():
    print('{}:{}'.format(k, v))


while unvalid_input:

    if situation1.lower() == "encryption" or situation1.lower() == "decryption":
        unvalid_input = False

    else:
        situation1 = input("Unvalid input!\nTry again: ")


if situation1.lower() == "encryption":
    print("Your text: ", input_text, "\nEncrypted text: ", encrypted_text, sep='')
elif situation1.lower() == "decryption":
    print("Your text: ", input_text, "\nDecrypted text: ", decrypted_text, sep='')