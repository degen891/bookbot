from collections import defaultdict

def count_words_and_chars(txt):
    word_count = 0
    char_count = defaultdict(int)

    for word in txt.split():
        word_count += 1
        for c in word.lower():
            if c.isalpha():
                char_count[c] += 1
    
    return word_count, char_count


def main():
    file_path = 'books/frankenstein.txt'
    try:
        with open(file_path, 'r') as f:
            file_contents = f.read()
        
        word_count, char_count = count_words_and_chars(file_contents)

        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count} words found in the document\n")

        for char, count in sorted(char_count.items()):
            print(f"The '{char}' character was found {count} times")

        print("--- End report ---")

    except FileNotFoundError:
        print(f"File {file_path} not found.")


if __name__ == "__main__":
    main()
