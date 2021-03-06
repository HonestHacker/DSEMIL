# DSEMIL
De Situ Exec Maths Instruction Language
## Author.
Copyright © Makar Kuznetsov (2021)
All rights reserved.
License is GNU GPL v3 (see file LICENSE for more information)
## Getting Started.
### Install DSEMIL.
It's very easy! Execute:<br>
<code>git clone https://github.com/HonestHacker/DSEMIL.git</code><br>
... and done!
### Hello World (sum calculator).
Create file sum.dsemil and write code:
<br><code>
	{ Calculator of sum a + b = c, where a, b — summands and c — sum }<br>
	_____________<br>
	input <- a, b<br>
		c = a + b<br>
	output -> c</code><br>
Then write in Terminal:
<br><code>python3 DSEMILEngine.py sum.py</code><br>
... and execute this command. Write values of a and b and rejoice :)