import pandas as pd


class Patient:
    def __init__(self, patient_id, redcap_pd, list_of_visit_dates_required, age_visit_margin=0):
        self.patient_id = patient_id
        self.list_of_visits_age = []
        self.visit_data = None
        self.other_data = None
        self.patient_data = None
        self.list_of_visit_dates_required = list_of_visit_dates_required
        self.list_of_visit_that_are_missing = []
        self.age_visit_margin = age_visit_margin
        self.get_patient_data(redcap_pd)
        self.get_list_of_visit_that_are_missing()

    def get_patient_data(self, redcap_pd):
        # get the rows from the padas data frame redcap_pd that have patient_id as self.patient_id
        # save the rows in self.patient_data
        self.patient_data = redcap_pd.loc[redcap_pd['patient_id'] == self.patient_id]
        self.visit_data = self.patient_data.loc[self.patient_data['redcap_repeat_instrument'] == 'clinical_visit']
        # get the row with no entry in redcap_repeat_instrument
        self.other_data = self.patient_data.loc[self.patient_data['redcap_repeat_instrument'].isnull()]

    def create_missing_visits(self):
        # create the missing visits
        pass

    def get_list_of_visit_that_are_missing(self):
        # get a list of all the visit ids for this patient
        # save the list in self.list_of_visits_id
        # 3 for every pationet get the alrady existing clinical visits
        pass

    def get_patient_data(self,):
        # save the new self.visit_data to the self.patient_data
        pass


