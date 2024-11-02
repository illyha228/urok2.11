# try:
#     filename: str = 'test.txt'
#     file = open(filename, 'r')
#     content = file.read()
#     lines = content.split('\n')
#     for line in lines:
#         counter: int = 0
#         words = line.split(' ')
#         for word in words:
#             if len(word) > 1 and not word.isdigit() or word.isalpha() and word == 'I':
#                 counter += 1
#         print(f'{line} - {counter}')
#
# except FileNotFoundError as e:
#     print(f"File Not Found: {filename}")
# except Exception as e:
#     print(f"Exeption: {e}")
import hashlib

from Tools.scripts.pysource import binary_re

# try:
#     filename: str = 'text.txt'
#     file = open(filename, 'a')
#     text: str = input('Enter some text')
#     file.write(text+'\n')
#
# except FileNotFoundError as e:
#     print(f"File Not Found: {filename}")
# except Exception as e:
#     print(f"Exeption: {e}")

# try:
#     filename: str = 'tesr.bin'
#     file = open(filename, 'wb')
#     text: str = input('Enter some text')
#
#     file.write(text.encode())
#     file.close()
#     binary_reabele_text: file.read().decode()
#     print(f"Binary readed text:  {binary_reabele_text}")
#
# except FileNotFoundError as e:
#     print(f"File Not Found: {filename}")
# except Exception as e:
#     print(f"Exeption: {e}")


# import hashlib
# import binascii
#
# try:
#     filename: str = 'binary_file.txt'
#     file = open(filename, 'wb')
#     text: str = input('Enter some text: ')
#     encode_text = text.encode()
#
#     file.write(encode_text)
#     file.close()
#
#     with open(filename, 'rb') as file:
#         binary_readable_text = file.read()
#
#     hex_encoded_text = binascii.hexlify(binary_readable_text).decode()
#     print(f"Hexadecimal encoded text: {hex_encoded_text}")
#
#     decoded_bytes = binascii.unhexlify(hex_encoded_text)
#     decoded_text = decoded_bytes.decode()
#     print(f"Decoded text: {decoded_text}")
#
# except FileNotFoundError as e:
#     print(f"File Not Found: {filename}")
# except Exception as e:
#     print(f"Exeption: {e}")


from fileinput import filename


try:
    filename: str = "data.csv"
    users: dict = {
        1: {
            "name": "jon",
            "surname": "Doe",
            "age": 30,
            "city": "New York",
            "email": "Jon.Doe@gmail.com"
        },

        2: {
            "name": "jin",
            "surname": "Die",
            "age": 25,
            "city": "Chikago",
            "email": "Jin.Die@gmail.com"
        },
        3: {
            "name": "Jack",
            "surname": "Mic",
            "age": 37,
            "city": "London",
            "email": "Jack.Mic@gmail.com"
        }
    }
    categories: str = ",".join(users[0].keys())
    with open(filename, 'w') as file:
        file.write(categories)
        file.write("\n")
        file.write()

except FileNotFoundError as e:
    print(f"File Not Found: {filename}")
except Exception as e:
    print(f"Exeption: {e}")
