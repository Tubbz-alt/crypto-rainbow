import hashlib, string

def reduce_plain(plain, reduction_index=1, length_target=5, debug = False):
	# print 'the plain is ', plain
	# A the SHA-1 encryption of the plaintext
	hashval = hashlib.sha1(plain).hexdigest()

	if debug:
		print 'hash val is ', hashval

	return reduce_hash(hashval, length_target, reduction_index)
	

def reduce_hash(hashval, char_len=5, reduction_index=1, debug=False):
	# We now apply the reduction functions
	# We simply take the first and last 3 letters of the hash
	# and concatinate them into a string!
	if debug:
		print 'init hashval ', hashval
		print int(hashval,16)+reduction_index
		print hex(int(hashval,16)+reduction_index)[2:-1]
		print hashlib.sha1(hex((int(hashval,16)+reduction_index) % 26**char_len)).hexdigest()

	hashval = hex(int(hashval,16)+reduction_index)[2:-1]
	hashval = hashlib.sha1(hex((int(hashval,16)+reduction_index) % 26**char_len)).hexdigest()
	resList = []
	indx = 0

	# Old reduction function that was used for every reduction
	# Simply returns first 3 alpha + last 3 flipped
	while True:
		if len(resList) == 3 and indx >0:
			indx = -1

		if debug:
			print 'curr indx, len, reduction', indx, len(resList), ''.join(resList)
		if hashval[indx] in string.ascii_lowercase:
			resList.append(hashval[indx])

		indx = indx+1 if indx>= 0 else indx-1

		if len(resList) >= char_len or indx>= len(hashval):
			# if len(resList) >= char_len:
			# 	print 'exited because len(resList) >= len(plain)'
			# if indx>= len(hashval):
			# 	print 'exited because indx>= len(hashval)'
			# print 'finished with indx', indx
			return ''.join(resList)

	# New reduction function that uses index to modify
	# return str((int(hashval,16)+1) % 26**length_target)
	# return str((int(hashval,16)+1) % 26**5)

if True:			
	# print reduce_plain('711c73f64afdce07b7e38039a96d2224209e9a6c',6)
	# print reduce_plain('test',2)
	# print reduce_hash('711c73f64afdce07b7e38039a96d2224209e9a6c',5,150,True)
	print reduce_hash('711c73f64afdce07b7e38039a96d2224209e9a6c',5,150,False)
