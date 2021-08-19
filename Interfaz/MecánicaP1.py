from tkinter import *

root = Tk()
root.title('Genius Guess')
root['bg'] = 'light blue'

label_t = Label(root, text='MECÁNICA NEWTONIANA', font=('Helvetica', 50), bg='light blue')
label_t.place(x=300, y=50)
label1 = Label(root, text='JUGADOR =', font=('Helvetica', 30), bg='light blue')
label1.place(x=250, y=300)
entry1 = Entry(root, font=('Helvetica', 30))
entry1.place(x=500, y=300)

img1 = PhotoImage(file ='imgs1\\1.png')
img2 = PhotoImage(file ='imgs1\\2.png')
img3 = PhotoImage(file ='imgs1\\3.png')
img4 = PhotoImage(file ='imgs1\\4.png')
img5 = PhotoImage(file ='imgs1\\5.png')
count = 0

def comm1():
    name = entry1.get()
    labelk = Label(root, text='PREGUNTA 1', font=('Helvetica', 35), bg='light blue')
    labelk.place(x=540, y=10)
    labelk1 = Label(root, text='LEE CON ATENCIÓN', font=('Helvetica', 30), bg='light blue')
    labelk1.place(x=500, y=70)
    labelk2 = Label(root, image=img1)
    labelk2.place(x=420, y=120)

    def comm2():
        global count
        count += 1
        labelz = Label(root)
        labelz.pack()
        labelz.after(10, lanjut2)

    def lanjut2():
        labell = Label(root, text='PREGUNTA 2', font=('Helvetica', 35), bg='light blue')
        labell.place(x=540, y=10)
        labell1 = Label(root, text='LEE CON ATENCIÓN', font=('Helvetica', 30), bg='light blue')
        labell1.place(x=500, y=70)
        labell2 = Label(root, image=img2)
        labell2.place(x=420, y=120)

        def comm3():
            global count
            count += 1
            labelz1 = Label(root)
            labelz1.pack()
            labelz1.after(10, lanjut3)

        def lanjut3():
            labelll = Label(root, text='PREGUNTA 3', font=('Helvetica', 35), bg='light blue')
            labelll.place(x=540, y=10)
            labelll1 = Label(root, text='LEE CON ATENCIÓN', font=('Helvetica', 30), bg='light blue')
            labelll1.place(x=500, y=70)
            labelll2 = Label(root, image=img3)
            labelll2.place(x=420, y=120)

            def comm4():
                global count
                count += 1
                labelzz1 = Label(root)
                labelzz1.pack()
                labelzz1.after(10, lanjut4)

            def lanjut4():
                labellll = Label(root, text='PREGUNTA 4', font=('Helvetica', 35), bg='light blue')
                labellll.place(x=540, y=10)
                labellll1 = Label(root, text='LEE CON ATENCIÓN', font=('Helvetica', 30), bg='light blue')
                labellll1.place(x=500, y=70)
                labellll2 = Label(root, image=img4)
                labellll2.place(x=420, y=120)

                def comm5():
                    global count
                    count += 1
                    labelzzz1 = Label(root)
                    labelzzz1.pack()
                    labelzzz1.after(10, lanjut5)

                def lanjut5():
                    labelllll = Label(root, text='PREGUNTA 5', font=('Helvetica', 35), bg='light blue')
                    labelllll.place(x=540, y=10)
                    labelllll1 = Label(root, text='LEE CON ATENCIÓN', font=('Helvetica', 30), bg='light blue')
                    labelllll1.place(x=500, y=70)
                    labelllll2 = Label(root, image=img5)
                    labelllll2.place(x=420, y=120)
                    buttonlll1.destroy()
                    buttonlll2.destroy()
                    buttonlll3.destroy()
                    buttonlll4.destroy()
                    labellll.destroy()
                    labellll1.destroy()
                    labellll2.destroy()

                    def final_c():
                        global count
                        count += 1
                        labelzzzz1 = Label(root, bg='light blue')
                        labelzzzz1.pack()
                        labelzzzz1.after(10, final)

                    def final():
                        label_ft = Label(root, text='JUGADOR =', font=('Helvetica', 35), bg='light blue')
                        label_ft.place(x=300, y=300)
                        label_ft1 = Label(root, text='R. CORRECTAS =', font=('Helvetica', 35), bg='light blue')
                        label_ft1.place(x=250, y=400)
                        label_f = Label(root, text=name, font=('Helvetica', 35), bg='light blue')
                        label_f.place(x=600, y=300)
                        label_f1 = Label(root, text=count, font=('Helvetica', 35), bg='light blue')
                        label_f1.place(x=650, y=400)
                        buttonllll1.destroy()
                        buttonllll2.destroy()
                        buttonllll3.destroy()
                        buttonllll4.destroy()
                        labelllll.destroy()
                        labelllll1.destroy()
                        labelllll2.destroy()

                    buttonllll1 = Button(root, text='A).', relief=FLAT, font=('Helvetica', 30), command=final)
                    buttonllll1.place(x=300, y=620)
                    buttonllll2 = Button(root, text='B).', relief=FLAT, font=('Helvetica', 30), command=final)
                    buttonllll2.place(x=500, y=620)
                    buttonllll3 = Button(root, text='C).', relief=FLAT, font=('Helvetica', 30), command=final_c)
                    buttonllll3.place(x=800, y=620)
                    buttonllll4 = Button(root, text='D).', relief=FLAT, font=('Helvetica', 30), command=final)
                    buttonllll4.place(x=1000, y=620)

                buttonlll1 = Button(root, text='A).', relief=FLAT, font=('Helvetica', 30), command=comm5)
                buttonlll1.place(x=300, y=620)
                buttonlll2 = Button(root, text='B).', relief=FLAT, font=('Helvetica', 30), command=lanjut5)
                buttonlll2.place(x=500, y=620)
                buttonlll3 = Button(root, text='C).', relief=FLAT, font=('Helvetica', 30), command=lanjut5)
                buttonlll3.place(x=800, y=620)
                buttonlll4 = Button(root, text='D).', relief=FLAT, font=('Helvetica', 30), command=lanjut5)
                buttonlll4.place(x=1000, y=620)
                buttonll1.destroy()
                buttonll2.destroy()
                buttonll3.destroy()
                buttonll4.destroy()
                labelll.destroy()
                labelll1.destroy()
                labelll2.destroy()

            buttonll1 = Button(root, text='A).', relief=FLAT, font=('Helvetica', 30), command=comm4)
            buttonll1.place(x=300, y=620)
            buttonll2 = Button(root, text='B).', relief=FLAT, font=('Helvetica', 30), command=lanjut4)
            buttonll2.place(x=500, y=620)
            buttonll3 = Button(root, text='C).', relief=FLAT, font=('Helvetica', 30), command=lanjut4)
            buttonll3.place(x=800, y=620)
            buttonll4 = Button(root, text='D).', relief=FLAT, font=('Helvetica', 30), command=lanjut4)
            buttonll4.place(x=1000, y=620)
            buttonl1.destroy()
            buttonl2.destroy()
            buttonl3.destroy()
            buttonl4.destroy()
            labell.destroy()
            labell1.destroy()
            labell2.destroy()

        buttonl1 = Button(root, text='A).', relief=FLAT, font=('Helvetica', 30), command=lanjut3)
        buttonl1.place(x=300, y=620)
        buttonl2 = Button(root, text='B).', relief=FLAT, font=('Helvetica', 30), command=comm3)
        buttonl2.place(x=500, y=620)
        buttonl3 = Button(root, text='C).', relief=FLAT, font=('Helvetica', 30), command=lanjut3)
        buttonl3.place(x=800, y=620)
        buttonl4 = Button(root, text='D).', relief=FLAT, font=('Helvetica', 30), command=lanjut3)
        buttonl4.place(x=1000, y=620)

        labelk.destroy()
        labelk1.destroy()
        labelk2.destroy()
        buttonk1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()

    buttonk1 = Button(root, text='A).', relief=FLAT, font=('Helvetica', 30), command=lanjut2)
    buttonk1.place(x=300, y=620)
    button2 = Button(root, text='B).', relief=FLAT, font=('Helvetica', 30), command=lanjut2)
    button2.place(x=500, y=620)
    button3 = Button(root, text='C).', relief=FLAT, font=('Helvetica', 30), command=lanjut2)
    button3.place(x=800, y=620)
    button4 = Button(root, text='D).', relief=FLAT, font=('Helvetica', 30), command=comm2)
    button4.place(x=1000, y=620)
    label_t.destroy()
    label1.destroy()
    entry1.destroy()
    button1.destroy()


button1 = Button(root, text='EMPEZAR', font=('Helvetica', 30), command=comm1)
button1.place(x=600, y=450)
root.mainloop()
