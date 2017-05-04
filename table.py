import hashlib, chain, cPickle, random, string, time, reductor, conversions, cPickle

# chris -> 711c73f64afdce07b7e38039a96d2224209e9a6c

# num_Chain = 2**(2.0/3)
# chain_len = 2**(1.0/3)
def genTable(num_chars=5, num_chains=50000, chain_len=200, debug=False):
	# We keep two dictionaries: {plain,hash}, {hash,plain}
	# This allows for faster lookups, good memory sacrifice to save time

	newly_generated = False

	forward_dic = {} # {plain,hash}
	backward_dic = {} # {hash,plain}
	try:
		forward_dic = cPickle.load('forward.pckl')
		backward_dic = cPickle.load('backward.pckl')
	except:
		newly_generated = True


	for x in range(num_chains):
		if x % 1000 == 0:
			print 'have generated ', x
		rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))

		while rnd_string in forward_dic.keys():
			rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))

		(key, val) = chain.create_chain(rnd_string, forward_dic.keys(), chain_len, debug)

		while key == None:
			print 'found a Collision'
			rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))

			while rnd_string in forward_dic.keys():
				rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))
			(key, val) = chain.create_chain(rnd_string, forward_dic.keys(), chain_len, debug)

		forward_dic[key] = val
		backward_dic[val] = key

	if newly_generated:
		cPickle.dump(forward_dic,'forward.pckl')
		cPickle.dump(backward_dic,'backward.pckl')

	return (forward_dic, backward_dic)


def crackSHA1(hashval, debug=False):
	(forward_dic, backward_dic) = genTable()

	indx = len(forward_dic.values())
	while hashval not in forward_dic.values() and indx >= 0:
		indx -= 1
		hashval = reductor.reduce_hash(hashval,5, indx, False)

		if debug:
			print 'curr indx: ', indx

	if hashval in forward_dic.values():
		return chain.find_hash_in_chain(backward_dic[hashval], hashval)
	else:
		return 'no luck finding it after checking ', indx



start = time.time()
print crackSHA1('711c73f64afdce07b7e38039a96d2224209e9a6c')
# print crackSHA1(conversions.b64_to_hex('7iEjysAibZbmoZP/9v5w3MPnUW0='))
# print crackSHA1(conversions.b64_to_hex('qwaEUA9V60H/7EDP4cKZY/x36NI='))
end = time.time()
print end - start