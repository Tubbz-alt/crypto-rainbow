import hashlib, string

debug = True

def reduce(plain):
	# A the SHA-1 encryption of the plaintext
	hashval = hashlib.sha1(plain).hexdigest()

	if debug:
		print 'hash val is ', hashval

	# We now apply the reduction functions
	# We simply take the first and last 3 letters of the hash
	# and concatinate them into a string!
	resList = []
	indx = 0

	while True:
		if len(resList) == 3:
			indx = -1

		if debug:
			print 'curr indx, len', indx, len(resList)
		if hashval[indx] in string.ascii_lowercase:
			resList.append(hashval[indx])

		indx = indx+1 if indx>= 0 else indx-1

		if len(resList) >= 6 or indx>= len(plain):
			if debug:
				print 'finished with indx', indx
			return ''.join(resList)

if debug:			
	print reduce('test me')