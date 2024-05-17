import os

# ディレクトリ、検索文字列、置換文字列を指定
directory = r"your Directory"
search_string = r"変換前の文字列"
replace_string = r"変化後の文字列"


def replace_in_filenames(directory, search_string, replace_string):
    for filename in os.listdir(directory):
        # ファイル名に指定した文字列が含まれている場合のみ置換を行う
        if search_string in filename:
            new_filename = filename.replace(search_string, replace_string)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"ファイル名を置換しました: {filename} -> {new_filename}")



# 関数を呼び出して置換を実行
replace_in_filenames(directory, search_string, replace_string)
