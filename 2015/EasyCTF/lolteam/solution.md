1) The file extension is  `.pcapng` so we know we are going to need to use WireShark.

2) Open the file, and string-search the package-bytes for password, since that's what we're looking for.

3) It'll send you to one package, follow the TCP-Stream for it, find something interesting:

    password=flag%7Bno%2C_lolteam_is_not_an_admin_account%7D

4) That is an encoded URL, so paste that into DuckDuckGo (Google won't work :D DDG > Google just saying...)
and arrive at the flag.

Flag: **flag{no,_lolteam_is_not_an_admin_account}**
