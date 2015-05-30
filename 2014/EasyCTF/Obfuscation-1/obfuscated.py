from itertools import starmap, cycle                                                           
 
def mystery(a, b):                                                                                                                          
    a = filter(lambda _: _.isalpha(), a.upper())                                   
    #important                                                               
    def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))                              
 
    return "".join(starmap(enc, zip(a, cycle(b))))                                     

text = "SWQHRGZZUSSWWBJWMRQTMRYVWVXJMADMKICSVBZCZXMENGJLVWEUDUQYVSEMKRWUBFJF"              
apple = "FOODISYUMMY"                                                                         
 
final = mystery(text, apple)                                                                                                                                           
 
#Everything below this point I added
#===================================

for q in xrange(26):
    text = mystery(text, apple)
    print text  
