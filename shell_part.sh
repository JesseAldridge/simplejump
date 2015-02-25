
function d {
    export SIMPLE_JUMP_D_CALLED=1
    ~/simplejump/on_cd.py "`pwd`" "$@"
    pushd "$@" > /dev/null
}

function z {

    # (test d to make sure it hasn't been stolen)
    d .

    builtin cd "`~/simplejump/jump.py "$@"`"
}
