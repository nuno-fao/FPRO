def count(word, phrase):
    word = word.lower()
    phrase = phrase.lower()
    words = phrase.split(" ")
    count = 0
    for x in words:
        if x==word:
            count+=1
    return count