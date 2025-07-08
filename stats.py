def count_words(content):
    return len(content.split())

def letter_count(book):
    letter_dict = {}
    book = book.lower()
    letters = list(book)
    for i in letters:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    return letter_dict

def sort_on(items):
    return items["num"]

def letters_to_list(letter_dict):
    letters_list = []
    for letter, count in letter_dict.items():
        letters_organized = {"char": letter, "num": count}
        letters_list.append(letters_organized)
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list