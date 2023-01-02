bundle ()
{
    local dest dir
    dest="bin"
    dir="bin/project"
    mkdir -p "$dir"
    cp "__init__.py" "$dir"
    cp "Settings.py" "$dir"
    cp -r "lib" "$dir"
    cd "$dest"
    zip -r "project.zip" "project"
    cd ".."
    rm -rf "$dir"
}

bundle
