import time, sys, itertools, threading, pickle, atexit
from datetime import datetime
patients_list = [{'ID Index':0,'Patient ID':'', 'Name':'', 'Day':'', 'Month':'', 'Year':'', 'Age':'', 'Gender':'', 
                  'Blood':'', 'Phone':''}]
with open('data.pickle', 'rb') as files:
    data = pickle.load(files)
    patients_list = data
def animating(text, state):
    done = False
    def animate():
        sys.stdout.write(text)
        sys.stdout.flush()
        for c in itertools.cycle(['.']):
            if done:
                break
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.2)
    threading.Thread(target=animate).start()
    time.sleep(0.5)
    done = True
    if state == 1:
        sys.stdout.write('\nPatient Medical Record ID saved successfully\n\n')
    elif state == 2:
        sys.stdout.write('\nPatient Name saved successfully\n')
    elif state == 3:
        sys.stdout.write('\nPatient Gender saved successfully\n')
    elif state == 4:
        sys.stdout.write('\nPatient Blood Type saved successfully\n')
    elif state == 5:
        sys.stdout.write('\nPatient Birth Date and Age saved successfully\n')
    elif state == 6:
        sys.stdout.write('\nPatient Phone Number saved successfully\n')
    elif state == 7:
        sys.stdout.write('\nPatient Record entried successfully\n')
    elif state == 8:
        sys.stdout.write('\nPatient Record not created. Back to Main Page\n')
    else:
        sys.stdout.write('')
    time.sleep(0.5)
def save_data(id_number, name, day, month_name, year, birthdate, gender, blood, ph_number):
    patient_new = {'ID Index':int(id_number), 'Patient ID':id_number, 'Name':name, 'Day':day, 
                     'Month':month_name, 'Year': year, 'Age':birthdate, 'Gender':gender, 'Blood':blood, 
                     'Phone':ph_number}
    patients_list.append(patient_new)
def show_all_data():
    time.sleep(0.5)
    iterable_list = []
    iterated_patients_list = [i.setdefault('Patient ID') for i in patients_list]
    for i in iterated_patients_list:
        if i != '':
            for keys in ['ID index', 'Patient ID', 'Name', 'Day', 'Month', 'Year', 'Age', 'Gender', 'Blood', 
                         'Phone']:
                each_keys_values = [i.setdefault(keys) for i in patients_list]
                iterable_list.append(each_keys_values)
    else:
        patients_list_null = []
        for keys in range(10):
            each_keys_values = [i for i in patients_list_null]
            iterable_list.append(each_keys_values)
    iterable_list = zip(iterable_list[0], iterable_list[1], iterable_list[2], iterable_list[3], 
                        iterable_list[4], iterable_list[5], iterable_list[6], iterable_list[7], 
                        iterable_list[8], iterable_list[9])
    iterable_list = list(iterable_list)
    iterable_list.sort()
    if len(iterable_list) != 0:
        iterable_list.pop(0)
    t1, t2, t3, t4, t5, t6, t7 = 'No.', 'Patient ID', 'Name', 'Birthdate', 'Age', 'Gender', 'Blood' 
    t8 = 'Phone Number'
    border = '-'
    print(' '+border.center(130, '-'))
    print(t1.center(5, ' ')+'|'+t2.center(14, ' ')+'|'+t3.center(40, ' ')+'|'+t4.center(21, ' ')+'|'+
          t5.center(7, ' ')+'|'+t6.center(10, ' ')+'|'+t7.center(9, ' ')+'|'+t8.center(18, ' ')+'|')
    print(' '+border.center(130, '-'))
    nomor = 0
    for items in iterable_list:
        nomor += 1
        birthdate = items[6]
        age = calculate_age(birthdate)
        v1, v2, v3 = str(nomor), 'MedRec-'+items[1], items[2], 
        v4, v5, v6 = str(items[3])+' '+items[4]+' '+str(items[5]), str(age), items[7]
        v7, v8 = items[8], '+62'+items[9]
        print(v1.center(5, ' ')+'|'+v2.center(14, ' ')+'|'+v3.center(40, ' ')+'|'+v4.center(21, ' ')+'|'+
              v5.center(7, ' ')+'|'+v6.center(10, ' ')+'|'+v7.center(9, ' ')+'|'+v8.center(18, ' ')+'|')
    time.sleep(0.5)
def show_selected_data(input):
    time.sleep(0.5)
    animating('Loading', 0)
    print('')
    title = ' PATIENT RECORD '
    bottom = '='
    for patient in patients_list:
        if input == patient['Patient ID']:
            birthdate = patient['Age']
            age = calculate_age(birthdate)
            print('\n', title.center(130, '='))
            print('\nPatient ID \t: MedRec-'+patient['Patient ID']+'\nName \t\t: '+patient['Name'])
            print('Birthdate \t: '+str(patient['Day'])+' '+patient['Month']+' '+str(patient['Year']))
            print('Age \t\t: '+str(age)+'\nGender \t\t: '+patient['Gender'])
            print('Blood Type \t: '+patient['Blood']+'\nPhone Number \t: +62'+patient['Phone'])
            print('\n', bottom.center(130, '='), '\n')
            time.sleep(0.5)
            break
    else:
        print('\n', title.center(130, '='), '\n')
        print(f'Patient with MedRec-{input} not found.')
        print('\n', bottom.center(130, '='), '\n')
        time.sleep(0.5)
    return input
def id_error_filtering():
    while True:
        id_filter = input('Please enter Patient Records ID = MedRec-')
        if (id_filter.isdigit()) and (len(id_filter) == 3):
            print(f'Patient Records ID = MedRec-{id_filter}')
            time.sleep(0.5)
            break
        else:
            print('\nInvalid Entry : Patient ID must be 3 numeric entries')
            time.sleep(0.5)
    return id_filter
def id_error_handling():
    while True:
        id_number = input('Please enter Patient Records ID = MedRec-')
        if (id_number.isdigit()) and (len(id_number) == 3):
            id_list = [i.setdefault('Patient ID') for i in patients_list]
            if id_number in id_list:
                print(f'\nError Duplicates : Patient with ID MedRec-{id_number} already exists')
                time.sleep(0.5)
            else:
                print(f'Patient Records ID = MedRec-{id_number}')
                time.sleep(0.5)
                animating('Saving', 1)
                break
        else:
            print('\nInvalid Entry : Patient ID must be 3 numeric entries')
            time.sleep(0.5)
    return id_number
def name_entry():
    name = input('Please enter Patient Name = ').title()
    while True:
        if len(name) != 0:
            print('Patient Name =', name)
            time.sleep(0.5)
            animating('Saving', 2)
            print('')
            break
        else:
            print('\nInvalid Entry : Patient Name must not be empty')
            time.sleep(0.5)
        name = input('Please enter Patient Name = ').title()
    return name
def birth_date():
    def get_date_input(prompt):
        while True:
            date_str = input(prompt)
            try:
                date = datetime.strptime(date_str, '%d-%m-%Y')
                return date.date()
            except ValueError:
                print('\nInvalid Entry : Patient Birthdate must be in format DD-MM-YYYY')
                time.sleep(0.5)
    birthdate = get_date_input('Please enter Patient Birthdate (DD-MM-YYYY) = ')
    age = calculate_age(birthdate)
    day = birthdate.day
    month_name = birthdate.strftime('%B')
    year = birthdate.year
    print('Patient Birthday = ', day, month_name, year)
    time.sleep(0.5)
    animating('Saving', 0)
    print("\nPatient Age = ", age)
    time.sleep(0.5)
    animating('Saving', 5)
    return day, month_name, year, birthdate
def calculate_age(birthdate):
        today = datetime.today().date()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
def gender_type():
    print('\n1. Male\n2. Female')
    gender = input('Please enter Patient Gender = ')
    while True:
        if gender == '1':
            print('Patient Gender = Male')
            time.sleep(0.5)
            gender = 'Male'
            break
        elif gender == '2':
            print('Patient Gender = Female')
            time.sleep(0.5)
            gender = 'Female'
            break
        else:
            print(f'\nError Message : Option Number {gender} is invalid')
            time.sleep(0.5)
        print('\n1. Male\n2. Female')
        gender = input('Please enter Patient Gender = ')
    animating('Saving', 3)
    return gender
def blood_type():
    while True:
        print('\n1. A\n2. B\n3. AB\n4. O')
        blood = input('Please enter Patient Blood Type = ')
        if blood == '1' or blood == '2' or blood == '3' or blood == '4':
            if blood == '1':
                print(f'Patient Blood Type = A')
                time.sleep(0.5)
                blood = 'A'
            elif blood == '2':
                print(f'Patient Blood Type = B')
                time.sleep(0.5)
                blood = 'B'
            elif blood == '3':
                print(f'Patient Blood Type = AB')
                time.sleep(0.5)
                blood = 'AB'
            else:
                print(f'Patient Blood Type = O')
                time.sleep(0.5)
                blood = 'O'
            break
        else:
            print(f'\nError Message : Option Number {blood} is invalid')
            time.sleep(0.5)
    animating('Saving', 4)
    return blood
def phone_number():
    while True:
        ph_number = input('\nPlease enter Patient Phone Number (without Country Code) = ')
        ph_number_iterated = [i.setdefault('Phone') for i in patients_list]
        if (ph_number.isdigit()) and len(ph_number) >= 10 and len(ph_number) <= 12:
            if ph_number[0] == '0':
                ph_number = '{}'.format(ph_number[1:])
                print(f'Patient Phone Number = +62{ph_number}')
                time.sleep(0.5)
                if ph_number in ph_number_iterated:
                    print(f'\nError Duplicates : Patient with Phone Number +62{ph_number} already exists')
                    time.sleep(0.5)
                else:
                    animating('Saving', 6)
                    break
            else:
                ph_number = '{}'.format(ph_number[:])
                print(f'Patient Phone Number = +62{ph_number}')
                time.sleep(0.5)
                if ph_number in ph_number_iterated:
                    print(f'\nError Duplicates : Patient with Phone Number +62{ph_number} already exists')
                    time.sleep(0.5)
                else:
                    animating('Saving', 6)
                    break
        else:
            print('\nError Messages : Patient Number must have 11 or 12 numeric entries')
            time.sleep(0.5)
    return ph_number
def each_patient_delete(input):
    for each_patient in patients_list:
        if input == each_patient['Patient ID']:
            patients_list.remove(each_patient)
            break
def main_page():
    while True:
        title = ' PATIENT PERSONAL RECORDS '
        bottom = '='
        print('\n', title.center(130, '='))
        print('\n1. Create New Patient Records\n2. Update Patient Records')
        print('3. Delete Patient Records\n4. Read Patient Records\n5. Exit\n')
        print(bottom.center(130, '='), '\n')
        mp_input = input('Please enter Option Number = ')
        if mp_input == '1':
            title = ' CREATE NEW PATIENT RECORDS '
            print('\n', title.center(130, '='), '\n\nPlease fill out New Patient Records\n')
            time.sleep(0.5)
            id_number = id_error_handling()
            name = name_entry()
            (day, month_name, year, birthdate) = birth_date()
            age = calculate_age(birthdate)
            gender = gender_type()
            blood = blood_type()
            ph_number = phone_number()
            while True:
                print('')
                animating('Fetching all saved entries', 0)
                print('')
                a = '\nWill New Patient Record above be created?\n'
                b = f'\nPatient ID \t: MedRec-{id_number}\nName \t\t: {name}\nBirthdate \t: {day} {month_name} {year}'
                c = f'\nAge \t\t: {age}\nGender \t\t: {gender}\nBlood Type \t: {blood}\nPhone Number \t: +62{ph_number}'
                d = '\n1. Yes\n2. No\n'
                print(b+c)
                time.sleep(0.5)
                print(a+d)
                c_input = input('Please enter Option Number = ')
                time.sleep(0.5)
                if c_input == '1' or c_input == '2':
                    if c_input == '1':
                        print('\nOption input = Yes')
                        time.sleep(0.5)
                        animating('Uploading', 7)
                        save_data(id_number, name, day, month_name, year, birthdate, gender, blood, ph_number)
                    else:
                        print('\nOption input = No')
                        time.sleep(0.5)
                        animating('Aborting', 8)
                    break
                else:
                    print(f'\nError Message : Option number {c_input} is invalid')
                    time.sleep(0.5)
        elif mp_input == '2':
            while True:
                title = ' UPDATE PAGE '
                print('\n', title.center(130, '='), '\n')
                show_all_data()
                print('\n', bottom.center(130, '='), '\n')
                print('1. Find Patient Record to update by ID\n2. Back to Main Page\n')
                up_input = input('Please entry option number = ')
                time.sleep(0.5)
                up_list = ['1', '2']
                if up_input in up_list:
                    if up_input == '1':
                        id_matched_input = id_error_filtering()
                        id_list = [i.setdefault('Patient ID') for i in patients_list]
                        if id_matched_input in id_list:
                            while True:
                                show_selected_data(id_matched_input)
                                time.sleep(0.5)
                                print('1. Update Patient ID\n2. Update Name\n3. Update Birthdate')
                                print('4. Update Gender\n5. Update Blood Type\n6. Update Phone Number\n7. Back')
                                key = (input('Please entry option number = '))
                                key_list = ['1', '2', '3', '4', '5', '6', '7']
                                if key in key_list:
                                    def yes():
                                        print('\nOption input = Yes')
                                        time.sleep(0.5)
                                        animating('Updating', 0)
                                        print('\nPatient Record updated successfully')
                                        time.sleep(0.5)
                                    def no():
                                        print('\nOption input = No')
                                        time.sleep(0.5)
                                        animating('Aborting', 0)
                                        print('\nPatient Record not updated')
                                    def wrong_input():
                                        print(f'\nError Message : Option number {confirmation} is invalid\n')
                                        time.sleep(0.5)
                                    if key == '1':
                                        print('\nOption input = Update Patient ID')
                                        time.sleep(0.5)
                                        id_number_new = id_error_handling()
                                        while True:
                                            print('\nDo you confirm to update data?\n\n1. Yes\n2. No')
                                            confirmation = input('Please entry option number = ')
                                            if confirmation == '1':
                                                for i in patients_list:
                                                    if id_matched_input == i['Patient ID']:
                                                        i['Patient ID'] = id_number_new
                                                        i['ID Index'] = int(id_number_new)
                                                        id_matched_input = id_number_new
                                                yes()
                                            elif confirmation == '2':
                                                no()
                                            else:
                                                wrong_input()
                                                continue
                                            break
                                    elif key == '2':
                                        print('\nOption input = Update Patient Name')
                                        time.sleep(0.5)
                                        name_new = name_entry()
                                        while True:
                                            print('\nDo you confirm to update data?\n\n1. Yes\n2. No')
                                            confirmation = input('Please entry option number = ')
                                            if confirmation == '1':
                                                for i in patients_list:
                                                    if id_matched_input == i['Patient ID']:
                                                        i['Name'] = name_new
                                                yes()
                                            elif confirmation == '2':
                                                no()
                                            else:
                                                wrong_input()
                                                continue
                                            break
                                    elif key == '3':
                                        print('\nOption input = Update Patient Birthdate')
                                        time.sleep(0.5)
                                        (day_new, month_new, year_new, age_new) = birth_date()
                                        while True:
                                            print('\nDo you confirm to update data?\n\n1. Yes\n2. No')
                                            confirmation = input('Please entry option number = ')
                                            if confirmation == '1':
                                                for i in patients_list:
                                                    if id_matched_input == i['Patient ID']:
                                                        i['Day'] = day_new
                                                        i['Month'] = month_new
                                                        i['Year'] = year_new
                                                        i['Age'] = age_new
                                                yes()
                                            elif confirmation == '2':
                                                no()
                                            else:
                                                wrong_input()
                                                continue
                                            break
                                    elif key == '4':
                                        print('\nOption input = Update Patient Gender')
                                        time.sleep(0.5)
                                        gender_new = gender_type()
                                        while True:
                                            print('\nDo you confirm to update data?\n\n1. Yes\n2. No')
                                            confirmation = input('Please entry option number = ')
                                            if confirmation == '1':
                                                for i in patients_list:
                                                    if id_matched_input == i['Patient ID']:
                                                        i['Gender'] = gender_new
                                                yes()
                                            elif confirmation == '2':
                                                no()
                                            else:
                                                wrong_input()
                                                continue
                                            break
                                    elif key == '5':
                                        print('\nOption input = Update Patient Blood Type')
                                        time.sleep(0.5)
                                        blood_new = blood_type()
                                        while True:
                                            print('\nDo you confirm to update data?\n\n1. Yes\n2. No')
                                            confirmation = input('Please entry option number = ')
                                            if confirmation == '1':
                                                for i in patients_list:
                                                    if id_matched_input == i['Patient ID']:
                                                        i['Blood'] = blood_new
                                                yes()
                                            elif confirmation == '2':
                                                no()
                                            else:
                                                wrong_input()
                                                continue
                                            break
                                    elif key == '6':
                                        print('\nOption input = Update Patient Phone Number')
                                        time.sleep(0.5)
                                        phone_new = phone_number()
                                        while True:
                                            print('\nDo you confirm to update data?\n\n1. Yes\n2. No')
                                            confirmation = input('Please entry option number = ')
                                            if confirmation == '1':
                                                for i in patients_list:
                                                    if id_matched_input == i['Patient ID']:
                                                        i['Phone'] = phone_new
                                                yes()
                                            elif confirmation == '2':
                                                no()
                                            else:
                                                wrong_input()
                                                continue
                                            break
                                    else:
                                        print('\nOption input = Back to Update Page')
                                        time.sleep(0.5)
                                        break
                                else:
                                    print(f'\nError Message : Option number {key} is invalid\n')
                                    time.sleep(0.5)
                                    continue
                        else:
                            show_selected_data(id_matched_input)
                            time.sleep(0.5)
                            print('Back to Update Page')
                            time.sleep(0.5)
                            animating('Loading All Record', 0)
                            print('')
                            continue
                    elif up_input == '2':
                        print('\nOption input = Back to Main Page')
                        time.sleep(0.5)
                        break
                else:
                    print(f'\nError Message : Option number {up_input} is invalid\n')
                    time.sleep(0.5)
        elif mp_input == '3':
            while True:
                animating('Loading All Record', 0)
                print('')
                title = ' DELETE PAGE '
                print('\n', title.center(130, '='), '\n')
                show_all_data()
                print('\n', bottom.center(130, '='), '\n')
                time.sleep(0.5)
                print('1. Find Patient Record to delete by ID\n2. Back to Main Page\n')
                dp_input = input('Please enter Option Number = ')
                time.sleep(0.5)
                if dp_input == '1' or dp_input == '2':
                    if dp_input == '1':
                        id_matched_input = show_selected_data(id_error_filtering())
                        time.sleep(0.5)
                        id_list = [i.setdefault('Patient ID') for i in patients_list]
                        if id_matched_input in id_list:
                            print('1. Proceed to delete\n2. Cancel delete. Back to Delete Page\n')
                            while True:
                                time.sleep(0.5)
                                confirmation = input('Please enter Option Number = ')
                                if confirmation == '1' or confirmation == '2':
                                    if confirmation == '1':
                                        each_patient_delete(id_matched_input)
                                        print('\nOption input = Proceed to delete')
                                        time.sleep(0.5)
                                        animating('Deleting', 0)
                                        print('\nPatient Record deleted successfully\n')
                                        time.sleep(0.5)
                                    else:
                                        print('\nOption input = Cancel delete')
                                        time.sleep(0.5)
                                        animating('Aborting', 0)
                                        print('\nPatient Record not deleted\n')
                                        time.sleep(0.5)
                                    break
                                else:
                                    print(f'\nError Message : Option number {confirmation} is invalid')
                                    time.sleep(0.5)
                                    continue
                        else:
                            print('Back to Delete Page')
                            time.sleep(0.5)
                    else:
                        print('\nOption input = Back to Main Page')
                        time.sleep(0.5)
                        break
                else:
                    print(f'\nError Message : Option number {dp_input} is invalid')
                    time.sleep(0.5)
        elif mp_input == '4':
            while True:
                time.sleep(0.5)
                title = ' PATIENTS DATABASE '
                print('\n', title.center(130, '='))
                print('\n1. Read all Patients Record\n2. Read a Patient Record')
                print('3. Back to Main Page\n')
                print(bottom.center(130, '='), '\n')
                rp_input = input('Please enter Option Number = ')
                rp_list = ['1', '2', '3']
                if rp_input in rp_list:
                    if rp_input == '1':
                        time.sleep(0.5)
                        print('\nOption input = Read all Patients Record')
                        time.sleep(0.5)
                        animating('Loading All Record', 0)
                        title = ' ALL PATIENTS RECORDS '
                        print('\n\n', title.center(130, '='), '\n')
                        show_all_data()
                        print('\n', bottom.center(130, '='), '\n')
                        input('Press Enter to Continue')
                    elif rp_input == '2':
                        time.sleep(0.5)
                        print('\nOption input = Read a Patient Record')
                        time.sleep(0.5)
                        show_selected_data(id_error_filtering())
                        input('Press Enter to Continue')
                    else:
                        time.sleep(0.5)
                        print('\nOption input = Back to Main Page')
                        time.sleep(0.5)
                        break
                    continue
                else:
                    print(f'\nError Message : Option number {rp_input} is invalid')
                    time.sleep(0.5)
        elif mp_input == '5':
            def save_data_before_exit():
                with open('data.pickle', 'wb') as files:
                    pickle.dump(data, files)
            data = patients_list
            time.sleep(0.5)
            atexit.register(save_data_before_exit)
            animating('Exiting', 0)
            print('\nExit successfully')
            time.sleep(0.5)
            exit()
        else:
            print(f'\nError Message : Option number {mp_input} is invalid')
            time.sleep(0.5)
            continue
main_page()