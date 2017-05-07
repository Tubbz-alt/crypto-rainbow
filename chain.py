import hashlib, reductor, time

# The number of times we'll reduce
num_chars = 5

def create_chain(chain_head, chain_len=200, debug = False):
	if debug:
		print 'beginnig chain starting with ', chain_head
	reduced_val = reductor.hash_and_reduce(chain_head, 0, debug)

	if debug:
		print 'reducted first with reduced_val ', reduced_val

	for x in range(1,chain_len):
		reduced_val = reductor.hash_and_reduce(reduced_val, x, debug)

	return (chain_head, hashlib.sha1(reduced_val).hexdigest())

def find_hash_in_chain(chain_head, hashval, chain_len=100000, debug=False):
	hashed_head = hashlib.sha1(chain_head).hexdigest()
	if hashed_head == hashval:
		return chain_head
	reduced_val = reductor.reduce_hash(hashed_head, num_chars, 0)

	for x in range(1,chain_len):
		hashed_head = hashlib.sha1(reduced_val).hexdigest()
		if hashed_head == hashval:
			return reduced_val
		reduced_val = reductor.reduce_hash(hashed_head,num_chars,x)

	return None

# Returns a list of the potential chain_ends to check against table
def get_list_red(hashval, num_chars=5, chain_len=200,):
	hash_list = [hashval]

	for x in range(0,chain_len):
		reduced_val = reductor.reduce_hash(hashval,num_chars, chain_len-x-1)
		new_hash = hashlib.sha1(reduced_val).hexdigest()

		for y in range(chain_len-x,chain_len):
			reduced_val = reductor.reduce_hash(new_hash,num_chars,y)
			new_hash = hashlib.sha1(reduced_val).hexdigest()
		hash_list.append(hashlib.sha1(reduced_val).hexdigest())
	return hash_list

if False:
	res = find_hash_in_chain('abcde','e938b72279981fce748e5b2d1c4f454121ed4448') # cceca
	if res == None:
		print "you're stupid"
	else:
		print res