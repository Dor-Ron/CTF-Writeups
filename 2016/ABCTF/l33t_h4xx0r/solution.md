# l33t h4xx0r - 70 Solution
---

We see that the php source is comparing our input to the flag by these 2 lines.

    $PASSWORD =  (file_get_contents("flag.txt"));
    ...
    if(strcmp($PASSWORD, $_GET['password']) == 0){
  			$success = true;
    }

So we have to exploit the string comparison function **strcmp** somehow. A google search will tell you that comparing a string to an array using **strcmp()** will return 0 meaning the equivalent. So we need to take advantage of this vulnerability.

Simply edit the url to the following and it'll show us the flag

`http://yrmyzscnvh.abctf.xyz/web6/?password[]=`

Flag: **abctf{always_know_whats_going_on}**
