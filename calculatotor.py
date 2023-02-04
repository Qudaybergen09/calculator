import tkinter
from tkinter import END, ttk


class Yashin(tkinter.Tk):
    def __init__(self,*args):
        super().__init__(*args)

        self.title('Window')
        self.geometry('450x550')
        self.config(bg = 'gray')
        self.resizable(1,1)


        self.entry = tkinter.Entry(width=75,font='arial 20')
        self.entry.place(x=0,y=0,height=35)

        self.btn_1 = ttk.Button(width=20,text='1',command=self.btn_1)
        self.btn_1.place(x=0,y=50,height=45)
  
 

        self.btn_2 = ttk.Button(width=20,text='2',command=self.btn_2)
        self.btn_2.place(x=150,y=50,height=45)

        self.btn_3 = ttk.Button(width=20,text='3',command=self.btn_3)
        self.btn_3.place(x=300,y=50,height=45)

        self.btn_4 = ttk.Button(width=20,text='4',command=self.btn_4)
        self.btn_4.place(x=0,y=110,height=45)
        
        self.btn_5 = ttk.Button(width=20,text='5',command=self.btn_5)
        self.btn_5.place(x=150,y=110,height=45)

        self.btn_6 = ttk.Button(width=20,text='6',command=self.btn_6)
        self.btn_6.place(x=300,y=110,height=45)

        self.btn_7 = ttk.Button(width=20,text='7',command=self.btn_7)
        self.btn_7.place(x=0,y=170,height=45)

        self.btn_8 = ttk.Button(width=20,text='8',command=self.btn_8)
        self.btn_8.place(x=150,y=170,height=45)

        self.btn_9 = ttk.Button(width=20,text='9',command=self.btn_9)
        self.btn_9.place(x=300,y=170,height=45)

        self.btn_10 = ttk.Button(width=20,text='0',command=self.btn_10)
        self.btn_10.place(x=150,y=230,height=45)

           
    
    
    
    def btn_1(self):
        self.entry.insert(0,self.btn_1['text'])

    def btn_2(self):
        self.entry.insert(0,self.btn_2['text'])

    def btn_3(self):
        self.entry.insert(0,self.btn_3['text'])

    def btn_4(self):
        self.entry.insert(0,self.btn_4['text'])

    def btn_5(self):
        self.entry.insert(0,self.btn_5['text'])

    def btn_6(self):
        self.entry.insert(0,self.btn_6['text'])

    def btn_7(self):
        self.entry.insert(0,self.btn_7['text'])

    def btn_8(self):
        self.entry.insert(0,self.btn_8['text'])

    def btn_9(self):
        self.entry.insert(0,self.btn_9['text'])

    def btn_10(self):
        self.entry.insert(0,self.btn_10['text'])


    

   

    


    
    
    
    



    



        



app = Yashin()
app.mainloop()