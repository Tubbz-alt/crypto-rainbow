import hashlib, reductor, time
# from reductor import reduce_plain

# The number of times we'll reduce
# num_reductions = 5

def chain_plain(plain, chain_heads=[], chain_len=100000, debug = False):
	if debug:
		print 'beginnig chain starting with ', plain
	reduced_val = reductor.reduce_plain(plain, debug)

	if debug:
		print 'reducted first with reduced_val ', reduced_val

	for x in range(2,chain_len):
		reduced_val = reductor.reduce_plain(reduced_val, debug)
		if reduced_val in chain_heads:
			if debug:
				print 'found a cycle!!! for ', reduced_val
			break 
		if debug:
			print 'reduction #', x, ' with reduced_val ', reduced_val
		# TODO: Handle small reduced_val
		# if len(reduced_val) < 6:

	return (plain, hashlib.sha1(reduced_val).hexdigest())
	# return (plain, reduced_val)

def find_hash_in_chain(chain_head, hashval, chain_len=100000):
	reduced_val = reductor.reduce_plain(chain_head, debug)

	for x in range(2,chain_len):
		reduced_val = reductor.reduce_plain(reduced_val, debug)

		if hashval == hashlib.sha1(reduced_val).hexdigest():
			return reduced_val

	return None



if True:
	# cceca
	res = find_hash_in_chain('abcde','e938b72279981fce748e5b2d1c4f454121ed4448')

	if res == None:
		print "you're stupid"
	else:
		print res