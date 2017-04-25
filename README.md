# crypto-rainbow

A python script that will find the hash value for any SHA-1 hash of a 6 letter word
	* The test cases are base 64 encoded SHA-1 hashes
	* The reduction function consists of simply concatenating the first and last 3 letters of the hash
	* We chain 5 times or until our reductions are less than 6 chars long

## Some Helpful resources:
* [RainbowTables by Kestas Kuliukas](http://kestas.kuliukas.com/RainbowTables/)
* [Wikipedia link](https://en.wikipedia.org/wiki/Rainbow_table)
* [SO question wihth walk-thru example](https://crypto.stackexchange.com/questions/5900/example-rainbow-table-generation)
* [SO explanation of reduction functions](http://stackoverflow.com/questions/5741247/how-does-a-reduction-function-used-with-rainbow-tables-work)
* [Series written by Paul Faulstich ](https://stichintime.wordpress.com/2009/04/09/rainbow-tables-part-5-chains-and-rainbow-tables/)
