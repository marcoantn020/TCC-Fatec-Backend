# API de Podologos

## Projeto de conclusão de curso - Fatec Garça
### Analise e Desenvolvimento de Sistemas

### Database
**patient**
- id_patient: INT AUTO_INCREMENT PRIMARY KEY
- username: VARCHAR(200)
- password: VARCHAR(200)
- is_admin: BOOLEAN
- is_active: BOOLEAN
- first_name: VARCHAR (80)
- last_name: VARCHAR (200)
- birth_date: DATETIME
- genre: char(1)
- email: VARCHAR (200)
- zipcode: VARCHAR (10)
- city: VARCHAR (50)
- street: VARCHAR (140)
- number: VARCHAR (5)
- district: VARCHAR (100)
- practice_activity: BOOLEAN
- what_activity: VARCHAR (100)
- created_at: DATETIME
- updated_at: DATETIME

#
**pathology**
- id_pathology: INT AUTO_INCREMENT PRIMARY KEY
- id_patient: INT
- has_diabetes: BOOLEAN
- observations_diabetes: TEXT
- have_hypertension: BOOLEAN
- observations_hypertension: TEXT
- take_medicines: BOOLEAN
- observations_medicines: TEXT
- allergic_to_medicine: BOOLEAN
- which_medicine: VARCHAR(254)
- have_cancer: BOOLEAN
- which_type_cancer: VARCHAR(254)
- has_pacemaker: BOOLEAN
- has_pin: BOOLEAN
- is_cadiaco: BOOLEAN
- have_foot_surgery: BOOLEAN
- which_foot: VARCHAR(200)
- about_the_foot_of_the_patient_has_callus: BOOLEAN
- about_the_foot_of_the_patient_has_callosity: BOOLEAN
- about_the_foot_of_the_patient_has_fissure: BOOLEAN
- about_the_foot_of_the_patient_has_dryness: BOOLEAN
- about_the_foot_of_the_patient_has_psoriasis: BOOLEAN
- about_the_foot_of_the_patient_has_pantar_wart: BOOLEAN
- about_the_nail_of_the_patient_has_onychocryptosis: BOOLEAN
- about_the_nail_of_the_patient_has_onycholysis: BOOLEAN
- about_the_nail_of_the_patient_has_onychomycosis: BOOLEAN
- about_the_nail_of_the_patient_has_onychophoresis: BOOLEAN
- sensitive_to_pain: VARCHAR(30)
- type_of_sock: VARCHAR(150)
- type_of_shoe: VARCHAR(150)
- shoe_number: VARCHAR(3)
- created_at: DATETIME
- updated_at: DATETIME

#

**medical_consultation**
- id_medical_consultation: INT AUTO_INCREMENT PRIMARY KEY
- id_patient: INT
- id_pathology: INT
- left_foot_professional_observation: VARCHAR(50)
- right_foot_professional_observation: VARCHAR(50)
- type_pressure_left_foot: VARCHAR(3)
- type_pressure_right_foot: VARCHAR(3)
- left_foot_mono_filament_test: VARCHAR(150)
- right_foot_mono_filament_test: VARCHAR(150)
- left_foot_dermatological_pathology: VARCHAR(150)
- right_foot_dermatological_pathology: VARCHAR(150)
- pathology_present_in_nail_left_foot: VARCHAR(150)
- pathology_present_in_nail_right_foot: VARCHAR(150)
- performed_procedure: TEXT
- date_of_scheduling: DATETIME
- consultation_completed: BOOLEAN
- date_consultation_completed: DATETIME
- date_unchecked: DATETIME
- consultation_unchecked: BOOLEAN

#
***
### Levantamento de requisitos

**Problema**
- Atualmente o cadastro de pacientes é feito numa planilha e armazenado em pastas, não so o cadastro mais tambem a consulta é salva desta maneira.
As consultas são marcadas pelo whatsapp, quando uma consulta é realizada uma ficha com detalhes do atendimento é preeenchida, o podologo avisa
o paciente 10 minutos antes da consulta. Cada consulta dura no minimo 40 minutos podendo durar ate 1 horas dependo do estado das patologias do paciente.

**Dor**
- Gerenciar os agendamentos das consultas.

**Solucao KISS** [Keep-It-Simple-Stupid](https://tiagoaguiar.co/a-tecnica-do-kiss-como-programador~Zd-ocMkXp2w#:~:text=A%20t%C3%A9cnica%20Kiss%2C%20um%20acr%C3%B3nimo,significa%3A%20Mantenha%20isso%20simplesmente%20est%C3%BApido!):
- Sistema para gerenciar as consultas.

**Features**
- gerenciar pagamentos
- sistema de pontos (acumulou x pontos ganha desconto de x%)
- gerenciar estoque dos produtos

#
***
### Tecnologias e seus motivos

**Language**
- [python](https://www.python.org/)
- __motivo__: utilizada no aprendizado durante todo o periodo letivo

**Framework**
- [fastapi](https://fastapi.tiangolo.com/)
- __motivo__: facilidade em criar documentacao interativa, utilizando api do swagger

**Database**
- [mysql](https://www.mysql.com/)
- __motivo__: preferencia do desenvolvedor, por ter maior conhecimento nessa base SQL, alem de ser ensinada durante o curso

**Architecture**
- [clean architecture](https://blog.devgenius.io/clean-architecture-c-martin-uncle-bob-5a7a17e4fadb)
- __motivo__: isolamento da regra de negocio, deixando sistema livre de frameworks

**metodologia**
- [domain driven designer](https://engsoftmoderna.info/artigos/ddd.html#:~:text=DDD%20%C3%A9%20uma%20abordagem%20para,mas%20dentro%20de%20um%20contexto)

**resumo**
- DDD é uma abordagem para desenvolvimento de sistemas de software complexos, em que:
  - 1 o foco está no domínio do sistema;
  - 2 desenvolvedores e especialistas no negócio devem explorar esse domínio de forma colaborativa;
  - 3 como resultado, eles devem se comunicar usando uma linguagem ubíqua, mas dentro de um contexto


#
***
### Endpoints
**login**
- /__login__

**patient**
- /__create__
- /__update__
- /__logged__
- /__schedule__
- /__schedule/list__

**Podiatrist**
- /__register/pathology__
- /__search/patient/{patient_id}__
- /__list/patient__
- /__search/patient/by/{name}__
- /__schedule/cancel__
- /__schedule/list__
- /__medical_attendance__

#
***
### Documentação
- http://0.0.0.0/docs

#
***
### COMANDOS
OBS: é nescessario ter o **[docker](https://docs.docker.com/desktop/install/linux-install/)** e **[docker-compose](https://docs.docker.com/desktop/install/linux-install/)** instalado
- docker-compose up --build   
  - OBS: esse comando deve ser rodado uma unica vez, a não ser que você altere algo em requirements ou no Dockerfile
- parar aplicação
  - docker-compose stop
- rodar aplicação
  - docker-compose start

#
***
Created by - Marco Antonio 