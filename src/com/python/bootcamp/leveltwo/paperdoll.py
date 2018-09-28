# Given a string, return a string where for every character 
# in the original there are three characters

def paper_doll(text):
    result = ""
    for s in text:
        result += s * 3
    return result