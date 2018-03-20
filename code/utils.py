import sqlite3

# conn = sqlite3.connect('journalert.db')
# c = conn.cursor()



def initializeDatabase(c):
    '''
    Initialization of the database (only have to do this once)
        ### ADD SCHEMA DESCRIPTION
    '''

    c.execute("""CREATE TABLE patients(id integer PRIMARY KEY, name text, journal text)""")
    c.execute("""CREATE TABLE employees(id integer PRIMARY KEY)""")
    c.execute("""CREATE TABLE schedule(patient_id integer, employee_id integer, time_start text, time_end text,
                FOREIGN KEY(patient_id) REFERENCES patient(id)),
                FOREIGN KEY(emplyee_id) REFERENCES employee(id)""")
    c.execute("""CREATE TABLE journals(patient_id integer,
                FOREIGN KEY(patient_id) REFERENCES patient(id))""")


    conn.commit()



    #Database for the logEntry
    conn_log = sqlite3.connect('log.db')
    c_log = conn_log.cursor()

    c_log.execute("""CREATE TABLE entries(patient_id, employee_id, timestamp)""")


    return 0

def createPatient(c):
    '''
    Create a patient with a journal (use help-function)
        Input:
            @patient_id
            @name
            @journal_id

    '''
    return 0

def createEmployee(c):
    '''
    Create a employee
        Input:
            @employee_id
    '''
    return 0

def deletePatient(c):
    '''
    Delete an appointment from the schedule
        Input:
            @patient_id
    '''
    return 0

def deleteEmployee(c):
    '''
    Delete an employee the schema
        Input:
            @employee_id
    '''
    return 0

def deleteAppointment(c):
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
