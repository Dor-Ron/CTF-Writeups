1) In terminal we do: `cat eps1.9_zer0-day_b7604a922c8feef666a957933751a074.avi`

We get back:

	RXZpbCBDb3JwLCB3ZSBoYXZlIGRlbGl2ZXJlZCBvbiBvdXIgcHJvbWlzZSBhcyBleHBlY3RlZC4g\nVGhlIHBlb3BsZSBvZiB0aGUgd29ybGQgd2hvIGhhdmUgYmVlbiBlbnNsYXZlZCBieSB5b3UgaGF2\nZSBiZWVuIGZyZWVkLiBZb3VyIGZpbmFuY2lhbCBkYXRhIGhhcyBiZ
	WVuIGRlc3Ryb3llZC4gQW55\nIGF0dGVtcHRzIHRvIHNhbHZhZ2UgaXQgd2lsbCBiZSB1dHRlcmx5IGZ1dGlsZS4gRmFjZSBpdDog\neW91IGhhdmUgYmVlbiBvd25lZC4gV2UgYXQgZnNvY2lldHkgd2lsbCBzbWlsZSBhcyB3ZSB3YXRj\naCB5b3UgYW5kIHlvdXIgZGFyayB
	zb3VscyBkaWUuIFRoYXQgbWVhbnMgYW55IG1vbmV5IHlvdSBv\nd2UgdGhlc2UgcGlncyBoYXMgYmVlbiBmb3JnaXZlbiBieSB1cywgeW91ciBmcmllbmRzIGF0IGZz\nb2NpZXR5LiBUaGUgbWFya2V0J3Mgb3BlbmluZyBiZWxsIHRoaXMgbW9ybmluZyB3aWxsIGJlIHRo\nZ
	SBmaW5hbCBkZWF0aCBrbmVsbCBvZiBFdmlsIENvcnAuIFdlIGhvcGUgYXMgYSBuZXcgc29jaWV0\neSByaXNlcyBmcm9tIHRoZSBhc2hlcyB0aGF0IHlvdSB3aWxsIGZvcmdlIGEgYmV0dGVyIHdvcmxk\nLiBBIHdvcmxkIHRoYXQgdmFsdWVzIHRoZSBmcmVlIHBlb3BsZSwgY
	SB3b3JsZCB3aGVyZSBncmVl\nZCBpcyBub3QgZW5jb3VyYWdlZCwgYSB3b3JsZCB0aGF0IGJlbG9uZ3MgdG8gdXMgYWdhaW4sIGEg\nd29ybGQgY2hhbmdlZCBmb3JldmVyLiBBbmQgd2hpbGUgeW91IGRvIHRoYXQsIHJlbWVtYmVyIHRv\nIHJlcGVhdCB0aGVzZSB3b3Jkcz
	ogImZsYWd7V2UgYXJlIGZzb2NpZXR5LCB3ZSBhcmUgZmluYWxs\neSBmcmVlLCB3ZSBhcmUgZmluYWxseSBhd2FrZSF9Ig==

2) From the double equal sign padding, I assumed the message was encrypted in base64, so I tried: `cat eps1.9_zer0-day_b7604a922c8feef666a957933751a074.avi | base64 -d`

Which gave back: `Evil Corp, we have delivered on our promise as expected. base64: invalid input`

3) That wasn't the flag, but I googled **Evil Corp, we have delivered on our promise as expected.** and found: [Mr. Robot](http://www.tvfanatic.com/quotes/we-are-fsociety-we-are-finally-free-we-are-finally-awake/)

4) The flag was the bolded titled which was:

flag: **We are fsociety, we are finally free, we are finally awake!**
