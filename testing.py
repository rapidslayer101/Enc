ascii_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def b85s_to_bits(s):
    bin_data = ''.join(format(i, f'07b') for i in bytearray(s, encoding='utf-8'))
    return int(bin_data, 2).to_bytes((len(bin_data)+7) // 8, 'big')


def bits_to_b85s(b):
    bin_data = bin(int.from_bytes(b, byteorder='big')).replace("0b", "")

    def bits_to_string(bts):
        b85s = ""
        for i in range(0, len(bts), 7):
            b85s += chr(int(bts[i:i+7], 2))
        return b85s

    b85s = bits_to_string(bin_data)
    counter = 0
    while True:
        if b85s[counter] not in ascii_set:
            b85s = bits_to_string(f"0{bin_data}")
            break
        if counter == len(b85s) - 1:
            break
        counter += 1
    return b85s


string = "hi"

byte_data = b85s_to_bits(string)
print("Converted")


# file
with open("output1", "wb") as f:
    f.write(byte_data)

with open("output0", "w") as f:
    f.write(string)

output = bits_to_b85s(byte_data)
print("Converted")

if output == string:
    print("success")

with open("output2", "w") as f:
    f.write(output)
input("Done")
