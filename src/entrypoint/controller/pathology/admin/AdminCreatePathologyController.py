from src.entrypoint.schemas.pathology_schema import PathologyInputCreate
from src.dataProvider.repositories.pathology.CreatePathologyImpl import CreatePathologyImpl
from src.dataProvider.repositories.pathology.UpdatePatientToActiveImpl import UpdatePatientToActiveImpl
from src.dataProvider.repositories.pathology.FindByPathologyByPatientIdImpl import FindByPathologyByPatientIdImpl
from src.dataProvider.repositories.patient.FindPatientByIdImpl import FindPatientByIdImpl
from src.core.usecase.pathology.impl.admin.AdminCreatePathologyUseCaseImpl import AdminCreatePathologyUseCaseImpl


class AdminCreatePathologyController:

    @staticmethod
    def handle(input_data: PathologyInputCreate):
        create_pathology = CreatePathologyImpl()
        update_patient_to_active = UpdatePatientToActiveImpl()
        find_patient_by_id = FindPatientByIdImpl()
        find_by_pathology_by_patient_id = FindByPathologyByPatientIdImpl()
        create_pathology_use_case = AdminCreatePathologyUseCaseImpl(
            create_pathology=create_pathology,
            find_patient_by_id=find_patient_by_id,
            update_patient_to_active=update_patient_to_active,
            find_by_pathology_by_patient_id=find_by_pathology_by_patient_id)
        return create_pathology_use_case.execute(
            id_patient=input_data.id_patient,
            has_diabetes=input_data.has_diabetes,
            observations_diabetes=input_data.observations_diabetes,
            have_hypertension=input_data.have_hypertension,
            observations_hypertension=input_data.observations_hypertension,
            take_medicines=input_data.take_medicines,
            observations_medicines=input_data.observations_medicines,
            allergic_to_medicine=input_data.allergic_to_medicine,
            which_medicine=input_data.which_medicine,
            have_cancer=input_data.have_cancer,
            which_type_cancer=input_data.which_type_cancer,
            has_pacemaker=input_data.has_pacemaker,
            has_pin=input_data.has_pin,
            is_cadiaco=input_data.is_cadiaco,
            have_foot_surgery=input_data.have_foot_surgery,
            which_foot=input_data.which_foot,
            about_the_foot_of_the_patient_has_callus=input_data.about_the_foot_of_the_patient_has_callus,
            about_the_foot_of_the_patient_has_callosity=input_data.about_the_foot_of_the_patient_has_callosity,
            about_the_foot_of_the_patient_has_fissure=input_data.about_the_foot_of_the_patient_has_fissure,
            about_the_foot_of_the_patient_has_dryness=input_data.about_the_foot_of_the_patient_has_dryness,
            about_the_foot_of_the_patient_has_psoriasis=input_data.about_the_foot_of_the_patient_has_psoriasis,
            about_the_foot_of_the_patient_has_pantar_wart=input_data.about_the_foot_of_the_patient_has_pantar_wart,
            about_the_nail_of_the_patient_has_onychocryptosis=input_data.about_the_nail_of_the_patient_has_onychocryptosis,
            about_the_nail_of_the_patient_has_onycholysis=input_data.about_the_nail_of_the_patient_has_onycholysis,
            about_the_nail_of_the_patient_has_onychomycosis=input_data.about_the_nail_of_the_patient_has_onychomycosis,
            about_the_nail_of_the_patient_has_onychophoresis=input_data.about_the_nail_of_the_patient_has_onychophoresis,
            sensitive_to_pain=input_data.sensitive_to_pain,
            type_of_sock=input_data.type_of_sock,
            type_of_shoe=input_data.type_of_shoe,
            shoe_number=input_data.shoe_number
        )
