from setuptools import setup

setup(
	name = "flickr_api",
	version = '0.3',
	description = "Python wrapper for the Flickr API",
	author = "Alexis Mignon",
	author_email = "alexis.mignon@gmail.com",
	url = "http://code.google.com/p/python-flickr-api/",
	packages = ["flickr_api"],
	install_requires = [
		"oauth",
	],
	license = "BSD License",
)
