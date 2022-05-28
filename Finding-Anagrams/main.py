# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1,word2):
    # [assignment] Add your code here
    #convert words to lowercase
    word1=word1.lower()
    word2=word2.lower()

    #remove all whitespaces from words
    word1=word1.split()
    word2=word2.split()
    
    #Join the words back with no whitespace
    word1=''.join(word1)
    word2=''.join(word2)

    #sort words in ascending order
    word1=sorted(word1)
    word2=sorted(word2)

    #compare words to establish if anagram
    if word1==word2:
        print(True, " The words are an anagram")
        return True
    else:
        print(False, " The words are not an anagram")
        return False

find_anagrams("Desperation", "A rope ends it")
