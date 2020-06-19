'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case | if word length < 2, word can't contain "th"
    if len(word) < 2:
        return 0
    # check if first two letters are "th"
    if word[:2] == "th":
        # if yes, increase count_th by one 
        # then, recursively check next two letters
        # eg, the third and fourth letter
        return 1 + count_th(word[2:])
    # if no, don't increase count_th by one
    # recursively check the next two letters
    # eg, second and third letter
    return count_th(word[1:])
