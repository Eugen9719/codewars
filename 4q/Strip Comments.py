def strip_comments(strng, markers):
    split_strng = strng.split('\n') # ['apples, pears # and bananas', 'grapes', 'bananas !apples']
    new_strng = []
    for i in split_strng:
        for j in range(len(i)):
            if i[j] in markers:
                i=i[:j].rstrip()
                break
        new_strng.append(i)
    return '\n'.join(new_strng)



print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples',
                     ['#', '!']))  # 'apples, pears\ngrapes\nbananas')
print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))  # , 'a\nc\nd')
print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))  # , ' a\nc\nd')

print(strip_comments('  . . lemons\nbananas @ cherries watermelons watermelons\nlemons bananas avocados',
                     ['=', '^', '.', '!', '#', '@', '-', ',', "'"]))

# '\nbananas\nlemons bananas avocados'