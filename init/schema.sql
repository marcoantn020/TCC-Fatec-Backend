DROP DATABASE `app`;
CREATE DATABASE `app`;
USE app;


CREATE TABLE IF NOT EXISTS  `app`.`patient` (
   id_patient INT AUTO_INCREMENT PRIMARY KEY,
   username VARCHAR(200),
   password VARCHAR(200),
   is_admin BOOLEAN,
   is_active BOOLEAN,
   first_name VARCHAR (80),
   last_name VARCHAR (200),
   birth_date DATETIME,
   genre char(1),
   email VARCHAR (200),
   zipcode VARCHAR (10),
   city VARCHAR (50),
   street VARCHAR (140),
   number VARCHAR (5),
   district VARCHAR (100),
   practice_activity BOOLEAN,
   what_activity VARCHAR (100),
   created_at DATETIME,
   updated_at DATETIME
) ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS  `app`.`medical_consultation` (
   id_medical_consultation INT AUTO_INCREMENT PRIMARY KEY,
   id_patient INT,
   id_pathology INT,
   left_foot_professional_observation VARCHAR(50),
   right_foot_professional_observation VARCHAR(50),
   type_pressure_left_foot VARCHAR(3),
   type_pressure_right_foot VARCHAR(3),
   left_foot_mono_filament_test VARCHAR(150),
   right_foot_mono_filament_test VARCHAR(150),
   left_foot_dermatological_pathology VARCHAR(150),
   right_foot_dermatological_pathology VARCHAR(150),
   pathology_present_in_nail_left_foot VARCHAR(150),
   pathology_present_in_nail_right_foot VARCHAR(150),
   performed_procedure TEXT,
   date_of_scheduling DATETIME,
   consultation_completed BOOLEAN,
   date_consultation_completed DATETIME,
   date_unchecked DATETIME,
   consultation_unchecked BOOLEAN
) ENGINE=INNODB;


CREATE TABLE IF NOT EXISTS  `app`.`pathology` (
   id_pathology INT AUTO_INCREMENT PRIMARY KEY,
   id_patient INT,
   has_diabetes BOOLEAN,
   observations_diabetes TEXT,
   have_hypertension BOOLEAN,
   observations_hypertension TEXT,
   take_medicines BOOLEAN,
   observations_medicines TEXT,
   allergic_to_medicine BOOLEAN,
   which_medicine VARCHAR(254),
   have_cancer BOOLEAN,
   which_type_cancer VARCHAR(254),
   has_pacemaker BOOLEAN,
   has_pin BOOLEAN,
   is_cadiaco BOOLEAN,
   have_foot_surgery BOOLEAN,
   which_foot VARCHAR(200),
   about_the_foot_of_the_patient_has_callus BOOLEAN,
   about_the_foot_of_the_patient_has_callosity BOOLEAN,
   about_the_foot_of_the_patient_has_fissure BOOLEAN,
   about_the_foot_of_the_patient_has_dryness BOOLEAN,
   about_the_foot_of_the_patient_has_psoriasis BOOLEAN,
   about_the_foot_of_the_patient_has_pantar_wart BOOLEAN,
   about_the_nail_of_the_patient_has_onychocryptosis BOOLEAN,
   about_the_nail_of_the_patient_has_onycholysis BOOLEAN,
   about_the_nail_of_the_patient_has_onychomycosis BOOLEAN,
   about_the_nail_of_the_patient_has_onychophoresis BOOLEAN,
   sensitive_to_pain VARCHAR(30),
   type_of_sock VARCHAR(150),
   type_of_shoe VARCHAR(150),
   shoe_number VARCHAR(3),
   created_at DATETIME,
   updated_at DATETIME
) ENGINE=INNODB;


 ALTER TABLE medical_consultation ADD FOREIGN KEY(id_patient) REFERENCES patient(id_patient);
 ALTER TABLE medical_consultation ADD FOREIGN KEY(id_pathology) REFERENCES pathology(id_pathology);
 ALTER TABLE pathology ADD FOREIGN KEY(id_patient) REFERENCES patient(id_patient);

INSERT INTO patient (username, password, is_admin) VALUES ("marco", "$2b$08$tWHGxUW0WueOUoE5rA3ijOkpH1nPUdzAqOiYQD4wnCOxvlNbNYHSe", true);