import logfile 


# -----------------------------File Reader---------------------------

# this function read content from file and store it in list
def read_file(path,mode):
    file=open(path,mode)
    content=[each.split(",") for each in file]
    file.close()
    return content


# --------------------------File Updater------------------------------

# this function concate the data to  update  the file
def updater(content):
    lst=[data[0]+','+data[1]+','+data[2]+','+data[3]+','+data[4] for data in content]
    file=open("database.txt","w")
    file.writelines(lst)
    file.close()


# ---------------------------searching ----------------------------

# this function allow user to search book by its title
def booksearch(title):
    con=read_file("database.txt","r")
    books=[i[:-1] for i in con if i[1]==title]
    return books
    # ret
    # for i in con:
    #     if i[1]==title:
    #         booksi[:-1])
        


# --------------------------Checkout--------------------------------



#this function update the data after checkingout of book 
def bookcheckout(member_id,book_id,date,path,mode):
    con=read_file(path,mode)
    if con[(int(book_id)-1)][-2]=='0':
        con[(int(book_id)-1)][-2]=member_id
       
        updater(con)
        #updating the log file on checkingout the book
        logfile.checkout(book_id,member_id,date,logfile.transcation_id)
        print("Withdraw SuccessFully")
    else:
        print("Already Borrowed")
    
    
  



# ----------------------------Returning---------------------------------

#function to update data on return the book
def bookreturn(book_id,content,issuedate,returndate,path,mode):
    con=read_file(path,mode)
    if con[(int(book_id)-1)][-2] != '0':
        member_id=con[(int(book_id)-1)][-2]
        con[(int(book_id)-1)][-2]='0'
        print("Return SuccessFully")
        updater(con)
        logfile.returning(book_id,member_id,issuedate,returndate,logfile.transcation_id)
    else: 
        print("Error Book is Already in Library")
        