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


def online_count(statuses):
    online_status = []
    for status in statuses.values():
        if status == "online":
            online_status.append(status)

    return len(online_status)


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))
