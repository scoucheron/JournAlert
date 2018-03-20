
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


def createEmployee():
    '''
    Create a employee
        Input:
            @employee_id
    '''
    c.execute("INSERT INTO employees VALUES (employee_id)")
    c.execute("INSERT INTO employees VALUES (?)", (employee_id))


def deletePatient():
    '''
    Delete an appointment from the schedule
        Input:
            @patient_id
    '''
    c.execute("INSERT INTO employees VALUES (employee_id)")
    return 0

def deleteEmployee():
    '''
    Delete an employee the schema
        Input:
            @employee_id
    '''
    return 0

def deleteAppointment():
    '''
    Delete an appointment from the schedule
        Input:
            @journal_id
        Output:
            Boolean -> If it was done or not (need an exception)
    '''
    return 0


def createEntry(patient_id, employee_id, timeFrom, timeTo):
    '''
    Create an entry in the schedule
        Input:
            @patient_id: the ID of the patient to fetch the journal from
            @employee_id: The ID for the employee which
        Output:
            An entry in the schedule containing a @patient_id, @employee_id, a time from and a time to
    '''
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
