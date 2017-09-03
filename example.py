#!/usr/bin/env python

"""
	Small example script that publish post with JPEG image
"""

# import library
import wordpresslib

print 'Example of posting.'
print

url = raw_input('Wordpress URL (xmlrpc.php will be added):')
user = raw_input('Username:')
password = raw_input('Password:')

# prepare client object
wp = wordpresslib.WordPressClient(url+"xmlrpc.php", user, password)

# select blog id
wp.selectBlog(0)
	
# upload image for post
# imageSrc = wp.newMediaObject('python.jpg')

# FIXME if imageSrc:

# create post object
post = wordpresslib.WordPressPost()
post.title = 'Test post'
post.description = '''
Python is the best programming language in the earth !

No image BROKEN FIXME <img src="" />

'''
#post.categories = (wp.getCategoryIdFromName('Python'),)

# Add tags
post.tags = ["python", "snake"]

# do not publish post
idNewPost = wp.newPost(post, False)

print
print 'Posting successful! (Post has not been published though)'
	

