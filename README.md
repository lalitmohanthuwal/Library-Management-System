Overview
A Python-based library management system with a graphical user interface (GUI) built using Tkinter. The system allows librarians to manage books, track issues, and handle returns through an intuitive interface.

Features
Book Management: Add, view, and delete books from the library

Issue Tracking: Record which books are issued to students

Return Processing: Handle book returns and update availability status

User-Friendly Interface: Simple GUI with clear navigation

Prerequisites
Python 3.x

MySQL Server

Required Python packages:

Copy
pip install pymysql cryptography pillow
Installation
Clone the repository:

Copy
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
Set up the database:

Create a MySQL database named library

Run the following SQL commands to create the necessary tables:

sql
Copy
CREATE TABLE books (
    bid VARCHAR(20) PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    status VARCHAR(20)
);

CREATE TABLE books_issued (
    bid VARCHAR(20) PRIMARY KEY,
    issueto VARCHAR(50)
);
Configure database access:

Update the connection details in each Python file (or create a central configuration file)

Default credentials:

python
Copy
mypass = "lalit"
mydatabase = "library"
Usage
Run the main application:

Copy
python main.py
Main Menu Options
Add Book: Enter new book details (ID, Title, Author, Status)

Delete Book: Remove a book by its ID

View Books: See all books in the library

Issue Book: Record when a book is issued to a student

Return Book: Process book returns

File Structure
Copy
library-management-system/
│── main.py                # Main application entry point
│── AddBook.py             # Add new books functionality
│── DeleteBook.py          # Remove books functionality
│── ViewBooks.py           # Display all books
│── IssueBook.py           # Book issuing system
│── ReturnBook.py          # Book return processing
│── image.webp             # Background image for main window
│── README.md              # This file
Troubleshooting
MySQL Connection Errors:

Verify MySQL server is running

Check username/password in connection settings

Install cryptography package: pip install cryptography

GUI Display Issues:

Ensure all required packages are installed

Check image file path in main.py

Contributing
Contributions are welcome! Please fork the repository and submit pull requests.
#   L i b r a r y - M a n a g e m e n t - S y s t e m  
 