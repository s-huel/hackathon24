USE `Lerend_Kwalificeren`;

-- Insert into Admin table
INSERT INTO `Admin` (`AdminID`, `Email`, `Password`, `FirstName`, `LastName`, `DateOfBirth`) 
VALUES
(1, 'admin@rijnijssel.nl', 'admin', 'John', 'Doe', '1999-01-01');

-- Insert into Teacher table
INSERT INTO `Teacher` (`TeacherID`, `Email`, `Password`, `FirstName`, `LastName`, `DateOfBirth`, `Picture`, `LBC`, `PO`) 
VALUES
('T001', 'teacher@rijnijssel.nl', 'teacher', 'Jane', 'Doe', '1999-01-01', NULL, TRUE, TRUE);

-- Insert into Class table
INSERT INTO `Class` (`Classnumber`, `Name`, `TeacherID`, `Cohort`, `StartYear`, `Kwebbelcode`) 
VALUES
(1, 'LBC1', 'T001', 1, 2020, 25604);

-- Insert into Student table
INSERT INTO `Student` (`Studentnumber`, `Email`, `Password`, `FirstName`, `LastName`, `DateOfBirth`, `Picture`, `Classnumber`) 
VALUES
(1, 'student@rijnijssel.nl', 'student', 'Joke', 'Doe', '1999-01-01', NULL, 1);
