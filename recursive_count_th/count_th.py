'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # set targets
    target = "th".lower()
    target_length = len("th")
    word_length = len(word)
    # base cases
    if word_length < target_length:
        return 0
    if target in word is False:
        return 0
    # check first two characters and increment by 1
    if word[0:target_length] == target:
        return count_th(word[target_length-1:]) + 1
    # check remaining characters
    return count_th(word[target_length-1:])

