JoliesChoses
============

Tous les matins, à l'heure que vous souhaitez, des jolies choses dans votre boite mail

How It Works
============
	
Adding websites
---------------

If you want to add websites to the one I chose, just respect the same presentation :
Let's take the case of bonjourmadame.fr (well known, that's for a reason I guess), the website is like this (the image zone) :
> <div class="photo">
> <div class="permalink"><a href="http://bonjourmarion.fr/post/41934955472">+</a></div>
> <img src="http://25.media.tumblr.com/a2899372850582bc906c855673cbf8f0/tumblr_mh707plpKC1s4rgpyo1_500.jpg" alt="">
> </div>
So, actually, what is important is 
```<div class="photo">
src="http://25.media.tumblr.com/a2899372850582bc906c855673cbf8f0/tumblr_mh707plpKC1s4rgpyo1_500.jpg"
</div>```
What we see is that the parent's div class-name is "photo" and there's the img tag in this div.
So, when you're making the config file "heySexyLady" it should looks like :
> http://bonjourmarion.fr|Your title, sentence, joke or something|class|photo
The title is the sentence that will be just before you're image. Leave blank if not needed/wanted.


Just run the python program when you want to crowl the pages