from hash_helper import *
import sys

file_name = sys.argv[1]

# SHA1
print('SHA1:')
hex = sha1_hex(file_name)
print('     HEX: ' + hex.upper())

b32 = sha1_base32(file_name)
print('     BASE32: ' + b32.decode('UTF-8'))

b64 = sha1_base64(file_name)
print('     BASE64: ' + b64.decode('UTF-8'))

# MD5
print('MD5:')
hex = md5_hex(file_name)
print('     HEX: ' + hex.upper())

b32 = md5_base32(file_name)
print('     BASE32: ' + b32.decode('UTF-8').split('=', 1)[0])

b64 = md5_base64(file_name)
print('     BASE64: ' + b64.decode('UTF-8'))
