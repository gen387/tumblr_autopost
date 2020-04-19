# tumblr_autopost
A simple bot utilizing Selenium and Python for autoposting links on Tumblr. The way it works is a little weird with calling pressing keys, but it was the only way I found consistently working in case of Tumblr. It's really simple and made to be used with a single account, so there's no hashing password, no reading addresses from a file, no simultaneous or consequtive logging. 
There will be some changes concerning time.sleep and impicitly_wait; looks like waiting for some elements of the page gives more consistency with connection problems occuring.

--

Things to install:
- python
- pip3
- chrome with uBlock Origin

Via pip3
- selenium
- pyperclip
- pynput

To avoid bot getting interupted by blue-glass element of Tumblr, I used uBlock with customized filters. They are imported at the beginning. 
