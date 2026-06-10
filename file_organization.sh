#!/bin/bash

# 設定
ignore_patterns=("__archive" "_archive" "makestr.txt" "makestr.py" "temp.py" "_temp.py" "file_organization.sh")

# ファイルを無視リストでチェック
should_ignore() {
    local filename=$1
    for pattern in "${ignore_patterns[@]}"; do
        if [[ "$filename" == "$pattern" ]]; then
            return 0  # 無視する
        fi
    done
    return 1  # 無視しない
}

# ディレクトリを作成してファイルを移動
move_to_archive() {
    local filepath=$1
    local subdir=$2
    local archive_dir="./_archive/$subdir"
    
    mkdir -p "$archive_dir"
    mv "$filepath" "$archive_dir/"
}

# パターンマッチングと処理
process_file() {
    local filepath=$1
    local filename=$(basename "$filepath")
    
    should_ignore "$filename" && return 0
    
    # ABC/ARC/AGC/APC パターン: abc461_a.py
    if [[ "$filename" =~ ^(abc|arc|agc|apc)[0-9]{3}_[a-z0-9]\.py$ ]]; then
        local contest_name="${BASH_REMATCH[1]^}"  # abc -> ABC
        local contest_num=$(echo "$filename" | sed -E 's/^[a-z]+([0-9]{3}).*/\1/')
        move_to_archive "$filepath" "${contest_name}${contest_num}"
        return 0
    fi
    
    # typical90 パターン: typical90_ab.py
    if [[ "$filename" =~ ^typical90_[a-z]{1,2}\.py$ ]]; then
        move_to_archive "$filepath" "typical90"
        return 0
    fi
    
    # past パターン: past202301_a.py
    if [[ "$filename" =~ ^past[0-9]{6}_[a-z]\.py$ ]]; then
        move_to_archive "$filepath" "past"
        return 0
    fi
    
    # デフォルト: すべて _archive に移動
    mv "$filepath" "./_archive/"
}

# メイン処理
for filepath in ./*.py; do
    [[ ! -f "$filepath" ]] && continue
    process_file "$filepath"
done

