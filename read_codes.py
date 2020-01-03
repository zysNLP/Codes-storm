#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:58:26 2020

@author: zysNLP
"""


with open("berts/bert-master/run_classifier.py", 'r') as f:
    codes = f.read().splitlines()

codes = [code.rstrip() for code in codes]
codes_del_annotation = []
for code_line in codes:
    if code_line == '' or code_line[0] == "#":
        continue
    elif code_line[:3] == "'''" or code_line[:3] == '"""':
        if code_line[-3:] =="'''" or code_line[-3:] == '"""':
            continue
    else:
        #print(code_line)
        codes_del_annotation.append(code_line)

dict_elements = {}
import_modules = []   
for code in codes_del_annotation:
    if code[:4] == 'from' or code[:6] == 'import':
        import_modules.append(code)
        dict_elements['import_modules'] = import_modules
        continue
    packages = [] # [package_name, as_name, function_name]
    for im in import_modules:
        if im[:4] == 'from':
            ix_import = im.find('import')
            package = im[5:ix_import]
            funtion = im[ix_import+7:]
            packages.append([package, '', funtion])
            if package[:2] == "__":
                pass
        elif im[:6] == 'import':
            ix_as = im.find('as')
            if ix_as != -1:
                package = im[7:ix_as]
                as_name = im[ix_as+3:]
                packages.append([package, as_name, ''])
            else:
                package = im[7:]
                packages.append([package, '', ''])
        continue
    package_names = [i[0] for i in packages] + [i[1] for i in packages]
    package_names = [i for i in package_names if i != '']            
    
    code = "flags = tf.flags"
    code_split_equal = [i.strip() for i in code.split('=')]
    code_split_equal = [i.split(".") for i in code_split_equal]
    
    # read package.class or def
            





