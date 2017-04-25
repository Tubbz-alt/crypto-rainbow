import hashlib, chain, cPickle, random, string, time

# chris -> 711c73f64afdce07b7e38039a96d2224209e9a6c

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

	return (forward_dic, backward_dic)


def crackSHA1(hashval):
	(forward_dic, backward_dic) = genTable()

	if hashval in forward_dic.values():
		return chain.find_hash_in_chain(backward_dic[hashval], hashval)

# start = time.time()
# genTable()
# end = time.time()
# print end - start

# cPickle.dump(annexed,pickleFile)
# annexed = cPickle.load(pickleFile)

