def capital_indexes(word):
    response_list = []
    for index, letter in enumerate(word):
        if letter.isupper():
            response_list.append(index)

    return response_list


def mid(string):
    length_of_string = len(string)
    dict_of_string = list(string)

    if length_of_string % 2 != 0:
        index = int(length_of_string / 2)
        return dict_of_string[index]
    else:
        return ""


tester = "abc"
testert = "aaaa"
testert3 = "aaaaaaa"

print(mid(testert3))
