""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5

# Question 1
def lines_from_file(path):
    """
    Takes in a string path, which indicates the location of a txt file.
    The lines should appear in the same order as they appear in the file, so the
    first row of the file will be the first element of the list. Any spaces or
    newlines at the beginning or end of the line should be removed.
    """
    assert readable(open(path)), 'The stream cannot be read.'
    list = []
    for x in readlines(open(path)):
        list.append(x.strip())
    open(path).close()
    return list

def new_sample(path, i):
    """
    Takes in a string, path, and a nonnegative integer, i, and returns the
    paragraph in the i-th line of the file. Lines are zero-indexed, so the 0-th
    line is the top line of the file.
    """
    assert i >= 0, 'i must be nonnegative'
    for x in range(i + 1):
        if x == i:
            return readlines(open(path))[x].strip()
# End Question 1
# Question 2
def analyze(sample_paragraph, typed_string, start_time, end_time):
    """
    Outputs a list containing two values: words per minute and accuracy
    percentage. WPM is a measure of the number of words typed per minutes,
    and Accuracy Percentage is a measure of the percent of typed words that were
    typed correctly.
    """
    wpm = (len(typed_string) / 5) / ((end_time - start_time) / 60)
    words_in_sample_paragraph = sample_paragraph.split()
    words_in_typed_paragraph = typed_string.split()
    if len(words_in_typed_paragraph) == 0 and len(words_in_sample_paragraph) != 0:
        return [wpm, 0.0]
    accuracy_counter = 0
    len_sample = len(words_in_sample_paragraph)
    len_typed = len(words_in_typed_paragraph)
    len_typed_counter = len_typed
    accuracy_percentage = (accuracy_counter / len_typed) * 100
    y = 0
    if len_typed == 1 and len(words_in_typed_paragraph[0]) > 0:
        len_string = len(words_in_typed_paragraph[0])
        while len_string > 0:
            if y == len_typed:
                break
            if words_in_sample_paragraph[0][y] == words_in_typed_paragraph[0][y]:
                accuracy_counter += 1
                y += 1
            else:
                len_string -= 1
        if len_typed > len_sample:
            accuracy_percentage = (accuracy_counter / len_sample) * 100
        accuracy_percentage = (accuracy_counter / len_typed) * 100
        return [wpm, accuracy_percentage]
    else:
        while len_typed_counter > 0:
            if y == len(words_in_sample_paragraph):
                break
            if words_in_sample_paragraph[y] == words_in_typed_paragraph[y]:
                accuracy_counter += 1
                y += 1
                len_typed_counter -= 1
            else:
                len_typed_counter -= 1
                y += 1
        if len_typed > len_sample:
            accuracy_percentage = (accuracy_counter / len_sample) * 100
        accuracy_percentage = (accuracy_counter / len_typed) * 100

    return [wpm, accuracy_percentage]
# End Question 2
# Question 3
def pig_latin(word):
    """
    Takes in a single word as a string value and returns the translated version
    of the word, according to the rules of Pig Latin.
    """
    index = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_list = list(word)
    if word[0] in vowels:
        return word + 'way'
    for x in range(len(word_list)):
        if word_list[x] in vowels:
            index = x
            break
    return word[index:] + word[:index] + 'ay'
# End Question 3
# Question 4
def autocorrect(user_input, words_list, score_function):
    """
    Takes in the word typed by the user, and returns the closest approximation
    for an incorrectly spelled word by searching through the words list for the
    word with lowest difference compared to the word typed by the user.
    """
    for x in words_list:
        if x == user_input:
            return user_input
    counter = 0
    lowest_index = 0
    curr_lowest = score_function(user_input, words_list[counter])
    length = len(words_list)

    while length > 0:
        if curr_lowest > score_function(user_input, words_list[counter + 1]):
            curr_lowest = score_function(user_input, words_list[counter + 1])
            lowest_index = counter + 1
            length -= 1
            counter += 1
        else:
            length -= 1
            counter += 1
        return words_list[lowest_index]
# End Question 4
# Question 5
def swap_score(word1, word2):
    """
    Returns the number of characters needed to substitute the characters in the
    first string into the corresponding characters in the second string.
    """
    def score_keep(word1, word2, score):
        while word1 != '' or word2 != '':
            if word1[0] != word2[0]:
                score += 1
                return score_keep(word1[1:], word2[1:], score)
            return score
    return score_keep(word1, word2, 0)
# End Question 5

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________
        substitute_char = ______________
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
