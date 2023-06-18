files="./*"
ignoreFiles=("__archive" "_archive" "makestr.txt" "makestr.py" "temp.py" "_temp.py" "file_organization.sh")

for filepath in $files; do
    filename=${filepath:2}  # ファイルパスの先頭2文字を削除

    # ファイルが ignoreFiles に含まれる場合はスキップ
    if [[ "${ignoreFiles[@]}" =~ "${filename}" ]]; then
        continue
    fi

    patternAbc="((abc|arc|agc)[0-9]{3})_[a-z]\.py"
    if [[ "${filename}" =~ ${patternAbc} ]]; then
        matched_part=${BASH_REMATCH[1]}
        if [ ! -d "./_archive/${matched_part}" ]; then
            mkdir "./_archive/${matched_part}"
        fi
        modifyfilepath="./_archive/${matched_part}/${filename}"
        mv "$filepath" "$modifyfilepath"
        continue
    fi
done
    # modifyfilepath="./_archive/"${filepath:2}
    # mv $filepath $modifyfilepath