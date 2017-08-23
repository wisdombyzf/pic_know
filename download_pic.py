# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:52:52 2017

@author: 张帆

验证码下载程序
"""
import requests as re
import threading 
import time
#换多进程。。。。多线程的效率几乎没有变。。。。原来是网络的问题

login_url = "http://seat.lib.whu.edu.cn/auth/signIn"
captcha_url = 'http://seat.lib.whu.edu.cn//simpleCaptcha/captcha'
username ='233333'
password = '1024'
thread_count=2      #线程数
download_num=10  #每个线程下载图片的数量

def login(i):
    html=re.get(login_url)#登陆以刷新，获取新的验证码
    #print("下载"+str(i)+"次")  
    pic=re.get(captcha_url)
    #在对应文件夹下储存验证码图片
    im=open(str(i)+".jpg","wb")
    im.write(pic.content)
    im.flush()
    im.close()
    
class mythread(threading.Thread):
    #初始化，传入将要下载图片的起始与终结编号
    def __init__(self,thread_begin,thread_end):
        threading.Thread.__init__(self)
        self.thread_begin=thread_begin
        self.thread_end=thread_end
        
    def run(self):
        for k in range(self.thread_begin,self.thread_end):
            login(k)
            print("正下载"+str(k)+"号")
            time.sleep(1)#自己控制下载速率。。。。为啥速率快了之后会死机？？？
            
       


if __name__=='__main__':
    for x in range(thread_count):
        time.sleep(1)
        thread1=mythread(download_num*x,download_num*(x+1))
        thread1.start()
    
   
    



























