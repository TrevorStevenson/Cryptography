## Usage guidelines:

You will need Python 3 installed to run these scripts. You can download it at www.python.org/downloads.

Download the project, open terminal and cd into the downloaded project folder.

### Frequency Analysis Tool:

Runs frequency analysis on characters, digraphs, and trigraphs in a ciphertext to help decipher a simple substitution cipher.

1. Open cipher.txt and paste your ciphertext into the file
2. Run chmod 755 frequency_analysis.py
3. Run ./frequency_analysis.py
4. View the output in single.txt, double.txt, and triple.txt

### Extended Euclidean Algorithm:

Gives the greatest common divisor and expresses it as a linear combination of the two numbers. Also calculates inverses mod n.

1. Run chmod 755 euclidean.py
2. Run ./euclidean.py
3. Enter your first number and press enter
4. Enter your second number and press enter
5. View the output in the terminal

### Discrete Log Tool:

Solves the discrete logarithm problem that is important for cracking public key cryptosystems like ElGamal.

1. Run chmod 755 discrete_log.py
2. Run ./discrete_log.py
3. Enter the base number as g
4. Enter the congruence mod n as h
5. Enter the modulus as p
6. View the exponent in the terminal
7. Note that if p is very large it will take some time to output a solution

