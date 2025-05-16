def count_the_words(text_to_count):
    word_array = text_to_count.split()
    word_count = len(word_array)
    return word_count

def temp():
    print(f"{word_count} words found in the document")

def count_the_letters(text_to_count):
    little_letters =  text_to_count.lower()
    list_of_letters = list(little_letters)
    data_dict = {}
    for letter in list_of_letters:
        if letter in data_dict:
            count = data_dict[letter]
            data_dict[letter] = count + 1
        else:
            data_dict[letter] = 1
    list_of_dicts = []
    for key in data_dict:
        if key.isalpha():
            mini_dict = {"char": key, "num": data_dict[key]}
            list_of_dicts.append(mini_dict)
    sorted_list_of_dicts = sorted(list_of_dicts, reverse=True, key=lambda x: x['num'])
    return sorted_list_of_dicts
