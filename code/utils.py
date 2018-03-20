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

<<<<<<< HEAD
def createPatient(patient_id, name, journal_id, c):
=======

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
>>>>>>> cb3153e5ac707b4867b09c59d9134e27b83b31a8
    '''
    Create a patient with a journal (use help-function)
        Input:
            @patient_id
            @name
            @journal_id

    '''
<<<<<<< HEAD
=======


    return 0
>>>>>>> cb3153e5ac707b4867b09c59d9134e27b83b31a8

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
    print "lol"

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
