# from os import truncate
from database import booksearch


# ----------------getting Data From User----------------------

title=input("Enter The title of Required Book ==>===>")

# ------------------calling function--------------------------

books=booksearch(title)
for book in books:
    print(f"id={book[0]}\ntitle={book[1]}\nAuthor={book[2]}\nMember_id={book[3]}\n------------------------------")