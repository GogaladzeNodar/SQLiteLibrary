from faker import Faker
import random

fake = Faker()
MAX_PAGE_NUMBER = 5000


# For Capitalization
def capitalize_name(value):
    return value.title()


# for Authors
def generate_fake_authors(cursor, n):
    for _ in range(n):
        authorname = capitalize_name(fake.first_name())
        authorsurname = capitalize_name(fake.last_name())
        birthdate = fake.date_of_birth().isoformat()
        birthplace = capitalize_name(fake.city())

        cursor.execute(
            """INSERT INTO Author (authorname, authorsurname, birthdate, birthplace)
                          VALUES (?, ?, ?, ?)""",
            (authorname, authorsurname, birthdate, birthplace),
        )


# for Books
def generate_fake_books(cursor, n):
    cursor.execute("SELECT id FROM Author")
    author_ids = [row[0] for row in cursor.fetchall()]

    categories = [
        "Fiction",
        "Non-fiction",
        "Science Fiction",
        "Fantasy",
        "Biography",
        "History",
    ]

    for _ in range(n):
        authorid = random.choice(author_ids)
        bookname = capitalize_name(fake.catch_phrase())
        category = random.choice(categories)
        pagenumber = random.randint(1, MAX_PAGE_NUMBER)
        publicationdate = fake.date_between(
            start_date="-100y", end_date="today"
        ).isoformat()

        cursor.execute(
            """INSERT INTO Book (authorid, bookname, category, pagenumber, publicationdate)
                          VALUES (?, ?, ?, ?, ?)""",
            (authorid, bookname, category, pagenumber, publicationdate),
        )
