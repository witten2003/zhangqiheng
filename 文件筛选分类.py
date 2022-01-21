# 创作者：恒少
# 创作目的：
# 时间：16:21 2021/12/22

"""本工具说明：将当前程序所在目录下（相对路径）的已经命名好的文件夹如‘jpg’（如没有请先分类创建好），
含有不属于该文件类型的文件，该工具可以 提纯 （并删除原文件夹）"""

import os
import shutil

path = './'
#先创建两个新的归类文件夹（如果没有）

os.makedirs(path + 'documents')
os.makedirs(path + 'image')

#需要处理的’纯净物‘后缀名存储到list中，以便筛选
image_list = ['png','jpg','svg','gif']  #可修改
documents_list = ['text','docx']        #可修改

#移动文件
for i in image_list:
    cur_path = path + i
    if os.path.exists(cur_path):
        files = os.listdir( cur_path )
        #移动目录中的文件
        for file in files:
            if file.split('.')[-1] == i:#过滤网？？？
                shutil.move(cur_path + '/' + file , path + '/image')
        #结束循环删除旧文件夹（如果变空)，也可以保留原文件夹
        # os.removedirs(cur_path)

for j in documents_list:
    cur_path = path + j
    if os.path.exists(cur_path):
        files = os.listdir(cur_path)
        for file in files:
            if file.split('.')[-1] == j:
                shutil.move(cur_path + '/' + file, path + '/documents')
       # os.removedirs(cur_path)