#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct
from Crypto.Cipher import AES
from target.target import Target

class Decryption:
    def decrypt_file(self, key, in_filename, encrypt_ext_name='.7days', out_filename=None, chunksize=24*1024):
        if not out_filename:
            out_filename = in_filename.replace(".7days","")
        with open(in_filename, 'rb') as infile:
            self.origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(self.origsize)
