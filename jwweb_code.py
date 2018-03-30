# tkinter实现下载验证码
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import requests
import os
import time

def Get_vcode():
    result = requests.get("http://jwgl.hist.edu.cn/jwweb/sys/ValidateCode.aspx")
    # 下载验证码
    if not os.path.isdir("code"):
        os.mkdir("code")
        if not os.path.isdir("code/all"):
            os.mkdir("code/all")
    with open('code/all/vcode.jpg', 'wb') as f:
        f.write(result.content)
    f.close()

def spilt(imgFile, H=4, V=1):
    imgFileNameList = []
    ImgObj = Image.open(imgFile)
    imgFileName = os.path.split(imgFile)[1]
    imgFileName = imgFileName[:imgFileName.rindex('.')]
    for i in imgFileName:
        imgFileNameList.append(i+".jpg")
    crtW, crtH = ImgObj.size
    hStep = crtW // H
    vStep = crtH // V
    for i in range(V):
        for j in range(H):
            OutFileNameTemp = imgFileNameList[j][:imgFileNameList[j].rindex('.')]
            OutFileName = os.path.join("code",OutFileNameTemp,imgFileNameList[j])
            if not os.path.isdir(os.path.join("code",OutFileNameTemp)):
                os.mkdir(os.path.join("code",OutFileNameTemp))
            OutNewFileName = OutFileName
            if os.path.isfile(OutFileName):
                OutNewFileName = OutFileName[:OutFileName.rindex('.')] + \
                              '_' + str(time.time()).split(".")[0] \
                              + OutFileName[OutFileName.rindex('.'):]
            box = (j * hStep, i * vStep, (j + 1) * hStep, (i + 1) * vStep)
            cropped = ImgObj.crop(box)
            cropped.save(OutNewFileName)

def rename(oldfile, newFile):
    newFileTemp = newFile
    if os.path.isfile(newFile):
       newFileTemp = newFile[:newFile.rindex('.')] + \
                             '_' + str(time.time()).split(".")[0]\
                             + newFile[newFile.rindex('.'):]
    os.rename(oldfile, newFileTemp)

def save_ok():
    # 创建一个空的图片
    img = Image.new('RGB', (122, 54), (255, 255, 255))
    drawBrush = ImageDraw.Draw(img)  # 创建画刷，用来写文字到图片img上
    # # 创建字体，fontFile为字体文件，若非系统字体需加详细路径
    font = ImageFont.truetype("C:\Windows\Fonts\SHOWG.TTF", 30)
    # # 使用特定字体写字，（textX0,textY0）为文字开始的左上角起始位置
    drawBrush.text((0, 15), "Save OK", fill=(0, 0, 0), font=font)
    if not os.path.isdir("code"):
        os.mkdir("code")
    img.save("code\ok.jpg")

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("验证码 V2.0")
        self.pack(fill=BOTH, expand=1)
        self.createWidgets()

    def createWidgets(self):
        self.Button = Button(self, text='先点显示', command=self.showImg, width = 16, height = 1)
        self.Button.pack()
        self.urlInput = Entry(self)
        self.urlInput.pack()
        self.Button1 = Button(self, text='在点保存', command=self.saveImg, width = 16, height = 1)
        self.Button1.pack()

    def showImg(self):
        Get_vcode()
        load = Image.open("code/all/vcode.jpg")  # 图片的相对路径
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=82)

    def saveImg(self):
        # 保存验证码
        str = self.urlInput.get()
        if not (len(str)<4):
            NewCodeFile = os.path.join("code\\all", str + ".jpg")
            rename("code/all/vcode.jpg", NewCodeFile)
            spilt(NewCodeFile)
            if not os.path.isfile("code/ok.jpg"):
                save_ok()
            load = Image.open("code/ok.jpg")  # 图片的相对路径
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=0, y=82)
            print(str)
        else:print("字符小于四个!")


if __name__ == '__main__':
    root = Tk()
    root.geometry("125x140")
    app = Window(root)
    root.mainloop()

