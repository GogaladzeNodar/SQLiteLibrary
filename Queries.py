"""
იპოვეთ და დაბეჭდეთ ყველაზე მეტი გვერდების მქონე წიგნის ყველა ველი
იპოვეთ და დაბეჭდეთ წიგნების საშუალო გვერდების რაოდენობა
დაბეჭდეთ ყველაზე ახალგაზრდა ავტორი
დაბეჭდეთ ისეთი ავტორები რომელსაც ჯერ წიგნი არ აქვს

ბონუს დავალება:
იპოვეთ ისეთ 5 ავტორი რომელსაც 3 ზე მეტი წიგნი აქვს
"""

BOOK_WITH_THE_MOST_PAGES = """
SELECT id, authorid, bookname, category, pagenumber, publicationdate
FROM Book 
WHERE pagenumber = (SELECT MAX(pagenumber) from Book);
"""


AVERAGE_BOOK_PAGES = """
SELECT AVG(pagenumber) FROM Book;
"""

YOUNGEST_AUTHOR = """
SELECT * FROM Author
WHERE  birthdate = (SELECT MAX(birthdate) FROM Author);
"""


AUTHORS_WHO_DO_NOT_HAVE_BOOKS_YET = """
SELECT Author.*
FROM Author
LEFT JOIN Book ON Author.id = Book.authorid
WHERE Book.id IS NULL;
"""


AUTHORS_WHO_HAVE_MORE_THEN_3_BOOKS = """
SELECT Author.id, Author.authorname, COUNT(Book.id) AS book_count
from Author
INNER JOIN Book ON Author.id = Book.authorid
GROUP BY Author.id, Author.authorname
HAVING COUNT(Book.id) > 3
LIMIT 5; 
"""
