We first connect to the leviathon0 server through ssh, with the credentials supplied to us.

`ssh leviathan0@leviathan.labs.overthewire.org`

We are prompted for a password. Type **leviathan0** and connect.

This wargame is trickier than bandit, in that no instructions are supplied, but we know that we're looking for the password to leviathon1

Steps I did to solve Leviathon0-1:

1)  `ls`  -  nothing showed up. Okay maybe there are hidden files and/or directories.

2)  `ls -a` - Aha! I knew it we get back `.  ..  .backup  .bash_logout  .bashrc  .profile`
    Know .bash_logout, .bashrc, and .profile are configuration files, so it's probably not hidden in them.

3)  `cd .backup && ls`  - we get back `bookmarks.html`

4)  `grep "password" bookmarks.html`  - get back:
    <DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html |
    This will be fixed later, the password for leviathan1 is rioGegei8m" 
    ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
  

Flag: **rioGegei8m**



