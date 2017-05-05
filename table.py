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

	list_red = chain.get_list_red(hashval, num_chars, chain_len)

	for (chain_head, chain_end) in table.iteritems():
		if chain_head in list_red:
			res = chain.find_hash_in_chain(chain_head, hashval, chain_len)
			if res != None:
				return res

	return 'no luck finding it after checking ', indx



start = time.time()
print crackSHA1('711c73f64afdce07b7e38039a96d2224209e9a6c')
# print crackSHA1(conversions.b64_to_hex('7iEjysAibZbmoZP/9v5w3MPnUW0='))
# print crackSHA1(conversions.b64_to_hex('qwaEUA9V60H/7EDP4cKZY/x36NI='))
end = time.time()
print 'attempt took %fs to complete ' % (end - start)/60.0