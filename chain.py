import hashlib, reductor, time

# The number of times we'll reduce
# num_reductions = 5

def create_chain(chain_head, chain_len=200, debug = False):
	if debug:
		print 'beginnig chain starting with ', chain_head
	reduced_val = reductor.hash_and_reduce(chain_head, 0, debug)

	if debug:
		print 'reducted first with reduced_val ', reduced_val

	for x in range(1,chain_len):
		reduced_val = reductor.hash_and_reduce(reduced_val, x, debug)

	return (chain_head, hashlib.sha1(reduced_val).hexdigest())
	# return (chain_head, reduced_val)

def find_hash_in_chain(chain_head, hashval, chain_len=100000, debug=False):
	if chain_head == reductor.reduce_hash(hashval, 5, 0):
		return chain_head
	reduced_val = reductor.hash_and_reduce(chain_head, chain_len-1, debug)

	for x in range(1,chain_len):
		reduced_val = reductor.hash_and_reduce(reduced_val, x, debug)
		if hashval == hashlib.sha1(reduced_val).hexdigest():
			return reduced_val

	return None

def get_list_red(hashval, num_chars=5, chain_len=200,):
	res_red = [reductor.reduce_hash(hashval,num_chars, 0)]
	res_has = [hashlib.sha1(res_red[0]).hexdigest()]

	for x in range(1,chain_len):
		res_red.append(reductor.hash_and_reduce(res_red[x-1],x))
		res_has = [hashlib.sha1(res_red[x]).hexdigest()]
	return (res_red, res_has)

def is_hash_in_chain(hashval, chain_end, chain_len=100000):
	if hashval == chain_end:
		return True

	for x in range(chain_len-1,-1,-1):
		pass


if False:
	# cceca
	res = find_hash_in_chain('abcde','e938b72279981fce748e5b2d1c4f454121ed4448')

	if res == None:
		print "you're stupid"
	else:
		print res