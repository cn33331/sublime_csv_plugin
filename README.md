# sublime_csv_plugin
Better Reading csv


只需要把文件`csv-viw`放到sublime txt软件的Packages下即可使用

example：`cp -r ./csv-view /Users/mac/Library/Application\ Support/Sublime\ Text/Packages `

不支持**中文字符**

# 文件

* `csv-view.sublime-commands`

  载入该文件,sublim可以使用shift+command+p打开命令面板进行搜索插件功能

* `Default.sublime-keymap`

  设置插件三个功能的快捷方式

* `Main.sublime-menu`

  设置插件功能在sublim上方菜单栏出现

以上三个文件可任意保留

* `csv-view.py`

  脚本执行的主体文件

# 功能

* `read_csv_view`

  读取当前csv文件内容，调整格式，不改变原有文件，创建新的视图进行展示

* `read_csv_local`

  读取当前csv文件内容，调整格式，将调整格式后的内容同本地内容进行替换

* `return_csv`

  将调整格式后的内容在本地转化为一般的csv格式

# 使用

![](./csv-view/tme/1.gif)

