import sublime
import sublime_plugin
import csv
import re


class ReadCsvViewCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # 提取当前视图(csv)的所有内容
        # rawdata：str
        selection = self.view.sel()[0]
        selection = (selection if self.view.substr(selection)
                     else sublime.Region(0, self.view.size()))

        rawdata = self.view.substr(selection)

        # 将视图的内容转化成便于观看的形式，调整格式
        # rawdata->str2
        f = open('2.csv', 'w')
        f.write(rawdata)
        f.close()
        tab = []

        # 第一次遍历比较获得，每一项需要设置的宽度
        with open('2.csv') as f2:
            f_csv = csv.reader(f2)
            j = 1
            for row in f_csv:
                i = 0
                # print(row)
                for li in row:
                    # print(li)
                    if j == 1:
                        tab.append(len(li))
                    else:
                        if tab[i] < len(li):
                            tab[i] = len(li)
                    # print(tab[i])
                    i = i+1
                    # print(i)
                j += 1
                # print(tab)

        # print(tab)

        # 第二次遍历，调整格式
        str2 = ""
        tab1 = tab
        with open('2.csv') as f3:
            f_csv1 = csv.reader(f3)
            for row1 in f_csv1:
                i = 0
                str1 = ""
                for li1 in row1:
                    str1 = str1+(li1.ljust(tab1[i], " "))+"｜   ｜"
                    # li1.center(tab1[i], " ")
                    i = i+1
                # print(str1)
                str2 = str2 + str1 + "\n"
                # print(str2)
        # 创建新的临时视图，把修改后的字符串存放到视图中
        # print(self.view.window().folders())
        # print(self.view.window().project_file_name())
        # print(self.view.window().active_panel())
        # print(self.view.window().extract_variables())
        # print(type(self.view.window().extract_variables()))
        new_view = self.view.window().new_file()
        new_view.set_syntax_file('Packages/C++/C++.sublime-syntax')
        new_view.set_name('csv_record_view')
        new_view.insert(edit, 0, str2)


class ReadCsvLocalCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        file_path = self.view.window().extract_variables()['file']
        csvall = sublime.Region(0, self.view.size())

        csv_width_tab = []
        with open(file_path) as f1:
            f_csv = csv.reader(f1)
            header_flag = 1
            for row in f_csv:
                tab_flag = 0
                for column in row:
                    if header_flag == 1:
                        csv_width_tab.append(len(column))
                    else:
                        if csv_width_tab[tab_flag] < len(column):
                            csv_width_tab[tab_flag] = len(column)
                    tab_flag = tab_flag+1
                header_flag += 1

        # print(csv_width_tab)
        tablen = len(csv_width_tab)
        complete_str = ""
        tab1 = csv_width_tab
        with open(file_path) as f2:
            f_csv1 = csv.reader(f2)
            for row1 in f_csv1:
                tab_flag = 0
                row_str = ""
                for column1 in row1:
                    if tab_flag != tablen-1:
                        row_str = row_str + \
                            (column1.ljust(tab1[tab_flag], " "))+"｜   ｜"
                    else:
                        row_str = row_str + \
                            (column1.ljust(tab1[tab_flag], " "))
                    tab_flag = tab_flag+1
                # print(row_str)
                complete_str = complete_str + row_str + "\n"
                # print(complete_str)
        self.view.set_syntax_file('Packages/C++/C++.sublime-syntax')
        self.view.replace(edit, csvall, complete_str)


class ReturnCsvCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        file_path = self.view.window().extract_variables()['file']
        csvall = sublime.Region(0, self.view.size())
        data = self.view.substr(csvall)

        rowstr1 = ""
        f = open('2.csv', 'w+')
        csv_file = csv.writer(f)

        for f_csv in data:
            if f_csv != "\n":
                rowstr1 = rowstr1+f_csv
            else:
                strinfo = re . compile('｜   ｜')
                rowstr1 = strinfo.sub('---', rowstr1)
                strinfo1 = re . compile(' ')
                rowstr1 = strinfo1.sub('', rowstr1)
                # print(rowstr1)
                tab = re.split("---", rowstr1)
                print(tab)
                rowstr1 = ""
                csv_file.writerow(tab)

        f.seek(0)
        csvallstr = f.read()
        print(csvallstr)
        # syntax_path = '/Users/mac/Library/Application/Sublime \
        # Text/Packages/rainbow_csv/pregenerated_grammars/CSV (Rainbow).sublime-syntax'
        # self.view.set_syntax_file(syntax_path)
        self.view.replace(edit, csvall, csvallstr)
