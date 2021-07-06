files="./*"
ignoreFiles=("archive", "makestr.txt", "makestr.py", "temp.py")
for filepath in $files; do
    # if [ ${filepath:2} = "archive" -o ${filepath:2} = "makestr.txt" -o ${filepath:2} = "makestr.py" -o ${filepath:2} = "temp.py" ]; then
    if [ ${filepath:2} = "archive" -o ${filepath:2} = "makestr.txt" -o ${filepath:2} = "makestr.py" -o ${filepath:2} = "temp.py" ]; then
        continue;
    fi
    modifyfilepath="./archive/"${filepath:2}
    mv $filepath $modifyfilepath
done