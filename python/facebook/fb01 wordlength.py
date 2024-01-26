
def avg_word_length(x):

    if not x:
        return None
    words=x.split()
    word_lengths=[len(word) for word in words]
    avg_word_length=sum(word_lengths)/len(words)
    return (avg_word_length)



assert avg_word_length('ibm') == 3
assert avg_word_length('') == None
assert avg_word_length('ibm microsoft') == 6
assert avg_word_length(' Hello World ') == 5
assert avg_word_length('The movie ends with The-end') == 4.6
print('passed')
