The key to solving this problem is knowing how the random module works.
If you generate a seed, then all the random numbers generated will always be the same.
Therefore, we make a script with a **random.seed(999999999999999999999999999999999999)**
then just print out **key=math.floor(random.random()*1000000)**
And that number would be what you submit when you use telnet/netcat to connect to the port.
After entering **310295.0** I was presented with the flag.

Flag: stuyctf{Nevar_use_k0nstant_seeds}
