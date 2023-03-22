#!/usr/bin/env python
# coding: utf-8

# ## Meu Projeto: Uber99

# In[1]:


from tkinter import *
import pandas as pd
from datetime import datetime
import os

pasta_local = os.getcwd()

def btn_clicked():
    uber = float(entry0.get())
    valor_99 = float(entry1.get())
    outros = float(entry2.get())
    gastos = float(entry4.get())
    pix = float(entry3.get())

    df = pd.read_excel(fr'{pasta_local}\uber99.xlsx')
    
    data = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
    mes = (datetime.now().month)-1
    #print(mes)
    
    df.loc[mes, 'dias'] += 1
    df.loc[mes, 'uber'] += uber
    df.loc[mes, 'app_99'] += valor_99
    df.loc[mes, 'extra'] += outros
    df.loc[mes, 'gastos'] += gastos
    df.loc[mes, 'pix'] += pix
    df.loc[mes, 'total'] = (df.loc[mes, 'uber'] + df.loc[mes, 'app_99'] +  df.loc[mes, 'extra']) - df.loc[mes, 'gastos']
    df.loc[mes, 'média/dia'] = df.loc[mes, 'total'] / df.loc[mes, 'dias']
    
    df.to_excel(fr'{pasta_local}\uber99.xlsx', index=False)

    valor_total_dia = (uber + valor_99 + outros) - gastos
    valor_total_mes = df.loc[mes, 'total']
    media_mes = df.loc[mes, 'média/dia']
    texto_final = f'{data} - Valor total dia: R$ {valor_total_dia:,.2f} - Valor total mês: R$ {valor_total_mes:,.2f} - Média por dia: R$ {media_mes:,.2f}'
    mensagem = Label(text=texto_final, background='#19CF1A', foreground='#000000')
    mensagem.place(x = 10, y = 755)

 




window = Tk()

window.title('Valores do dia Uber/99')
window.geometry("491x897")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 897,
    width = 491,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = fr"{pasta_local}\background.png")
background = canvas.create_image(
    246.0, 448.5,
    image=background_img)

img0 = PhotoImage(file = fr"{pasta_local}\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 177, y = 791,
    width = 139,
    height = 70)

entry0_img = PhotoImage(file = fr"{pasta_local}\img_textBox0.png")
entry0_bg = canvas.create_image(
    287.5, 245.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 180.0, y = 210,
    width = 215.0,
    height = 68)

entry1_img = PhotoImage(file = fr"{pasta_local}\img_textBox1.png")
entry1_bg = canvas.create_image(
    287.5, 359.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 180.0, y = 324,
    width = 215.0,
    height = 68)

entry2_img = PhotoImage(file = fr"{pasta_local}\img_textBox2.png")
entry2_bg = canvas.create_image(
    287.5, 473.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 180.0, y = 438,
    width = 215.0,
    height = 68)

entry3_img = PhotoImage(file = fr"{pasta_local}\img_textBox3.png")
entry3_bg = canvas.create_image(
    287.5, 701.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 180.0, y = 666,
    width = 215.0,
    height = 68)

entry4_img = PhotoImage(file = fr"{pasta_local}\img_textBox4.png")
entry4_bg = canvas.create_image(
    287.5, 587.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 180.0, y = 552,
    width = 215.0,
    height = 68)

window.resizable(False, False)
window.mainloop()


# In[ ]:




