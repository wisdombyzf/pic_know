# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:43:41 2017

@author: 张帆
利用python的sklearn库的svm
通过已标记的数据，训练模型
大力出奇迹。。。。直接上的25*50的图片，未降维，感觉速度好像并不是特别慢
所以暂时不做处理，
如进一步处理，好像能以每行，每列的黑色像素点个数作为特征值。。。
"""

from sklearn.svm import SVC
from sklearn.externals import joblib
from PIL import Image
import numpy as np
import os

#读取文件中的图片，图片名的首字母即为图片类型
x_list=[]
y_list=[]
dir_path="test_data"
my_data=os.listdir(dir_path) 
for x in my_data:
    im=Image.open(dir_path+"\\"+x)
    im_arr=np.array(im)
    im_arr=np.reshape(im_arr,im_arr.size)
    x_list.append(im_arr)
    y_list.append(x[0])

'''
im_test=Image.open("test.png").convert('L')
arr_test=np.array(im_test)
arr_test=np.reshape(arr_test,arr_test.size)
'''
arr_x=np.array(x_list)
arr_y=np.array(y_list)

'''
arr_y=np.array([0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G',
                'H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
                'V','W','X','Y','Z'])
'''


test=SVC()
test.fit(arr_x,arr_y)
joblib.dump(test,"model.pkl")#将训练好的模型文件储存
#print(test.predict([arr_test]))



