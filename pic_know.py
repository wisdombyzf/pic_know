# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:36:46 2017

@author: 张帆
验证码识别部分
通过读取之前建立的模型，进行识别
识别率大概只有80%，应该是某些数据太少了。。。。
还有一些问题要处理
"""


from sklearn.svm import SVC
from sklearn.externals import joblib
from PIL import Image
import numpy as np    

toknow=SVC()
toknow=joblib.load("model.pkl")

def cut_pic(pic_name):  
    my_list=[]
    num_test=0
    im=Image.open(pic_name).convert("L")
    test=np.zeros((im.size[1],im.size[0]),dtype='uint8')
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            temp=im.getpixel((y,x))   
            if temp>130:
                temp=255       
            else:
                temp=0   #降噪。。。。。将颜色偏白的去除
            test[x][y]=temp


    f_first=0
    f_end=0
    flag_first=True
    flag_end=False
    pic_cuted_height=50     #图片切割后的每片的高与宽
    pic_cuted_width=25
    
    for x in range(im.size[0]):
        if flag_first==True:
            for y in range(im.size[1]):
                if test[y][x]==0:
                    f_first=x
                    flag_first=False
                    flag_end=True
                    break
                
        if flag_end==True:
            flag2=True
            for y in range(im.size[1]):
                if test[y][x]==0:
                    flag2=False
            if flag2==True:
                f_end=x
                line_length=f_end-f_first
                if line_length>=pic_cuted_width:
                    line_length=pic_cuted_width
                    
                    #如果两个验证码部分重叠，未分离开，是不是在这设置一个回滚机制呢？
                
                arr_temp=np.full((pic_cuted_height,pic_cuted_width),255,dtype='uint8')
                for x1 in range(line_length):
                    for y1 in range(pic_cuted_height):
                        arr_temp[y1][x1]=test[y1][x1+f_first]
                #im_temp=Image.fromarray(arr_temp)
                try:
                    #有问题，待解决，先这样处理
                    im_temp=Image.fromarray(arr_temp)
                    im_temp.save(str(num_test)+".jpg")                    
                    my_im=Image.open(str(num_test)+".jpg")
                    ab=np.array(my_im)
                    ab=np.reshape(ab,ab.size)
                    my_list.append(ab)
                    #arr_temp=np.reshape(arr_temp,arr_temp.size)
                    #name_list.append(toknow.predict([ab]))
                    
                except:
                    print("出现错误")
                flag_first=True
                flag_end=False    
    temp=toknow.predict(my_list)
    my_result="".join(temp)#字符列表转字符串
    #print(my_result)
    return my_result


if __name__=='__main__':
    for x in range(5,16):
        print(cut_pic(str(x)+".jpg"))
    







































