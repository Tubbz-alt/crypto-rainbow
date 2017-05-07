# crypto-rainbow

A python script that will find the hash value for any SHA-1 hash of lowercase words

* To see the monster in action run `python test.py`
	* It's a series of test ran on 5 letters SHA-1 hashes
	* I have no idea of what these values are so please do not hold me responsible for their decryption


* We have 2 reduction functions which provide almost similar performance
	* The first runs a crazy computation and then splits the result into a equal amount of hex values that are then `% 26` to match it to a corresponding value of the alphabet. Lastly we concatenate the result.
	* The second turns the hash into a byte array. We then run the result thru some crazy computation and concatenate!
	

* You're Probably thinking that we ought to thread this. We started it. Just haven't gotten around to finishing it


* **Parameters** used for the chains:
	* `NUM_CHAINS = int(math.ceil((26**num_chars)**(2.0/3))*1.5)`
	* `CHAIN_LEN = int(math.ceil((26**num_chars)**(1.0/3))*1.5)`
	* Why? Because we seem to get good results with them


## Usage
`python attack.py [hash] [length of pre-hashed value]`

`python attack.py [hash] [length of pre-hashed value] [ Debug: True/False]`

**Please note that you are responsible for your own type checking. Otherwise we'll simply raise the error**

## Write Up
	For a more academic explanation of our work (read what we told our prof in attempt to get an A),
	have a look at the write up .pdf file included.

	Want a TLDR:
		If you want to keep your users passwords safe,
			first off,
				SHA-256 is the way to go.
					MD5 is now a joke,
					Google (And most definitely the NSA) have broken SHA-1 (read using SHA-1 is for the weak).
		Secondly,
			Hashing isn't enough. Make sure you salt everything.

## Some Helpful resources to better understand the beauty of rainbow tables:
* [Rainbow Tables by Kestas Kuliukas](http://kestas.kuliukas.com/RainbowTables/)
* [Wikipedia link](https://en.wikipedia.org/wiki/Rainbow_table)
* [SO question wihth walk-thru example](https://crypto.stackexchange.com/questions/5900/example-rainbow-table-generation)
* [SO explanation of reduction functions](http://stackoverflow.com/questions/5741247/how-does-a-reduction-function-used-with-rainbow-tables-work)
* [Series written by Paul Faulstich](https://stichintime.wordpress.com/2009/04/09/rainbow-tables-part-5-chains-and-rainbow-tables/)
* [Example of Reduction Function](https://crypto.stackexchange.com/questions/37832/how-to-create-reduction-functions-in-rainbow-tables)

Don't know what hashing is? [Visit this link](http://bfy.tw/Bds2)
