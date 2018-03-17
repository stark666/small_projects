#coding=utf-8
#添加GUI
from Tkinter import *
import re

root=Tk()
root.title('sudoku')
root.geometry('320x400+30+30')


class point():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.available=[]
		self.value=0

def rownum(p,sudoku):       #行已知数字
	row=set(sudoku[p.y])
	row.remove(0)
	return row

def colnum(p,sudoku):   #列已知数字
	col=[]
	for item in sudoku:
		col.append(item[p.x])
	col=set(col)
	col.remove(0)
	return col

def block(p,sudoku):      #3*3区域内已知数字
	block=[]
	for i in range(3):
		for j in range(3):
			block.append(sudoku[p.y/3*3+i][p.x/3*3+j])
	block=set(block)
	block.remove(0)
	return block

def initpoint(sudoku):         #所有空白区域可填充的数字
	pointlist=[]
	for index_row,item_row in enumerate(sudoku):
		for index_col,item_col in enumerate(item_row):
			if item_col==0:
				p=point(index_col,index_row)
				for j in range(1,10):
					if j not in rownum(p,sudoku) and j not in colnum(p,sudoku) and j not in block(p,sudoku):
						p.available.append(j)
				pointlist.append(p)
	return pointlist

def check(p,sudoku):       #检测是否符合数独规则
	if p.value not in rownum(p,sudoku) and p.value not in colnum(p,sudoku) and p.value not in block(p,sudoku):
		return True
	else:
		return False

def show(sudoku):            
	for item in sudoku:
		for i in item:
			print i,
		print ''

def tryinsert(p,sudoku):            #核心，优化的穷举法，使用迭代
	#pointlist=initpoint(sudoku)
	for value in p.available:
		p.value=value
		if check(p,sudoku):
			sudoku[p.y][p.x]=p.value
			if len(pointlist)==0:
				print ''
				show(sudoku)
				for i in range(9):
					for j in range(9):
						num[i][j].set(sudoku[i][j])
				return


			p2=pointlist.pop()
			tryinsert(p2,sudoku)
			sudoku[p.y][p.x]=0
			pointlist.append(p2)
		else:
			pass




def get_sudoku(num):
	global pointlist
	for i in range(9):
		if i<8:
			sudoku.append([])
		for j in range(9):
			if num[i][j].get()=='':
				sudoku[i].append(0)
			else:
				sudoku[i].append(int(num[i][j].get()))
	show(sudoku)
	pointlist=initpoint(sudoku)
	p=pointlist.pop()
	tryinsert(p,sudoku)
#	
#	print sudoku_2
#	for i in range(9):
#		for j in range(9):
#			num[i][j].set(sudoku[i][j])
	#return sudoku
	




if __name__=='__main__':

	sudoku=[[]]
	num=[[]]
	for i in range(9):
	#	sudoku.append([])
		num.append([])
		for j in range(9):
			num[i].append([])
			num[i][j]=StringVar()
			num[i][j].set('')
			#sudoku[i].append(Entry(root,width=3,font = ('Helvetica', '16', 'bold'),textvariable=num[i][j]).place(x=20+30*j+5*(j/3),y=20+30*i+5*(i/3),width=30,height=30))
			Entry(root,width=3,font = ('Helvetica', '16', 'bold'),textvariable=num[i][j]).place(x=20+30*j+5*(j/3),y=20+30*i+5*(i/3),width=30,height=30)

	Button(root,text='sudoku',font = ('Helvetica', '16', 'bold'),command=lambda: get_sudoku(num)).place(x=20,y=320,width=280,height=60)

	#sudoku=get_sudoku(num)

	mainloop()
