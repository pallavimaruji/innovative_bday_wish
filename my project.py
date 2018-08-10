from tkinter import *


def display(canvas, e, num):
    t = Message(canvas, text="try again", font=('georgia', 12, 'bold', 'italic'), bg="pink")
    if num == 1:
        data1 = e.get()
        if data1 == "dodo":
            yo = Tk()
            yo.title("lakshya's wish")
            canvas1 = Canvas(yo, bg="chocolate1", width="1500", height="2000")
            pic1 = PhotoImage(file="lakshya.gif", master=yo)
            id = canvas1.create_image(300, 350, image=pic1)
            p1=PhotoImage(file="yo.gif",master=yo)
            id=canvas1.create_image(1000,300,image=p1)
            canvas1.pack()
            yo.mainloop()
        else:
            id = canvas.create_window(660, 320, window=t)

    if num == 2:
        data2 = e.get()
        if data2 == "seju":
            jal = Tk()
            jal.title("sejal's wish")
            canvas2 = Canvas(jal, bg="skyblue", width="1500", height="2000")
            pic2 = PhotoImage(file="sejal.gif", master=jal)
            id = canvas2.create_image(250, 310, image=pic2)
            p2 = PhotoImage(file="sim.gif", master=jal)
            id = canvas2.create_image(900, 300, image=p2)
            canvas2.pack()

            jal.mainloop()
        else:
            id = canvas.create_window(860, 320, window=t)
    if num == 3:
        data3 = e.get()
        if data3 == "meenu":
            meenu = Tk()
            meenu.title("meenal's wish")
            canvas3 = Canvas(meenu, bg="cyan", width="1500", height="2000")
            pic3=PhotoImage(file="meenal.gif",master=meenu)
            id=canvas3.create_image(230,285,image=pic3)
            p3 = PhotoImage(file="minti.gif", master=meenu)
            id = canvas3.create_image(950, 340, image=p3)
            canvas3.pack()

            meenu.mainloop()
        else:
            id = canvas.create_window(1050, 320, window=t)
    if num == 4:
        data4 = e.get()
        if data4 == "pallu":
            pallu = Tk()
            pallu.title("pallavi's wish")
            canvas4 = Canvas(pallu, bg="grey", width="1500", height="2000")
            pic4 = PhotoImage(file="pallavi.gif", master=pallu)
            id = canvas4.create_image(230, 275, image=pic4)
            p4 = PhotoImage(file="pallv.gif", master=pallu)
            id = canvas4.create_image(940, 350, image=p4)
            canvas4.pack()

            pallu.mainloop()
        else:
            id = canvas.create_window(830, 570, window=t)
    if num == 5:
        data5 = e.get()
        if data5 == "kanu":
            kanu = Tk()
            kanu.title("nakul's wish")
            canvas5 = Canvas(kanu, bg="sea green", width="1500", height="2000")
            pic5 = PhotoImage(file="nakul.gif", master=kanu)
            id = canvas5.create_image(280, 310, image=pic5)
            p5 = PhotoImage(file="nj.gif", master=kanu)
            id = canvas5.create_image(960, 340, image=p5)
            canvas5.pack()

            kanu.mainloop()
        else:
            id = canvas.create_window(1030, 570, window=t)
    if num == 6:
        data6 = e.get()
        if data6 == "jk":
            jk = Tk()
            jk.title("jatin's wish")
            canvas6 = Canvas(jk, bg="cadetblue", width="1500", height="2000")
            pic6 = PhotoImage(file="jatin.gif", master=jk)
            id = canvas6.create_image(230, 330, image=pic6)
            p6 = PhotoImage(file="jk1.gif", master=jk)
            id = canvas6.create_image(950,320, image=p6)
            canvas6.pack()

            jk.mainloop()
        else:
            id = canvas.create_window(1230, 570, window=t)
    if num == 7:
        data7 = e.get()
        if data7 == "manshu":
            manshu = Tk()
            manshu.title("mansha's wish")
            canvas7 = Canvas(manshu, bg="pink", width="1500", height="2000")
            pic7 = PhotoImage(file="mansha.gif", master=manshu)
            id = canvas7.create_image(220, 275, image=pic7)
            p7 = PhotoImage(file="m.gif", master=manshu)
            id = canvas7.create_image(900, 285, image=p7)

            canvas7.pack()
            manshu.mainloop()
        else:
            id = canvas.create_window(1250, 320, window=t)


def soul():
    root = Tk()
    root.title("Birthday Surprise::Friendship Test!!")
    canvas = Canvas(root, bg="misty rose", width="1500", height="2000")
    pic1 = PhotoImage(file="chikka.gif", master=root)
    id = canvas.create_image(380, 300, image=pic1)
    id = canvas.create_text(1100, 50, text="Guess us by the name you call!!", font=('Georgia', 20, 'bold'),
                            fill="purple")
    id = canvas.create_text(1100, 600, text="Tap us and unwrap the wish!!", font=('Georgia', 20, 'bold', 'italic'),
                            fill='springgreen4')

    pic2 = PhotoImage(file="dodo.gif", master=root)
    btn1 = Button(canvas, image=pic2, command=lambda: display(canvas, e1, 1))
    id = canvas.create_window(660, 180, window=btn1)
    e1 = Entry(canvas, width=10, bg="coral1", fg="white", font=('Georgia', 20, 'italic'))
    id = canvas.create_window(660, 270, window=e1)

    pic3 = PhotoImage(file="kaju.gif", master=root)
    btn2 = Button(canvas, image=pic3, command=lambda: display(canvas, e2, 2))
    id = canvas.create_window(860, 180, window=btn2)
    e2 = Entry(canvas, width=10, bg="coral1", fg="white", font=('Georgia', 20, 'italic'))
    id = canvas.create_window(860, 270, window=e2)

    pic4 = PhotoImage(file="minion.gif", master=root)
    btn3 = Button(canvas, image=pic4, command=lambda: display(canvas, e3, 3))
    id = canvas.create_window(1050, 180, window=btn3)
    e3 = Entry(canvas, width=10, bg="coral1", fg="white", font=('Georgia', 20, 'italic'))
    id = canvas.create_window(1050, 270, window=e3)

    pic5 = PhotoImage(file="pallu.gif", master=root)
    btn4 = Button(canvas, image=pic5, command=lambda: display(canvas, e4, 4))
    id = canvas.create_window(830, 430, window=btn4)
    e4 = Entry(canvas, width=10, bg="coral1", fg="white", font=('Georgia', 20, 'italic'))
    id = canvas.create_window(830, 520, window=e4)

    pic6 = PhotoImage(file="kanu.gif", master=root)
    btn5 = Button(canvas, image=pic6, command=lambda: display(canvas, e5, 5))
    id = canvas.create_window(1030, 430, window=btn5)
    e5 = Entry(canvas, width=10, bg="coral1", fg="white", font=('Georgia', 20, 'italic'))
    id = canvas.create_window(1030, 520, window=e5)

    pic7 = PhotoImage(file="jk.gif", master=root)
    btn6 = Button(canvas, image=pic7, command=lambda: display(canvas, e6, 6))
    id = canvas.create_window(1230, 430, window=btn6)
    e6 = Entry(canvas, width=10, bg="coral1", fg="white", font=('Georgia', 20, 'italic'))
    id = canvas.create_window(1230, 520, window=e6)

    pic8 = PhotoImage(file="manshu.gif", master=root)
    btn7 = Button(canvas, image=pic8, command=lambda: display(canvas, e7, 7))
    id = canvas.create_window(1250, 180, window=btn7)
    e7 = Entry(canvas, width=10, bg="coral1", fg="white", font=('Georgia', 20, 'italic'))
    id = canvas.create_window(1250, 270, window=e7)

    canvas.pack()
    root.mainloop()


def begin(a,e,f):
    r = e.get()
    t = f.get()
    if r == "pihu@khatarnak.com" and t == "lalten":
        soul()
    else:
        id = a.create_text(540, 580, text="Try Again", font=('georgia', 20, 'bold'))

def letsgo():
    start = Tk()
    start.title("Authentication Required!")
    a = Canvas(start, bg="olivedrab1", width=1500, height=1500)
    id = a.create_text(750, 100, text="Na na itni bhi jaldi kya h..!\nzara kuch sawalo ke jawab toh\ndeti jao.! ", font=('georgia', 20, 'bold'))

    id = a.create_text(750, 200, text="USERNAME", font=('georgia', 20, 'italic'))
    e = Entry(a, width=18, font=('georgia', 20, 'italic'))
    id = a.create_window(750, 260, window=e)
    id=a.create_text(1100,260,text="(your name @ your fav. comment.com)",font=('georgia',12,'bold'))

    id = a.create_text(750,320, text="PASSWORD", font=('georgia', 20, 'italic'))
    f = Entry(a, width=18, font=('georgia', 20, 'italic'))
    id = a.create_window(750, 380, window=f)
    id=a.create_text(1100,380,text="(light which kills darkness)",font=('georgia',12,'bold'))

    q = Button(start, text="Click Me Beautiful!", bg="white",width=20,font=('georgia',15,'bold','italic') ,command=lambda:begin(a,e,f))
    id = a.create_window(750, 450, window=q)
    a.pack()
    start.mainloop()
pihu=Tk()
pihu.title("BIRTHDAY SURPRISE!")
l=Canvas(pihu,bg="black",width=800,height=600)
g=Button(l,text="CLICK ME TO CONTINUE..!",bg="red",font=('georgia',25,'bold','italic'),command=letsgo)
id=l.create_window(400,300,window=g)
l.pack()
pihu.mainloop()
