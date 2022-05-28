# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    #read story.txt
    with open(filename) as story:
        words = story.read()
    
    #Separate words and store in list
    words_ls = words.split()
    
    return words_ls


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    #Declare Dictionary text_ls
    text_dict = {}

    #Prepare Words for input into Dictionary as {word:len(word)}   
    for word in text:
        n = (len(word))
        text_dict.update({word:n})
    
    return text_dict
    

print(count_words())