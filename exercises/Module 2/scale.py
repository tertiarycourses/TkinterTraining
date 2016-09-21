from tkinter import *

root = Tk()

def main():
	w = Scale(root,from_= 0,to = 100, orient = HORIZONTAL, command = update)
	w.pack()
	root.mainloop()

def update(duty):
	pass
	#pwm.ChangeDutyCycle(float(duty))

if __name__ == "__main__":main()
