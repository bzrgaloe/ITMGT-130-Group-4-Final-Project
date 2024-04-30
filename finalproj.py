clinic_schedule = {
    "Sun": {
        "09:00": [],
        "10:00": [],
        "11:00": [],
        "12:00": [],
        "13:00": [],
        "14:00": [],
        "15:00": [],
        "16:00": []
    },
    "Mon": {
        "09:00": [],
        "10:00": [],
        "11:00": [],
        "12:00": [],
        "13:00": [],
        "14:00": [],
        "15:00": [],
        "16:00": []
    },
    "Tues": {
        "09:00": [],
        "10:00": [],
        "11:00": [],
        "12:00": [],
        "13:00": [],
        "14:00": [],
        "15:00": [],
        "16:00": []
    },
    "Wed": {
        "09:00": [],
        "10:00": [],
        "11:00": [],
        "12:00": [],
        "13:00": [],
        "14:00": [],
        "15:00": [],
        "16:00": []
    },
    "Thurs": {
        "09:00": [],
        "10:00": [],
        "11:00": [],
        "12:00": [],
        "13:00": [],
        "14:00": [],
        "15:00": [],
        "16:00": []
    },
    "Fri": {
        "09:00": [],
        "10:00": [],
        "11:00": [],
        "12:00": [],
        "13:00": [],
        "14:00": [],
        "15:00": [],
        "16:00": []
    },
    "Sat": {
        "09:00": [],
        "10:00": [],
        "11:00": [],
        "12:00": [],
        "13:00": [],
        "14:00": [],
        "15:00": [],
        "16:00": []
    },
}

dentist = {
    1: {"First_Name": "Aaron", "Last_Name": "Anthony"},
    2: {"First_Name": "Brandon", "Last_Name": "Barry"},
    3: {"First_Name": "Cole", "Last_Name": "Cook"},
    4: {"First_Name": "Donte", "Last_Name": "Divincenzo"},
    5: {"First_Name": "Edward", "Last_Name": "Edwards"},
    6: {"First_Name": "Franklin", "Last_Name": "Fox"},
    7: {"First_Name": "Gideon", "Last_Name": "Garrett"},
    8: {"First_Name": "Harry", "Last_Name": "Harrison"},
    9: {"First_Name": "Inigo", "Last_Name": "Ingram"},
    10: {"First_Name": "Jackson", "Last_Name": "Jackson"}
}

room = {
    1: [],
    2: [],
    3: []
}

patient_id = 0

print("\nDental Clinic Information System\n")

def clinic():
    global patient_id
    patient_inquiry = True
    while patient_inquiry:
        patient_id += 1
        patient_first_name = input("Patient First Name: ")
        patient_last_name = input("Patient Last Name: ")
        patient_preferred_day = input("Patient's preferred day of appointment (Sun, Mon, Tues, Wed, Thurs, Fri, Sat): ")
        patient_preferred_time = input("Patient's preferred time on chosen day (HH:MM): ")
        
        if sched_check(patient_preferred_day, patient_preferred_time):
            nonbooked_dentists = []
            for i, dentist_info in dentist.items():
                availability = True
                for existing_appointment in clinic_schedule[patient_preferred_day][patient_preferred_time]:
                    if existing_appointment.startswith(f"Booked: Dentist: {dentist_info['First_Name']} {dentist_info['Last_Name']}"):
                        availability = False
                        break
                if availability:
                    nonbooked_dentists.append((i, dentist_info))
            
            if nonbooked_dentists:
                print("Available dentists:")
                for id, dentist_information in nonbooked_dentists:
                    print(f"{id}: {dentist_information['First_Name']} {dentist_information['Last_Name']}")
                dentist_choice = int(input("Enter the number of your preferred dentist: "))
                if dentist_choice in dentist:
                    details = f"Booked: {patient_first_name} {patient_last_name}, Dentist: {dentist[dentist_choice]['First_Name']} {dentist[dentist_choice]['Last_Name']}"
                    appointment(patient_preferred_day, patient_preferred_time, details)
                else:
                    print("No such dentist in the database.")
            else:
                print("No dentists.")
        else:
            print("Unfortunately, schedule is ful")

        patient_inquiry = input("Do you want to schedule another appointment? (yes/no): ").lower().startswith('yes')

    print("\nFor demonstration purposes, print the schedule to show data is retained:")
    for day, appointments in clinic_schedule.items():
        print(day)
        for time_slot, bookings in appointments.items():
            print(f"  {time_slot}: {bookings}")

    return clinic_schedule

def sched_check(patient_preferred_day, patient_preferred_time):
    if patient_preferred_day in clinic_schedule and patient_preferred_time in clinic_schedule[patient_preferred_day]:
        if len(clinic_schedule[patient_preferred_day][patient_preferred_time]) < 3:
            return True
    return False

def appointment(day, time_slot, details):
    global room

    existing_bookings = clinic_schedule[day][time_slot]
    available_rooms = [room_num for room_num, bookings in room.items() if len(bookings) < 3]
    
    if available_rooms:
        room_num = available_rooms[0]
        room[room_num].append(details)
        print(f"Thank you for booking an appointment :)! Here is your room number: {room_num}")
    else:
        print("Sorry, there is no room for the booking.")

    clinic_schedule[day][time_slot].append(details)
    
    return clinic_schedule

clinic()
