import sqlite3
from Fake_Data_Generator import generate_fake_authors, generate_fake_books
import Queries


conn = sqlite3.connect("library_db.sqlite3")
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

# Author table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Author(
                    id  INTEGER PRIMARY KEY,
                    authorname TEXT NOT NULL,
                    authorsurname TEXT,
                    birthdate TEXT,
                    birthplace TEXT 
                )"""
)


# Book table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Book(
               id INTEGER PRIMARY KEY,
               authorid INTEGER,
               bookname TEXT NOT NULL,
               category TEXT,
               pagenumber INTEGER CHECK (pagenumber >= 1), 
               publicationdate TEXT NOT NULL,
               FOREIGN KEY (authorid) REFERENCES Author (id)
            )"""
)

# Commit Changes
conn.commit()


# Fake Authors
generate_fake_authors(cursor, 500)

# Fake Books
generate_fake_books(cursor, 1000)


# BOOK_WITH_THE_MOST_PAGES
cursor.execute(Queries.BOOK_WITH_THE_MOST_PAGES)
The_thickest_book = cursor.fetchall()
print(f"The thickest book is {The_thickest_book} \n")


# AVERAGE_BOOK_PAGES
cursor.execute(Queries.AVERAGE_BOOK_PAGES)
average_pages = cursor.fetchone()
print(f"Average page for all books is {average_pages} \n")


# YOUNGEST AUTHOR
cursor.execute(Queries.YOUNGEST_AUTHOR)
young = cursor.fetchone()
print(f"Youngest author is - {young} \n")


# AUTHORS_WHO_DO_NOT_HAVE_BOOKS_YET
cursor.execute(Queries.AUTHORS_WHO_DO_NOT_HAVE_BOOKS_YET)
newbie = cursor.fetchall()
print(f"Authors with no books - {newbie} \n")


# AUTHORS_WHO_HAVE_MORE_THEN_3_BOOKS
cursor.execute(Queries.AUTHORS_WHO_HAVE_MORE_THEN_3_BOOKS)
more_then_3 = cursor.fetchall()
print(f"Authors who have more then 3 book - {more_then_3}")


cursor.close()
conn.close()
