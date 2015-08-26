# 設定
##マウス操作による関数の定義へジャンプ
####実装される機能は以下である。

~~~
Ctrl + 左クリック :関数定義へジャンプ
戻るボタン:ジャンプ元へ戻る
進むボタン:再度関数定義へジャンプ
~~~

####メニューを開く

~~~
Preferences > Browse Packages
~~~

####定義ファイルを作成
####Userディレクトリ配下へ以下のファイルを作成

~~~
Default (Windows).sublime-mousemap
~~~

####定義を記載する

~~~
[
    {
        "button": "button1", 
        "count": 1, 
        "modifiers": ["ctrl"],
        "press_command": "drag_select",
        "command": "goto_definition"
    },
    {
        "button": "button2", 
        "count": 1,
        "command": "jump_back"
    },
    {
        "button": "button3", 
        "count": 1,
        "command": "jump_forward"
    },
]
~~~
