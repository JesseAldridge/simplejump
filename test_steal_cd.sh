function cd {
    echo "stole cd"
    builtin cd "$@"
}
