# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
	# [assignment] Add your code here
	word = word.lower()
	anagram = anagram.lower()
	word_list = []
	words = word.split()
	first_word = (''.join(words))
	len_first_word = len(first_word)
	for i in first_word:
		word_list.append(i)

	anagram_list = []
	anagrams = anagram.split()
	second_word = (''.join(anagrams))
	len_second_word = len(second_word)
	for a in second_word:
		anagram_list.append(a)

	true = []
	if len_first_word == len_second_word:
		for w in word_list:
			c_w = word_list.count(w) #check how many times a single word appears 
			c_a = anagram_list.count(w)
			if c_w == c_a:
				if w in anagram_list:
					t = 'True'
					true.append(t)
		if len_first_word == len(true):
			return True
		else:
			return False
	else:
		return False

init = find_anagram("hello", "check")
init2 = find_anagram("below", "elbow") 

print(init)
print(init2)
