import hashlib, chain, cPickle

def genTable(num_reductions=5, num_chains=10, chain_len=20):
	# We keep two dictionaries: {plain,hash}, {hash,plain}
	# This allows for faster lookups, good memory sacrifice to save time
	forward_dic = {} # {plain,hash}
	backward_dic = {} # {hash,plain}

	

	


# cPickle.dump(annexed,pickleFile)
# annexed = cPickle.load(pickleFile)

