###
### Author: Sarah Stallman
### Class: CSc 110
### Description: This is a program that can look through files with grids of letters
###              as a wordsearch puzzle and identify where certain words are whether
###              they are forward backwards or up and down.
###

def search_within_column(word_dictionary, column, string):
    '''
    This function uses if statements within a for loop to iterate through
    each column at a time to see if a word is located there.
    The word_dictionary parameter is the dictionary containing the words
    we are looking for, spelled forward and backward.
    The column parameter tells us which column we are iterating through.
    The string parameter is the letters in the specific column that we converted
    to a string in the vertical function.
    '''
    for forward, backward in word_dictionary.items():
        if forward in string:
            row = string.index(forward) + 1
            print(str(forward), 'found at [' + str(row) + ', ' + str(column + 1) + ']')
        if backward in string:
            row = string.index(backward) + len(backward)
            print(str(forward), 'found at [' + str(row) + ', ' + str(column + 1) + ']')

def vertical(word_dictionary, puzzle, puzzle_file):
    '''
    This function uses a for loop within a while loop to convert each column
    of letters into a string.
    The word_dictionary parameter is the dictionary containing the words
    we are looking for, spelled forward and backward.
    The puzzle parameter is the file we use that contains the grid of letters
    to search through.
    The puzzle_file parameter is necessary for reopening the puzzle file so we can
    move to the next column.
    '''
    column = 0
    string = ''
    puzzle_list = puzzle.readlines()
    while column < int(len(puzzle_list)):
        for line in puzzle_list:
            line_split = line.split(' ')
            string += (line_split[column].strip('\n').lower())
        search_within_column(word_dictionary, column, string)
        puzzle.close()
        puzzle = open(puzzle_file, 'r')
        string = ''
        column += 1

def search_within_line(word_dictionary, line, row):
    '''
    This function uses if statements within a for loop to iterate through
    each line at a time to see if a word is located there.
    The word_dictionary parameter is the dictionary containing the words
    we are looking for, spelled forward and backward.
    The line parameter is the letters in the specific line that we converted
    to a string in the horizontal function.
    The row parameter tells us which row we are iterating through.
    '''
    for forward, backward in word_dictionary.items():
        if forward in line:
            column = line.index(forward) + 1
            print(str(forward), 'found at [' + str(row) + ', ' + str(column) + ']')
        if backward in line:
            column = line.index(backward) + len(backward)
            print(str(forward), 'found at [' + str(row) + ', ' + str(column) + ']')


def horizontal(word_dictionary, puzzle):
    '''
    This function uses a for loop to convert the lines in the puzzle file
    to strings and calls the search_within_line function for each row.
    The word_dictionary parameter is the dictionary containing the words
    we are looking for, spelled forward and backward.
    The puzzle parameter is the file we use that contains the grid of letters
    to search through.
    '''
    row = 1
    for line in puzzle:
        line = ''.join(line.strip().split(' ')).lower()
        search_within_line(word_dictionary, line, row)
        row += 1


def words(words_file):
    '''
    This function opens up the file containing the words we want to look
    for and converts them to a dictionary.
    The words_file parameter is the file inputted by the user.
    '''
    words = open(words_file, 'r')
    word_dictionary = {}
    for line in words:
        line_split = line.split(' : ')
        word_dictionary[line_split[0]] = line_split[1].strip('\n')
    return word_dictionary

def main():
    '''
    This is the main function where we ask the user to input the files
    with the list of words and the puzzle grid, as well as ask the user
    which direction we want to look in.  We also call the other functions.
    This function does not need a parameter.
    '''
    words_file = input('Enter word file:\n')
    words(words_file)
    puzzle_file = input('Enter puzzle file:\n')
    puzzle = open(puzzle_file, 'r')
    direction = input('Enter puzzle mode:\n')
    if direction == 'h':
        horizontal(words(words_file), puzzle)
    if direction == 'v':
        vertical(words(words_file), puzzle, puzzle_file)

main()
