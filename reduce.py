import hashlib, string

def reduce(plain):
	# A the SHA-1 encryption of the plaintext
	hashval = hashlib.sha1(plain).hexdigest()

	# We now apply the reduction functions
	# We simply take the first and last 3 letters of the hash
	# and concatinate them into a string!
	resList = []
	indx = 0

	while True:
		if len(resList) >= 3:
			indx = -indx

		if hashval[indx] in string.ascii_lowercase:
			resList.append(hashval[indx])

		indx = abs(indx) + 1

		if len(resList) >= 6 or len(resList) >= indx:
			return ''.join(resList)

