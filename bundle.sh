bundle() {
	local dest dir
	dest="bin"
	dir="bin/addon"
	mkdir -p "$dir"
	cp "__init__.py" "$dir"
	cp "Settings.py" "$dir"
	cp -r "lib" "$dir"
	cd "$dest"
	zip -r "addon.zip" "addon"
	cd ".."
	rm -rf "$dir"
}

bundle
