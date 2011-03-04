WordPress Python Library
========================

A simple python library for WordPress (XML-RPC interface).

The following methods are supported:

* getUsersBlogs
* getUserInfo
* getPost
* getRecentPosts
* newPost
* editPost
* deletePost
* newMediaObject
* getCategoryList
* getPostCategories
* setPostCategories
* getTrackbackPings
* publishPost
* getPingbacks
* tags

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




