#!/usr/bin/env python

cipher_text = "p3E1rJA0MagvLKAyAwEsnKAsMaIhsD==".decode('rot13')
print cipher_text.decode('base64') #=> 'stuyctf{base64_is_fun}'
