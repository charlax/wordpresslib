#!/usr/bin/env python

"""
	Test code for:
		
	WordPress xml-rpc client library
	use MovableType API
	
	Copyright (C) 2005 Michele Ferretti
	black.bird@tiscali.it
	http://www.blackbirdblog.it
	
	This program is free software; you can redistribute it and/or
	modify it under the terms of the GNU General Public License
	as published by the Free Software Foundation; either version 2
	of the License, or any later version.
	
	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with this program; if not, write to the Free Software
	Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA	02111-1307, USA.

"""

__author__ = "Michele Ferretti <black.bird@tiscali.it>"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2005/05/02 $"
__copyright__ = "Copyright (c) 2005 Michele Ferretti"
__license__ = "LGPL"

import unittest
import wordpresslib
import time

class TestWordPressClient(unittest.TestCase):
	
	def setUp(self):
		self.wp = wordpresslib.WordPressClient('http://www.site.com/wordpress/xmlrpc.php', 'username', 'password')
		self.wp.selectBlog(0)
		self.recentPosts = 10
		
	def ifEmpty(self, obj, msg):
		self.failUnless( '%s is None' % msg)
		self.failIf( obj == '', '%s is empty' % msg)		
		
	def testGetUserInfo(self):
		user = self.wp.getUserInfo()
		self.ifEmpty(user, 'user')
		self.ifEmpty(user.id, 'user id')

	def testGetUsersBlogs(self):
		blogs = self.wp.getUsersBlogs()
		self.failUnless( blogs, 'blogs is None')
		for blog in blogs:
			self.failUnless( blog, 'blog is None')
			self.ifEmpty(blog.id, 'blog id')
			self.ifEmpty(blog.url, 'blog url')

	def testGetRecentPosts(self):
		for post in self.wp.getRecentPosts(self.recentPosts):
			self.ifEmpty(post, 'post')
			self.ifEmpty(post.id, 'post id')

	def testGetCategoryList(self):
		categories = tuple(self.wp.getCategoryList())
		self.failUnless( categories, 'blog categories are None')
		for i in categories:
			self.ifEmpty(i, 'category item')
			self.ifEmpty(i.id, 'category id')
			self.ifEmpty(i.name, 'category name')
		
	def testNewPost(self):
		categories = tuple(self.wp.getCategoryList())
		p = wordpresslib.WordPressPost()
		p.title = 'Test'
		p.description = u'Questo \xe8 una stringa unicode'
		p.categories = (self.wp.getCategoryIdFromName('Progetti'),)
		idNewPost = self.wp.newPost(p, True)
		self.ifEmpty(idNewPost, 'new post id')
		self.failIf( idNewPost < 1 , 'new post id is less than 0')
		
		result = self.wp.deletePost(idNewPost)
		self.failUnless( result, 'deletePost %d failed, return=%s' % (idNewPost, str(result)) ) 
			
	def testGetPost(self):
		# gest last post
		lastPost = self.wp.getLastPost()
		self.failUnless( lastPost, 'last post is None')
		for i in range(lastPost.id, 0,-1):
			try:
				post = self.wp.getPost(i)
			except Exception, ex: 
				self.fail('post id = %d eccezione %s' % (i,ex))
			self.ifEmpty( post, 'post')
			self.ifEmpty( post.id, 'post id')
			self.ifEmpty( post.title, 'post title')
			self.ifEmpty( post.permaLink, 'post permaLink')
			self.ifEmpty( post.description, 'post description')
			self.ifEmpty( post.user, 'post user')
			self.ifEmpty( post.date, 'post date')
			self.ifEmpty( post.categories, 'post categories')
		
	def testGetNotFoundPost(self):
		# gest not found post
		try:
			post = self.wp.getPost(10000000)
		except Exception, ex:
			self.failIf(ex.id != 404, 'Post not found response is not 404')
			
	def testGetPostCategories(self):
		lastPost = self.wp.getLastPost()
		self.failUnless( lastPost, 'last post is None')
		i = 0
		for cat in self.wp.getPostCategories(lastPost.id):
			if i == 0:
				self.failIf( cat.isPrimary != 1, 'first post category is not isPrimary')	
			self.ifEmpty( cat, 'post category')
			self.ifEmpty( cat.name, 'post category name')
			i += 1
		
	def testDeletePost(self):
		lastPost = self.wp.getLastPost()
		self.failUnless( lastPost, 'last post is None')
		result = self.wp.deletePost(lastPost.id)
		self.failUnless( result, 'deletePost %d failed, return=%s' % (lastPost.id, str(result)) )
			
	def testGetLastPost(self):
		lastPost = self.wp.getLastPost()
		self.failUnless( lastPost, 'last post is None')
		self.ifEmpty( lastPost.id, 'post id')
		self.ifEmpty( lastPost.title, 'post title')
		self.ifEmpty( lastPost.permaLink, 'post permaLink')
		self.ifEmpty( lastPost.description, 'post description')
		self.ifEmpty( lastPost.user, 'post user')
		self.ifEmpty( lastPost.date, 'post date')
		self.ifEmpty( lastPost.categories, 'post categories')
			
	def testEditPost(self):
		categories = tuple(self.wp.getCategoryList())
		lastPost = self.wp.getLastPost()
		self.failUnless( lastPost, 'last post is None')
		p = wordpresslib.WordPressPost()
		p.title = lastPost.title +' (modificato)'
		p.date = time.time()
		p.description = lastPost.description + u'<br><br><em>Questa \xe8 una stringa unicode modificata</em>'
		p.categories = map(self.wp.getCategoryIdFromName, ('Python', 'Progetti'))
		self.wp.editPost(lastPost.id, p, True)
		
	def testPublishPost(self):
		lastPost = self.wp.getLastPost()
		self.failUnless( lastPost, 'last post is None')
		result = self.wp.publishPost(lastPost.id)	
		self.failUnless( result, 'publishPost %d failed, return=%s' % (lastPost.id, str(result)) )
		
	def testNewMediaObject(self):
		result = self.wp.newMediaObject('python.jpg')
		self.failUnless( result, 'newMediaObject result is None')
	
if __name__ == '__main__':
	unittest.main()
	"""
	suite = unittest.makeSuite(TestWordPressClient)
	unittest.TextTestRunner(verbosity=2).run(suite)
	"""