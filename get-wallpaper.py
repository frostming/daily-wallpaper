#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================
# Author: Frost Ming
# Email: mianghong@gmail.com
# Date: Jun 3, 2016
# =============================================
'''A small web crawler to get wallpapers from Momentum'''

import requests
import time
import os


def get_wallpaper_from_momemtum():
    s = requests.session()
    date = time.strftime('%Y-%m-%d', time.localtime())
    dir_path = 'wallpaper/%s' % date
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    start_json = 'https://momentumdash.com/app/backgrounds.json'
    img_prefix = 'https://momentumdash.com/backgrounds/'
    resp = s.get(start_json, verify=False)
    assert resp.status_code == 200
    bg_list = resp.json()['backgrounds']
    for bg in bg_list:
        img_url = img_prefix + bg['filename']
        filename = os.path.join(dir_path, bg['filename'])
        r = s.get(img_url, verify=False)
        if r.status_code != 200:
            continue
        with open(filename, 'wb') as fp:
            fp.write(r.content)


if __name__ == '__main__':
    get_wallpaper_from_momemtum()
