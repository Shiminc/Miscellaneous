def split_word(word):
    char_list = []
    for i in word:
        char_list.append(i)
    return char_list



def get_permutation(word=list):
    if len(word)==1:
        return word
    elif len(word)==2:
        return [word[0]+word[1],word[1]+word[0]]
    elif len(word)==3:
        return [word[0]+word[1]+word[2],
                word[0]+word[2]+word[1],
                word[1]+word[0]+word[2],
                word[1]+word[2]+word[0],
                word[2]+word[0]+word[1],
                word[2]+word[1]+word[0]]
    

def main():
    word=split_word("aac")
    print(set(get_permutation(word)))

if __name__ == "__main__":
    main()
