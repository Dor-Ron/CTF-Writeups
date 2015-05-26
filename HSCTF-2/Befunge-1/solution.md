Befunge uses reverse polish notation, therefore we write whatever numbers we want to multiply,
and then we write the operator. We need to multiply 2 user inputs, which in befunge, uses the ampersand.
Therefore, the befunge code is as follows:
**>&&*.@** 
where we take 2 user inputs, multiply them, pop the value from the stack using the period,
and ending the program using the at symbol.

After we write the code we need to **nc 104.236.80.67 5677** from terminal.
We input our code and get the following message returned.

*" Nice! The flag is 'A Whole New Language?' "*

Flag: A Whole New Language?
