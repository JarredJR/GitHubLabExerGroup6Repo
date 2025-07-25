IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'StudentDB')
    DROP DATABASE StudentDB;
GO
CREATE DATABASE StudentDB;
GO

USE StudentDB;
GO


CREATE TABLE dbo.Person (
    Person_ID     INT IDENTITY(1,1) PRIMARY KEY,
    LastName      NVARCHAR(100) NOT NULL,
    GivenName     NVARCHAR(100) NOT NULL,
    MiddleName    NVARCHAR(100) NULL
);
GO

CREATE TABLE dbo.Program (
    Program_ID           INT IDENTITY(1,1) PRIMARY KEY,
    ProgramDescription   NVARCHAR(200) NOT NULL
);
GO

CREATE TABLE dbo.Student (
    Student_ID     INT IDENTITY(1,1) PRIMARY KEY,
    StudentNumber  CHAR(10)     NOT NULL UNIQUE,
    Year           TINYINT      NOT NULL CHECK (Year BETWEEN 1 AND 5),
    Person_ID      INT          NOT NULL,
    Program_ID     INT          NOT NULL,
    CONSTRAINT FK_Student_Person  FOREIGN KEY (Person_ID)  REFERENCES dbo.Person(Person_ID),
    CONSTRAINT FK_Student_Program FOREIGN KEY (Program_ID) REFERENCES dbo.Program(Program_ID)
);
GO


CREATE PROCEDURE dbo.AddPerson
    @LastName      NVARCHAR(100),
    @GivenName     NVARCHAR(100),
    @MiddleName    NVARCHAR(100) = NULL,
    @NewPersonID   INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO dbo.Person (LastName, GivenName, MiddleName)
    VALUES (@LastName, @GivenName, @MiddleName);

    SET @NewPersonID = SCOPE_IDENTITY();
END;
GO

CREATE PROCEDURE dbo.EditPerson
    @PersonID      INT,
    @LastName      NVARCHAR(100),
    @GivenName     NVARCHAR(100),
    @MiddleName    NVARCHAR(100) = NULL
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE dbo.Person
       SET LastName   = @LastName,
           GivenName  = @GivenName,
           MiddleName = @MiddleName
     WHERE Person_ID = @PersonID;
END;
GO

CREATE PROCEDURE dbo.DeletePerson
    @PersonID INT
AS
BEGIN
    SET NOCOUNT ON;
    DELETE FROM dbo.Person
     WHERE Person_ID = @PersonID;
END;
GO

CREATE PROCEDURE dbo.ViewPerson
    @PersonID INT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT Person_ID, LastName, GivenName, MiddleName
      FROM dbo.Person
     WHERE Person_ID = @PersonID;
END;
GO

CREATE PROCEDURE dbo.AddProgram
    @ProgramDescription NVARCHAR(200),
    @NewProgramID       INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO dbo.Program (ProgramDescription)
    VALUES (@ProgramDescription);

    SET @NewProgramID = SCOPE_IDENTITY();
END;
GO

CREATE PROCEDURE dbo.EditProgram
    @ProgramID          INT,
    @ProgramDescription NVARCHAR(200)
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE dbo.Program
       SET ProgramDescription = @ProgramDescription
     WHERE Program_ID = @ProgramID;
END;
GO

CREATE PROCEDURE dbo.DeleteProgram
    @ProgramID INT
AS
BEGIN
    SET NOCOUNT ON;
    DELETE FROM dbo.Program
     WHERE Program_ID = @ProgramID;
END;
GO

CREATE PROCEDURE dbo.ViewProgram
    @ProgramID INT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT Program_ID, ProgramDescription
      FROM dbo.Program
     WHERE Program_ID = @ProgramID;
END;
GO

CREATE PROCEDURE dbo.AddStudent
    @StudentNumber CHAR(10),
    @Year          TINYINT,
    @PersonID      INT,
    @ProgramID     INT,
    @NewStudentID  INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    IF NOT EXISTS (SELECT 1 FROM dbo.Person  WHERE Person_ID = @PersonID)
        THROW 51000, 'Person_ID does not exist.', 1;

    IF NOT EXISTS (SELECT 1 FROM dbo.Program WHERE Program_ID = @ProgramID)
        THROW 51001, 'Program_ID does not exist.', 1;

    INSERT INTO dbo.Student (StudentNumber, Year, Person_ID, Program_ID)
    VALUES (@StudentNumber, @Year, @PersonID, @ProgramID);

    SET @NewStudentID = SCOPE_IDENTITY();
END;
GO

CREATE PROCEDURE dbo.EditStudent
    @StudentID     INT,
    @StudentNumber CHAR(10),
    @Year          TINYINT,
    @ProgramID     INT
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE dbo.Student
       SET StudentNumber = @StudentNumber,
           Year          = @Year,
           Program_ID    = @ProgramID
     WHERE Student_ID = @StudentID;
END;
GO

CREATE PROCEDURE dbo.DeleteStudent
    @StudentID INT
AS
BEGIN
    SET NOCOUNT ON;
    DELETE FROM dbo.Student
     WHERE Student_ID = @StudentID;
END;
GO

CREATE PROCEDURE dbo.ViewStudent
    @StudentID INT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT Student_ID, StudentNumber, Year, Person_ID, Program_ID
      FROM dbo.Student
     WHERE Student_ID = @StudentID;
END;
GO

CREATE PROCEDURE dbo.ViewStudentDetailed
    @StudentID INT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        p.LastName,
        p.GivenName,
        p.MiddleName,
        s.StudentNumber,
        pr.ProgramDescription AS Program,
        s.Year
    FROM dbo.Student s
    JOIN dbo.Person  p ON s.Person_ID  = p.Person_ID
    JOIN dbo.Program pr ON s.Program_ID = pr.Program_ID
    WHERE s.Student_ID = @StudentID;
END;
GO

CREATE PROCEDURE dbo.DeleteStudentDetailed
    @StudentID INT
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @pid INT;

    SELECT @pid = Person_ID
      FROM dbo.Student
     WHERE Student_ID = @StudentID;

    IF @pid IS NULL
        THROW 51002, 'Student_ID does not exist.', 1;

    DELETE FROM dbo.Student
     WHERE Student_ID = @StudentID;

    DELETE FROM dbo.Person
     WHERE Person_ID = @pid;
END;
GO
