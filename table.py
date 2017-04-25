import hashlib, chain, cPickle, random, string

def genTable(num_chars=5, num_reductions=5, num_chains=10, chain_len=100000, debug=False):
	# We keep two dictionaries: {plain,hash}, {hash,plain}
	# This allows for faster lookups, good memory sacrifice to save time
	forward_dic = {} # {plain,hash}
	backward_dic = {} # {hash,plain}



	for x in range(num_chains):
		rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))

		while rnd_string in forward_dic.keys():
			rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))

		(key, val) = chain.chain_plain(rnd_string, forward_dic.keys(), chain_len, debug)

		forward_dic[key] = val
		backward_dic[val] = key

	print forward_dic
	print backward_dic


# cPickle.dump(annexed,pickleFile)
# annexed = cPickle.load(pickleFile)

