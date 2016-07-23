# Solution, The Flash, 35
---

We go to the link in the problems description and check source. We see **c3RvcHRoYXRqcw==** commented out in the HTML. From the *==* padding we can tell the text was encrypted with base64, so we go to terminal and type

`$ echo "c3RvcHRoYXRqcw==" | base64 -D`

stdout for that command is:

`stopthatjs`

I use [this](https://noscript.net/) Firefox extension sometimes to disable the source on the page. Input the decrypted string from the commented out HTML code and voila, the flag.

Flag: **
ABCTF{no(d3)_js_is_s3cur3_dasjkhadbkjfbjfdjbfsdajfasdl}
**
