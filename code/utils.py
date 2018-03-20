import sqlite3

def initializeDatabase():
    '''
    Initialization of the database (only have to do this once)
        ### ADD SCHEMA DESCRIPTION
    '''
    return 0

def fillWithFakeData():
    '''
    Fills the database with fake data
        Input:

    '''
def createPatient():
    '''
    Create a patient with a journal (use help-function)
        Input:
            @patient_id
            @name
            @journal_id

    '''
    return 0

def createEmployee():
    '''
    Create a employee
        Input:
            @employee_id
    '''
    return 0

def deletePatient():
    '''
    Delete an appointment from the schedule
        Input:
            @patient_id
    '''
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

def printLogEntry(color):
    '''
    Prints all the red entries
        Input: Color of wanted entries

        Colors:
            GREEN == 1
            ORANGE == 2
            RED == 3
    '''

    # Make sure the color is correct and that there will be no errors
    if(color == 1):
        symbol = ('GREEN',)
    elif(color == 2):
        symbol = ('ORANGE',)
    elif(color == 3):
        symbol = ('RED',)
    else:
        print("Input color was wrong. (Has to be green [1], orange [2] or red [3]")
        return 0

    # Create a connection to the log database
    conn = sqlite3.connect('log.db')
    c. = conn.cursor()

    # Fetch all entries in the log with a given warning level (gree,orange,red) and print them
    print(x.fetchall())
    for row in c.execute('SELECT * FROM entries WHERE warning_level=?', symbol)
        print(row)

    # Close the connection
    conn.close()
