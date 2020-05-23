# Legomind_SHARED
# Attila Kekesi
# 23.05.2020

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import webbrowser

options = [None]		# Options for Combobox (A,B,C...)
var = [3, 4, 5, 6, 7]	# Number of Options
parts = ["Head", "Torso", "Legs", "Tool"]
who = [None]*len(parts)	# Wanted/Who
tip = [None]*len(parts)	# Tip/Guess
versuch = 0				# Number of Guesses
win = 0					# Number of Wins
wintmp = 0				# if already won for History text	
s_h = "s"				# Show/Hide
e_h = "E"				# Easy/Hard

def new_game():			# Start New Game
	clear_guess()		# Clear Guess
	clear_ans()			# Clear Answer
	clear_pre()			# Clear History

	global versuch
	global win
	global who
	global s_h

	opt_var()			# Fill Options with (A,B,C...) depend on Var (number of options) and fill Guess-Combobox with Options
	versuch = 0
	win = 0
	who = wanted()		# Create Wanted/Who
	s_h = "s"			# Reset Show/Hide --> Hide
	show_hide()			# Reset Show/Hide --> Hide

	# Fill Wanted with Who
	wanted_1.config(state=NORMAL)
	wanted_1.delete(1.0, END)
	wanted_1.tag_configure("justified", justify="center")
	wanted_1.insert(END, str(who[0]), "justified")
	wanted_1.config(state=DISABLED)
	wanted_2.config(state=NORMAL)
	wanted_2.delete(1.0, END)
	wanted_2.tag_configure("justified", justify="center")
	wanted_2.insert(END, str(who[1]), "justified")
	wanted_2.config(state=DISABLED)
	wanted_3.tag_configure("justified", justify="center")
	wanted_3.config(state=NORMAL)
	wanted_3.delete(1.0, END)
	wanted_3.insert(END, str(who[2]), "justified")
	wanted_3.config(state=DISABLED)
	wanted_4.tag_configure("justified", justify="center")
	wanted_4.config(state=NORMAL)
	wanted_4.delete(1.0, END)
	wanted_4.insert(END, str(who[3]), "justified")
	wanted_4.config(state=DISABLED)

def opt_var():			# Fill Options with (A,B,C...) depend on Var (number of Options)
						# Fill Guess-Combobox with Options
	global options
	global guess_1
	global guess_2
	global guess_3
	global guess_4
	if opt_comb.get() == "" or opt_comb.get() == str(var[0]):
		options = ["A", "B", "C"]
		opt_comb.current(0)
	elif opt_comb.get() == str(var[1]):
		options = ["A", "B", "C", "D"]
	elif opt_comb.get() == str(var[2]):
		options = ["A", "B", "C", "D", "E"]
	elif opt_comb.get() == str(var[3]):
		options = ["A", "B", "C", "D", "E", "F"]
	elif opt_comb.get() == str(var[4]):
		options = ["A", "B", "C", "D", "E", "F", "G"]

	# Fill Guess-Combobox with Otions
	guess_1 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
	guess_1.grid(row=2, column=2)
	guess_2 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
	guess_2.grid(row=3, column=2)
	guess_3 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
	guess_3.grid(row=4, column=2)
	guess_4 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
	guess_4.grid(row=5, column=2)

def wanted():			# Create new Wanted/Who randomly
	global options
	global who
	for i in range(len(who)):
		who[i] = random.choice(options)
	return who

def show_hide():		# Change Show/Hide
	global s_h
	if s_h == "s":
		wanted_1.config(bg="black")
		wanted_2.config(bg="black")
		wanted_3.config(bg="black")
		wanted_4.config(bg="black")
		s_h = "h"
	else:
		wanted_1.config(bg="white")
		wanted_2.config(bg="white")
		wanted_3.config(bg="white")
		wanted_4.config(bg="white")
		s_h = "s"

def guess():			# Collect Guess --> Tip
						# Check Guess --> Answer, History
						# Increase number of Guesses/Versuch
	check_opt_comb()
	clear_ans()
	global versuch
	global tip
	versuch += 1
	tip[0] = guess_1.get()
	tip[1] = guess_2.get()
	tip[2] = guess_3.get()
	tip[3] = guess_4.get()
	check_tip()

def check_opt_comb():	# Check if Var equal to number of Options
	global options
	global guess_1
	global guess_2
	global guess_3
	global guess_4
	if opt_comb.get() != str(len(options)):
		# If Var doesn't equal to number of Options
		# --> You can change Var
		#	--> new Wanted from new Var
		#	--> but your Guess remains
		if messagebox.askyesno("Warning","Number of Var. is wrong!\nDo you want change?", icon="warning") == True:
			try:
				tmp_1 = options.index(guess_1.get())
				if options.index(guess_1.get()) > len(options):
					tmp_1 = ""
			except:
				tmp_1 = ""
			try:
				tmp_2 = options.index(guess_2.get())
				if options.index(guess_2.get()) > len(options):
					tmp_2 = ""
			except:
				tmp_2 = ""
			try:
				tmp_3 = options.index(guess_3.get())
				if options.index(guess_3.get()) > len(options):
					tmp_3 = ""
			except:
				tmp_3 = ""
			try:
				tmp_4 = options.index(guess_4.get())
				if options.index(guess_4.get()) > len(options):
					tmp_4 = ""
			except:
				tmp_4 = ""
			new_game()
			try:
				guess_1.current(tmp_1)
			except:
				guess_1.set(tmp_1)
			try:
				guess_2.current(tmp_2)
			except:
				guess_2.set(tmp_2)
			try:
				guess_3.current(tmp_3)
			except:
				guess_3.set(tmp_3)
			try:
				guess_4.current(tmp_4)
			except:
				guess_4.set(tmp_4)
		else:
			opt_comb.current(len(options)-3)

def check_tip():		# Check Guess/Tip
						# Fill Answer
						# Fill History
	global tip
	global who
	global win
	global wintmp
	ans = [None]*len(tip)
	ans_col = [None]*len(tip)
	for i in range(len(tip)):
		for j in range(len(who)):
			tmp_t = 0
			tmp_w = 0
			if tip[i] == who[i]:
				ans[i] = u"\u2713"									# Tip equal to Who --> check mark, break
				break
			elif tip[i] == who[j] and i != j:						# Tip equal to another Who
				if tip[j] == who[j]:								# --> but the another Who still has a good Tip --> x
					ans[i] = u"\u2717"
				elif tip[j] != who[j]:								# --> the another Who don't have good Tip --> ...
					for m in range(i+1):							# 	--> add up these cases
						if tip[m] == tip[i] and tip[m] != who[m]:
							tmp_t += 1
					for n in range(j+1):
						if who[n] == tip[i] and tip[n] != who[n]:
							tmp_w += 1
					if tmp_t > tmp_w:								# 	--> Tip > Who --> x
						ans[i] = u"\u2717"
					elif tmp_t <= tmp_w:							# 	--> Tip < Who --> slash
						ans[i] = u"\uFF0F"
						break
			else:
				ans[i] = u"\u2717"									# else x

	if e_h == "H":													# if not easy --> sort Answers
		ans = sort(ans)

	# Fill Answers
	ans_1.config(state=NORMAL)
	ans_1.delete(1.0, END)
	ans_1.insert(END, ans[0], 'tag-center')
	ans_1.config(state=DISABLED)
	ans_2.config(state=NORMAL)
	ans_2.delete(1.0, END)
	ans_2.insert(END, ans[1], 'tag-center')
	ans_2.config(state=DISABLED)
	ans_3.config(state=NORMAL)
	ans_3.delete(1.0, END)
	ans_3.insert(END, ans[2], 'tag-center')
	ans_3.config(state=DISABLED)
	ans_4.config(state=NORMAL)
	ans_4.delete(1.0, END)
	ans_4.insert(END, ans[3], 'tag-center')
	ans_4.config(state=DISABLED)

	# Fill Answers with colour
	for i in range(len(ans)):
		if ans[i] == u"\u2713":
			ans_col[i] = "green"
		elif ans[i] == u"\uFF0F":
			ans_col[i] = "orange"
		else:
			ans_col[i] = "red"

	ans_1.config(bg=ans_col[0])
	ans_2.config(bg=ans_col[1])
	ans_3.config(bg=ans_col[2])
	ans_4.config(bg=ans_col[3])

	# Fill History
	pre.config(state=NORMAL)
	if wintmp != 0:
		pre.insert(END, "\n")
	pre.insert(END, " ~~~~")
	pre.insert(END, versuch)
	pre.insert(END, "~~~~\n ")
	for i in range(len(tip)):
		if i == 0:
			pre.insert(END, "")
		else:
			pre.insert(END, "  ")
		if tip[i] == "":
			pre.insert(END, "?")
		else:
			pre.insert(END, "")
			pre.insert(END, tip[i])
	pre.insert(END, "\n ")
	pre.insert(END, ans)
	pre.insert(END, "\n")

	# Fill History with colour
	for i in range(len(tip)):
		tmpcol = 3*versuch+((i+1)*2-1)/10 + win
		tmpnev = 'color' + str(versuch) + str(i+1)
		pre.tag_add(tmpnev,tmpcol,tmpcol+0.1)
		pre.tag_config(tmpnev, background="white", foreground=ans_col[i])

	# Check WIN with colour
	if ans[0] == u"\u2713" and ans[1] == u"\u2713" and ans[2] == u"\u2713" and ans[3] == u"\u2713":
		global s_h
		s_h = "h"
		show_hide()
		pre.tag_configure("color", foreground="green", font="bold")
		pre.insert(END, "  * WIN *", "color")
		wintmp = 1
		win = win + 1
	else:
		wintmp = 0

	pre.config(state=DISABLED)
	pre.yview_moveto(1)

def sort(a):
	for i in range(len(a)):	
		if a[i] == u"\u2713":
			a[i] = 1
		elif a[i] == u"\uFF0F":
			a[i] = 2
		elif a[i] == u"\u2717":
			a[i] = 3

	for i in range(len(a)):
		for j in range(i+1,len(a)):
			if a[i] > a[j]:
				tmp = a[i]
				a[i] = a[j]
				a[j] = tmp

	for i in range(len(a)):
		if a[i] == 1:
			a[i] = u"\u2713"
		elif a[i] == 2:
			a[i] = u"\uFF0F"
		elif a[i] == 3:
			a[i] = u"\u2717"
	return a

def easy_hard():
	global e_h
	if e_h == "E":
		Label(root, text="H").grid(row=1, column=3)
		e_h = "H"
	elif e_h == "H":
		Label(root, text="E").grid(row=1, column=3)
		e_h = "E"	

def info():
	url = "https://drive.google.com/open?id=1Jfz-ECxITRAg1vgqsN7_6cBn6IfIkvrU"
	webbrowser.open_new(url)

def video():
	url = "https://www.youtube.com/watch?v=g61y6o8w9KM&list=PLgRD4Phr5Y-XNZCLYAp_pjrH9JwWVzu3F"
	webbrowser.open_new(url)

def clear_guess():
	guess_1.delete(0, END)
	guess_2.delete(0, END)
	guess_3.delete(0, END)
	guess_4.delete(0, END)

def clear_ans():
	ans_1.config(state=NORMAL)
	ans_1.delete(1.0, END)
	ans_1.config(state=DISABLED)
	ans_1.config(bg="white")
	ans_2.config(state=NORMAL)
	ans_2.delete(1.0, END)
	ans_2.config(state=DISABLED)
	ans_2.config(bg="white")
	ans_3.config(state=NORMAL)
	ans_3.delete(1.0, END)
	ans_3.config(state=DISABLED)
	ans_3.config(bg="white")
	ans_4.config(state=NORMAL)
	ans_4.delete(1.0, END)
	ans_4.config(state=DISABLED)
	ans_4.config(bg="white")

def clear_pre():
	global versuch
	global win
	global wintmp
	versuch = 0
	win = 0
	wintmp = 0
	pre.config(state=NORMAL)
	pre.delete(1.0, END)
	pre.config(state=DISABLED)

def close_game():
	root.destroy()


root = Tk()
root.title("Legomind")
root.minsize(width = 332, height = 624)

root.grid_columnconfigure(0, minsize=30)
root.grid_columnconfigure(4, minsize=30)
root.grid_columnconfigure(6, minsize=30)
root.grid_rowconfigure(0, minsize=30)
root.grid_rowconfigure(6, minsize=20)
root.grid_rowconfigure(8, minsize=20)
root.grid_rowconfigure(12, minsize=30)

Label(root, text="E").grid(row=1, column=3)
Label(root, text="Wanted").grid(row=1, column=5)
Label(root, text="Guess").grid(row=1, column=2)
Label(root, text=parts[0]+":").grid(row=2, column=1, sticky=E)
Label(root, text=parts[1]+":").grid(row=3, column=1, sticky=E)
Label(root, text=parts[2]+":").grid(row=4, column=1, sticky=E)
Label(root, text=parts[3]+":").grid(row=5, column=1, sticky=E)
Label(root, text="History").grid(row=9, column=2)

guess_1 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
guess_1.grid(row=2, column=2)
guess_2 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
guess_2.grid(row=3, column=2)
guess_3 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
guess_3.grid(row=4, column=2)
guess_4 = ttk.Combobox(root, values=options, height=1, width=10, justify=CENTER)
guess_4.grid(row=5, column=2)

ans_1 = Text(root, state=DISABLED, height=1, width=2)
ans_1.grid(row=2, column=3)
ans_1.tag_configure('tag-center', justify='center')
ans_2 = Text(root, state=DISABLED, height=1, width=2)
ans_2.grid(row=3, column=3)
ans_2.tag_configure('tag-center', justify='center')
ans_3 = Text(root, state=DISABLED, height=1, width=2)
ans_3.grid(row=4, column=3)
ans_3.tag_configure('tag-center', justify='center')
ans_4 = Text(root, state=DISABLED, height=1, width=2)
ans_4.grid(row=5, column=3)
ans_4.tag_configure('tag-center', justify='center')

wanted_1 = Text(root, state=DISABLED, height=1, width=10)
wanted_1.grid(row=2, column=5)
wanted_2 = Text(root, state=DISABLED, height=1, width=10)
wanted_2.grid(row=3, column=5)
wanted_3 = Text(root, state=DISABLED, height=1, width=10)
wanted_3.grid(row=4, column=5)
wanted_4 = Text(root, state=DISABLED, height=1, width=10)
wanted_4.grid(row=5, column=5)

frame_1 = Frame(root)
frame_1.grid(row=10, column=5)
frame_2 = Frame(frame_1)
frame_2.pack(side=TOP)
frame_3 = Frame(frame_1)
frame_3.pack(side=TOP)

Label(frame_2, text="Opt. ").pack(side = LEFT)
opt_comb = ttk.Combobox(frame_2, values=var, height=1, width=3, justify=CENTER)
opt_comb.pack(side=LEFT, anchor=CENTER)

Button(root, text="Guess", command=guess, height=1, width=10).grid(row=7, column=2)
Button(root, text="Show/Hide", command=show_hide, height=1, width=10).grid(row=7, column=5)
Button(frame_3, text="Easy/Hard", command=lambda:[easy_hard(), clear_ans()], height=1, width=10).pack(side=TOP)
Button(frame_3, text="New", command=new_game, height=1, width=10).pack(side=TOP)
Button(frame_3, text="Clear", command=lambda:[clear_guess(), clear_ans(), clear_pre()], height=1, width=10).pack(side=TOP)
Button(frame_3, text="Info", command=info, height=1, width=10).pack(side=TOP)
Button(frame_3, text="Video", command=video, height=1, width=10).pack(side=TOP)
Button(frame_3, text="Close", command=close_game, height=1, width=10).pack(side=TOP)

scroll = Scrollbar(root)
pre = Text(root, state=DISABLED, height=23, width=12, yscrollcommand=scroll.set)
pre.grid(row=10, column=2, rowspan=2)
scroll.config(command=pre.yview)
scroll.grid(row=10, column=3, rowspan=2, sticky=N+S)

if __name__ ==  "__main__":
	root.mainloop()
