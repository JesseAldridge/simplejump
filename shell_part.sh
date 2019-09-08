
function cd {
    export SIMPLE_JUMP_CD_CALLED=1
    ~/simplejump/on_cd.py "`pwd`" "$@"
    pushd "$@" > /dev/null
}

function z {

    # (test cd to make sure it hasn't been stolen)
    cd .

    builtin cd "`~/simplejump/jump.py "$@"`"
    open .
}
