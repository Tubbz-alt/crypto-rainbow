import hashlib, chain, cPickle, random, string, time, reductor, conversions, threading

# chris -> 711c73f64afdce07b7e38039a96d2224209e9a6c

# num_chains = 2**(2.0/3)
# chain_len = 2**(1.0/3)
global forward_dic
global backward_dic

lock = threading.Lock()

def genTable(num_chars=5, num_chains=50000, chain_len=200, num_threads=10, debug=False):
	# We keep two dictionaries: {plain,hash}, {hash,plain}
	# This allows for faster lookups, good memory sacrifice to save time
	global forward_dic 
	global backward_dic 

	forward_dic = {} # {plain,hash}
	backward_dic = {} # {hash,plain}

	threads = [threading.Thread(target=f, args= (num_chars, num_chains/num_threads, chain_len)) for _ in range(num_threads)]
	for thread in threads:
	    thread.start()

	return (forward_dic, backward_dic)

def run_gen_threads(num_chars, num_chains, chain_len, debug=False):
	global forward_dic 
	global backward_dic 

	for x in range(num_chains):
		print 'have generated ', x
		rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))

		while rnd_string in forward_dic.keys():
			lock.aquire(True)
			rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))
			lock.release()

		(key, val) = chain.chain_plain(rnd_string, forward_dic.keys(), chain_len, debug)

		while key == None:
			print 'found a Collision'
			rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))

			while rnd_string in forward_dic.keys():
				rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))
			(key, val) = chain.chain_plain(rnd_string, forward_dic.keys(), chain_len, debug)

		forward_dic[key] = val
		backward_dic[val] = key

def crackSHA1(hashval, debug=True):
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


# cPickle.dump(annexed,pickleFile)
# annexed = cPickle.load(pickleFile)

start = time.time()
print crackSHA1('711c73f64afdce07b7e38039a96d2224209e9a6c')
# print crackSHA1(conversions.b64_to_hex('7iEjysAibZbmoZP/9v5w3MPnUW0='))
# print crackSHA1(conversions.b64_to_hex('qwaEUA9V60H/7EDP4cKZY/x36NI='))
end = time.time()
print end - start