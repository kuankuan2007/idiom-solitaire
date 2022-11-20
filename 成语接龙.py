import tkinter
from tkinter import *
import tkinter.ttk
import pypinyin
li=[]
searchList=[]
with open('成语.in',"r",encoding="utf-8") as f:
    exec(f.read())
    f.close
for i in li:
    searchList.append([i,pypinyin.pinyin(i[0],heteronym=True,style=pypinyin.NORMAL)[0],pypinyin.pinyin(i[0],heteronym=True)[0]])
    print(searchList[-1])
def mainsearch(s,type):
    global resultBox
    showResult=""
    result=[]
    if type=="不包括音调":
        for i in range(len(s)-1,-1,-1):
            condition=pypinyin.pinyin(s[i],heteronym=True,style=pypinyin.NORMAL)[0]
            print(condition)
            if condition[0]!=s[i]:
                showResult="字\""+s[i]+"\"有如下拼音"+str(condition)+"(不考虑音调)\n"
                for j in condition:
                    for k in searchList:
                        if j in k[1]:
                            result.append(k)
                break
    elif type=="包括音调":
        for i in range(len(s)-1,-1,-1):
            condition=pypinyin.pinyin(s[i],heteronym=True)[0]
            print(condition)
            if condition[0]!=s[i]:
                showResult="字\""+s[i]+"\"有如下拼音"+str(condition)+"(考虑音调)\n"
                for j in condition:
                    for k in searchList:
                        if j in k[2]:
                            result.append(k)
                break
    elif type=="同字":
        if len(s)>0:
            showResult="对字\""+s[-1]+"\"进行完全匹配\n"
            for i in searchList:
                if s[-1]==i[0][0]:
                    result.append(i)
    print(result)
    resultBox.delete(1.0,END)
    resultBox.insert(1.0,showResult)
    if len(result)==0:
        resultBox.insert(2.0,"对不起词库中没有与此匹配的词")
    for i in result:
        resultBox.insert(END,i[0]+"   "+str(i[2])+"\n")
def search_chengyu1(search_content):
    s=search_content.get()
    global searchType
    type=searchType.get()
    print(s,type)
    mainsearch(s,type)
def search_chengyu2(choose_type):
    type=choose_type.get()
    global searchBox
    s=searchBox.get()
    print(s,type)
    mainsearch(s,type)


screen=Tk()
screen.iconbitmap("logo.ico")
screen.title("成语接龙查找器")
scro =Scrollbar()
scro.grid(column=3, row=2,columnspan=1,sticky=N+S)
resultBox=Text(yscrollcommand=scro.set,width=40,height = 10,font=('microsoft yahei', 12, 'bold'))
scro.config(command=resultBox.yview)
resultBox.config(state="normal")
resultBox.grid(column=0, row=2,columnspan=3,sticky="W")
search_content = StringVar()
search_content.trace("w", lambda name, index, mode, search_content=search_content: search_chengyu1(search_content))
choose_type=StringVar()
choose_type.trace("w", lambda name, index, mode, choose_type=choose_type: search_chengyu2(choose_type))
hint=Label(screen,text="末字:",font=('microsoft yahei',16, 'bold'))
hint.grid(column=0,row=1)
searchBox=Entry(screen,font=('microsoft yahei', 16, 'bold'),width=8,justify='center',textvariable=search_content)
searchBox.grid(column=1,row=1)
searchType=tkinter.ttk.Combobox(screen,width=10,font=('microsoft yahei', 16, 'bold'),textvariable=choose_type)
searchType["value"] = ("不包括音调", "包括音调", "同字")
searchType.config(state="readonly")
searchType.current(0)
searchType.grid(column=2,row=1)


screen.mainloop()