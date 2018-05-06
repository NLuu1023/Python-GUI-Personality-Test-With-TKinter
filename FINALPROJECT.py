from tkinter import *

class Quiz:

    def _init_(self):
        
        self.root = Tk()
        self.root.configure(bg="sky blue")
        
        self.photo = PhotoImage(file="keep_the_world.gif")
        self.main_photo = Label(self.root, image=self.photo).pack(expand=YES)

        self.introduction = Label(self.root, text = "Welcome to the Society Placement Exam!", fg="red", bg="light yellow", font=("pristina 30 bold")).pack(fill=X, expand=YES)
        self.nameRequest = Label(self.root, text = "What is your name?", bg="light yellow", font=("Pristina 16")).pack(fill=X, expand=YES)
        self.name_v = StringVar()
        self.name = Entry(self.root, justify=CENTER, textvariable = self.name_v)
        self.name.pack(expand=YES)
        
        self.nextPage = Button(self.root, text="Let's Begin!", bg="red", fg="white", font=("Pristina 14"), activebackground="black", activeforeground="white", command=self.next_page).pack(expand=YES)
        self.root.mainloop()

    def next_page(self):
        
        self.root.destroy()
        self.questions()

    def questions(self):
        
        self.root2 = Tk()
        self.root2.configure(bg="light yellow")
        self.instructions = Label(self.root2, text="Please Answer These Following Questions", font=("Pristina 18 bold"), fg="red", bg="light yellow").pack()
        
        self.correct1 = BooleanVar()
        self.correct2 = BooleanVar()
        self.correct3 = BooleanVar()
        self.correct4 = BooleanVar()

        self.Q1_1 = Label(self.root2, text = "If you’re running late to work, do you speed to make it on time?", font=("Pristina 16"), justify=LEFT, bg="light yellow").pack(expand=YES, anchor=W)
        self.Q1_1rad = Radiobutton(self.root2, text = "Risk it", variable = self.correct1, value = "True",indicatoron=0, width = 15, font=("Pristina 14"), bg="light yellow")
        self.Q1_1rad.pack(expand=YES, anchor=W)
        self.Q1_1rad2 = Radiobutton(self.root2, text = "Stay safe", variable = self.correct1, value = "False",indicatoron=0, width = 15, font=("Pristina 14"), bg="light yellow")
        self.Q1_1rad2.pack(expand=YES, anchor=W)

        self.Q1_2 = Label(self.root2, text = "There is a bomb in a crowded building with three minutes until detonation, you have the instructions, do you flee instead of attempting to defuse it?",
                          bg="light yellow", font=("Pristina 16")).pack(expand=YES, anchor=W)
        self.Q1_2rad = Radiobutton(self.root2, text = "Flee", variable = self.correct2, value = "True", indicatoron=0, width = 15, font=("Pristina 14"),bg="light yellow")
        self.Q1_2rad.pack(expand=YES, anchor=W)
        self.Q1_2rad2 = Radiobutton(self.root2, text = "Attempt to diffuse it", variable = self.correct2, value = "False",indicatoron=0, width = 15, font=("Pristina 14"), bg="light yellow")
        self.Q1_2rad2.pack(expand=YES, anchor=W)

        self.Q1_3 = Label(self.root2, text = "Your team at work develops an incredible project. Your boss comes to you with a promotion, but the rest of your team will receive no credit. Do you accept his offer?",
                          bg="light yellow", font=("Pristina 16")).pack(expand=YES, anchor=W)
        self.Q1_3rad = Radiobutton(self.root2, text = "Take the promotion", variable = self.correct3, value = "True",indicatoron=0, width = 15, font=("Pristina 14"), bg="light yellow")
        self.Q1_3rad.pack(expand=YES, anchor=W)
        self.Q1_3rad2 = Radiobutton(self.root2, text = "Stick with your team", variable = self.correct3, value = "False",indicatoron=0, width = 15, font=("Pristina 14"), bg="light yellow")
        self.Q1_3rad2.pack(expand=YES, anchor=W)

        self.Q1_4 = Label(self.root2, text = "You discover your sibling runs a dog fighting ring. Do you help your sibling hide their crime instead of turning them in?",
                          bg="light yellow", font=("Pristina 16")).pack(expand=YES, anchor=W)
        self.Q1_4rad = Radiobutton(self.root2, text = "Help with the cover up", variable = self.correct4, value = "True",indicatoron=0, width = 15, font=("Pristina 14"), bg="light yellow")
        self.Q1_4rad.pack(expand=YES, anchor=W)
        Q1_4rad2 = Radiobutton(self.root2, text = "Turn them in", variable = self.correct4, value = "False",indicatoron=0, width = 15, font=("Pristina 14"), bg="light yellow")
        Q1_4rad2.pack(expand=YES, anchor=W)

        self.final_page = Button(self.root2, text="Next", bg="red", fg="white", activebackground="black", activeforeground="white",font=("Pristina 14"),  command=self.questions1).pack(expand=YES, anchor=E)
        self.root2.mainloop()

    def questions1(self):

        self.root2.destroy()
        self.root3 = Tk()
        self.root3.configure(bg="light yellow")
        
        self.Q2 = Label(self.root3, text = "Do you prefer the company of other people, animals, or yourself most?", font=("Pristina 16"), bg="light yellow").pack(expand=YES, anchor=W)

        self.var = StringVar()
        self.var.set(0)

        MODES = [
            ("People", 1),
            ("Animals", 2),
            ("Myself", 3),
            ]
        for text, mode in MODES:
            self.Q2rad = Radiobutton(self.root3, text = text,indicatoron=0, width = 15, font=("Pristina 14"), variable = self.var, value = mode, bg="light yellow")
            self.Q2rad.pack(expand=YES, anchor=W)

        self.final_page = Button(self.root3, text="Next", bg="red", fg="white", activebackground="black", activeforeground="white",font=("Pristina 14"),  command=self.questions2).pack(expand=YES, anchor=E)
        self.root3.mainloop()

    def questions2(self):

        self.root3.destroy()
        self.root4 = Tk()
        self.root4.configure(bg="light yellow")

        self.Q3Label =Label(self.root4, text = "On a scale of 1 to 5, with 5 being all the time and 1 being not at all, answer the following questions: ", font=("Pristina 18"), bg="light yellow" ).pack(expand=YES, anchor=W)
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

        self.Q3_1Label=Label(self.root4, text = "How much do you exercise?", font=("Pristina 16"), bg="light yellow").pack(expand=YES, anchor=W)
        self.Q3_1rad=Radiobutton(self.root4, text = "1", variable = self.var1, value = -10, indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_1rad.pack(expand=YES, anchor=W)
        self.Q3_1rad=Radiobutton(self.root4, text = "2", variable = self.var1, value = -5,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_1rad.pack(expand=YES, anchor=W)
        self.Q3_1rad=Radiobutton(self.root4, text = "3", variable = self.var1, value = 0.0,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_1rad.pack(expand=YES, anchor=W)
        self.Q3_1rad=Radiobutton(self.root4, text = "4", variable = self.var1, value = 5, indicatoron=0, width = 5, font=("Pristina 14"),bg="light yellow")
        self.Q3_1rad.pack(expand=YES, anchor=W)
        self.Q3_1rad=Radiobutton(self.root4, text = "5", variable = self.var1, value = 10, indicatoron=0, width = 5, font=("Pristina 14"),bg="light yellow")
        self.Q3_1rad.pack(expand=YES, anchor=W)

        self.Q3_2Label=Label(self.root4, text = "How much time do you spend outdoors?",font=("Pristina 16"),  bg="light yellow").pack(expand=YES, anchor=W)
        self.Q3_2rad=Radiobutton(self.root4, text = "1", variable = self.var2, value = -10,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_2rad.pack(expand=YES, anchor=W)
        self.Q3_2rad=Radiobutton(self.root4, text = "2", variable = self.var2, value = -5,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_2rad.pack(expand=YES, anchor=W)
        self.Q3_2rad=Radiobutton(self.root4, text = "3", variable = self.var2, value = 0.0,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_2rad.pack(expand=YES, anchor=W)
        self.Q3_2rad=Radiobutton(self.root4, text = "4", variable = self.var2, value = 5, indicatoron=0, width = 5, font=("Pristina 14"),bg="light yellow")
        self.Q3_2rad.pack(expand=YES, anchor=W)
        self.Q3_2rad=Radiobutton(self.root4, text = "5", variable = self.var2, value = 10,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_2rad.pack(expand=YES, anchor=W)

        self.Q3_3Label=Label(self.root4, text = "How good are you at solving math problems?",font=("Pristina 16"),  bg="light yellow").pack(expand=YES, anchor=W)
        self.Q3_3rad=Radiobutton(self.root4, text = "1", variable = self.var3, value = -10,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_3rad.pack(expand=YES, anchor=W)
        self.Q3_3rad=Radiobutton(self.root4, text = "2", variable = self.var3, value = -5, indicatoron=0, width = 5, font=("Pristina 14"),bg="light yellow")
        self.Q3_3rad.pack(expand=YES, anchor=W)
        self.Q3_3rad=Radiobutton(self.root4, text = "3", variable = self.var3, value = 0.0,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_3rad.pack(expand=YES, anchor=W)
        self.Q3_3rad=Radiobutton(self.root4, text = "4", variable = self.var3, value = 5,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_3rad.pack(expand=YES, anchor=W)
        self.Q3_3rad=Radiobutton(self.root4, text = "5", variable = self.var3, value = 10,indicatoron=0, width = 5, font=("Pristina 14"), bg="light yellow")
        self.Q3_3rad.pack(expand=YES, anchor=W)
        
        self.final_page = Button(self.root4, text="Next", bg="red", fg="white", activebackground="black", activeforeground="white",font=("Pristina 14"),  command=self.result).pack(expand=YES, anchor=E)
        self.root4.mainloop()

    def result(self):

        self.root4.destroy()
        self.root5 = Tk()
        self.root5.configure(bg="light yellow")
        
        self.a = self.name_v.get()
        self.c = self.var.get()
        self.h = self.var1.get()

        self.counter = 0
        if self.correct1.get() == 1:
            self.counter += 1
        if self.correct2.get() == 1:
            self.counter += 1
        if self.correct3.get() == 1:
            self.counter += 1
        if self.correct4.get() == 1:
            self.counter += 1
       
        self.s = self.name_v.get()
        Label(self.root5, text = "Thank you " + self.s + ", for taking our placement exam!", fg="red", bg="light yellow", font=("pristina", 30)).pack(expand=YES, anchor=N)

        self.personality = self.var.get()
        
        #elif statements uses counter to determine personality alignment
        if self.counter > 2:
            if self.personality == "1":
                Label(self.root5, text = """Congratulations! You are a Gang Leader! You are the Lawful Evil of the world. You maintain order in your ranks, and have a
                habit of punishing those who do not fall in line. Who needs morals?""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
            elif self.personality == "2":
                Label(self.root5, text = """Congratulations! You are an Exotic Animal Smuggler! You are the Neutral Evil of the world. You're morals are certainly questionable, and so are you're choices. You follow no rules and answer to no authority but your ever-changing whim.""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
            elif self.personality == "3":
                Label(self.root5, text = """Congratulations! You are an Illegal Hacker! You are the Chaotic Evil of the world. No rules or authority could stop you, or enforce a sense of order.""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
        elif self.counter < 2:
            if self.personality == "1":
                Label(self.root5, text = """Congratulations! You are Personal Security! You are the Lawful Good of the world. You always follow the law and do what is right.""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
            elif self.personality == "2":
                Label(self.root5, text = """Congratulations! You are a Wildlife Conservationist! You are the Neutral Good of the world! You know that nature is an immovable force, so you do what you can to help, and let the rest take its course.""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
            elif self.personality == "3":
                Label(self.root5, text = """Congratulations! You are a Video Game Developer! You are the Chaotic Good of the world. You try your best to make everyone happy, but your ever-changing ambitions lead to hectic stories.""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
        elif self.counter == 2:
            if self.personality == "1":
                Label(self.root5, text = """Congratulations! You are an Army Soldier! You are the Lawful Neutral of the world. You don't pay much attention to what's right or wrong. What morals you follow are unimportant, so long their are orders to follow.""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
            elif self.personality == "2":
                Label(self.root5, text = """Congratulations! You are an Everyday Hunter! You are the True Neutral of the world. The Average Joe. Seriously, what do you even do?""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)
            elif self.personality == "3":
                Label(self.root5, text = """Congratulations! You are an IT Specialist! You are the Chaotic Neutral of the world. The repitition of "Have you tried turning it off and on again?" has drained you of all hope for the future. You live in the now.""", font=("Pristina 12 "), bg="light yellow").pack(expand=YES, anchor=N)



        self.strength = self.var1.get()
        self.dexterity = self.var2.get()
        self.intelligence = self.var3.get()

        #elif statements to determine attribute levels
        if self.personality == "1":
            self.strengthLevel = 30 + self.strength
            self.dexterityLevel =20 + self.dexterity
            self.intelligenceLevel = 10 + self.intelligence
            Label(self.root5, text = "Strength: " + str(self.strengthLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
            Label(self.root5, text = "Dexterity: " + str(self.dexterityLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
            Label(self.root5, text = "Intelligence: " + str(self.intelligenceLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
        elif self.personality == "2":
            self.strengthLevel = 10 + self.strength
            self.dexterityLevel =30 + self.dexterity
            self.intelligenceLevel = 20 + self.intelligence
            Label(self.root5, text = "Strength: " + str(self.strengthLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
            Label(self.root5, text = "Dexterity: " + str(self.dexterityLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
            Label(self.root5, text = "Intelligence: " + str(self.intelligenceLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
        elif self.personality == "3":
            self.strengthLevel = 10 + self.strength
            self.dexterityLevel =20 + self.dexterity
            self.intelligenceLevel = 30 + self.intelligence
            Label(self.root5, text = "Strength: " + str(self.strengthLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
            Label(self.root5, text = "Dexterity: " + str(self.dexterityLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)
            Label(self.root5, text = "Intelligence: " + str(self.intelligenceLevel), font=("Pristina 14 "), bg="light yellow").pack(expand=YES, anchor=N)

        self.root5.mainloop()

Quiz()._init_()

