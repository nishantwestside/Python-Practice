ch = input("Please Enter Your Own Character : ")
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("The Given Character ", ch, "is a Vowel")
else:
    print("The Given Character ", ch, "is a Consonant")
if(ch.isupper()):
    print("The Given Character ", ch, "is an Uppercase Alphabet")
else:
    print("The Given Character ", ch, "is a Lowercase Alphabet")
