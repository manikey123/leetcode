# Calculate the average word length.
# For the given set of words return the average word length.
def avg_word_length(x):
        if not x:
            return None

        words = x.split()
        total_length = 0
        word_count = 0

        for word in words:
            total_length += len(word)
            word_count += 1

        avg_word_length = total_length / word_count
        return avg_word_length
    # if not x:
    #     return None
    # words=x.split()
    # word_lengths=[len(word) for word in words]
    # avg_word_length=sum(word_lengths)/len(words)
    # return (avg_word_length)
assert avg_word_length('ibm') == 3
assert avg_word_length('') == None
assert avg_word_length('ibm microsoft') == 6
assert avg_word_length(' Hello World ') == 5
assert avg_word_length('The movie ends with The-end') == 4.6
print('passed')
