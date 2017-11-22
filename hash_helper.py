import hashlib
import base64
import sys

file_name = sys.argv[1]

####
# SHA1
####

def sha1_hex(fname):
  hash_sha1 = hashlib.sha1()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_sha1.update(chunk)
  return hash_sha1.hexdigest()

def sha1_base32(fname):
  hash_sha1 = hashlib.sha1()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_sha1.update(chunk)
  digest = hash_sha1.digest()
  return base64.b32encode( digest )

def sha1_base64(fname):
  hash_sha1 = hashlib.sha1()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_sha1.update(chunk)
  digest = hash_sha1.digest()
  return base64.b64encode( digest )

####
# MD5
####

def md5_hex(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  return hash_md5.hexdigest()

def md5_base32(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  digest = hash_md5.digest()
  return base64.b32encode( digest )

def md5_base64(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      hash_md5.update(chunk)
  digest = hash_md5.digest()
  return base64.b64encode( digest )

# SHA1
print( 'SHA1:')
hex = sha1_hex(file_name)
print( '     HEX: ' + hex.upper() )

b32 = sha1_base32(file_name)
print( '     BASE32: ' + b32.decode( 'UTF-8' ) )

b64 = sha1_base64(file_name)
print( '     BASE64: ' + b64.decode( 'UTF-8' ) )

# MD5
print( 'MD5:')
hex = md5_hex(file_name)
print( '     HEX: ' + hex.upper() )

b32 = md5_base32(file_name)
print( '     BASE32: ' + b32.decode( 'UTF-8' ).split('=', 1)[0] )

b64 = md5_base64(file_name)
print( '     BASE64: ' + b64.decode( 'UTF-8' ) )
