# function that generate transcation_id
def transcation_id(file):
    log_content=[each.split(",") for each in file]
    if len(log_content)==0:
        return 1
    else:
        transcation= int(log_content[-1][0])
        return (transcation+1)

# function that update logfile of checkingout the book
def checkout(book_id,member_id,date,transaction_id):  
    log=open("logfile.txt","r+")
    log.write(str(transaction_id(log))+','+book_id+','+date+','+member_id+"\n")
    log.close()

# function that update logfile on returning the book
def returning(book_id,member_id,issuedate,returndate,transaction_id):
    log=open("logfile.txt","r+")
    log.write(str(transaction_id(log))+','+book_id+','+issuedate+','+returndate+','+member_id+"\n")
    log.close()

