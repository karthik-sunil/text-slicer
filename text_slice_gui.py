#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
        for i in range(len(text_slices)):
                text_slice = ""
                text_slice+= text_slices[i]
                lab = tk.Label(frame,text = 'Slice '+str(i+1))
                lab.pack()
                outputtxt = tk.Text(frame,height = 20, width = 50)
                outputtxt.pack()
                outputtxt.insert(tk.END, text_slice+' '+str(len(text_slice)))
    else:
        outputtxt = tk.Text(frame,height = 20, width = 50)
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

    
    
inputtxt = tk.Text(frame,
                   height = 20,
                   width = 50)
inputtxt.pack()

sliceButton = tk.Button(frame,

                        text = "Slice!", 
                        command = SliceInput)
sliceButton.pack()
scroll_bar = tk.Scrollbar(frame)
scroll_bar.pack( side = 'right',fill = 'y' )
frame.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




