import hashlib, string


def hash_and_reduce(val_to_reduce, reduction_index=1, debug=False):
	hashval = hashlib.sha1(val_to_reduce).hexdigest()

	if debug:
		print 'hash val is ', hashval

	return reduce_hash(hashval, len(val_to_reduce), reduction_index, debug)

# my  reduction function
'''Given a SHA1 hash, add index val, mod, hex then re hash
lastly, we %26 every so often to get a letter of the alphabet'''
def reduce_hash(hashval, num_chars=5, reduction_index=1, debug=False):
	# string.ascii_lowercase
	letters = 'abcdefghijklmnopqrstuvwxyz'
	hashval = hashval[::-1]
	hashval = hashlib.sha1(hex((int(hashval,16)+reduction_index) % 26**num_chars)).hexdigest()
	res = []
	for x in range(5):
		curr = int(hashval[8*x:8*(x+1)], 16)
		res.append(letters[curr %26])
	return ''.join(res[::-1])

	
# Chris's reduction function
def reduce_hash2(hashval, num_chars=5, reduction_index=1, debug=False):
	lettersLower = 'abcdefghijklmnopqrstuvwxyz'

	results = []
	byteArray = getBytes(hashval)
	for i in xrange(num_chars):
		index = byteArray[(i + reduction_index) % len(byteArray)]
		newChar = lettersLower[index % len(lettersLower)]
		results.append(newChar)
	return "".join(results)

def getBytes(hashV):
	results = []
	remaining = int(hashV, 16)
	while remaining > 0:
		results.append(remaining % 256)
		remaining //= 256
	return results

if False:			
	# print reduce_plain('711c73f64afdce07b7e38039a96d2224209e9a6c',6)
	# print reduce_plain('test',2)
	# print reduce_hash('711c73f64afdce07b7e38039a96d2224209e9a6c',5,150,True)
	print reduce_hash('711c73f64afdce07b7e38039a96d2224209e9a6c',5,150,False)

if False:
	print hash_and_reduce('tests',0)
	print reduce_hash('04d13fd0aa6f0197cf2c999019a607c36c81eb9f',5,0,)
	print hash_and_reduce('fbcba',1,)
	print reduce_hash('5d707e0eef4147cf550a178ea8a3de917915fb37',5,1,)
	# hashlib.sha1('affce').hexdigest() -> 8b4c7720f9087a784ffee378ae60189c76e2d683