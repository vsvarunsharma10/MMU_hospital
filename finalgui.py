import Tkinter as tk
import ttk
from PIL import Image, ImageTk
LARGE_FONT = ("Helvetica",12)



class Onewindow(tk.Tk):
	def __init__(self, *args,**kwargs):

		tk.Tk.__init__(self, *args,**kwargs)
		container = tk.Frame(self,width = 720, height = 1280)
		self.geometry("1480x1080")
		container.pack(side = "top",fill ="both",expand = True)

		container.grid_rowconfigure(0,weight =1)
		container.grid_columnconfigure(0,weight =1)
		

		self.frames = {}
		for F in (StartPage,Pageone,Pagetwo):
			frame = F(container,self)
			self.frames[F] = frame
			
			frame.grid(row =0, column =0, sticky = "snew")
		self.show_frame(StartPage)



	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()




class StartPage(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__ (self,parent,bg = "#232424")

		#form no. f1

		self.f1 = tk.Frame(self,bg = "#3B3F40")
		self.f1.grid(row = 0 , column = 0, sticky = 'nsew', padx = 10, pady = 10)
		label = tk.Label(self.f1, text = "  PhyX  ",font = LARGE_FONT,bg= "#043313",fg = "white",padx = 130,pady = 3)
		label.place(x =0,y =10,relwidth = 1)
		button = tk.Button(self.f1,text = "New Patient", padx = 25, pady = 40, 
									command = lambda:controller.show_frame(self.newFrame()))
		button.grid(row = 3,column = 2,sticky = "nw",pady = [60,20],padx = [110,0])

		#from no. f2

		self.f2 = tk.Frame(self,bg = "#3B3F40")
		self.f2.grid(row =1 , column = 0 , sticky = 'w',padx= 10, pady = 10)

		
		label = tk.Label(self.f2,text = "Old Patient",font = LARGE_FONT,bg= "#043313",fg = "white",padx = 50)
		label.place(x=0,y=10,relwidth = 1)

		button = ttk.Button(self.f2,text = "Enter"
									,command = lambda : controller.show_frame(Pagetwo))
		button.grid(row = 11,column = 1,sticky = "nw",pady = 10, padx = 80)

		#label stuff
		self.name = tk.Label(self.f2, text = 'Name',bg= "#3B3F40",fg = "white")
		self.name.grid(row = 7,column = 0,pady = [50,0],padx = 0)

		self.mobile_no = tk.Label(self.f2, text = 'Mobile No.',bg= "#3B3F40",fg = "white")
		self.mobile_no.grid(row = 9,column = 0,pady = 30,padx = [5,0])

		self.name_entry = ttk.Entry(self.f2,width = 30)
		self.name_entry.grid(row = 7,column = 1,sticky = "nw",pady = [50,0],padx=40)

		self.mobile_entry= ttk.Entry(self.f2,width = 30)
		self.mobile_entry.grid(row = 9, column = 1,pady = 10,padx = 40)


		#new frame
		self.f3 = tk.Frame(self,pady = 5,bg = "#3B3F40")
		self.f3.place(relx = 0.769, rely = 0.012)

		label = tk.Label(self.f3,text = "List of Patient",bg= "#043313",fg = "white",width = 40) 
		label.pack(expand = True,fill = "x")
		lists= tk.Listbox(self.f3,height = 30, width = 30)
		lists.pack(expand = True)

		
	def newFrame(self):
			self.f = tk.Frame(self, padx = 0, pady = 1,bg = "#3B3F40")
			
			self.f.place(x =365,y = 10,height = 510)
			self.label = tk.Label(self.f,text = "",bg= "#3B3F40",fg = "white")
			self.label.pack()

			#entry stuff
			self.name_entry = tk.Entry(self.f,width = 30)
			self.name_entry.pack(pady = [40,0],padx = [160,320])
			
			self.mobile_entry= tk.Entry(self.f,width = 30)
			self.mobile_entry.pack(pady = [25,0],padx = [160,320])
			self.address_entry = tk.Text(self.f,height = 5,width= 23)
			self.address_entry.pack(pady = [70,0], padx = [160,320])

			self.problem_entry = tk.Entry(self.f,width= 30)
			self.problem_entry.pack(pady = [20,0], padx = [160,320])

			self.city_entry = tk.Entry(self.f,width = 30)
			self.city_entry.pack(pady = [30,0], padx = [160,320])
			self.state_entry = tk.Entry(self.f,width = 30)
			self.state_entry.pack(pady = [30,30], padx = [160,320])

			#label stuff
			self.label1 = tk.Label(self.f, text = 'Register Patient',font=("Helvetica", 14),bg= "#043313",fg = "white")
			self.label1.place(x =0,relwidth = 1,rely = 0.02)

			self.name = tk.Label(self.f, text = 'Name',bg= "#3B3F40",fg = "white")
			self.name.place(x = 80 ,y = 60)

			self.mobile_no = tk.Label(self.f, text = 'Mobile No.',bg= "#3B3F40",fg = "white")
			self.mobile_no.place(x = 80, y = 105)
	
			#combobox
			self.combo_sex = tk.StringVar()
			self.sex_box = ttk.Combobox(self.f, width = 27,textvariable = self.combo_sex)
			self.sex_box['value'] = ("male",("female"),("karvaado"))
			self.sex_box.bind("<<ComboboxSelected>>",self.newselection)
			self.sex_box.place(x = 160, y = 150)

			self.sex = tk.Label(self.f, text = 'Sex',bg= "#3B3F40",fg = "white")
			self.sex.place(x = 80, y = 150)

			self.address = tk.Label(self.f, text = 'Address',bg= "#3B3F40",fg = "white")
			self.address.place(x = 80, y = 190)

			self.problem = tk.Label(self.f, text = 'Problem',bg= "#3B3F40",fg = "white")
			self.problem.place(x = 80, y = 295)

			self.city = tk.Label(self.f, text = 'City',bg= "#3B3F40",fg = "white")
			self.city.place(x = 80, y = 345)

			self.state = tk.Label(self.f, text = 'State',bg= "#3B3F40",fg = "white")
			self.state.place(x =80, y = 390)

			self.button = ttk.Button(self.f,text = "Submit")
									#,command = lambda : controller.show_frame(Pagetwo))
			self.button.place(x = 290, y= 450)
			self.button = ttk.Button(self.f,text = "Clear")
									#,command = lambda : controller.show_frame(Pagetwo))
			self.button.place(x = 140, y= 450)
			return self.f

	def newselection(self,event):
		self.value = self.sex_box.get()
		print "run"

		
		

class Pageone(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent,width = 400, height = 200,bg = "red")
		self.place(x = 100, y= 150)
		label = tk.Label(self, text = "Page one",font = LARGE_FONT)
		label.pack(pady = 10, padx = 10)
		button = tk.Button(self,text = "Back to Home"
			,command = lambda: controller.show_frame(StartPage))
		button.pack(pady = 10, padx =10)

#Doctor workspace
class Pagetwo(tk.Frame):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent,bg = "#232424")
		self.f3 = tk.Frame(self,pady = 5,bg = "#3B3F40")
		self.f3.place(x = 10,y= 10,height = 450)

		label = tk.Label(self.f3,text = "List of Patient",bg= "#29515E",fg = "white",width = 40) 
		label.pack(expand = True,fill = "x")
		lists= tk.Listbox(self.f3,height = 28, width = 40)
		lists.insert(1,"Malkit Singh")
		lists.pack(expand = True)
		#lists.bind('<Button-1>',self.detail_label)

		label = tk.Label(self,text = "Doctor Workspace",font = LARGE_FONT,bg = "#232424",fg = "white")
		label.pack(pady = 10,padx = 10)
		
		#frame diagonsis
		self.f4 = tk.Frame(self,bg = "")
		self.f4.place(x=13,y=470)

		self.button = tk.Button(self.f4,text = "Diagnosis",width = 39,height = 2,
									 command = lambda:controller.show_frame(self.diagnose_frame()) )
									
		self.button.pack()

		#functions

		self.diagnose_frame()

		self.problem_names()
		
		self.history_summary()

		self.detail_label()

		self.list_of_problems()

		self.scheduling_combobox()

		#tabs frame
	def history_summary(self):

		self.f7 = tk.Frame(self,padx = 0, pady = 1, bg= "#29515E")
		self.f7.place(x= 830,y =10)
		self.notebook = ttk.Notebook(self.f7,height = 200,width = 500)

		#history_tab
		self.history_tab = tk.Frame(self.notebook)
		self.notebook.add(self.history_tab,text = "History")

		self.tree = ttk.Treeview(self.history_tab)
		ttk.Style().configure("Treeview", background="#29515E", 
 								foreground="white", fieldbackground="red")
		 
		self.tree["columns"]=("one","two")

		self.tree.column("one", width=130 )
		self.tree.column("two", width=130 )

		self.tree.heading("#0",text = "Problems")
		self.tree.heading("one", text="Exercise")
		self.tree.heading("two", text="Medicine")

		
		
		 
		self.date_1 = self.tree.insert("", 1, "dir2", text="25/4/16")
		self.tree.insert(self.date_1, "end", "dir 2", text="Migrane", values=("       Kapalbhati","      Ashwagandha"))
		self.tree.insert(self.date_1, "end", "dir 3", text="Back Pain", values=("       Chakarasan","      Ashmiharas"))

		#self.tree.insert(self.date_1, "end", "dir 4", text="Exercise", values=("Sureya Namaskar"))
		#self.tree.insert(self.date_1, "end", "dir 5", text="Medicine", values=("Lemon soda"))

		
		self.id3= self.tree.insert("", 3, "dir3", text="24/4/16")
		self.tree.insert(self.id3,"end","dir4",text = "example",values= ("hello"))
		self.tree.pack(expand= True)

		#summary_tab
		self.summary_tab = tk.Frame(self.notebook)
		self.notebook.add(self.summary_tab,text = "Summary")
		self.notebook.pack(padx=5,pady =5)


		

		
		
	def problem_names(self):
		self.f7 = tk.Frame(self,padx = 0, pady = 1,bd = 10,relief=tk.RIDGE,bg= "#29515E")
		self.f7.place(x= 1040,y =260,height = 320,width = 305)
		

		self.var1 = tk.IntVar()
		self.var2 = tk.IntVar()
		self.var3 = tk.IntVar()
		self.var4 = tk.IntVar()
		self.var5 = tk.IntVar()
		self.var6 = tk.IntVar()
		self.var7 = tk.IntVar()
		self.var8 = tk.IntVar()
		self.var9 = tk.IntVar()
		self.var10 = tk.IntVar()
		self.var11 = tk.IntVar()
		self.var12 = tk.IntVar()
	

		#Exercise_Parent
		self.exercise_label = ttk.Label(self.f7,text = " Exercises ")
		self.exercise_label.place(x = 10 ,y =10)

		#Exercise_Child
		self.checkbutton = tk.Checkbutton(self.f7,text = "A",variable = self.var3,bg= "#29515E")
	
		self.checkbutton.place(x = 25, y = 40)
		self.checkbutton = tk.Checkbutton(self.f7,text = "B",variable = self.var4,bg= "#29515E")
		self.checkbutton.place(x = 25, y = 100)
		self.checkbutton = tk.Checkbutton(self.f7,text = "C",variable = self.var5,bg= "#29515E")
		self.checkbutton.place(x = 25, y = 160)
		self.checkbutton = tk.Checkbutton(self.f7,text = "D",variable = self.var6,bg= "#29515E")
		self.checkbutton.place(x = 25, y = 220)

		#Exercises_Parent
		self.medicine_label = tk.Label(self.f7,text = " Medicine ")
		self.medicine_label.place(x = 200, y = 10)
		

		#Exercise_Child
		self.checkbutton = tk.Checkbutton(self.f7,text = "A",variable = self.var7,bg= "#29515E")
		self.checkbutton.place(x = 215, y = 40)
		self.checkbutton = tk.Checkbutton(self.f7,text = "B",variable = self.var8,bg= "#29515E")
		self.checkbutton.place(x = 215, y = 100)
		self.checkbutton = tk.Checkbutton(self.f7,text = "C",variable = self.var9,bg= "#29515E")
		self.checkbutton.place(x = 215, y = 160)
		self.checkbutton = tk.Checkbutton(self.f7,text = "D",variable = self.var10,bg= "#29515E")
		self.checkbutton.place(x = 215, y = 220)


		button = tk.Button(self.f7,text = "Submit")
									
		button.place(x=110,y= 260)



		
		

	#diagnosis body	
	def diagnose_frame(self):
		self.f5 = tk.Frame(self, padx = 0, pady = 1,bg = "#3B3F40")
		self.f5.place(x =310,y = 10,height = 710)
		self.p= ImageTk.PhotoImage(file = "a.png")

		#create canvas
		self.canvas =  tk.Canvas(self.f5,width = 500, height = 867,bg ="#3B3F40" )
		self.canvas.pack()	
		self.canvas.create_image(240,370,image = self.p,anchor=tk.CENTER)

		button = tk.Button(self.f5,text = "Flip",width = 10,height = 2,
									 command =lambda:self.flip_body() )
									
		button.place(x=320,y= 30)
		self.canvas.bind("<Button-1>",self.draw_oval_front)


	def draw_oval_front(self,event):
		self.x = self.canvas.canvasx(event.x)
		self.y = self.canvas.canvasy(event.y)
 		print event.x
 		print event.y
 		self.c= self.canvas.find_all()
 		print self.c
		x1,y1 =event.x-1,event.y-1
		x2,y2 = event.x+1,event.y+1

		self.id1=self.canvas.create_oval(x1,x2,y1,y2,fill = "green")
		self.canvas.coords(self.id1,x1-10,y1-10,x2+10,y2+10)




	def draw_oval_back(self,event):
		self.x = self.canvas1.canvasx(event.x)
		self.y = self.canvas1.canvasy(event.y)
 		print event.x
 		print event.y
 		self.c= self.canvas1.find_all()
 		print self.c
		x1,y1 =event.x-1,event.y-1
		x2,y2 = event.x+1,event.y+1

		self.id1=self.canvas1.create_oval(x1,x2,y1,y2,fill = "green")
		self.canvas1.coords(self.id1,x1-10,y1-10,x2+10,y2+10)	



	#flip body
	def flip_body(self):
		self.f6 = tk.Frame(self, padx = 0, pady = 1,bg = "#3B3F40")
		self.f6.place(x =310,y = 10,height = 710)
		self.p= ImageTk.PhotoImage(file = "b.png")
		self.canvas1 =  tk.Canvas(self.f6,width = 500, height = 867,bg ="#3B3F40" )
		self.canvas1.pack()	
		self.canvas1.create_image(240,370,image = self.p,anchor=tk.CENTER)

		button = tk.Button(self.f6,text = "Flip",width = 10,height = 2,
									 command =lambda:self.diagnose_frame() )
									
		button.place(x=320,y= 30)
		self.canvas1.bind("<Button-1>",self.draw_oval_back)


	def list_of_problems(self):
		self.f3 = tk.Frame(self,relief=tk.RIDGE,bg= "#29515E")
		self.f3.place(x = 825,y= 260,height = 320,width= 203)

		self.label = tk.Label(self.f3,text = "List of Problems",bg= "#29515E",fg = "white") 
		self.label.place(x = 55,y =5)
		self.lists= tk.Listbox(self.f3,height = 17, width = 30,bg = "#012C42",fg = "white",relief=tk.RIDGE)
		self.lists.insert(1,"Migrane","Back Pain")
		self.lists.place(x = 10,y=25)
		#self.lists.bind('<Button-1>',self.detail_label)
		
		
		
	def detail_label(self):
		self.f = tk.Frame(self, padx = 0, pady = 1,bg = "white",width = 50)
		self.f.place(x = 13,y = 525)
		self.label = tk.Label(self.f,text = "Problem : Back pain",
								font = ("Helvetica",14),bg= "#29515E",fg = "green",height = 7,width=25)
		self.label.pack(expand = "False")
		

	def scheduling_combobox(self):
		
		self.frame_scheduling = tk.Frame(self,relief=tk.RIDGE,bg= "#29515E")
		self.frame_scheduling.place(x = 825,y= 590,height = 100,width= 300)

		#Week_box
		self.combo_week = tk.StringVar()
		self.week_box = ttk.Combobox(self.frame_scheduling, width = 27,textvariable = self.combo_week)
		self.week_box['value'] = ("1",("2"),("3"))
		self.week_box.bind("<<ComboboxSelected>>",self.newselection)
		self.week_box.place(x=50,y=5)

		self.week_label = tk.Label(self.frame_scheduling, text = 'Week',bg= "#3B3F40",fg = "white")
		self.week_label.place(x = 5,y = 5)

		#Day_box
		self.combo_day = tk.StringVar()
		self.day_box = ttk.Combobox(self.frame_scheduling, width = 27,textvariable = self.combo_day)
		self.day_box['value'] = ("1",("2"),("3"))
		self.day_box.bind("<<ComboboxSelected>>",self.newselection)
		self.day_box.place(x=50,y=40)

		self.day_label = tk.Label(self.frame_scheduling, text = 'Day',bg= "#3B3F40",fg = "white")
		self.day_label.place(x = 5,y = 40)

		#Time_box
		self.combo_time = tk.StringVar()
		self.time_box = ttk.Combobox(self.frame_scheduling, width = 27,textvariable = self.combo_time)
		self.time_box['value'] = ("1",("2"),("3"))
		self.time_box.bind("<<ComboboxSelected>>",self.newselection)
		self.time_box.place(x=50,y=70)

		self.time_label = tk.Label(self.frame_scheduling, text = 'Time',bg= "#3B3F40",fg = "white")
		self.time_label.place(x = 5,y = 70)	


	def newselection(self,event):
		self.value = self.sex_box.get()
		print "run"	
	
if __name__ == "__main__":

	app = Onewindow()
	app.mainloop()	
