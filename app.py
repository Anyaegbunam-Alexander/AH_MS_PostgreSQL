# Entry point to the program.

import sys
from classes import Doctor, Facility, Laboratory, Patient
from utils import (ask_entry, facility_menu, welcome, end_session, main_menu,
                   doctor_menu, patient_menu, laboratory_menu, invalid_option)

#creates new objects of the different classes
new_facility = Facility()
new_lab = Laboratory()
new_patient = Patient()
new_doctor = Doctor()
new_doctor.add_doctor


# The main function that starts the whole program and asks the user for the first input
def main():
  print(welcome)
  print('Select from the following options, or select 0 to stop: \n'.strip(),
        main_menu)
  main_entry = ask_entry()

  while main_entry == 'Wrong' or main_entry > 4 or main_entry < 0:
    print(invalid_option)
    main_entry = ask_entry()

  if main_entry == 0:
    print(end_session)
    sys.exit()

  if main_entry == 1:
    doctor()
  elif main_entry == 2:
    facility()
  elif main_entry == 3:
    lab()
  elif main_entry == 4:
    patient()


# calls different Facility methods according to user input
def facility():
  print(facility_menu)
  facli_entry = ask_entry()

  while facli_entry == 'Wrong' or facli_entry < 0 or facli_entry > 6:
    print(invalid_option)
    facli_entry = ask_entry()

  if facli_entry == 0:
    print(end_session)
    sys.exit()

  if facli_entry == 1:
    new_facility.display_facilities()

  if facli_entry == 2:
    new_facility.write_list_of_facilities_to_file()

  if facli_entry == 3:
    new_facility.add_facility()

  if facli_entry == 4:
    new_facility.edit_facility_info()

  if facli_entry == 5:
    new_facility.delete_facility_info()

  if facli_entry == 6:
    print('')
    main()

  facility()


# calls different Laboratory methods according to user input
def lab():
  print(laboratory_menu)
  lab_entry = ask_entry()

  while lab_entry == 'Wrong' or lab_entry < 0 or lab_entry > 6:
    print(invalid_option)
    lab_entry = ask_entry()

  if lab_entry == 0:
    print(end_session)
    sys.exit()

  if lab_entry == 1:
    new_lab.display_labs_list()

  if lab_entry == 2:
    new_lab.write_list_of_labs_to_file()

  if lab_entry == 3:
    new_lab.add_lab()

  if lab_entry == 4:
    new_lab.edit_lab_info()

  if lab_entry == 5:
    new_lab.delete_lab_info()

  if lab_entry == 6:
    print('')
    main()

  lab()


# calls different Patient methods according to user input
def patient():
  print(patient_menu)
  pat_entry = ask_entry()

  while pat_entry == 'Wrong' or pat_entry < 0 or pat_entry > 7:
    print(invalid_option)
    pat_entry = ask_entry()

  if pat_entry == 0:
    print(end_session)
    sys.exit()

  if pat_entry == 1:
    new_patient.display_patients_list()

  if pat_entry == 2:
    new_patient.write_list_of_patients_to_file()

  if pat_entry == 3:
    new_patient.search_patient_by_id()

  if pat_entry == 4:
    new_patient.add_patient()

  if pat_entry == 5:
    new_patient.edit_patient_info()

  if pat_entry == 6:
    new_patient.delete_patient_info()

  if pat_entry == 7:
    print('')
    main()

  patient()


# calls different Doctor methods according to input
def doctor():
  print(doctor_menu)
  doc_entry = ask_entry()

  while doc_entry == 'Wrong' or doc_entry < 0 or doc_entry > 8:
    print('not a valid option.')
    doc_entry = ask_entry()

  if doc_entry == 0:
    print(end_session)
    sys.exit()

  if doc_entry == 1:
    new_doctor.display_doctors_list()

  if doc_entry == 2:
    new_doctor.write_list_of_doctors_to_file()

  if doc_entry == 3:
    new_doctor.search_doctor_by_id()

  if doc_entry == 4:
    new_doctor.search_doctor_by_name()

  if doc_entry == 5:
    new_doctor.add_doctor()

  if doc_entry == 6:
    new_doctor.edit_doc_info()

  if doc_entry == 7:
    new_doctor.delete_doctor_info()

  if doc_entry == 8:
    print('')
    main()

  doctor()


# Calls the main() function which is the entry point to the program.
main()
