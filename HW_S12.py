import string


def read_file(filename):
    """Reads a text file and returns the content as a string."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return ""


def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def get_unique_words(text):
    """Splits text into words and returns the set of unique words."""
    words = text.split()
    return set(words)


def compare_books(file1, file2):
    """Compares the number of unique words in two books."""
    text1 = clean_text(read_file(file1))
    text2 = clean_text(read_file(file2))

    unique_words1 = get_unique_words(text1)
    unique_words2 = get_unique_words(text2)

    print(f"Book 1 ('{file1}') has {len(unique_words1)} unique words.")
    print(f"Book 2 ('{file2}') has {len(unique_words2)} unique words.")

    if len(unique_words1) > len(unique_words2):
        print(f"The author of '{file1}' used more unique words.")
    elif len(unique_words1) < len(unique_words2):
        print(f"The author of '{file2}' used more unique words.")
    else:
        print("Both authors used the same number of unique words.")


# Run the function for text1.txt and text2.txt
compare_books('text1.txt', 'text2.txt')