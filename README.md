WordPress Python Library
========================

⚠️ **This library is not maintained anymore**

A simple python library for WordPress (XML-RPC interface).

The following methods are supported:

* Publishing new post (title, body, tags, categories, custom fields…)
* Editing old post
* Publishing draft post
* Deleting post
* Changing post categories
* Getting blog and user informations
* Upload multimedia files like movies or photos
* Getting last recents post
* Getting last post
* Getting Trackbacks of post
* Getting Pingbacks of post

Example
=======

	import wordpresslib
	
	url = "http://www.mysite.com/wordpress/xmlrpc.php"
	
	wp = wordpresslib.WordPressClient(url, 'username', 'password')
	
	wp.selectBlog(0)
	
	post = wordpresslib.WordPressPost()
	
	post.title = 'Title'
	post.description = 'Content'
	post.tags = ["wordpress", "lib", "python"]
	
	# Set to False to save as a draft
	idPost = wp.newPost(post, True)

Contributing
============

Very happy to have contributions to this project. Please write tests for any new features and always ensure the current tests pass.

License: GNU/GPL

Thanks
======

This project has been started by Michele Ferretti in 2005.

Original project was here: 

* http://code.google.com/p/wordpress-library/
* http://www.blackbirdblog.it/progetti/wordpress-library#english
