import tkinter as tk
from tkinter import scrolledtext
win = tk.Tk()
win.title('英语长篇阅读答案检索器ver3.1')
win.geometry('835x370')

ltextr1=tk.Label(win,text='原文章+问题放置处', font=('SimHei', 12),fg='blue')
ltextr1.place(x=220, y=3, anchor='nw')
textr1=scrolledtext.ScrolledText(win,height=21,width=50,
                font=('SimHei',10),relief="solid",borderwidth=0.5)
textr1.place(x=5, y=25, anchor='nw')




ltext1=tk.Label(win,text='处理后文章', font=('SimHei', 12))
ltext1.place(x=645, y=3, anchor='nw')
text1=scrolledtext.ScrolledText(win,height=12,width=50,
                font=('SimHei',10),relief="solid",borderwidth=0.5)
text1.place(x=375, y=25, anchor='nw')
ltext2=tk.Label(win,text='处理后问题',
                font=('SimHei', 12))
ltext2.place(x=645, y=188, anchor='nw')
text2=scrolledtext.ScrolledText(win,height=11,width=50,
                font=('SimHei',10),relief="solid",borderwidth=0.5)
text2.place(x=375, y=211, anchor='nw')


ltexta=tk.Label(win,text='可能的答案', font=('SimHei', 12))
ltexta.place(x=745, y=3, anchor='nw')
texta3 = tk.Text(win,height=19,width=10,
                 font=('SimHei',12),relief="solid",borderwidth=0.5)
texta3.place(x=745, y=25, anchor='nw')



def getinput():
    art_qes=textr1.get("0.0","end")
    art_qeslist=[x.strip('（( ') for x in art_qes.split('\n')]
    lis=list('）). ')
    for i in art_qeslist:
        sum=0
        for j in i:
            if j.isdigit():
                sum+=1
                continue
            else:
                break
        if sum>0 and j in lis:
            break
    art_qes=art_qes.replace(i,'/////'+i)
    s=art_qes.split('/////')
    return s
        

def inputdel():
    textr1.delete('0.0','end')


def artso(x):
    text1.delete('0.0','end')
    art='\n'+x.replace('\n（','\n')
    artlis=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    artlis1=[x+')' for x in artlis]
    artlis2=['('+x+')' for x in artlis]
    artlis3=[x+'）' for x in artlis]
    artlis4=['（'+x+')' for x in artlis]
    artlis5=[x+'.' for x in artlis]
    artlis6=[x+' ' for x in artlis]
    artlis=artlis1+artlis2+artlis3+artlis4+artlis5+artlis6


    num=0
    arts=art
    for i in artlis:
        arts=arts.replace('\n'+i,'\n'+'***'+i.strip('（）().')+':')
    artls=arts.split('***')
    artls=artls[1:]
    
    

    artls=[x.lower().split(':',1) for x in artls]

    
    return artls
def artso_(x):
    artls=artso(x)
    for i in artls:
        text1.insert('end','{}\n\n'.format(i))
    return artls

def artdel():
    text1.delete('0.0','end')
    
    
def qesso(x):
    qes=x.split('\n')
    qes=[x for x in qes if len(x)>0]
    qeslis1=list('（( ')
    ls=[]
    for i in qes:
        while 1:
            if i[0] in qeslis1:
                i=i[1:]
            else:
                break
        ls.append(i)
    ls=[x for x in ls if len(x)>0]
    ls=[x for x in ls if x[0].isdigit()]
    qesls=[]
    for i in ls:
        for j in i:
            if j.isdigit():
                continue
            else:
                break
        qesls.append(i.lower().split(j,1))
    return qesls

def qesso_(x):
    qesls=qesso(x)
    for i in qesls:
        text2.insert('end','{}\n\n'.format(i))
    return qesls

def qesdel():
    text2.delete('0.0','end')
    
def clear(x,y):
    ls=[]
    for i in x:
        ld=[]
        for j in i:
            sum=0
            for k in y:
                if j in k:
                    sum+=1
            if sum<4:
                ld.append(j)
        ls.append(i)
    return ls
            
    
    
        
def search():
    text1.delete('0.0','end')
    text2.delete('0.0','end')
    texta3.delete('0.0','end')
    s=getinput()
    art=artso_(s[0])
    qes=qesso_(s[1])
    
    art_0=[x[0] for x in art]
    art_1=[x[1] for x in art]
    art_1=[x.replace('!',' ').replace(',',' ').replace('.',' ').replace('(',' ').replace(':',' ').replace('\n',' ').replace(')',' ') for x in art_1]
    qes_0=[x[0] for x in qes]
    qes_1=[x[1] for x in qes]
    qes_1=[x.replace('!',' ').replace(',',' ').replace('.',' ').replace('(',' ').replace(':',' ').replace(')',' ').split() for x in qes_1]
    qesword=clear(qes_1,art_1)


    ls_=[]
    for x in range(len(qesword)):
        ls__=[]
        for y in range(len(art_1)):
            sum=0
            for i in qesword[x]:
                if i in art_1[y]:
                    sum+=1
            ls__.append([art_0[y].upper(),sum])
        ls_.append([qes_0[x],sorted(ls__,key=lambda x:x[1],reverse=True)])
    ls=[]
    for i in ls_:
        ld=[i[0]]
        for j in i[1]:
            if j[1]==i[1][0][1]:
                ld.append(j[0])
        ls.append(ld)
    
    testarg1=text1.get("0.0","end")
    testarg2=text2.get("0.0","end")
    if len(testarg1)<5 or len(testarg2)<5:
        texta3.insert('end','输入错误')
        return 0


    for i in ls:
        line=''
        for j in i[1:]:
            line=line+j+'、'
        texta3.insert('end','{}:{}\n'.format(i[0],line.strip('、')))
        
        
                
    


def anwdel():
    texta3.delete('0.0','end')
    




def alldel():
    textr1.delete('0.0','end')
    text1.delete('0.0','end')
    text2.delete('0.0','end')
    texta3.delete('0.0','end')













button1=tk.Button(win,text='清除输入',width=15, font=('SimHei', 10),
                  relief="solid",borderwidth=0.5,command=inputdel)
button1.place(x=5, y=305, anchor='nw')





button2=tk.Button(win,text='清除处理后文章',width=15, font=('SimHei', 10),
                  relief="solid",borderwidth=0.5,command=artdel)
button2.place(x=125, y=305, anchor='nw')


button4=tk.Button(win,text='清除处理后问题',width=15, font=('SimHei', 10),
                  relief="solid",borderwidth=0.5,command=qesdel)
button4.place(x=246, y=305, anchor='nw')

button5=tk.Button(win,text='运行',height=1,width=16,
                  font=('SimHei', 15),relief="solid",borderwidth=0.5,
                  command=search)
button5.place(x=5, y=330, anchor='nw')

button6=tk.Button(win,text='清除',height=1,width=16,
                  font=('SimHei', 15),relief="solid",borderwidth=0.5,
                  command=alldel)
button6.place(x=192, y=330, anchor='nw')

button7=tk.Button(win,text='清除答案',width=11,
                  font=('SimHei', 10),relief="solid",borderwidth=0.5,
                  command=anwdel)
button7.place(x=745, y=337, anchor='nw')
texta3.insert('end','Icenood1es ')


win.mainloop()

