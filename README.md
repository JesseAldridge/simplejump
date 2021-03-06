simplejump
==========

To install, just run something like this:
```
cd ~
git clone git://github.com/JesseAldridge/simplejump.git
echo "source ~/simplejump/shell_part.sh" >> .bashrc
```

You will need to modify `shell_part.sh` is you use a path different from the one I use.

Then restart your shell and you're done.

Now, after you cd to a directory you can jump back to it with `z <partial name>`.

Example:

    $ cd
    $ pwd
    /Users/jessealdridge

    $ mkdir -p foo/bar/baz
    $ cd foo/bar/baz
    $ cd
    $ z ba
    $ pwd
    /Users/jessealdridge/foo/bar/baz

When multiple results match, simplejump guesses which directory you want based
on the number of times you've accessed the directory, how recently you've
accessed it, and other factors.

This project is mostly a clone of z (https://github.com/rupa/z).
