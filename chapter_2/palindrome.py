import read_file
word_list = read_file.load('words.txt')
palindrome_list = []

def find_palindrome():
	for word in word_list:
		if len(word) > 1 and word == word[::-1]:
			palindrome_list.append(word)


find_palindrome()
print("\nNumber of palindromes found: {}\n".format(len(palindrome_list)))
print(*palindrome_list,sep='\n')
print("\n{} of the file is a palindrome!".format((len(palindrome_list)*100)/len(word_list)))
