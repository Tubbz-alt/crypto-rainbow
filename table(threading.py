'''The equivalent of table.py but we use threading while generating
IT IS NOT FULLY DONE, 
only generates 1/100 of the required values
no clear improvements noticed'''
import hashlib, chain, cPickle, random, string, time, reductor, conversions, cPickle, csv, threading

# num_Chain = 2**(2.0/3)
# chain_len = 2**(1.0/3)

'''2 out of 20
attempt took 5.935867mnts to complete'''

correct = 0
table = {}
num_threads = 10

lock = threading.Lock()

def get_table(num_chars=5, num_chains=75000, chain_len=250, debug=False):
	# We save to a file for faster generation
	try:
		return get_old_table()
	except:
		pass


	threads = [threading.Thread(target=run_gen_threads, args= (num_chars, num_chains/num_threads, chain_len, x)) for x in range(num_threads)]
	for thread in threads:
		thread.start()

	for thread in threads:
	    thread.join()

	return get_old_table()

def run_gen_threads(num_chars, num_chains, chain_len, thread_num, debug=False):
	f = open('rbtb.txt', 'wt')
	writer = csv.writer(f)

	for x in range(num_chains):
		if x % 1000 == 0:
			print 'Thread %i has generated %i chains' % (thread_num, x)

		rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))
		(chain_head, chain_end) = chain.create_chain(rnd_string, chain_len, debug)

		lock.acquire(True)
		writer.writerow((chain_head,chain_end))
		lock.release()


def get_old_table(tab_name='rbtb.txt'):
	global table 
	with open(tab_name, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			table[row[0]] = row[1]
	return table

def crackSHA1(hashval, debug=False):
	table = get_table()

	num_chains=75000
	chain_len=250
	num_chars=5

	print 'finished generating table'
	list_hash = chain.get_list_red(hashval, num_chars, chain_len)

	for (chain_head, chain_end) in table.iteritems():
		if chain_end in list_hash:
			res = chain.find_hash_in_chain(chain_head, hashval, chain_len)
			if res != None:
				global correct
				correct = correct + 1
				return res


	return 'no luck finding it after checking '

start = time.time()
print crackSHA1('3e83b13d99bf0de6c6bde5ac5ca4ae687a3d46db')
print '==================================================='
print crackSHA1('711c73f64afdce07b7e38039a96d2224209e9a6c')
print '==================================================='
print crackSHA1('d8d6a288a51e2489da3fecf2891d4a9d427e727f')
print '==================================================='
print crackSHA1('3b19ecd69b492a40e3061f17786b33c28f504239')
print '==================================================='
print crackSHA1('e7258d35a6b4c2f1942fcada490ecce41cf1bb32')
print '==================================================='
print crackSHA1('29f2a328decf7a91bdde9d6e8f37a69bb13e2085')
print '==================================================='
print crackSHA1('c286217add963b9cae2cd3886f66ec4931e308e9')
print '==================================================='
print crackSHA1('bd909fdab812aa2e0ccbfe23fc84da5cae68cad6')
print '==================================================='
print crackSHA1('7bc70bc7a58c340e993fef5a82070c029a174f14')
print '==================================================='
print crackSHA1('1ce2d6f9491304c88e8154c3a2271ca04694f256')
print '==================================================='
print crackSHA1('c3de758aa2d37701882d43d70c96e3e2131f7c35')
print '==================================================='
print crackSHA1('ad691d435b47042374277cd89e2c156683e2ba70')
print '==================================================='
print crackSHA1('8b83cb03a8042a8d87009a45fbac32fc746f29c0')
print '==================================================='
print crackSHA1('e687ad1057c96571974d3750a253917d3d823f05')
print '==================================================='
print crackSHA1('63e02fb4eabc3959540c4ab40becf245dd6f295f')
print '==================================================='
print crackSHA1('d92d266f60eff2f6bd9f5ffa522c8dd7830ac6d2')
print '==================================================='
print crackSHA1('c1448a59c6f3719863b1e3e2cdb7baee30b993c0')
print '==================================================='
print crackSHA1('b9279dd530966836a04c9881b1bdb4a1aae3c572')
print '==================================================='
print crackSHA1('0d8be45f65c033345972cb416161d59ef2d71451')
print '==================================================='
print crackSHA1('6cd93a1728a02d69582e4882d0e61c5103dba107')
print '==================================================='
print str(correct) + " out of 20"
# print crackSHA1(conversions.b64_to_hex('7iEjysAibZbmoZP/9v5w3MPnUW0='))
# print crackSHA1(conversions.b64_to_hex('qwaEUA9V60H/7EDP4cKZY/x36NI='))
end = time.time()
print 'attempt took %fmnts to complete ' % ((end - start)/60.0)