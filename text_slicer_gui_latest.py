#!/usr/bin/env python
# coding: utf-8

# In[31]:


import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("Slice Text into ~400 character sentences")
frame.geometry('400x400')
def SliceInput():
    text = inputtxt.get(1.0, "end-1c")
    if (len(text)>400):
        text_slices = slicer(text)
        #print('SLICES')
        #print(text_slices)
        #print('-'*50)
        print(len(text_slices))
        #mylist = tk.Listbox(frame, yscrollcommand = scroll_bar.set,height = len(text_slices)+1, width=100 )
        mylist = tk.Listbox(frame, yscrollcommand = scroll_bar.set, width=200)
        for i in range(len(text_slices)):
                text_slice = ""
                text_slice+= text_slices[i]
                #lab = tk.Label(frame,text = 'Slice '+str(i+1))
                #lab.pack()
                #outputtxt = tk.Text(frame,height = 5, width = 100)
                #outputtxt.pack()
                if len(text_slice)<=400:
                    mylist.insert(tk.END, str(i+1) + " " + str(text_slice))
                    mylist.insert(tk.END, "-"*200)
                else:
                    mylist.insert(tk.END,  str(i+1) + " " +"!LONGER THAN 400! "+ str(text_slice))
                    mylist.insert(tk.END, "-"*200)
                    
                #outputtxt.insert(tk.END, text_slice+' '+str(len(text_slice)))
        mylist.pack()
        scroll_bar.config( command = mylist.yview )  

    else:
        outputtxt = tk.Text(frame,height = 5, width = 100)
        outputtxt.pack()
        outputtxt.insert(tk.END, text)
        
def slicer(text):
    #print('in slicer')
    #print(text)
    if text[-1]==' ':
        text.pop()
    text_list = text.split('.')
    text_list = [t+'.' for t in text_list]
    text_slices = []
    len_text = len(text_list)
    if (len_text%2)==0:
        text_slices = sentences(text_list)
    else:
        last_sentence = text_list.pop()
        text_slices = sentences(text_list)
        text_slices.append(last_sentence)
    return text_slices
        

def sentences(l):
    #print('in sentences')
    #print(text_list)
    if l[-1]=='.':
        l.pop()
    le = [len(x) for x in l]
    n = len(l)-1
    temp = []
    for v in l:
        print(v)
    i = 0
    #print(le)
    if (n>2):
        #print(n)
        while(i<=n-1):
            #print(i)
            if (le[i]+le[i+1] <=400):
                temp.append(l[i]+l[i+1])
                print(temp)
                #print(temp)
                i+=2
            elif(le[i]+le[i+1]>400):
                temp.append(l[i])
                i+=1
    else:
        if(le[0]+le[1]<=399):
            temp.append(l[0]+' '+l[1])
        else:
            temp = l
    return temp
def input_clear():
    inputtxt.delete('1.0',tk.END)
    
    
inputtxt = tk.Text(frame,
                   height = 5,
                   width = 100)
inputtxt.pack()

sliceButton = tk.Button(frame,

                        text = "Slice!", 
                        command = SliceInput)
sliceButton.pack()
scroll_bar = tk.Scrollbar(frame)
scroll_bar.pack( side = 'right',fill = 'y' )
clearButton = tk.Button(frame, text = "Clear", command = input_clear)
clearButton.pack()
frame.mainloop()


# In[16]:


t =  "To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure? [33] On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain."


# In[20]:





# In[ ]:




