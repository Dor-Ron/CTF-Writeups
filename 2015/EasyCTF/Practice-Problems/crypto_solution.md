**Problem**
-----------

Do you like crypto? We do. Try decrypting this: `lqef ef s fehzwa fgpflelglevt oezqak. dwsj ef tvm_jv_fejt_gz_sti_iv_lqa_kasw_oqswwatjaf`


**Solution**
------------

Since the title of the problem doesn't suggest we use a specific cipher and the text has no distinguishing feature, such as 
the base64 padding, we really can't tell the encryption algorithm was used on the text. So the next best thing is to use a
cryptogram solver and hope that it'll save us the trouble of figuring out how to decrypt the text. I used [quipquip](http://www.quipqiup.com/index.php)
But some other good ones are [rumkin cryptogram solver](http://rumkin.com/tools/cipher/cryptogram.php). The top result using *quipquip* was:

**this is a simple substitution cipher. flag is nod_go_sign_up_anz_zo_the_real_challenges**

and

**this is a simple substitution cipher. flag is now_go_sign_up_any_yo_the_real_challenges**

Combining the two, and using our logic, we come up with the flag which is:

Flag: **now_go_sign_up_and_do_the_real_challenges**
