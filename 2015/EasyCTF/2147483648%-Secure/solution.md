1) Go to [site](https://www.easyctf.com/static/problems/intro-js/index.html)

2) Ctrl+u to view source, find some interesting hexadecimal content towards the bottom

    var _0xa107=["\x64\x65\x76\x65\x6C\x6F\x70\x65\x72\x5F\x63\x6F\x6E\x73\x6F\x6C\x65\x5F\x69\x73\x5F\x79\x6F\x75\x72\x5F\x66\x72\x69\x65\x6E\x64","\x65\x61\x73\x79\x63\x74\x66\x7B","\x7D"];
    var _0x6fdc=[_0xa107[0],_0xa107[1],_0xa107[2]];
    var secret=_0x6fdc[0];
    secret=_0x6fdc[1]+secret+_0x6fdc[2];

3) Luckily for us, on Chrome at least the console is pretty feature packed, it'll convert the hex to ascii for us,
so all we have to do is type **secret** in the console and we get back:

    easyctf{developer_console_is_your_friend}

Flag: **easyctf{developer_console_is_your_friend}**
