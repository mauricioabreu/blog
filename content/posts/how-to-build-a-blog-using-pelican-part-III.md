How to build a blog using Pelican - Part III
============================================

date

:   2016-01-05 16:00

tags

:   pelican, python, travis

slug

:   how-to-build-a-blog-using-pelican-part-III

This is the last post of this series. In the [last
post](%7Bfilename%7D/how-to-build-a-blog-using-pelican-part-II.rst) I
talked about plugins and tools used to deploy this blog.

Today we are going to check what kind of magic trick I am using to get
fresh and updated content after a simple git push. In resume it uses
[Travis CI](https://travis-ci.org/) and SSH authentication.

SSH keys
--------

I am not that kind of crazy-about-security-person but I try to do my
best. At work I use SSH keys, two-factor authentication when possible
and other security mechanisms. In order to make it easier to write and
publish content, we don't want to ask for passwords when deploying our
new content to the server - it would not work easily for tablets or
smartphones, would it?

Now you need to generate a pair of SSH keys. Github has a [good
tutorial](https://help.github.com/articles/generating-ssh-keys/) around
this topic.

After setting up a new SSH key we need to install [Travis
encryption](https://docs.travis-ci.com/user/encryption-keys/) tool:

``` {.sourceCode .shell}
$ gem install travis
```

Right after generating the SSH keys you need to add it to your
*authorized\_keys* file inside your server.

``` {.sourceCode .shell}
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

We don't want to send our unencrypted file to Github, right? To achieve
a higher level of security we need to encrypt our file using that Travis
tool we just installed:

``` {.sourceCode .shell}
$ travis encrypt-file deploy-key # (the private one, not the .pub)
```

This command will generate a file with the .enc extension. Add the .enc
file to repository.

**Don't ever publish your rsa\_file to the upstream. After being visible
to other you are by yourself.**

Travis CI
---------

Travis CI is a continuous integration platform. It is an easy to use
online tool that provides a backend infrastructure to test and deploy
code.

First you need to setup a Travis account, authenticated with Github and
turn on your blog repository. Currently Travis is only integrated to
Github so if you are using Bitbucket you may want to use another
service.

To run Travis jobs your code needs to maintain a .travis.yml file. Here
is how my file looks like:

``` {.sourceCode .shell}
language: python
sudo: false
branches:
  only:
    - master
git:
  submodules: false
before_install:
    - git submodule update --init --recursive
    - echo -e "Host 162.243.186.254\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
    - openssl aes-256-cbc -K $encrypted_bd9d366e80a4_key -iv $encrypted_bd9d366e80a4_iv -in deploy-key.enc -out deploy-key -d
    - chmod 600 deploy-key
    - mv deploy-key ~/.ssh/id_rsa
install: "pip install -r requirements.txt"
script: 
    - pelican content
    - fab publish
```

This file above describes the steps and resources used to run the Travis
jobs.

In plain english it build a Python job only when it is the master
branch.

before\_install is an important directive that tells what is needed to
bootstrap the environment (project provision goes here). Also it adds my
Digital Ocean droplet IP to the known hosts, decrypts the deploy-key.enc
file (file generated running travis-encrypt command) and copy it to the
SSH keys in the Travis containers.

install is another important directive. Note that we are not creating a
virtualenv here. It is not so necessary here because Travis isolates
jobs using Docker containers so everything is dropped after finished.

script is the part where we tell which commands need to run in order to
achieve our goal: generate the static content and publish it using
Fabric.

Conclusion
----------

I hope you have learned something on this series. Leave a comment if you
have any questions on how to setup a blog using Pelican.

Peace! :-)
