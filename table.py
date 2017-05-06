import hashlib, chain, cPickle, random, string, time, reductor, conversions, cPickle, csv

# chris -> 711c73f64afdce07b7e38039a96d2224209e9a6c

# num_Chain = 2**(2.0/3)
# chain_len = 2**(1.0/3)
def get_table(num_chars=5, num_chains=50000, chain_len=200, debug=False):
	# We save to a file for faster generation
	try:
		return get_old_table()
	except:
		pass
	f = open('rbtb.txt', 'wt')
	writer = csv.writer(f)
	for x in range(num_chains):
		if x % 1000 == 0:
			print 'have generated ', x

		rnd_string = ''.join(random.choice(string.lowercase) for i in range(num_chars))
		(chain_head, chain_end) = chain.create_chain(rnd_string, chain_len, debug)

		writer.writerow((chain_head,chain_end))

	return get_old_table()

def get_old_table(tab_name='rbtb.txt'):
	table = {}
	with open('rbtb.txt', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			table[row[0]] = row[1]
	return table

def crackSHA1(hashval, debug=False):
	table = get_table()

	num_chains=50000
	chain_len=200
	num_chars=5

	print 'finished generating table'
	(list_red, list_hash) = chain.get_list_red(hashval, num_chars, chain_len)
	print len(list_red), len(set(list_red))
	i = 0
	for (chain_head, chain_end) in table.iteritems():
		if chain_head in list_red:
			print 'found a collision ' , chain_head
			res = chain.find_hash_in_chain(chain_head, hashval, chain_len)
			if res != None:
				return res
		if chain_end in list_hash:
			res = chain.find_hash_in_chain(chain_head, hashval, chain_len)
			if res != None:
				return res


	return 'no luck finding it after checking '

start = time.time()
print crackSHA1('df51e37c269aa94d38f93e537bf6e2020b21406c')
print '==================================================='
print crackSHA1('cbad02dba1fa008182dffde5e421e24c28949312')
print '==================================================='
print crackSHA1('670dcd8d36377885602119ccf57fa228013c927a')
print '==================================================='
print crackSHA1('e3e587c863fdedfaad8e28c00d3e95d9678009a6')
print '==================================================='
print crackSHA1('e7258d35a6b4c2f1942fcada490ecce41cf1bb32')
print '==================================================='
print crackSHA1('443f4c88549fa4a11b2e1bacef35c59b04bb52ff')
print '==================================================='
print crackSHA1('3931f9c32a344236789e7793492ce27dd2111552')
print '==================================================='
# print crackSHA1(conversions.b64_to_hex('7iEjysAibZbmoZP/9v5w3MPnUW0='))
# print crackSHA1(conversions.b64_to_hex('qwaEUA9V60H/7EDP4cKZY/x36NI='))
end = time.time()
print 'attempt took %fmnts to complete ' % ((end - start)/60.0)