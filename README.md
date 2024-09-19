Tiny Library DataBase.  

PROJECT STRUCTURE:

 LibraryDB.py           # Main script to create tables, populate data, and run queries
 Fake_Data_Generator.py  # Contains functions to generate fake data for authors and books 
 queries.py              # SQL queries used in the project
 requirements.txt        # List of dependencies to install
 README.md               # Project documentation
 .gitignore              # Git ignore file


Features:

- Store information about authors (name, surname, birthdate, birthplace).
- Store information about books (title, category, number of pages, publication date, and author).
- Perform queries such as:
  1. Finding the book with the most pages.
  2. Calculating the average number of pages in all books.
  3. Retrieving the youngest author.
  4. Listing authors who do not have books.
  5. Finding authors with more than 3 books.
- Use fake data generation to simulate a large dataset of authors and books for testing.



Installation:

CLONE REPOSITORY
git clone https://github.com/GogaladzeNodar/SQLiteLibrary.git 

CREATE VIRTUALENVIRONMENT
python -m venv venv
source venv/bin/activate  for MAC
venv\Scripts\activate  for Windows


INSTALL PYTHON PACKAGES
pip3 install -r requirements.txt   FOR MAC



RUN CODE
python Library_DB.py


