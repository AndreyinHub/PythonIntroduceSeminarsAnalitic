# HW_5_2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# https://pythonworld.ru/moduli/modul-collections.html
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

    
def rle_encode():

    li = input('\nEnter yor instatnt sequence, chars only: ')
    i = 0
    code_str = ""

    while i < len(li):

        count = 1
        while i + 1 < len(li) and li[i] == li[i + 1]:
            count += 1
            i += 1

        code_str += str(count) + li[i]
        i += 1

    with open("text_code_words.txt", "w") as data: 
        data.writelines(code_str)
    return code_str
	
def rle_decode():
    decode_str = ''
    count = ''
    
    data = open("text_code_words.txt", "r")
    code_words = data.readline()
    
    for ltr in code_words:
        if ltr.isdigit():
            count += ltr
        else :
            if not count:
                decode_str += ltr
            else: 
                decode_str += int(count) * ltr
                count = ''
    with open("text_words.txt", "w") as data:
        data.writelines(decode_str)
                
    data.close()
                
    return decode_str

print('Encode sequence: ', rle_encode(), '\n')
print('Decode sequence: \n', rle_decode(), '\n')