def ispalindrum (word):
    if len(word)==1:
        return True
    elif len(word)>1:
        if word[0]==word[-1]:
            if len(word)==2:
                return True
            else:
                return ispalindrum(word[1:-1])
        else:
            return False
        


def main():
    print(ispalindrum('a')==True)
    print(ispalindrum('')==False)
    print(ispalindrum('b')==True)
    print(ispalindrum('bc')==False)
    print(ispalindrum('ab')==False)
    print(ispalindrum('ac')==False)
    print(ispalindrum('aa')==True)
    print(ispalindrum('bb')==True)
    print(ispalindrum('abc')==False)
    print(ispalindrum('aac')==False)
    print(ispalindrum('abba')==True)
    print(ispalindrum('aaaa')==True)
    print(ispalindrum('aaa')==True)
    print(ispalindrum('aba')==True)
    print(ispalindrum('abca')==False)
    print(ispalindrum('abcde')==False)
    print(ispalindrum('abaca')==False)
    print(ispalindrum('ababa')==True)
    

    s="ab"
    print(s[1:-1])
if __name__ == "__main__":
    main()


