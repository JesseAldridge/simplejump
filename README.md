simplejump
==========

To install, first do:

    cd ~
    git clone git://github.com/JesseAldridge/simplejump.git


Then, add the following to your `.bashrc` (or `.bash_profile` on OS X) (or `.zshrc` if you're using zsh):

    . ~/simplejump/shell_part.sh

Then restart your shell.

Now, after you cd to a directory you can jump back to it with `z <partial name>`.

Example:

    $ cd
    $ pwd
    /Users/jessealdridge2
    $ mkdir -p foo/bar/baz
    $ cd foo/bar/baz
    $ cd ~
    $ z ba
    $ pwd
    /Users/jessealdridge2/foo/bar/baz

[rvm](https://rvm.io/) causes problems with this.  Not sure why.

This project is a clone of z (https://github.com/rupa/z).
