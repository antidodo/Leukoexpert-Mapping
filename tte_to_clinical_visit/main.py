import pandas as pd
from patients import Patient

def simulated_clinical_visit_from_tte():
    """
    This will take infromation from the redcap data from time to event mesures and chreate simulated clinical visit data.
    The data will be saved in a csv file.

    importetnt !!! when uploading the result using the webinterface the "Erlauben, das leere Werte vorhandene Werte überschreiben?" auf Ja stellen
    :return:
    """

    # 1 get redcap export
    path_to_redcap_export = "data/redcap_export.csv"
    redcap_pd = pd.read_csv(path_to_redcap_export)
    # 2 create a opject for every patient
    # 2.1 get a list of all patient ids
    patient_ids = redcap_pd['patient_id'].unique()
    # 2.2 create a list of patient objects
    patients = []
    for patient_id in patient_ids:
        # 3 for every pationet get the alrady existing clinical visits . this happens at the creation of the patient object
        patients.append(Patient(patient_id, redcap_pd))




    # 4 get all relevant dates for clinical visits


    # 5 check what clinical visit is missing

    # 6 simulate the missing clinical visits

    # 7 same the Patients wih the all the clinical visits to a csv file



if __name__ == '__main__':
    simulated_clinical_visit_from_tte()
