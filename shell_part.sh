
# overwrite `cd` to write to frecency db first

function cd { 
    export SIMPLE_JUMP_CD=1
    ~/simplejump/on_cd.py "`pwd`" "$@"
    builtin cd "$@"
}

function z {

    # (test cd to make sure it hasn't been stolen)
    cd .

    builtin cd "`~/simplejump/jump.py "$@"`"
}
