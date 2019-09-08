
function cd {
    export SIMPLE_JUMP_CD_CALLED=1
    ~/Dropbox/simplejump/on_cd.py "`pwd`" "$@"
    pushd "$@" > /dev/null
}

function z {

    # (test cd to make sure it hasn't been stolen)
    cd .

    builtin cd "`~/Dropbox/simplejump/jump.py "$@"`"
    open .
}
