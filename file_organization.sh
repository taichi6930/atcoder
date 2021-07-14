files="./*"
ignoreFiles=("archive", "makestr.txt", "makestr.py", "temp.py", "file_organization.sh")
for filepath in $files; do
    if [ ${filepath:2} = "archive" \
    -o ${filepath:2} = "makestr.txt" \
    -o ${filepath:2} = "makestr.py" \
    -o ${filepath:2} = "temp.py" \
    -o ${filepath:2} = "file_organization.sh"\
    -o ${filepath:2} = "go_to_light_blue"\
     ]; then
        continue;
    fi
    modifyfilepath="./archive/"${filepath:2}
    mv $filepath $modifyfilepath
done