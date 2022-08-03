from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import sys





class MainWindow(qtw.QMainWindow):

	def __init__ (self):
		super().__init__()
		#game and data initalized here..
		self.Game = flames()
		self.process_data ={}

		#Title name and app size exectute here..
		self.setWindowTitle("Flames")
		self.setWindowIcon(qtg.QIcon("source/images/logo.ico"))
		self.setFixedSize(qtc.QSize(500,600))

		#Main application layout
		self.page_layout = qtw.QVBoxLayout()

		#Input of person-1,person-2 and click-button layout
		self.input_layout = qtw.QHBoxLayout()
		self.input_layout.setAlignment(qtc.Qt.AlignVCenter)

		#Output display section process status and result of game "flames"
		self.output_layout = qtw.QHBoxLayout()
		


		#Game reset option and quit click button layout
		self.reset_layout = qtw.QHBoxLayout()
		self.reset_layout.setAlignment(qtc.Qt.AlignBottom)


		self.notes = qtw.QLabel("Just for fun.")
		self.notes.setProperty("class","notes")
		self.notes.setAlignment(qtc.Qt.AlignCenter)


		self.logodis = qtw.QLabel("icon.png")
		self.logodis.setPixmap(qtg.QPixmap("source/images/icon.png"))
		self.logodis.setScaledContents(True)
		self.logodis.setFixedSize(qtc.QSize(150,150))
		

		"""
		-------------------------------------------------------
			->Two Input field create for person-1 and person-2
				>style property 

			->Click Button to proceed the Game.
				>style property
				>calling game function.
		-------------------------------------------------------
		"""
		#Two Input field person-1 and person-2 layout 
		self.input_key_layout = qtw.QVBoxLayout()


		#first person name input field
		self.person1 = qtw.QLineEdit()
		self.person1.setProperty("class","person1")
		self.person1.setPlaceholderText("Enter First Person  Name")

		#second person name input field
		self.person2 = qtw.QLineEdit()
		self.person2.setProperty("class","person2")
		self.person2.setPlaceholderText("Enter Second Person Name")

		#inserting the two input field to the layout
		self.input_key_layout.addWidget(self.person1)
		self.input_key_layout.addWidget(self.person2)

		#Create the Click Button.
		self.input_trigger = qtw.QPushButton("Check")
		self.input_trigger.setProperty("class","Chkbtn")

		#Click Button Triggering the Game function.
		self.input_trigger.clicked.connect(self.startGame)

		#Inserting the two input layout and Button to the input layout. 
		self.input_layout.addLayout(self.input_key_layout)
		self.input_layout.addWidget(self.input_trigger)
	
		"""
		-----------------------------------------------------------------
			->Game Process Dispalyed in process-layout section.
				-> compare and remaining letter of two names.
					>style property
		Repeated......
				->Round label use to display striked data
					>style property

				->Striked element Display element informtion
					>style property

				->Remaining element Display information
					>style property
		end of repeat.

			->Final result Display in final-res-layout section.
				->Bonding level calculation output display in precentage.
					>style property

				->Total no of remaining letters count is display
					>style property

				->Final result Image Display
					>style property

				->related quotes of result
					>style property
		-----------------------------------------------------------------

		"""
		#Two Divison of Data represented.
		self.process_layout =qtw.QVBoxLayout()
		self.final_res_layout = qtw.QVBoxLayout()

		#inserting the two division into the output display 
		self.output_layout.addLayout(self.process_layout)
		self.output_layout.addLayout(self.final_res_layout)

		"""
		---------------------------------------------------------------
			->Reset window and quit options that section layout.
				->Reset button 
					>style property
					>reset game and window function calling

				->Quit button
					>style property
					>exit function calling
		----------------------------------------------------------------

		"""
		#Click button of reset app and game
		self.reset_button = qtw.QPushButton("Reset")
		self.reset_button.setProperty("class","Restbtn")

		#calling the Reset function
		self.reset_button.clicked.connect(self.clicked_reset)

		#Click button of quit app
		self.quit_button = qtw.QPushButton("Quit")
		self.quit_button.setProperty("class","Quitbtn")

		#calling button of quit function
		self.quit_button.clicked.connect(self.quit_button_clicked)

		self.footer= qtw.QLabel("Created by @Joel T George")
		self.footer.setProperty("class","footer")

		#Inserting two button in reset layout.
		self.reset_layout.addWidget(self.reset_button)
		self.reset_layout.addWidget(self.quit_button)
	
		self.logo_title_layout = qtw.QVBoxLayout()
		self.logo_title_layout.setAlignment(qtc.Qt.AlignTop|qtc.Qt.AlignJustify)


		self.footer_layout=qtw.QVBoxLayout()
		self.footer_layout.setAlignment(qtc.Qt.AlignBottom|qtc.Qt.AlignJustify)


		#Inserting three function section
		self.page_layout.addLayout(self.logo_title_layout)
		self.setlogo(True)
		self.page_layout.addLayout(self.input_layout)
		self.page_layout.addLayout(self.output_layout)
		self.page_layout.addLayout(self.reset_layout)
		self.page_layout.addLayout(self.footer_layout)
	
		#Final to the app windows
		self.widget = qtw.QWidget()
		self.widget.setLayout(self.page_layout)
		self.setCentralWidget(self.widget)




	def quit_button_clicked(self,s):
		alertquit = qtw.QMessageBox()
		alertquit.setProperty("class","alertbox")
		alertquit.setText("Are you sure Quit!")
		alertquit.setWindowTitle("Alert")
		alertquit.setIcon(qtw.QMessageBox.Warning)
		alertquit.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
		alertquit.buttonClicked.connect(self.quit_button_action)
		alertquit.exec_()
		
	def notify(self,message,title):
		alertquit = qtw.QMessageBox()
		alertquit.setProperty("class","alertbox")
		alertquit.setText(message)
		alertquit.setWindowTitle(title)
		alertquit.setIcon(qtw.QMessageBox.Information)
		alertquit.setStandardButtons(qtw.QMessageBox.Ok)
		alertquit.exec_()


	def startGame(self):
		p1,p2=self.person1.text(),self.person2.text()
		self.name_modify_totitle(p1,p2)

		if p1=="" or p2=="" :
			self.notify("Kindly Feed Information to Proceed.","Invalid Inputs")

		else:
			p1,p2=p1.replace(" ",""),p2.replace(" ","")
			p1,p2=p1.lower(),p2.lower()
			self.process_data=self.Game.flame(p1,p2)
			self.setlogo(False)
			self.input_restrict(True)
			self.GameReportBoard(self.process_data)

	def quit_button_action(self,s):
		if s.text() == "OK":
			sys.exit()


	def name_modify_totitle(self,per1,per2):
		self.person1.setText(per1.title())
		self.person2.setText(per2.title())


	def input_restrict(self,boolval):
		if boolval==True:
			self.person1.setEnabled(False)
			self.person2.setEnabled(False)
			self.input_trigger.setEnabled(False)
		else:
			self.input_trigger.setEnabled(True)
			self.person1.setEnabled(True)
			self.person2.setEnabled(True)

	def set_null_input(self):
		self.person1.setText("")
		self.person2.setText("")

	def setlogo(self,boolv):
		if boolv==True:
			self.logo_title_layout.addWidget(self.logodis)
			self.logo_title_layout.addWidget(self.notes)
			self.footer_layout.addWidget(self.footer)
		elif boolv==False:
			self.delete_label(self.logodis,self.logo_title_layout)
			self.delete_label(self.notes,self.logo_title_layout)
			self.delete_label(self.footer,self.footer_layout)

	def clicked_reset(self):
		self.setlogo(True)
		self.Reset(self.process_layout)
		self.Reset(self.final_res_layout)
		self.set_null_input()
		self.input_restrict(False)
		
	def delete_label(self,label,layout):
	
		for i in reversed(range(layout.count())):
				
			if layout.itemAt(i).widget() == label:
				layout.itemAt(i).widget().setParent(None)
				break

				

	def Reset(self,layout):
		if layout.count() == 0:
			return
		else:
			for i in reversed(range(layout.count())):
				if layout.itemAt(i).widget() is not None:
				
					layout.itemAt(i).widget().setParent(None)
				elif layout.itemAt(i).widget() is None:
					self.Reset(layout.itemAt(i))
				else:
					continue



	def process_display(self,sno,st_colr,rm_colr,strd,rem):
		sno=str(sno)
		#rounds of flames elements strike display.
		rounds = qtw.QLabel(f"Round: {sno}")
		rounds.setProperty("class","rounds")

		#striked element is display.
		strikes = qtw.QLabel(f"striked: {strd}")
		strikes.setProperty("class","strikes")
		strikes.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.273, stop:0 {st_colr}, stop:1 #151B25);")
			
		#remaining elements is display.
		remletter = qtw.QLabel(f"Remaining letter: { rem }")
		remletter.setProperty("class","remletter")
		remletter.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.273, stop:0 {rm_colr}, stop:1 #151B25);")
		
		#inserting each label.
		self.process_layout.addWidget(rounds)
		self.process_layout.addWidget(strikes)
		self.process_layout.addWidget(remletter)

	def final_result_display(self,bond_level,photo,message,bal_count):

		#display bonding level by calculate total charater and striked character.
		bondinglevel = qtw.QLabel("Bonding Level is {:.2f}%".format(bond_level))
		bondinglevel.setProperty("class","bondinglevel")

		#display result photo by final character
		result_pic = qtw.QLabel(f"{photo}")
		result_pic.setPixmap(qtg.QPixmap(f"source/images/{photo}"))
		result_pic.setFixedSize(qtc.QSize(333,328))
		result_pic.setScaledContents(True)

		#relatable quotes of result character
		bondmessage = qtw.QLabel(f"{message}")
		bondmessage.setFixedSize(qtc.QSize(333,50))
		bondmessage.setProperty("class","bondmess")

		#remaining character count is display
		balc = qtw.QLabel(f"Balance letters: {bal_count}")
		balc.setProperty("class","balc")


		self.final_res_layout.addWidget(bondinglevel)
		self.final_res_layout.addWidget(balc)
		self.final_res_layout.addWidget(result_pic)
		self.final_res_layout.addWidget(bondmessage)



	def GameReportBoard(self,data):
		i=0
		[pic,mes,sd,rm]= self.Game.result_img(data["final_letter"])
		t,c =data["totalstring"],data["balance_letter_count"]
		bondprec = (c/t)*100

		balw = qtw.QLabel("Balance letters: {}".format(data["balance_letters"]))
		balw.setProperty("class","balw")
		balw.setFixedSize(qtc.QSize(142,28))
		self.process_layout.addWidget(balw)
		

		for x in data["process_results"]:
			self.process_display(i+1,sd,rm,x["striked"],x["remainletters"])			
			i+=1


		#final result
		self.final_result_display(bondprec,pic,mes,data["balance_letter_count"])


		

class flames ():
	def __init__(self):
		pass


	

	def CompareStrike(self,p1,p2):
		l1= list(p1)
		l2 = list(p2)
		m=[]
		for x in range(len(p1)):
			for y in range(len(p2)):
				if l1[x] == l2[y]:
					l1[x],l2[y] = "0","0"
					m.append("0")
					break
		for j in m:
			l1.remove("0")
			l2.remove("0")
		l1.extend(l2)
		i="".join(l1)
		del m		
		return i
	def result_img(self,letter):
		imgandqutoes ={
			"F":["Friend.jpg","A sweet friendship,\nrefreshes the soul","#057DCD","#43B0F1"],
			"L":["Love.jpg","Love is master key of opening.\na gate of happiness","#E87A00","#D89C60"],
			"A":["Affection.jpg","We can live without religion and meditation,\nbut we cannot survive without human affection","#3D550C","#59981A"],
			"M":["Marriage.jpg","loves is deep , love is wide.\nIt's the only thing that reaches a soul","#420264","#5C038C"],
			"E":["Enemy.jpg","The enemy is fear.We think it is hate,\nbut it is fear","#5F1300","E10032"],
			"S":["Sister.jpg","A loving brother or sister is a gift\nfor your soul","#1C4670","#278AB0"]
		}
		return imgandqutoes[letter]

	def flame(self,p1,p2):
		pass
		data ={}
		bal = self.CompareStrike(p1,p2)
		data["balance_letters"] = bal
		
		data["totalstring"] = len(p1+p2)

		count=len(bal)
		data["balance_letter_count"]=count
		data["process_results"]=[]
		fl = list("FLAMES")
		for i in range(5):
			rem = count%len(fl)
			single=""
			if rem==0:
				single = fl[len(fl)-1]
				fl.remove(single)
		
			elif rem < len(fl) and rem != 1 and rem !=0:
				
				pass
				cpy=[]
				single = fl[rem-1]
				fl.remove(single)
				j=0
				f =len(fl)
				while j < len(fl) :
					if j>=rem-1:
						break
				
					
					cpy.append(fl[j])
					fl[j]='0'  
							
					j+=1
			
				k=j
				while k <= j and k > 0 :

					fl.remove('0')
					k-=1
				fl.extend(cpy)
				del cpy


			elif rem ==1:
				single = fl[0]
				fl.remove(single)
				fls = "".join(fl)
			data["process_results"].append({"striked":single,"remainletters":"".join(fl)})
		data["final_letter"] = 	fl[0]
		return data



app = qtw.QApplication([])

with open("source/style/main.css","r") as file:
	app.setStyleSheet(file.read())



window =  MainWindow()
window.show()
app.exec_()

