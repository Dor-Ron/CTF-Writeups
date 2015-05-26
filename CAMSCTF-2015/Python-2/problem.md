1.) Take the RGB value of every pixel in one image.(Start at (0,0). Move down to (0,299). Go to (1,0). Move to (1,299). And so on. Read the files in numerical order.)
2.) Add all of the R values, G values, and B values in each image. (Have one R sum, one B sum, one G sum for every image.)
3.) Take these sums and convert them into strings. Take the MD5 hash of each string.
4.) Concatenate these MD5 hashes into one string.
5.) Take the MD5 hash of the new string.
6.) Do this for every image and concatenate the final MD5 hashes into one string. (Image 1 final hash + Image 2 final hash + ...)
7.) Take the MD5 of this string to get the flag.
**PIL.zip**

p.s. we had to download PIL.zip
