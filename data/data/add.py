def xor_encrypt_decrypt(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
key = "mysecretkey"
list = []
list.append(xor_encrypt_decrypt('test1234',key))
list.append('\n')
list.append(xor_encrypt_decrypt('1234',key))
list.append('\n')
list.append(xor_encrypt_decrypt('answer',key))
a = open('./data/data/pass.txt','w')
a.writelines(list)
