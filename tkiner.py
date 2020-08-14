from tkinter import *
from tkinter import messagebox
import tweepy
consumer_key = "nR2UYn7Ra0tAXA0vOSik4BsTL"
consumer_secret = "s1PbtuQfCl7TD9hrf9u9BG8u0jadMBmZnyE41UWSdWbuni4SQj"
access_token = "395936666-QJCwbLQWzthaaolNgCrmlHh4NqZbPHJsKu5pYm3E"
access_key = "NpsfOuSBvPVPpYYD1rO6LiSTRvMn7fz6HP6zgWY7JCFhV"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_key)
api = tweepy.API(auth)
class MyWindow:
	def __init__(self,win):
		self.name=Label(win,text='WELCOME TO TWITTER BOT ',fg='blue',font=("Castellar",20))
		self.name.place(x=150,y=50)
		self.var = StringVar()
		self.var1 = StringVar()
		self.var2 = StringVar()
		self.var3 = StringVar()
		self.txtfld=Entry( text="Enter Hashtag",bd=5,textvariable=self.var)
		self.txtfld.place(x=150,y=150)
		self.lbl1=Label(win,text='Enter Hashtag',fg='black')
		self.lbl1.place(x=50,y=150)
		self.lbl2=Label(win,text='Enter no of tweets',fg='black')
		self.lbl2.place(x=300,y=150)
		self.txtfld1=Entry( text="Enter no of tweets1",bd=5,textvariable=self.var1)
		self.txtfld1.place(x=425,y=150)
		self.btn1=Button(win,text='Hit to Like',bg='blue',command=self.hashtag_used)
		self.btn1.place(x=290,y=200)
		self.txtfld2=Entry(text="Enter Username",bd=5,textvariable=self.var2)
		self.txtfld2.place(x=150,y=250)
		self.lbl3=Label(win,text='Enter Username',fg='black')
		self.lbl3.place(x=50,y=250)
		self.lbl4=Label(win,text='Enter no of tweets',fg='black')
		self.lbl4.place(x=300,y=250)
		self.txtfld3=Entry(text="Enter no of tweets2",bd=5,textvariable=self.var3)
		self.txtfld3.place(x=425,y=250)
		self.btn2=Button(win,text='Hit to like',bg='blue',command=self.user_timeline)
		self.btn2.place(x=290,y=300)
	def user_timeline(self):
		search=self.txtfld2.get()
		value=int(self.txtfld3.get())
		print('user based is called',search,value)
		for i in tweepy.Cursor(api.user_timeline, id=search).items(value):
		    try:
		        print('liked')
		        i.favorite()
		    except tweepy.TweepError as e:
		        print(e.reason)
		    except StopIteration:
		        break
		self.var2.set("")
		self.var3.set("")
		messagebox.showinfo('info','Done')
	def hashtag_used(self):
		print('xyz')
		search=self.txtfld.get()
		value=int(self.txtfld1.get())
		print('hashtag is called',search,value)
		for i in tweepy.Cursor(api.search,search).items(value):
		    try:
		        print('liked')
		        i.favorite()
		    except tweepy.TweepError as e:
		        print(e.reason)
		    except StopIteration:
		        break
		self.var.set("")
		self.var1.set("")
		messagebox.showinfo('info','Done')
window=Tk()
mywin=MyWindow(window)
window.title('TWITTER BOT')
window.geometry("700x400+10+20")
window.mainloop()