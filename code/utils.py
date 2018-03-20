import sqlite3

def initializeDatabase():
    '''
    Initialization of the database (only have to do this once)
        ### ADD SCHEMA DESCRIPTION
    '''
    return 0


def fillJournAlert(patient_number, schedule_number, employee_number):
    '''
    Fills the log databse with fake data (only have to do this once)
        Input:
            @conn: a connection to the JournAlert database
            @patient_number: number of patients to add (has to be equal to number of journals)
            @schedule_number: number of appointments to create (less than patients)
            @employee_number: number of employees to create (less than patients)
    '''


def fillLog(entry_number, green_percentage, orange_percentage, red_percentage):
    '''
    NB! HAS TO BE CALLED AFTER journalert.db IS FILLED
    Fills the log databse with fake data (only have to do this once)
        Input:
            @entries: how many entries in the log that is to be created
            @green_percentage: percentage of green entries
            @orange_percentage: percentage of orange entries
            @red_percentage: percentage of red entries

    '''


def createPatient():
    '''
    Create a patient with a journal (use help-function)
        Input:
            @patient_id
            @name
            @journal_id

    '''
    c.execute("INSERT INTO patients VALUES (?, ?, ?)", (patient_id, name, journal_id))
    conn.commit()

def createEmployee(employee_id, conn, c):
    '''
    Create a employee
        Input:
            @employee_id
    '''

    c.execute("INSERT INTO employees VALUES (?)", (employee_id))
    conn.commit()

def deletePatient(patient_id, conn, c):
    '''
    Delete an appointment from the schedule
        Input:
            @patient_id
    '''
    c.execute("DELETE patients WHERE patient_id=?", (patient_id))
    conn.commit()


def deleteEmployee(employee_id, conn, c):
    '''
    Delete an employee the schema
        Input:
            @employee_id
    '''

    c.execute("DELETE employees WHERE employee_id=?", (employee_id))
    conn.commit()

def deleteAppointment(appointment_id, conn, c):
    '''
    Delete an appointment from the schedule
        Input:
            @journal_id
        Output:
            Boolean -> If it was done or not (need an exception)
    '''

    c.execute("DELETE schedules WHERE id=?", (appointment_id))
    conn.commit()

def createEntry(patient_id, employee_id, timeFrom, timeTo, conn, c):
    '''
    Create an entry in the schedule
        Input:
            @patient_id: the ID of the patient to fetch the journal from
            @employee_id: The ID for the employee which
        Output:
            An entry in the schedule containing a @patient_id, @employee_id, a time from and a time to
    '''

    c.execute("INSERT INTO schedules VALUES (?, ?, ?, ?)", (patient_id, employee_id, timeFrom, timeTo))
    conn.commit()

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
