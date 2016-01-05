How to build a blog using Pelican - Part I
##########################################

:date: 2015-12-19 16:41
:tags: pelican, python
:slug: how-to-build-a-blog-using-pelican-part-I

This post is part of a tutorial series showing how I built this blog: the stack, tools, workflow and deploy.

In case you are wondering, this is a static site. It means every page you get is not dynamically generated. It is a bunch of HTML files being served to the web.

Pelican
-------

Pelican is a static site generator written in Python. Pelican has a nice set of features. Here is the most important ones:

- Write content in reStructuredText, Markdown, or AsciiDoc formats
- Custom themes
- Lots of plugins
- RSS feeds
- Import from Wordpress


Why static? It might sound weird but static sites are having a come back. And it is a good thing!

Static sites are easier to deploy because you don't need a full stack, only a web server serving the static content (HTML, CSS, JS).

How to start
------------

First you need to install Pelican:

    $ pip install pelican

Create the structure of your blog:

    | $ mkdir blog
    | $ pelican blog

This command will create an `output` folder with static files ready to be served.

You can now create a file using reStructuredText to write your first post:

    | $ mdkir content
    | $ vim content/my_first_post.rst

After writing some text you need to generate the static files:

    $ pelican content

A message like this

    Done: Processed 4 articles, 0 drafts, 0 pages and 0 hidden pages in 0.25 seconds.

will appear in your console. See how fast it is! Impressive, right?

Use Python built-in HTTP server to serve your content locally

    $ python -m SimpleHTTPServer 8000

and here you go! Open your preferred web browser and enter `http://localhost:8000/`.

More on how to write content and build a structure (content folders, configuration files, static directories) you can read on `Pelican docs`_.

Serving
-------

nginx_ is a good choice to serve your blog. 
I use Ubuntu on my server and to get it up and running was easy like:

    $ (sudo) apt-get install nginx

After having nginx running you can change your configuration files to your own purposes. Here are an example_.

Theming
-------

Pelican comes with a default theme. This blog is using Flex_ theme, a clean and beautiful theme designed mainly by Alexandre Vicenzi and others contributors.

In the `next post <{filename}/how-to-build-a-blog-using-pelican-part-II.rst>`_ I will talk about some tools and workflow.

.. _Pelican docs: http://docs.getpelican.com
.. _nginx: http://nginx.org/
.. _example: https://raw.githubusercontent.com/mauricioabreu/blog/master/maugzoide.com.conf
.. _Flex: https://github.com/alexandrevicenzi/flex
