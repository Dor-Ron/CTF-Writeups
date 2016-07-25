# tatami - 70, Solution
---

We see the downloadable's file extension is **.pcapng**, that is our queue to use *Wireshark* or a similar program of your choice to audit the net traffic log. There are a few GET requests, we don't really care for the *CSS* and *JS* ones, as they are meant for the webpage we're looking for and not for the flag usually. We see this one which stands out `http://pasted.co/325c08c1/fullscreen.php?hash=2f45dc03ba0f7494bc6adced32046763&linenum=false` and when we visit the link it prompts us for a password before we can see the content. So we look for a POST request log entry, and sure enough there is one with the field of `"password_325c08c1" = "nowaifunolaifu"` Which is our password.

We get a huge string of data which seems to be base64 encoded from the *=* sign padding at the end. A google search led me to using the data to encode an image. In an html file, do the following:

`<img src = image:data; base64, <<<data>>>`

And using the problem's data it will render to the following ![image](./flag.png)

Flag: **WEEB{GAS_TEH_NONWEEBS}**
