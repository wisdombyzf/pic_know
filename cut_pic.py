'''
验证码分割，并通过pytesseract进行预分类，减少手工劳动量


'''

import pytesseract
from PIL import Image
import numpy as np

def pic_cut(i) :
    
    #通过pytesseract进行预分类
    #begin
    image = Image.open(str(i)+'.jpg')
    imgry = image.convert('L')
    threshold = 22  
    table = []  
    for kkk in range(256):  
        if kkk < threshold:  
            table.append(0)  
        else:  
            table.append(1)
    out = imgry.point(table,'1') 
    code = pytesseract.image_to_string(out)
    print(code)
    #end
    
    #对图片进行处理，降噪
    #begin
    im=imgry
    test=np.zeros((im.size[1],im.size[0]),dtype='uint8')
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            temp=im.getpixel((y,x))   
            if temp>130:
                temp=255       
            else:
                temp=0   #降噪。。。。。将颜色偏白的去除
            test[x][y]=temp
    #end

    #对图片进行分割
    #begin
    f_first=0
    f_end=0
    flag_first=True
    flag_end=False
    pic_cuted_height=50     #图片切割后的每片的高与宽
    pic_cuted_width=25
    pic_name_point=0
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
                
                arr_temp=np.full((pic_cuted_height,pic_cuted_width),255,dtype='uint8')
                for x1 in range(line_length):
                    for y1 in range(pic_cuted_height):
                        arr_temp[y1][x1]=test[y1][x1+f_first]
                im_temp=Image.fromarray(arr_temp)
                try:
                    im_temp.save(str(code[pic_name_point])+"\\"+str(i)+".jpg")
                    #储存在对应文件夹中，如pytesseract识别出的0储存在0文件夹中
                except:
                    print("储存出现错误")
                pic_name_point=pic_name_point+1
                flag_first=True
                flag_end=False
      #end    
    
    

if __name__=='__main__':
    for i in range(999):
        try:           
            pic_cut(i)
            print("完成"+str(i)+"次")
        except:
            print("失败一次")


 
 
        
