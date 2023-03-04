def split_word(word):
    char_list = []
    for i in word:
        char_list.append(i)
    return char_list



def get_permutation(word=list):
    if len(word)==1:
        return word
    

def main():
    word=split_word("a")
    print(get_permutation(word))

if __name__ == "__main__":
    main()
