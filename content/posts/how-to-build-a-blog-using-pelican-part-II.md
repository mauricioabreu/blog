How to build a blog using Pelican - Part II
===========================================

date

:   2015-12-25 19:00

tags

:   pelican, python

slug

:   how-to-build-a-blog-using-pelican-part-II

In the [last
post](%7Bfilename%7D/how-to-build-a-blog-using-pelican-part-I.rst) I
showed you a bigger picture of the stack used by this blog. This one is
to show some tools that make it easier to write, review and deploy it to
production.

Pelican is very useful alone. You can write and deploy content to your
site only running some commands. But if you need a fancier, easier and
better workflow to frequently deploy content you might install and setup
other tools.

Fabric
------

[Fabric](http://www.fabfile.org/) is a tool designed to turn SSH
deployment and system administrator tasks trivial.

After installing Pelican you can use the pelican-quickstart command to
setup a well structured project architecture. You will be asked some
questions in order to generate the files needed by Pelican.

The part we are aiming is the following
"Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)".
Say yes to this question and two files will be added to your project:
Fabfile and Makefile.

Makefile is very useful but this time we will use Fabric only. You can
remove this file if you want.

My workflow makes use of 3 \`fab functions\`: build, serve and publish.

*build*

Build is a function to build the local version of your site. It turns
your content into static files into output folder.

*serve*

Serve runs a local server so you can point to <http://localhost:8000> to
see how your writings look like.

*publish*

Publish executes a rsync operation to send all the content inside output
folder to your server.

What does it mean at all? It is the whole set of commands I use
everytime I blog.

Plugins
-------

I consider a plugin to be a tool. A tool is something you use to achieve
a goal. Some tools have a lot of responsabilities, others not so much -
they perform micro tasks.

This blog uses 2 plugins: assets and gzip\_cache. Former is a useful
plugin to compile and minify CSS and JS files, reducing the amount of
files browsers need to download. The latter is a plugin to compress
files to prevent the web server to do it at runtime. You can find more
info on how to use the plugin ecosystem in the [Pelican
docs](http://docs.getpelican.com/en/latest/plugins.html).

Note that to use plugins you better have some knowledge of
git submodules.

In the [next
post](%7Bfilename%7D/how-to-build-a-blog-using-pelican-part-III.rst) I
will talk about the deployment of this blog using Travis CI and how I
managed to use SSH key authentication to make deploys after a simple
git push.
