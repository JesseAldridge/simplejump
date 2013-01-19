simplejump
==========

z (https://github.com/rupa/z) wasn't working for me, so I made my own


To install, first do:

    cd ~
    git clone git@github.com:JesseAldridge/simplejump.git


Then, add the following to your `.bashrc` (or `.bash_profile` on OS X):

    . ~/simplejump/rebind_cd.sh


Now after you cd to a directory you can jump back to it with `z <partial name>`.

Example:

    $ pwd
    /Users/jessealdridge2
    $ cd ~/foo/bar/baz
    $ cd ~
    $ z ba
    $ pwd
    /Users/jessealdridge2/foo/bar/baz
