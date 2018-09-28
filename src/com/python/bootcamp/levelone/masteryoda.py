# Given a sentence, return a sentence with the words reversed
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    words = text.split()
    result = " "
    return result.join(words[::-1])