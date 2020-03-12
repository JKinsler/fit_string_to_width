"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright', 10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit.

    pseudo code:
    Take in string
    parse string into a list with 'split()', save as a variable string_list
    make a 'count' variable which is assigned as an integer
    New_line = str variable
    for each word in the string_list:
        while count < character limit, add words to the line:
            Increase the count by the word length 
            Add a space
            Increase the count by 1 for the space
            Reduce the words from the string_list
            if string_list = []:
                break
        print new_line
        set count=0
        """

    string_list = string.split()
    # gives ['Hello,', 'world!', 'I', 'love', 'Python', 'and', 'Hackbright']
    
    new_line = []

    iterable = ""


    def count(new_line):
        count = 0
        for word in new_line:
            count += len(word)
        return count

    for index in range(len(string_list)):
        # print(word, index)
        word = string_list[0]
        if (count(new_line)+count(word)) <= limit:
            # print(count(new_line) + count(word))
            
            # add new word to the line
            new_line.append(word)
            new_line.append(" ")
            # print(f'new_line {new_line}')
            
            # remove the word from string list
            string_list.pop(0)
            # print(f'string_list: {string_list}')
        
        else:
            new_string = iterable.join(new_line)
            print(new_string)
            new_line = []
            new_line.append(word)
            new_line.append(" ")
            string_list.pop(0)

    
    if string_list == []:
                new_string = iterable.join(new_line)
                print(new_string)


    return
            





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
