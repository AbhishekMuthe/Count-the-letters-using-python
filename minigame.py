import random 
import tkinter
import inflect
count = 0
countword = "Dont type this"
p = inflect.engine()
numbers = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
words = []
for number in numbers:
	 a = p.number_to_words(number)
	 words.append(a)
time = 30				
score = 0
def start(event):
	if time == 30:
		countdown()
	word()
def word():
	global time
	global count
	global score
	global countword
	if time > 0:
		e.focus_set()
		if e.get().lower() == countword.lower():     
			score = score + 1
		e.delete(0, tkinter.END)
		random.shuffle(words)
		word = words[0]
		for char in word:
			count = count + 1
		countword = p.number_to_words(count)
		count = 0
		label.config(fg = 'Black', text = word, font = ('Arial', 35))
		ScoreLabel.config(text = 'Score: ' + str(score))
	

def countdown():
	global time
	global count
	global score
	if time > 0:
		time = time - 1
		TimeLabel.config(text = 'Time Left: ' + str(time))
		TimeLabel.after(1000, countdown)
	else:
		e.delete(0, tkinter.END)
		NoteLabel.config(text = "Game Over", font = ('Arial', 12))
		ScoreLabel.config(text = 'Score:' + str(score))
		label.config(text = "")
window = tkinter.Tk()
window.geometry('400x400')
window.title('Count the Letters')
NoteLabel = tkinter.Label(window, text = "Type the number of letters in text", font = ('Arial', 12))
NoteLabel.pack()
TimeLabel = tkinter.Label(window, text = 'Time Left: ' + str(time) , font = ('Arial', 12))
TimeLabel.pack()
ScoreLabel = tkinter.Label(window, text = 'Score:' + str(score) , font = ('Arial', 12))
ScoreLabel.pack()
label = tkinter.Label(window, font = ('Arial', 12))
label.pack()

e = tkinter.Entry(window)
window.bind('<Return>', start)
e.pack()
e.focus_set()
window.mainloop()