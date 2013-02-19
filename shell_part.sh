
# overwrite `cd` to write to frecency db first

function cd { 
    ~/simplejump/on_cd.py `pwd` "$@"
    builtin cd "$@"
}

function z {
    # echo jumping to: `~/simplejump/jump.py "$@"`
    builtin cd `~/simplejump/jump.py "$@"`
}