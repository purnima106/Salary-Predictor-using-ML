from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import	LinearRegression

root = Tk()
root.title("Salary Predictor")
root.geometry("500x500+100+100")
root.configure(bg = "lightblue")
f = ("cambria" , 30 , "bold")

lab_header = Label(root, text = "Salary Predictor", font = f)
lab_header.pack(pady = 20)

def find():
	try:
		data = pd.read_csv("C:/Users/Purnima/OneDrive/Desktop/ML2/esmsep23.csv")
		feature = data[["exp"]]
		target = data["sal"]
		x_train, x_test, y_train,y_test = train_test_split(feature, target, random_state = 1)
		model = LinearRegression()
		model.fit(x_train, y_train)
		exp = float(ent_exp.get())
		sal = model.predict([[exp]])
		msg = "salary = " + str(round(sal[0], 2)) + "K"
		lab_sal.configure(text=msg)
	except ValueError:
		msg = "Only numbers expected"
		lab_sal.configure(text=msg)
		
lab_exp = Label(root, text = "Enter experience ", font = f)
ent_exp = Entry(root, font = f)
btn_pre = Button(root, text="Predict Salary",foreground = "white",background="black",font = f,command=find)
lab_sal = Label(root, font = f)
lab_exp.pack(pady = 10)
ent_exp.pack(pady = 10)
btn_pre.pack(pady=10)
lab_sal.pack(pady = 10)

root.mainloop()