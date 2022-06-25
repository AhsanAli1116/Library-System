from database import read_file
import matplotlib.pyplot as plt

# -------------------Loading Data-----------------------------
log=read_file("logfile.txt",'r')
content=read_file("database.txt",'r')

logids=[ids[1] for ids in log]
titles=[title[1] for title in content]
pop=[]
for logid in logids:
    pop.append(titles[int(logid)])

uniquetitles=list(set(titles))
dic={}
for book in uniquetitles:
    dic[book]=(pop.count(book))/2


# -----------------Plotting-----------------
plt.pie(dic.values(),labels=dic.keys())
plt.title("Popularity Chart")
plt.show()