import hashlib
import base64

####
# Helpers
####

def chunked_file_import(fname,chunk_trunk):
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
      chunk_trunk.update(chunk)
  return chunk_trunk

####
# SHA1
####

def sha1_hex(fname):
  hash_sha1 = hashlib.sha1()
  hash_sha1 = chunked_file_import(fname,hash_sha1)
  return hash_sha1.hexdigest()

def sha1_base32(fname):
  hash_sha1 = hashlib.sha1()
  hash_sha1 = chunked_file_import(fname,hash_sha1)
  digest = hash_sha1.digest()
  return base64.b32encode(digest)

def sha1_base64(fname):
  hash_sha1 = hashlib.sha1()
  hash_sha1 = chunked_file_import(fname,hash_sha1)
  digest = hash_sha1.digest()
  return base64.b64encode(digest)

####
# MD5
####

def md5_hex(fname):
  hash_md5 = hashlib.md5()
  hash_md5 = chunked_file_import(fname,hash_md5)
  return hash_md5.hexdigest()

def md5_base32(fname):
  hash_md5 = hashlib.md5()
  hash_md5 = chunked_file_import(fname,hash_md5)
  digest = hash_md5.digest()
  return base64.b32encode(digest)

def md5_base64(fname):
  hash_md5 = hashlib.md5()
  hash_md5 = chunked_file_import(fname,hash_md5)
  digest = hash_md5.digest()
  return base64.b64encode(digest)
