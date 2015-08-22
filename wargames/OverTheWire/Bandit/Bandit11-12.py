import os

string_to_decode = os.popen('data.txt').read()

print string_to_decode.decode('rot13')

#> u'The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu\n'
