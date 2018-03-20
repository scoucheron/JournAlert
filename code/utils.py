
def initializeDatabase():
    '''
    Initialization of the database (only have to do this once)
        ### ADD SCHEMA DESCRIPTION
    '''
    return 0

def createPatient(patient_id, name, journal_id, c):
    '''
    Create a patient with a journal (use help-function)
        Input:
            @patient_id
            @name
            @journal_id

    '''

    c.execute("INSERT INTO patients VALUES (?, ?, ?)", (patient_id, name, journal_id))
    conn.commit()

def createEmployee(employee_id, c):
    '''
    Create a employee
        Input:
            @employee_id
    '''

    c.execute("INSERT INTO employees VALUES (?)", (employee_id))
    conn.commit()

def deletePatient(patient_id, c):
    '''
    Delete an appointment from the schedule
        Input:
            @patient_id
    '''
    c.execute("DELETE patients WHERE patient_id=?", (patient_id))
    conn.commit()


def deleteEmployee(employee_id, c):
    '''
    Delete an employee the schema
        Input:
            @employee_id
    '''

    c.execute("DELETE employees WHERE employee_id=?", (employee_id))
    conn.commit()

def deleteAppointment(journal_id, c):
    '''
    Delete an appointment from the schedule
        Input:
            @journal_id
        Output:
            Boolean -> If it was done or not (need an exception)
    '''

    c.execute("DELETE schedules WHERE journal_id=?", (journal_id))
    conn.commit()

def createEntry(patient_id, employee_id, timeFrom, timeTo):
    '''
    Create an entry in the schedule
        Input:
            @patient_id: the ID of the patient to fetch the journal from
            @employee_id: The ID for the employee which
        Output:
            An entry in the schedule containing a @patient_id, @employee_id, a time from and a time to
    '''

    c.execute("INSERT INTO schedules VALUES (?, ?)", (patient_id, employee_id))
    conn.commit()

    return 0

def printRedEntries():
    '''
    Prints all the red entries
        Input: Log
    '''
    return 0

def printOrangeEntries():
    '''
    Prints all the orange entries
        Input: Log
    '''
    return 0

def printGreenEntries():
    '''
    Prints all the green entries
        Input: Log
    '''
    return 0
