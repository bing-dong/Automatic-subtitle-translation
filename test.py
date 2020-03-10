'''
friends 英文字幕对照查找中文
input：target--待翻译字幕   folder--字幕库
'''

import os
import re

target = r'C:\Users\17806\Downloads\[DownSub.com] The Full Ross & Rachel Story _ Friends.srt'
folder = r'D:\文件\Friends双语字幕'

def find_string(folder, string):
    # string = string.encode('utf-8')
    for root, dirs, files in os.walk(folder):
        # for name in dirs:
        #     print(os.path.join(root, name))
        for name in files:
            # print(os.path.join(root, name))
            # 字幕文件为gb18030编码方式，如不指定则默认以gbk打开，会有个别编码不能识别，出现错误：UnicodeDecodeError: 'gbk' codec can't decode byte 0xab in position 4180: illegal multibyte sequence
            with open(os.path.join(root, name), 'r', encoding='gb18030', errors='ignore') as f:
                for line in f:
                    # m = re.search(string, line)
                    # if m != None:
                        # return str(m.group(0))
                    if string in line:
                        return str(next(f))
    return '未找到\n'

# 匹配时间线
not_line = re.compile(r'[0-9]')
# 匹配待翻译字幕
is_line = re.compile(r'^-')
with open(target+'.srt', 'w') as out_file:
    with open(target, 'r') as input_file:
        for line in input_file:
            # 若开头为0-9则不是台词
            if not_line.match(line):
                # line = line.encode('utf-8')
                out_file.write(line)
                continue
            if is_line.match(line):
                string = line.split('-')[1].strip()
            else:
                string = line
            match_string = find_string(folder, string)
            # print(match_string)
            out_file.write(match_string)

