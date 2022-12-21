space = ' '
doc_header = f'Id{space * 3}Name{space * 19}Speciality{space * 6}Timing{space * 10}Qualification{space * 3}Room Number'
lab_header = f'Lab{space * 13}Cost'
patient_header = f'ID{space * 3}Name{space * 19}Disease{space * 9}Gender{space * 10}Age'


# This asks the user for an input and validates it
def ask_entry():
  entry = input('')

  try:
    response = int(entry)
  except ValueError as _:
    return 'Wrong'
  return response


# The different menus at each step of the program
facility_menu = '''
Facilities Menu:
0 - End Session
1 - Display Facilities list
2 - Write Facilities list to text file
3 - Add Facility
4 - Edit Facility
5 - Delete Facility
6 - Back to the Main Menu
'''

laboratory_menu = '''
Laboratories Menu:
0 - End Session
1 - Display Laboratories list
2 - Write Laboratories list to text file
3 - Add laboratory
4 - Edit laboratory
5 - Delete laboratory
6 - Back to the Main Menu
'''

doctor_menu = '''
Doctors Menu:
0 - End Session
1 - Display Doctors list
2 - Write Doctors list to text file
3 - Search for doctor by ID
4 - Search for doctor by name
5 - Add doctor
6 - Edit doctor info
7 - Delete doctor
8 - Back to the Main Menu
'''

patient_menu = '''
Patients Menu:
0 - End Session
1 - Display Patients list
2 - Write Patients list to text file
3 - Search for patient by ID
4 - Add patient
5 - Edit patient info
6 - Delete patient
7 - Back to the Main Menu
'''

main_menu = '''
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients
'''

welcome = 'Welcome to Alberta Hospital (AH) Management system'
end_session = 'Session Ended!'
invalid_option = 'Not a valid option!\nPlease Try again.'
