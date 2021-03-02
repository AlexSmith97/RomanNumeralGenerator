#Roman numerals are written left to right with symbols of decreasing magnitude.
#They are broken down straightforwardly with the following components:
#Numerals=[I:1, IV:4, V:5, IX:9, X:10, XL:40, L:50, XC:90, C:100, CD:400, D:500, CM:900, M:1000]
#Task: construct any number 1-1000

Numerals = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
Numerals = dict(sorted(Numerals.items(), key=lambda x: x[1], reverse=True)) #Sort in descending order

def RomanNumeral(x):
    Numeral = '' #start with an empty string
    if type(x) is int and 1 <= x <= 1000: #checking for an integer between 1 and 1000... if not returns an error message
        while x > 0:
            for i in Numerals:
                if x >= Numerals[i]:
                    x -= Numerals[i] 
                    Numeral += i 
                    break
        return Numeral
    else:
        return 'Please input an integer between 1 and 1000'
