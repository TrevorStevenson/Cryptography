#!/usr/bin/env python3

def decipher(file_name):
	with open(file_name, 'r') as f:
		ciphertext = ""
		for line in f:
			ciphertext += line
		ciphertext = ciphertext.replace('\n', '')
		ciphertext = ciphertext.replace(' ', '')
		ciphertext = ciphertext.lower()
		k = 1
		
		while k < 1000:
			sum = 0
			for i in range(k):
				sum += IndCo(ciphertext[i::k])
			
			if (sum/k) > 0.06:
				break
			k += 1

		print("The keyword is of length " + str(k))

		shifts = [0]*k
		blocks = [ciphertext[i::k] for i in range(k)]
		for j in range(1, k):
			for sigma in range(26):
				if MutIndCo(blocks[0], shift(blocks[j], sigma)) > 0.06:
					shifts[j] = sigma

		solve(ciphertext, k, shifts)

def IndCo(s):
	s = s.replace(' ', '')
	n = len(s)
	sum = 0
	alpha = 'abcdefghijklmnopqrstuvwxyz'

	for i in range(26):
		freq = s.count(alpha[i])
		sum += freq * (freq-1)

	return sum / (n * (n+1))

def MutIndCo(s, t):
	s = s.replace(' ', '')
	t = t.replace(' ', '')
	n = len(s)
	m = len(t)
	sum = 0
	alpha = 'abcdefghijklmnopqrstuvwxyz'

	for i in range(26):
		freq_s = s.count(alpha[i])
		freq_t = t.count(alpha[i])
		sum += (freq_s*freq_t)

	return sum / (n*m)

def shift(s, amount):
	shifted_s = ""
	for letter in s:
		x = (ord(letter)-ord('a')+amount) % 26 + ord('a')
		shifted_s += chr(x)

	return shifted_s

def solve(cipher, k, shifts):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for letter in alpha:
		key = letter
		for i in range(1, k):
			key += shift(letter, 26-shifts[i])

		index = 0
		plain = ""
		for i, l in enumerate(cipher):
			s = ord(key[i%k])-ord('a')
			plain += shift(l, 26-s)

		print(key + ': ' + plain[:30])

	correct_key = input("Enter the correct key: ")
	plain = ""
	for i, l in enumerate(cipher):
			s = ord(correct_key[i%k])-ord('a')
			plain += shift(l, 26-s)

	print(plain)

if __name__ == "__main__":
	decipher("cipher.txt")
