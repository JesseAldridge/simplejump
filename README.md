simplejump
==========

To install, just run: 
    `git clone git://github.com/JesseAldridge/simplejump.git ~/simplejump`

Then add `source ~/simplejump/shell_part.sh` to your `.bashrc` (or `.bash_profile` on OS X) (or `.zshrc` if you're using zsh)

Then restart your shell and you're done.

Now, after you cd to a directory you can jump back to it with `z <partial name>`.

Example:

    $ cd
    $ pwd
    /Users/jessealdridge
    $ mkdir -p foo/bar/baz
    $ cd foo/bar/baz
    $ cd ~
    $ z ba
    $ pwd
    /Users/jessealdridge/foo/bar/baz

When multiple results match, simplejump guesses which directory you want based
on the number of times you've accessed the directory, how recently you've
accessed it, and other factors.

You can add a number to your query to jump to the nth result.

Example:

    $ z d
    $ pwd
    /Users/jessealdridge/Desktop
    $ z d 2
    $ pwd
    /Users/jessealdridge/Dropbox


This project is mostly a clone of z (https://github.com/rupa/z).
