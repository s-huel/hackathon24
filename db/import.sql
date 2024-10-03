DROP DATABASE if EXISTS `Lerend_Kwalificeren`;

CREATE DATABASE `Lerend_Kwalificeren`;

USE `Lerend_Kwalificeren`;

CREATE TABLE `Admin` (
    `AdminID` INT NOT NULL PRIMARY KEY,
    `Email` VARCHAR(255) UNIQUE NOT NULL,
    `Password` VARCHAR(255) NOT NULL,
    `FirstName` VARCHAR(255) NOT NULL,
    `LastName` VARCHAR(255) NULL,
    `DateOfBirth` DATE NOT NULL
);

CREATE TABLE `Teacher` (
    `TeacherID` VARCHAR(5) NOT NULL PRIMARY KEY,
    `Email` VARCHAR(255) UNIQUE NOT NULL,
    `Password` VARCHAR(255) NOT NULL,
    `FirstName` VARCHAR(255) NOT NULL,
    `LastName` VARCHAR(255) NULL,
    `DateOfBirth` DATE NOT NULL,
    `Picture` BLOB NULL,
    `LBC` BOOLEAN DEFAULT FALSE,
    `PO` BOOLEAN DEFAULT FALSE
);

CREATE TABLE `Class` (
    `Classnumber` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Name` VARCHAR(255) NOT NULL,
    `TeacherID` VARCHAR(5) NOT NULL REFERENCES Teacher(TeacherID),
    `Cohort` INT NOT NULL,
    `StartYear` INT NOT NULL,
    `Crebcode` INT NOT NULL
);

CREATE TABLE `Student` (
    `Studentnumber` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Email` VARCHAR(255) UNIQUE NOT NULL,
    `Password` VARCHAR(255) NOT NULL,
    `FirstName` VARCHAR(255) NOT NULL,
    `LastName` VARCHAR(255) NULL,
    `DateOfBirth` DATE NOT NULL,
    `Picture` BLOB NULL,
    `Classnumber` INT NOT NULL REFERENCES Class(Classnumber)
);