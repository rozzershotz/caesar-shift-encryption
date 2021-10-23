EorD = input("Do you want to Encrypt (E) or decrypt (D): ")
StringThing = str(input("please give me a string: "))
shift = int(input("please give me the shift to do the thingy with: "))
alphabet = "a0bcd1e42fgh ijkl,m57n8o.6p9>qr/\s!tu`#v@w?xy3z"

def FindThingInThing(letter, alphabet):
    return alphabet.find(letter)

def Encrypt(string, shift, alphabet):
    EncryptedString = ""
    for i in string:
        originalposition = FindThingInThing(i, alphabet)
        newposition = originalposition + shift  
        if newposition >= len(alphabet):
            newposition = newposition - len(alphabet)
        newletter = alphabet[newposition]
        EncryptedString += newletter
    return EncryptedString

def Decrypt(string, shift, alphabet):
    DecryptedString = ""
    for i in string:
        originalposition = FindThingInThing(i, alphabet)
        newposition = originalposition - shift
        if newposition >= len(alphabet):
            newposition = newposition - len(alphabet)
        newletter = alphabet[newposition]
        DecryptedString += newletter
    return DecryptedString

if EorD == "E":
    print(Encrypt(StringThing, shift, alphabet))

if EorD == "D":
    print(Decrypt(StringThing, shift, alphabet))
