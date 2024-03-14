files="./*"
ignoreFiles=("__archive" "_archive" "makestr.txt" "makestr.py" "temp.py" "_temp.py" "file_organization.sh")

for filepath in $files; do
    filename=${filepath:2}  # ファイルパスの先頭2文字を削除

    # ファイルが ignoreFiles に含まれる場合はスキップ
    if [[ "${ignoreFiles[@]}" =~ "${filename}" ]]; then
        continue
    fi

    patternAbc="((abc|arc|agc|apc)[0-9]{3})_([a-z]|[0-9])\.py"
    if [[ "${filename}" =~ ${patternAbc} ]]; then
        matched_part=${BASH_REMATCH[1]}
        if [ ! -d "./_archive/${matched_part}" ]; then
            mkdir "./_archive/${matched_part}"
        fi
        modifyfilepath="./_archive/${matched_part}/${filename}"
        mv "$filepath" "$modifyfilepath"
        continue
    fi

    patternTypical="(typical90)_([a-z]{1,2})\.py"
    if [[ "${filename}" =~ ${patternTypical} ]]; then
        matched_part=${BASH_REMATCH[1]}
        if [ ! -d "./_archive/${matched_part}" ]; then
            mkdir "./_archive/${matched_part}"
        fi
        modifyfilepath="./_archive/${matched_part}/${filename}"
        mv "$filepath" "$modifyfilepath"
        continue
    fi

    patternPast="(past)([0-9]{6})_([a-z]{1})\.py"
    if [[ "${filename}" =~ ${patternPast} ]]; then
        matched_part=${BASH_REMATCH[1]}
        if [ ! -d "./_archive/${matched_part}" ]; then
            mkdir "./_archive/${matched_part}"
        fi
        modifyfilepath="./_archive/${matched_part}/${filename}"
        mv "$filepath" "$modifyfilepath"
        continue
    fi

    # patternOldAbc="(ABC|ARC|AGC)_([0-9]{2})_([A-Z]|[0-9])\.py"
    # if [[ "${filename}" =~ ${patternOldAbc} ]]; then
    #     contest_part="${BASH_REMATCH[1]}"
    #     contest_part_lowercase=$(echo "$contest_part" | tr '[:upper:]' '[:lower:]')
    #     number_part="${BASH_REMATCH[2]}"
    #     rank_part="${BASH_REMATCH[3]}"
    #     rank_part_lowercase=$(echo "$rank_part" | tr '[:upper:]' '[:lower:]')
    #     new_filename="${contest_part_lowercase}0${number_part}_${rank_part_lowercase}.py"
    #     mv "$filename" "$new_filename"
    # fi

    modifyfilepath="./_archive/"${filepath:2}
    mv $filepath $modifyfilepath
done
