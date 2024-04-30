CREATE TABLE clinic_room (
  clinic_room_id INT PRIMARY KEY,
  room_number INT
);


CREATE TABLE patient (
  patient_id INT PRIMARY KEY,
  patient_first_name VARCHAR(255) NOT NULL,
  patient_last_name VARCHAR(255) NOT NULL,
  phone_number VARCHAR(255)
);

CREATE TABLE dentist (
  dentist_id INT PRIMARY KEY,
  dentist_first_name VARCHAR(255) NOT NULL,
  dentist_last_name VARCHAR(255) NOT NULL
);

CREATE TABLE appointment (
  clinic_room_id INT,
  patient_id INT,
  dentist_id INT,
  appointment_date DATE,
  appointment_time TIME,
  FOREIGN KEY (clinic_room_id) REFERENCES clinic_room(clinic_room_id),
  FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
  FOREIGN KEY (dentist_id) REFERENCES Dentist(dentist_id)
);


insert into clinic_room (clinic_room_id, room_number)
values (1, 1);
insert into clinic_room (clinic_room_id, room_number)
values (2, 2);
insert into clinic_room (clinic_room_id, room_number)
values (3, 3);


INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (1, 'Aaron', 'Anthony');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (2, 'Brandon', 'Barry');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (3, 'Cole', 'Cook');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (4, 'Donte', 'Divincenzo');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (5, 'Edward', 'Edwards');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (6, 'Franklin', 'Fox');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (7, 'Gideon', 'Garrett');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (8, 'Harry', 'Harrison');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (9, 'Inigo', 'Ingram');
INSERT INTO dentist (dentist_id, dentist_first_name, dentist_last_name) 
VALUES (10, 'Jackson', 'Jackson');

