-- Create the Books table
CREATE TABLE Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
);

-- Insert the given data into the Books table
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');

-- Update the Year_Published of 1984 to 1950
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984';

-- Retrieve and display the Title and Author of all books where the Genre is Dystopian
SELECT Title, Author
FROM Books
WHERE Genre = 'Dystopian';

-- Remove all books published before the year 1950 from the table
DELETE FROM Books
WHERE Year_Published < 1950;

-- Add a new column for Rating
ALTER TABLE Books
ADD COLUMN Rating REAL;

-- Update Rating values for the books
UPDATE Books
SET Rating = 4.8
WHERE Title = 'To Kill a Mockingbird';

UPDATE Books
SET Rating = 4.7
WHERE Title = '1984';

UPDATE Books
SET Rating = 4.5
WHERE Title = 'The Great Gatsby';

-- Retrieve all books sorted by their Year_Published in ascending order
SELECT * FROM Books
ORDER BY Year_Published ASC;
