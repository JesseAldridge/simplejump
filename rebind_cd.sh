
# overwrite cd to write to file first

function cd { 
    ~/Dropbox/simplejump/on_cd.py `pwd` "$@"
    builtin cd "$@"
}

function z {
    builtin cd `~/Dropbox/simplejump/jump.py "$@"`
}