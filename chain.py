import hashlib, reductor, time
# from reductor import reduce_plain

# The number of times we'll reduce
# num_reductions = 5

def chain_plain(plain, chain_heads=[], chain_len=100000, debug = False):
	if debug:
		print 'beginnig chain starting with ', plain
	reduced_val = reductor.reduce_plain(plain, 0, debug)

	if debug:
		print 'reducted first with reduced_val ', reduced_val

	for x in range(1,chain_len):
		reduced_val = reductor.reduce_plain(reduced_val, x, debug)
		if reduced_val in chain_heads or reduced_val == plain:
			if debug:
				print 'found a cycle!!! for ', reduced_val
			return (None, None)
		if debug:
			print 'reduction #', x, ' with reduced_val ', reduced_val
		# TODO: Handle small reduced_val
		# if len(reduced_val) < 6:

	return (plain, hashlib.sha1(reduced_val).hexdigest())
	# return (plain, reduced_val)

def find_hash_in_chain(chain_head, hashval, chain_len=100000, debug=False):
	reduced_val = reductor.reduce_plain(chain_head, chain_len-1, debug)

	for x in range(chain_len-2,-1,-1):
		reduced_val = reductor.reduce_plain(reduced_val, x, debug)
		if reduced_val == 'chris':
			print 'MATCHHEEEED!!!!!'
		if hashval == hashlib.sha1(reduced_val).hexdigest():
			return reduced_val

	return None



if False:
	# cceca
	res = find_hash_in_chain('abcde','e938b72279981fce748e5b2d1c4f454121ed4448')

	if res == None:
		print "you're stupid"
	else:
		print res