from utils import doc_header, patient_header, lab_header
from config import conn, cur

cur = conn.cursor()


class Doctor:

  def __init__(self) -> None:
    ...

  # This asks the user to enter the doctor attributes or information
  def enter_doctor_info(self) -> None:
    doctor_name = input("Enter the doctor's name: ")
    specialization = input("Enter the doctor's speciality: ")
    working_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
    qualification = input("Enter the doctor's qualification: ")
    room_number = input("Enter the doctor's room number: ")

    self.doctor_name = doctor_name
    self.specialization = specialization
    self.working_time = working_time
    self.qualification = qualification
    self.room_number = room_number

  # This adds a new doctor to the database
  def add_doctor(self) -> None:
    self.enter_doctor_info()
    cur.execute(
      '''INSERT INTO doctor 
                    (name, specialization, time, 
                    qualification, room_number)
                VALUES 
                    (%s, %s, %s, %s, %s)''',
      (self.doctor_name, self.specialization, self.working_time,
       self.qualification, self.room_number))
    conn.commit()
    print('\nSuccessfully added doctor!')

  # displays all labs in the database
  def display_doctors_list(self) -> None:
    cur.execute('SELECT * FROM doctor ORDER BY id')
    doctors = cur.fetchall()
    print(f'\n{doc_header}')
    for doctor in doctors:
      print(self.display_doc_info(doctor))

  def search_doctor_by_id(self) -> None:
    id = input('\nEnter the doctor Id: ')
    try:
      id = int(id)
    except ValueError as _:
      print('Id must be a number')
    else:
      cur.execute('SELECT * FROM doctor WHERE id=%s', (id, ))
      found_doctor = cur.fetchone()
      if not found_doctor:
        print("Can't find the doctor with the same ID on the system\n")
      else:
        info = f'\n{doc_header}\n{self.display_doc_info(found_doctor)}'
        print(info)

  def search_doctor_by_name(self) -> None:
    name = input('\nEnter the doctor name: ')
    cur.execute('SELECT * FROM doctor WHERE name=%s', (name, ))
    found_doctor = cur.fetchone()
    if not found_doctor:
      print("Can't find the doctor with the same name on the system")
    else:
      info = f'\n{doc_header}\n{self.display_doc_info(found_doctor)}'
      print(info)

  # writes list of all doctors to a text file for easy share
  def write_list_of_doctors_to_file(self) -> None:
    cur.execute('SELECT * FROM doctor')
    doctors = cur.fetchall()
    with open('doctors.txt', 'w') as f:
      f.write(f'{doc_header}\n')
      for doctor in doctors:
        f.write(f'{self.display_doc_info(doctor)}\n')
    print('\nWrite success!')

  #formats a single doctor's information for display to the user.
  def display_doc_info(self, doc: tuple) -> str:
    d_id = str(doc[0])
    d_name = f'Dr. {doc[1]}'
    d_spe = doc[2]
    d_wt = doc[3]
    d_qul = doc[4]
    d_rm = doc[5]
    doc_info = f'{d_id.ljust(5)}{d_name.ljust(23)}{d_spe.ljust(16)}{d_wt.ljust(16)}{d_qul.ljust(16)}{d_rm}'
    return doc_info

  # This edits a doctor's information if it exists in the database
  def edit_doc_info(self) -> None:
    id = input(
      'Please enter the id of the doctor you want to edit their information: ')
    try:
      id = int(id)
    except ValueError as _:
      print('Id must be a number')
    else:
      cur.execute('SELECT * FROM doctor WHERE id=%s', (id, ))
      check_find = cur.fetchone()
      if not check_find:
        print("Can't find the doctor with the same ID on the system\n")
      else:
        new_doctor_name = input('Enter new Name: ')
        new_specialization = input('Enter new Specialist in: ')
        new_working_time = input('Enter new Timing: ')
        new_qualification = input('Enter new Qualification: ')
        new_room_number = input('Enter new Room number: ')

        cur.execute(
          '''UPDATE doctor 
                        SET name=%s, specialization=%s, 
                            time=%s, qualification=%s, room_number=%s 
                        WHERE id=%s''',
          (new_doctor_name, new_specialization, new_working_time,
           new_qualification, new_room_number, id))
      conn.commit()

      print('\nEdit success!')

  def delete_doctor_info(self) -> None:
    id = input('Please enter the id of the doctor you want to delete:  ')
    try:
      id = int(id)
    except ValueError as _:
      print('Id must be a number')
    else:
      cur.execute('SELECT * FROM doctor WHERE id=%s', (id, ))
      found_doctor = cur.fetchone()
      if not found_doctor:
        print("Can't find the doctor with the same ID on the system\n")
      else:
        cur.execute('DELETE FROM doctor WHERE id=%s', (id, ))
        conn.commit()
        print('\nDelete success!')


class Facility:

  def __init__(self) -> None:
    ...

  def add_facility(self) -> None:
    facility = input('Enter Facility name: ')
    self.facility = facility
    cur.execute('INSERT INTO facility (name) VALUES (%s)', (self.facility, ))
    conn.commit()
    print('Successfully added facility!')

  # displays all labs in the database
  def display_facilities(self) -> None:
    cur.execute('SELECT * FROM facility ORDER BY name')
    facilities = cur.fetchall()
    print('\nThe Hospital  Facilities are:')
    for facility in facilities:
      print(f'{facility[1]}')

  # writes list of all facilities to a text file for easy share
  def write_list_of_facilities_to_file(self) -> None:
    cur.execute('SELECT * FROM facility')
    facilities = cur.fetchall()
    with open('facilities.txt', 'w') as f:
      f.write('Hospital  Facilities\n')
      for facility in facilities:
        f.write(f'{facility[1]}\n')
    print('\nWrite success!')

  def edit_facility_info(self) -> None:
    facility_to_edit = input('Enter facility name to edit: ')
    cur.execute('SELECT * FROM facility WHERE name=%s', (facility_to_edit, ))
    found_facility = cur.fetchone()
    if not found_facility:
      print('\nNo facility with that name found!')
    else:
      new_facility_name = input('Enter new name: ')
      cur.execute('UPDATE facility SET name=%s WHERE name=%s',
                  (new_facility_name, facility_to_edit))
      conn.commit()
      print('\nEdit success!')

  def delete_facility_info(self) -> None:
    name = input(
      'Please enter the name of the Facility that you want to delete: ')
    cur.execute('SELECT * FROM facility WHERE name=%s', (name, ))
    found_facility = cur.fetchone()
    if not found_facility:
      print('\nNo facility with that name found!')
    else:
      cur.execute('DELETE FROM facility WHERE name=%s', (name, ))
      conn.commit()
      print('\nDelete success!')


class Laboratory:

  def __init__(self) -> None:
    ...

  # asks the user to input for lab details
  def enter_laboratory_info(self):
    lab_name = input('Enter Laboratory facility: ')
    cost = input('Enter Laboratory cost: ')

    self.lab_name = lab_name
    self.lab_cost = cost

  # adds a new doctor to the database
  def add_lab(self):
    self.enter_laboratory_info()
    try:
      self.lab_costcost = int(self.lab_cost)
    except ValueError as _:
      print('Cost must be a number')
    else:
      cur.execute('INSERT INTO lab (name, cost) VALUES (%s, %s)',
                  (self.lab_name, self.lab_cost))
      conn.commit()
      print('Successfully added laboratory!')

  # displays all labs in the database
  def display_labs_list(self):
    cur.execute('SELECT * FROM lab ORDER BY name')
    labs = cur.fetchall()
    print(f'\n{lab_header}')
    for lab in labs:
      lab_name = lab[1]
      lab_cost = str(lab[2])
      lab_info = f'{lab_name.ljust(16)}{f"${lab_cost}"}'
      print(lab_info)

  # writes list of all labs to a text file for easy share
  def write_list_of_labs_to_file(self):
    cur.execute('SELECT * FROM lab')
    laboratories = cur.fetchall()
    with open('laboratories.txt', 'w') as f:
      f.write(f'{lab_header}\n')
      for lab in laboratories:
        f.write(f'{lab[1].ljust(16)}{lab[2]}\n')
    print('\nWrite Success')

  def edit_lab_info(self):
    lab_to_edit = input('Enter lab name to edit: ')
    cur.execute('SELECT * FROM lab WHERE name=%s', (lab_to_edit, ))
    found_lab = cur.fetchone()
    if not found_lab:
      print('No lab with that name found!')
    else:
      new_lab_name = input('Enter new name: ')
      new_lab_cost = input('Enter new cost: ')
      cur.execute('UPDATE lab SET name=%s, cost=%s WHERE name=%s',
                  (new_lab_name, new_lab_cost, lab_to_edit))
      conn.commit()
      print('\nEdit Success!')

  def delete_lab_info(self):
    name = input(
      'Please enter the name of the laboratory you want to delete: ')
    cur.execute('SELECT * FROM lab WHERE name=%s', (name, ))
    found_lab = cur.fetchone()
    if not found_lab:
      print('No lab with that name found!')
    else:
      cur.execute('DELETE FROM lab WHERE name=%s', (name, ))
      conn.commit()
      print('\nDelete Success!')


class Patient:

  def __init__(self) -> None:
    ...

  # asks the user for the patient information
  def enter_patient_info(self) -> None:
    patient_name = input('Enter Patient name: ')
    disease = input('Enter Patient disease: ')
    gender = input('Enter Patient gender: ')
    age = input('Enter Patient age: ')

    self.patient_name = patient_name
    self.disease = disease
    self.gender = gender
    self.age = age

  # adds a patient to the database
  def add_patient(self) -> None:
    Patient.enter_patient_info(self)
    try:
      self.age = int(self.age)
    except ValueError as _:
      print('Age must be a number')
    else:
      cur.execute(
        '''INSERT INTO patient 
                        (name, disease, gender, age)
                    VALUES 
                        (%s, %s, %s, %s) ''',
        (self.patient_name, self.disease, self.gender, self.age))
      conn.commit()
      print('Successfully added patient!')

  def search_patient_by_id(self) -> None:
    id = input('Enter the Patient Id: ')
    try:
      id = int(id)
    except ValueError as _:
      print('Id must be a number')
    else:
      cur.execute('SELECT * FROM patient WHERE id=%s', (id, ))
      found_patient = cur.fetchone()
      if not found_patient:
        print("Can't find the patient with the same id on the system")
      else:
        info = f'{Patient.display_patient_info(self, found_patient)}'
        print(f'\n{patient_header}')
        print(info)

  # prepares patient information to be displayed to the user
  def display_patient_info(self, patient: tuple) -> str:
    p_id = str(patient[0])
    d_name = patient[1]
    p_disease = patient[2]
    p_gender = patient[3]
    p_age = str(patient[4])
    patient_info = f'{p_id.ljust(5)}{d_name.ljust(23)}{p_disease.ljust(16)}{p_gender.ljust(16)}{p_age}'
    return patient_info

  # displays a list of all the patients in the database
  def display_patients_list(self) -> None:
    cur.execute('SELECT * FROM patient ORDER BY id')
    patients = cur.fetchall()
    print(f'\n{patient_header}')
    for patient in patients:
      print(self.display_patient_info(patient))

  # writes list of all patients to a text file for easy share
  def write_list_of_patients_to_file(self) -> None:
    cur.execute('SELECT * FROM patient')
    patients = cur.fetchall()
    with open('patients.txt', 'w') as f:
      f.write(f'{patient_header}\n')
      for patient in patients:
        f.write(f'{self.display_patient_info(patient)}\n')
    print('\nWrite Success!')

  def edit_patient_info(self) -> None:
    id = input(
      'Please enter the id of the Patient you want to edit their information: '
    )
    try:
      id = int(id)
    except ValueError as _:
      print('Id must be a number')
    else:
      cur.execute('SELECT * FROM patient WHERE id=%s', (id, ))
      check_find = cur.fetchone()
      if not check_find:
        print("Can't find Patient with the same id on the system")
      else:
        new_patient_name = input('Enter new Name: ')
        new_disease = input('Enter new disease: ')
        new_gender = input('Enter new gender: ')
        new_age = input('Enter new age: ')
        cur.execute(
          '''UPDATE patient 
                        SET 
                            name=%s, disease=%s, gender=%s, age=%s 
                        WHERE id=%s''',
          (new_patient_name, new_disease, new_gender, new_age, id))

        conn.commit()
        print('\nEdit Success!')

  def delete_patient_info(self) -> None:
    id = input('Please enter the id of the Patient you want to delete: ')
    try:
      id = int(id)
    except ValueError as _:
      print('Id must be a number')
    else:
      cur.execute('SELECT * FROM patient WHERE id=%s', (id, ))
      check_find = cur.fetchone()
      if not check_find:
        print("Can't find Patient with the same id on the system")
      else:
        cur.execute('DELETE FROM patient WHERE id=%s', (id, ))
        conn.commit()
        print('\nDelete Success!')
