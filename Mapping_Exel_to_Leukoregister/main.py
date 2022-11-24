import pandas as pd
from map_demographics import mapping_demographics
from map_mri_review import mapping_mri_review
from map_first_symptoms import mapping_first_symptoms
from map_diagnostic_confirmation import mapping_diagnostic_confirmation
from map_time_to_event import mapping_time_to_event
from map_developmental_milestones import mapping_developmental_milestones
from map_medical_examination_clinical_visit import mapping_medical_examination_clinical_visit
from map_treatment import mapping_treatment


def mapp_exel_to_leuko_register():
    """
    Maps the data from the excel file to the leukoregister radcap csv and returns the mapped data in the same format as the
    csv that can be uplodat to redcap.
    :return: pd.DataFrame, the mapped data for the leukoregister project (rows=patients, cols=fields)
    """
    # get file name from args
    # curently as hardcoded variables drunig development
    excel_file_path = "data/Tabelle_MLD_Datenstruktur.xlsx"
    mrt_database_file_path = "data/MLD_MRT_database_kopie.csv"
    output_template_path = "mapping_csvs/output_template.csv"
    output_path = "output/mapped.csv"

    output_df = pd.read_csv(output_template_path)
    print("Mapping data...")

    output_df = mapping_demographics(excel_file_path,output_df)
    print("demographics mapped")
    output_df = mapping_mri_review(excel_file_path,mrt_database_file_path,output_df)
    print("mri review mapped")
    output_df = mapping_first_symptoms(excel_file_path,output_df)
    print("first symptoms mapped")
    output_df = mapping_time_to_event(excel_file_path,output_df)
    print("time to event mapped")
    output_df = mapping_diagnostic_confirmation(excel_file_path,output_df)
    print("diagnostic confirmation mapped")
    output_df = mapping_developmental_milestones(excel_file_path,output_df)
    print("developmental milestones mapped")
    output_df = mapping_medical_examination_clinical_visit(excel_file_path,output_df)
    print("medical examination clinical visit mapped")
    output_df = mapping_treatment(excel_file_path,output_df)
    print("treatment mapped")
    print("Mapping done")
    #save the mapped data to a csv

    output_df.to_csv(output_path, index=False)



if __name__ == '__main__':
    mapp_exel_to_leuko_register()