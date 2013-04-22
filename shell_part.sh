
# overwrite `cd` to write to frecency db first

function cd { 
    ~/simplejump/on_cd.py `pwd` "$@"
    builtin cd "$@"
}

function z {
    builtin cd "`~/simplejump/jump.py "$@"`"
}
