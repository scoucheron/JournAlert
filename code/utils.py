import sqlite3
import sys

def initializeDatabase(c):
    '''
    Initialization of the database (only have to do this once)
        ### ADD SCHEMA DESCRIPTION
    '''

    c.execute("""CREATE TABLE patients(id integer PRIMARY KEY, name text, journal text)""")
    c.execute("""CREATE TABLE employees(id integer PRIMARY KEY)""")
    c.execute("""CREATE TABLE schedule(id integer PRIMARY KEY, patient_id integer, employee_id integer, time_start text, time_end text,
                FOREIGN KEY(patient_id) REFERENCES patient(id)),
                FOREIGN KEY(emplyee_id) REFERENCES employee(id)""")
    c.execute("""CREATE TABLE journals(patient_id integer,
                FOREIGN KEY(patient_id) REFERENCES patient(id))""")
    # Save the changes
    c.commit()

    #Close the connection
    c.close()

    #Database for the logEntry
    conn_log = sqlite3.connect('log.db')
    c_log = conn_log.cursor()

    c_log.execute("""CREATE TABLE entries(patient_id, employee_id, timestamp)""")

    #Save the changes
    c_log.commit()

    #Close the connection
    conn_log.close()
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

    conn = sqlite3.connect('log.db)')


def fillLog(entry_number, green_percentage, orange_percentage, red_percentage):
    '''
    NB! HAS TO BE CALLED AFTER journalert.db IS FILLED
    NB2! percentages has to be 100 in total

    Fills the log databse with fake data (only have to do this once)
        Input:
            @entries: how many entries in the log that is to be created
            @green_percentage: percentage of green entries
            @orange_percentage: percentage of orange entries
            @red_percentage: percentage of red entries
    '''

    # Calculate how many of each entry there is
    total_percentage = green_percentage + orange_percentage + red_percentage

    # Has to be 100% in total
    if(total_percentage != 100):
        sys.exit("The given percentages did not add up to 100")

    number_green = entry_number * (green_percentage/100)
    number_orange = entry_number * (orange_percentage/100)
    number_red = entry_number * (red_percentage/100)


    # Open a connection to the log
    conn_log = sqlite3.connect('log.db')
    c_log = conn_log.cursor()

    # Open a connection to the JournAlert database
    conn = sqlite3('journalert.db')
    c = c.cursor()

    # Create green entries
    for x in range(number_green):
        c.execute('SELECT * FROM schedule')
        # Fetch an entry
        appoint = c.fetchone()

        # Create an entry in the log with the correct time of checking the journal
        createLogEntry(appoint[2], appoint[3], appoint[4], conn_log, c_log)

    # Create orange entries
    for x in range(number_orange):
        createLogEntry(patient_id, employee, time_now,, conn_log, c_log)

    # Create red entries
    for x in range(number_red):
        createLogEntry(patient_id, employee, time_now,, conn_log, c_log)


def createPatient(patient_id, name, journal_id, conn, c):
    '''
    Create a patient with a journal (use help-function)
        Input:
            @patient_id
            @name
            @journal_id

    '''
    c.execute("INSERT INTO patients VALUES (?, ?, ?)", (patient_id, name, journal_id))
    conn.commit()

    c.execute("SELECT id FROM patients WHERE id = ?", (patient_id))
    data = c.fetchone()
    if data is None:
        return False
    else:
        return True

def createEmployee(employee_id, conn, c):
    '''
    Create a employee
        Input:
            @employee_id
    '''

    c.execute("INSERT INTO employees VALUES (?)", (employee_id))
    conn.commit()

    c.execute("SELECT id FROM employees WHERE id = ?", (employee_id))
    data = c.fetchone()
    if data is None:
        return False
    else:
        return True

def deletePatient(patient_id, conn, c):
    '''
    Delete an appointment from the schedule
        Input:
            @patient_id
    '''
    c.execute("DELETE patients WHERE id=?", (patient_id))
    conn.commit()

    ''' asserting that the row has been deleted '''
    c.execute("SELECT id FROM patients WHERE id = ?", (patient_id))
    data = c.fetchone()
    if data is None:
        return True
    else:
        return False

def deleteEmployee(employee_id, conn, c):
    '''
    Delete an employee the schema
        Input:
            @employee_id
    '''

    c.execute("DELETE employees WHERE id=?", (employee_id))
    conn.commit()

    ''' asserting that the row has been deleted '''
    c.execute("SELECT id FROM employees WHERE id = ?", (employee_id))
    data = c.fetchone()
    if data is None:
        return True
    else:
        return False


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

def createAppointment(patient_id, employee_id, timeFrom, timeTo, conn, c):
    '''
    Create an entry in the schedule
        Input:
            @patient_id: the ID of the patient to fetch the journal from
            @employee_id: The ID for the employee
        Output:
            An entry in the schedule containing a @patient_id, @employee_id, a time from and a time to
    '''

    c.execute("INSERT INTO schedules VALUES (?, ?, ?, ?)", (patient_id, employee_id, timeFrom, timeTo))
    conn.commit()


def createLogEntry(patient_id, employee_id, timestamp, conn, c):
    '''
    Create an entry in the log
        Input:
            @patient_id: the ID of the patient to fetch the journal from
            @employee_id: The ID for the employee
            @timestamp:  Date and time
        Output:
            An entry in the log containing @patient_id, @employee_id, @timestamp
    '''
    c.execute("INSERT INTO entries VALUES (?, ?, ?)", (patient_id, employee_id, timestamp))
    conn.commit()




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
