CREATE TABLE Doctors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName text,
    lastName text,
    gender text,
    speciality text,
    hospitalName text,
    city text,
    fees INTEGER
);

CREATE TABLE Loc(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idF INTEGER,
    area text,
    FOREIGN KEY("idF") REFERENCES "Doctors"("id") ON DELETE CASCADE
);

CREATE TABLE patient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName text,
    lastName text,
    username text UNIQUE,
    passcode text,
    phone INTEGER,
    age INTEGER,
    gender text
);

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Ahmed', 'Yasser', 'Male', 'dentistry', 'AL_GALA', 'Cairo', '500');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Seif', 'Hossam', 'Male', 'Neurology', 'Tiba', 'Giza', '700');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Rawan', 'Nasser', 'Female', 'Diabetes', 'AL_GALA', 'Cairo', '800');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Ola','sherief','female','cardiology and vascular disease','Ain_El_Hayah','Cairo','460');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Ahmed','Nour','male','chest and respiratory','Ganzory','Cairo','550');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Ziad','Amr','male','Dermatology','Bahia','Cairo','290');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('youssif','Mohmed','male','Gynaecology and infertility','Celopatra','Cairo','300');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Noha','Abdelbary','Female','Dietitian and Nutrition','Ain_Shames','Cairo','500');

INSERT INTO Doctors (firstName, lastName, gender, speciality, hospitalName, city, fees)
VALUES ('Alaa','Ahmed','Female','Orthopedics','Celopatra','Cairo','450');

