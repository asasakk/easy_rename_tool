import os
import PySimpleGUI as sg

def replace_in_filenames(directory, search_string, replace_string):
    if not os.path.exists(directory):
        sg.popup_error(f"指定したディレクトリが存在しません: {directory}")
        return

    replaced_files = []
    for filename in os.listdir(directory):
        if search_string in filename:
            new_filename = filename.replace(search_string, replace_string)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            replaced_files.append((filename, new_filename))

    if replaced_files:
        result_message = "以下のファイル名が置換されました:\n"
        result_message += "\n".join([f"{old} -> {new}" for old, new in replaced_files])
        sg.popup(result_message)
    else:
        sg.popup("置換対象のファイルが見つかりませんでした。")

# GUIのレイアウト
layout = [
    [sg.Text('ディレクトリ'), sg.InputText(), sg.FolderBrowse('フォルダ選択')],
    [sg.Text('検索文字列'), sg.InputText()],
    [sg.Text('置換文字列'), sg.InputText()],
    [sg.Button('実行'), sg.Button('キャンセル')]
]

# ウィンドウの作成
window = sg.Window('ファイル名置換ツール', layout)

# イベントループ
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'キャンセル'):
        break
    elif event == '実行':
        directory = values[0]
        search_string = values[1]
        replace_string = values[2]
        replace_in_filenames(directory, search_string, replace_string)

# ウィンドウを閉じる
window.close()
