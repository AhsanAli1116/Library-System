from database import *


# ----------------getting Data From User----------------------
member_id=input("Enter Member_ID")
while not( member_id.isdigit() and len(member_id)==4):
    member_id=input("Enter Valid Member_ID")
book_id=input("Book_id")
date=input("Enter Date day/month/year")


# ------------------calling function--------------------------

bookcheckout(member_id,book_id,date,'database.txt','r')