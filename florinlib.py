'''
Python math library :
https://docs.python.org/3/library/math.html

'''

# function to determine the distance between two points (2D)
import math
#
#
# def distance2d(x1,y1,x2,y2):
#
#     dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#     return dist
#
#
# print(distance2d(0,0, 3,4))
#
#
# def distance3d(x1,y1,z1,x2,y2,z2):
#
#     dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
#     return dist
#
# print(distance3d(0,0,0,3,4,12))

word = list("whateveryouwant")
print(word)

# create a function to eliminate the repeating letters
# and keep only the first one of them, in order of its apparition


def eliminate_repeats(alist):
    # create a new list that contains only one of the repeating letters,
    # in order of its apparition

    new = []
    for let in alist:
        if let not in new:
            new.append(let)

    return new


print(eliminate_repeats(word))

# create a function to diplay the indexes where a certain letter is in  a alist
# if a letter appears multiple times, than the letter is followed by the list of indexes


def element_and_index(alist):
    tuplist =[]
    for ind , value in enumerate(alist):

        tuplist.append((value, ind))
    new = eliminate_repeats(alist)
    listoflists = []
    for let in new:
        u =[let]
        for pair in tuplist:
            if let == pair[0]:
                u.append(pair[1])
        listoflists.append(u)
    return listoflists


for ind, val in enumerate(element_and_index(word)):

    print (val)

# translate a text when a dictionary is given
# the translat_text function has two parameters,
# the text, and the dictionary,
# and it returns the translated text as a new_text


def translate_text(text, mydict):
    list_text = text.split()
    for i in range(len(list_text)):
        for key in mydict.keys():
            if list_text[i] == key:
                list_text.remove(list_text[i])
                list_text.insert(i, mydict[key])
#     new_text = ''
#     for word in  list_text:
#         new_text = new_text + ' ' + word
    return ' '.join(new_text)


print(translate_text(text1, dict1))
# a second translate function
def translate(text,translation_map):
    #use raw input and split the sentence into a list of words
    input_list = text.split()
    output_list = []

    #iterate the input words and append translation
    #(or word if no translation) to the output
    for word in input_list:
        translation = translation_map.get(word)
        output_list.append(translation if translation else word)

    #convert output list back to string
    return ' '.join(output_list)
