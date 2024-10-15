def count_words(txt):
	count = 0
	for word in txt.split():
		count += 1

	return count

def count_chars(txt):
	words = txt.split()
	char = {}

	for word in words:
		for c in word.lower():
			if c.isalpha() and c in char.keys():
				char[c] += 1
			elif c.isalpha():
				char[c] = 1
	return char


def main():
	with open('books/frakenstein.txt') as f:
		file_contents = f.read()
		print("--- Begin report of books/frankenstein.txt ---")
		print(f'{count_words(file_contents)} words found in the document\n')
		c = count_chars(file_contents)
		for e in c:
			print(f"The '{e}' character was found {c[e]} times")

		print("--- End report ---")
main()