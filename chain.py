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

	for y in range(2,chain_len):
		reduced_val = reductor.reduce_plain(reduced_val, debug)
		if reduced_val in chain_heads:
			if debug:
				print 'found a cycle!!! for ', reduced_val
			break 
		if debug:
			print 'reduction #', y, ' with reduced_val ', reduced_val
		# TODO: Handle small reduced_val
		# if len(reduced_val) < 6:

	# return (plain, hashlib.sha1(reduced_val).hexdigest())
	return (plain, reduced_val)

if False:
	start = time.time()
	print chain_plain('abcdef')
	end = time.time()
	print end - start