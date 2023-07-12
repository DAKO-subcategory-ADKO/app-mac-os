
from tkinter import *
import webview

tk = Tk()

a = "DAKO"

webview.create_window( '.:: DAKO System ::.', '../4.html',width=956,height=999,resizable=False,x=68, y=0, )
webview.start()