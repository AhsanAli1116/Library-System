from database import *


# ----------------getting Data From User----------------------
book_id=input("Enter Book_id")
issue_date=input("Enter Issue Date day/month/year")
return_date=input("Enter Return Date day/month/year")


# ------------------calling function------------------------

bookreturn(book_id,issue_date,return_date,"database.txt",'r')