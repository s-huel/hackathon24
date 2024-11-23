USE `Lerend_Kwalificeren`;

-- Insert into Admin table
INSERT INTO `Admin` (`AdminID`, `Email`, `Password`, `FirstName`, `LastName`, `DateOfBirth`) 
VALUES
(1, 'felix.huel@gmail.com', 'admin', 'Felix', 'Huel', '1999-01-01'),
(2, 'mehdiek@outlook.com', 'shark', 'Shark', 'The Great White', '1999-01-01');

-- Insert into Teacher table
INSERT INTO `Teacher` (`TeacherID`, `Email`, `Password`, `FirstName`, `LastName`, `DateOfBirth`, `Picture`, `LBC`, `PO`) 
VALUES
('GRESH', 'mehdiek@outlook.com', 'shark', 'Shark', 'The Great White', '1999-01-01', NULL, TRUE, TRUE);

-- Insert into Class table
INSERT INTO `Class` (`Classnumber`, `Name`, `TeacherID`, `Cohort`, `StartYear`, `Crebcode`) 
VALUES
(1, 'LBC1', 'GRESH', 1, 2020, 25604);

-- Insert into Student table
INSERT INTO `Student` (`Studentnumber`, `Email`, `Password`, `FirstName`, `LastName`, `DateOfBirth`, `Picture`, `Classnumber`, `Voortgang`) 
VALUES
(1, 'mehdiek03@gmail.com', 'student', 'Mehdi', 'El Khallouki', '1999-01-01', NULL, 1, 50);
