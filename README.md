JoliesChoses (Beautiful things)
===============================
-------------------------------

Every morning, at anytime, beautiful things in your inbox !

######Tested with python 2.7#######

How It Works
============
------------

Needs
-----
* Linux/Unix system

* Gmail account

* A brain

* Python and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) and [pycurl](http://pycurl.sourceforge.net/) working properly together

Blah Blah Blah
--------------
At the begining of bonjours.py, you have some constants that you must/can change so I can works. Feel free to change the things that are printed.
There're also sleep_wait, max_try values at the begining of the script. That's in case you lost Internet. It will wait **sleep_wait** seconds before retrying, and will try **max_try** times.
The **timeout_value** is the pycurl time (in seconds) before it times out.

Adding websites
---------------


If you want to add websites to the one I chose, just respect the same presentation :
Let's take the case of bonjourmadame.fr (well known, that's for a reason I guess), the website is like this (the image zone) :
```html
<div class="photo">
	<div class="permalink"><a href="http://bonjourmadame.fr/post/41934955472">+</a></div>
	<img src="http://25.media.tumblr.com/a2899372850582bc906c855673cbf8f0/tumblr_mh707plpKC1s4rgpyo1_500.jpg" alt="">
</div>
```
So, actually, what is important is 
```html
<div class="photo">
	<img src="http://25.media.tumblr.com/a2899372850582bc906c855673cbf8f0/tumblr_mh707plpKC1s4rgpyo1_500.jpg">
</div>
```
What we see is that the parent's div class-name is "photo" and there's the img tag in this div.
So, when you're making the config file "heySexyLady" it should looks like :
```txt
http://bonjourmadame.fr|Your title, sentence, joke or something|class|photo
```
As you see, it's divided into parts separated by a pipe (|).
The first part is the **website**, be sure it's a valid url or the program won't work.
The **title** is the sentence that will be written just before your image. Leave blank if not needed/wanted.
The third part is the type of the parent div. It can be a **class** or an **id**
The last part is the name of the previous part. Here **photo**.

###REMEMBER: In your title, no |, this character is reserved as a delimiter###


Adding recipients
-----------------

Adding recipients is quite easier. Actually, you just have to add the email address to the toSexyBoys file.
```txt
toto@titi.com
titi@toto.com
```

###REMEMBER: One email each line###


Launch repetitively
-------------------

Well, you'll need a *NIX. 
If you don't know about cronjobs, let's go see [there] (http://www.adminschoice.com/crontab-quick-reference) and when you know what this is you can go [there] (http://www.abunchofutils.com/utils/developer/cron-expression-helper/)
For example, my crontab is :
```sh
0 11 * * * python $HOME/bonjours.py >> $HOME/bonjourresult 2>&1
```
I chose to redirect in a file because I use print in the python script, and I want to keep logs of it.


Who made this?
==============
--------------

* [Me](http://quentin-dommerc.com) (web-CV)

* [Me](mailto:dommer.q@gmail.com) (email)

Why ?
=====
-----
[Hey dude, why not.] (http://3.bp.blogspot.com/-qnardgqMExs/Tn1YLXlEZXI/AAAAAAAAASQ/LBkqNTUZBHU/s1600/funny-pictures-fuck-you-thats-why.jpg)