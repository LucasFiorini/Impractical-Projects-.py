import loader

word_list = loader.load('test.txt')
anagram_list = []

name = input() 
print("Input name {}.".format(name))
name = name.lower()
print("Using name {}.".format(name))

name_sorted = sorted(name)

for word in word_list:
	word = word.lower()
	if word != name:
		if sorted(word) == name_sorted:
			anagram_list.append(word)
print()

if (len(anagram_list) == 0):
	print("You need a bigger dictionary!")
else:
	print("Anagrams: ", *anagram_list,sep='\n') 
