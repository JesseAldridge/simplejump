# Run this file by calling `source test_stead_d.sh`

unset SIMPLE_JUMP_D_CALLED

function d {
    echo "stole d"
    builtin cd "$@"
}
