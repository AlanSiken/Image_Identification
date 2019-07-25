# -*- coding: UTF-8 -*-
from aip import AipOcr
#定义常规变量
APP_ID = '16874087'
API_KEY = 'SFVcA25MYDvtGbe1es528ABt'
SECRET_KEY = 'ypiBXMONdYmVpAwY5Y6jZ84UmgZE5MGn'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)#初始化AipFace对象

def Get_File_Contnet(IMG_Path):
    with open(IMG_Path,'rb') as Ip:  #以二进制性质读待识别的图片
        return Ip.read()   #返回PIL读取结果

def main():
    IMG_Path = input('请输入待识别图片的路径：')
    result = aipOcr.advancedGeneral(Get_File_Contnet(IMG_Path))#调用通用文字识别, 图片参数为本地图片，并把返回值添加进result
    print('*'*32)
    print('识别到的数目：'%(result['result_num']))#取出数目条数
	#list =result['name']  #把返回值中的识别内容添加进列表中
    #for i in list:     
    #    print(i['name'])
    #    with open('识别内容.txt','a') as fd:  #以追加方式写+读打开文件，若不存在就新建一个
    #        fd.write(i['name'] + '\n')#写入识别内容


if __name__ == '__main__':
    main()

# D:/pythonpractice/Image/Dog.jpg