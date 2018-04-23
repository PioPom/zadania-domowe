tekst_do_zaszyfrowania = input("Podaj tekst do zaszyfrowania : ")
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM"
lowerCase = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
szyfr = ""
for x in tekst_do_zaszyfrowania :
    if x in upperCase :
        szyfr = szyfr + upperCase[upperCase.find(x) + 13]
    elif x in lowerCase :
        szyfr = szyfr + lowerCase[lowerCase.find(x) + 13]
    else :
        szyfr = szyfr + x
print(szyfr)
