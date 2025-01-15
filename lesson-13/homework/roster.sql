-- Create the Roster table
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);
-- Insert the given data into the Roster table
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);

-- Update the Name of Jadzia Dax to Ezri Dax
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';

-- Retrieve and display the Name and Age of all characters where the Species is Bajoran
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';

-- Remove all characters aged over 100 years from the table
DELETE FROM Roster
WHERE Age > 100;

-- Add a new column for Rank
ALTER TABLE Roster
ADD COLUMN Rank TEXT;

-- Update Rank values for the characters
UPDATE Roster
SET Rank = 'Captain'
WHERE Name = 'Benjamin Sisko';

UPDATE Roster
SET Rank = 'Lieutenant'
WHERE Name = 'Ezri Dax';

UPDATE Roster
SET Rank = 'Major'
WHERE Name = 'Kira Nerys';

-- Retrieve all characters sorted by their Age in descending order
SELECT * FROM Roster
ORDER BY Age DESC;

