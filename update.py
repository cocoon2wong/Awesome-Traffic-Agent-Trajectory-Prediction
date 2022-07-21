"""
@Author: Conghao Wong
@Date: 2022-07-21 16:45:48
@LastEditors: Conghao Wong
@LastEditTime: 2022-07-21 17:19:09
@Description: file content
@Github: https://github.com/cocoon2wong
@Copyright 2022 Conghao Wong, All Rights Reserved.
"""

import difflib
import os

BASE_PATH = '/Users/Shared/paper/'
TARGET_FILE = './list.md'


if __name__ == '__main__':
    all_files = os.listdir(BASE_PATH)

    paths = [p for p in all_files if p.endswith('pdf')
             and not p.startswith('_')]
    papers = [p[5:-5] for p in all_files if p.endswith('pdf')
              and not p.startswith('_')]

    with open(TARGET_FILE, 'r') as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        if line.startswith('* ') and '[paper]' in line:
            title = line.split(',')[0][2:].lower()
            l_title = len(title)

            for pattern, path in zip(papers, paths):

                l_pattern = len(pattern)
                l = min(l_title, l_pattern)

                s = difflib.SequenceMatcher(
                    None, pattern[:l], title[:l]).ratio()

                if s > 0.85:
                    print('Find {}.'.format(path))

                    lines[index] = '- [x] ~~' + line[2:-1] + '~~' + '\n' 

    with open(TARGET_FILE, 'w+') as f:
        f.writelines(lines)
