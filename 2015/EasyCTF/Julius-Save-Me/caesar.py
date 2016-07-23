def decrypt(text, key):
    key = key % 26
    arr = []
    orded = []
    enc = []
    text = text.lower()
    for letter in text:
        arr.append(letter)
    for letter in arr:
        ordletter = ord(letter)
        if ord("a") <= ordletter <= ord("z"):
            ordletter -= key
            if ordletter < ord("a"):
                ordletter += 26
        orded.append(ordletter)
    for number in orded:
        enc.append(chr(number))
    return "".join(enc)

text = "Cnebnl Vtxltk bl max uxlm unm fr ykbxgw ebdxl Gtihexhg uxmmxk yhk patmxoxk kxtlhg. Ha pxee. Max yetz bl xtlrvmy{Gti0exhg_ol_Vt3l4k}"
for _ in xrange(1, 26):
    flag = decrypt(text, _)
    if "easyctf{" in flag:
        print flag
