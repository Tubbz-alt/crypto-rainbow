import hashlib, string

def reduce_plain(plain, debug = True):
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
		if len(resList) == 3 and indx >0:
			indx = -1

		if debug:
			print 'curr indx, len, reduction', indx, len(resList), ''.join(resList)
		if hashval[indx] in string.ascii_lowercase:
			resList.append(hashval[indx])

		indx = indx+1 if indx>= 0 else indx-1

		if len(resList) >= len(plain) or indx>= len(hashval):
			if debug:
				if len(resList) >= len(plain):
					print 'exited because len(resList) >= len(plain)'
				if indx>= len(plain):
					print 'exited because indx>= len(hashval)'
				print 'finished with indx', indx
			return ''.join(resList)

def get_reduced_hash_from_hash(hashval, char_len=5, debug=True):
	# We now apply the reduction functions
	# We simply take the first and last 3 letters of the hash
	# and concatinate them into a string!
	resList = []
	indx = 0

	while True:
		if len(resList) == 3 and indx >0:
			indx = -1

		if debug:
			print 'curr indx, len, reduction', indx, len(resList), ''.join(resList)
		if hashval[indx] in string.ascii_lowercase:
			resList.append(hashval[indx])

		indx = indx+1 if indx>= 0 else indx-1

		if len(resList) >= char_len or abs(indx)>= len(hashval):
			if debug:
				print 'finished with indx', indx
			return hashlib.sha1(''.join(resList)).hexdigest()

if False:			
	# print reduce_plain('abcdefgh')
	print get_reduced_hash_from_hash('711c73f64afdce07b7e38039a96d2224209e9a6c')
