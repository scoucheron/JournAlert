import sqlite3
import sys
import os
import random
import datetime

def initializeDatabase():
    '''
    Initialization of the database (only have to do this once)
        ### ADD SCHEMA DESCRIPTION
    '''
    conn = sqlite3.connect('journalert.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE patients(patient_id integer PRIMARY KEY, name text, journal_id integer, FOREIGN KEY(journal_id) REFERENCES journal(patient_id))""")
    c.execute("""CREATE TABLE employees(id integer PRIMARY KEY)""")
    c.execute("""CREATE TABLE schedules(id integer PRIMARY KEY, patient_id integer, employee_id integer, timeFrom text, timeTo text, FOREIGN KEY(patient_id) REFERENCES patients(id), FOREIGN KEY(employee_id) REFERENCES employee(id))""")
    c.execute("""CREATE TABLE journals(patient_id integer PRIMARY KEY , FOREIGN KEY(patient_id) REFERENCES patients(id))""")

    # Save the changes
    conn.commit()

    #Database for the logEntry
    conn_log = sqlite3.connect('log.db')
    c_log = conn_log.cursor()

    c_log.execute("""CREATE TABLE entries(entry_id integer PRIMARY KEY, patient_id, employee_id, ts timestamp, warning_level text)""")

    #Save the changes
    conn_log.commit()

    #Close the connection
    c_log.close()
    c.close()
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

    conn = sqlite3.connect('journalert.db')
    c = conn.cursor()

    for i in range(patient_number):
        createPatient(i, str(i), i, conn, c)

    for i in range(employee_number):
        createEmployee(i, conn, c)

    year        = 2018
    month       = 5
    day         = 1
    hourFrom    = 00
    minFrom     = 00
    minTo       = 00

    # TO DO: make employees that haas no appointments
    for i in range(schedule_number):
        # choose random patients
        patient = random.randint(0, patient_number-1)
        # choose random employee
        employee = random.randint(0, employee_number-1)

        # new day
        if hourFrom == 23:
            minTo = 59
            hourTo = hourFrom
        else:
            hourTo = hourFrom+1

        start = datetime.datetime(year, month, day, hourFrom, minFrom)
        end = datetime.datetime(year, month, day, hourTo, minTo)

        createAppointment(i, patient, employee, start, end, conn, c)

        # Move time to next appointment
        # Assume 28 days in every month

        # New day
        if hourFrom == 23:
            hourFrom = 00
            minTo = 00
            day = day+1

            # New month
            if day == 28:
                day = 1
                month = month+1
            # New year
            if month == 12:
                month = 1
                year = year+1

        else:
            hourFrom = hourFrom + 1






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

    number_green = int(entry_number * (green_percentage/100))
    number_orange = int(entry_number * (orange_percentage/100))
    number_red = int(entry_number * (red_percentage/100))

    conn_log = sqlite3.connect('log.db')
    c_log = conn_log.cursor()

    # Open a connection to the JournAlert database
    conn = sqlite3.connect('journalert.db')
    c = conn.cursor()
    entry_id = 0
    # Create green entries
    for x in range(number_green):
        c.execute('SELECT * FROM schedules')
        # Fetch an entry
        all_appoint = c.fetchmany(number_green)
        # Create an entry in the log with the correct time of checking the journal
        createLogEntry(entry_id, all_appoint[x][1], all_appoint[x][2], all_appoint[x][3], conn_log, c_log, 4)
        entry_id = entry_id + 1

    # Create orange entries
    for x in range(number_orange):
        c.execute('SELECT * FROM schedules')
        # Fetch an entry
        all_appoint = c.fetchmany(number_green)
        # Create an entry in the log with the correct time of checking the journal
        createLogEntry(entry_id, all_appoint[x][1], all_appoint[x][2], all_appoint[x][3], conn_log, c_log, 4)
        entry_id = entry_id + 1

    # Create red entries
    for x in range(number_red):
        c.execute('SELECT patient_id FROM patients WHERE NOT EXISTS ( SELECT * FROM schedules)')
        appoint = c.fetchone()
        c.execute('SELECT * from employees')
        e_id = c.fetchone()
        # Create an entry in the log with the correct time of checking the journal
        createLogEntry(entry_id, 1, 1, '2018-03-20 14:00:00', conn_log, c_log, 4)
        entry_id = entry_id + 1


def createPatient(patient_id, name, journal_id, conn, c):
    '''
    Create a patient with a journal (use help-function)
        Input:
            @patient_id
            @name
            @journal_id
            @conn (Connection)
            @c    (Cursor)
        Output:
            Boolean -> successfull or not successfull
    '''
    c.execute("INSERT INTO patients VALUES (?, ?, ?)", (patient_id, name, journal_id))
    conn.commit()
    createJournal(patient_id, conn, c)


    ''' asserting that the entry has been created '''
    c.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
    data = c.fetchone()
    if data is None:
        return False
    else:
        return True



def createJournal(patient_id, conn, c):
    '''
    Creates a journal entry for a patient
        Input:
            @patient_id
            @conn (Connection)
            @c    (Cursor)
        Output:
            Boolean -> successfull or not successfull
    '''
    c.execute("INSERT INTO journals VALUES (?)", (patient_id,))
    conn.commit()

    ''' asserting that the entry has been created '''
    c.execute("SELECT * FROM journals WHERE patient_id = ?", (patient_id,))
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
            @conn (Connection)
            @c    (Cursor)
        Output:
            Boolean -> successfull or not successfull
    '''

    c.execute("INSERT INTO employees VALUES (?)", (employee_id,))
    conn.commit()

    ''' asserting that the entry has been created '''
    c.execute("SELECT id FROM employees WHERE id = ?", (employee_id,))
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
            @conn (Connection)
            @c    (Cursor)
        Output:
            Boolean -> successfull or not successfull
    '''
    c.execute("DELETE patients WHERE patient_id=?", (patient_id))
    conn.commit()

    ''' asserting that the row has been deleted '''
    c.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
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
            @conn (Connection)
            @c    (Cursor)
        Output:
            Boolean -> successfull or not successfull
    '''

    c.execute("DELETE employees WHERE id=?", (employee_id))
    conn.commit()

    ''' asserting that the entry has been deleted '''
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
            @conn (Connection)
            @c    (Cursor)
        Output:
            Boolean -> successfull or not successfull
    '''

    c.execute("DELETE schedules WHERE id=?", (appointment_id))
    conn.commit()

    ''' asserting that the entry has been deleted '''
    c.execute("SELECT id FROM schedules WHERE id = ?", (appointment_id))
    data = c.fetchone()
    if data is None:
        return True
    else:
        return False

def createAppointment(appointment_id, patient_id, employee_id, timeFrom, timeTo, conn, c):
    '''
    Create an entry in the schedule
        Input:
            @patient_id: the ID of the patient to fetch the journal from
            @employee_id: The ID for the employee
            @timeFrom
            @timeTo
            @conn (Connection)
            @c    (Cursor)
        Output:
            An entry in the schedule containing a @patient_id, @employee_id, a time from and a time to
    '''

    c.execute("INSERT INTO schedules VALUES (?, ?, ?, ?, ?)", (appointment_id ,patient_id, employee_id, timeFrom, timeTo))
    conn.commit()


def createLogEntry(entry_id, patient_id, employee_id, ts, conn, c, color):
    '''
    Create an entry in the log
        Input:
            @patient_id: the ID of the patient to fetch the journal from
            @employee_id: The ID for the employee
            @timestamp:  Date and time
            @conn (Connection)
            @c    (Cursor)
        Output:
            An entry in the log containing @patient_id, @employee_id, @timestamp
    '''
    if(color == 1):
        warning_level = ('GREEN',)
    elif(color == 2):
        warning_level = ('YELLOW',)
    elif(color == 3):
        warning_level = ('RED',)
    elif(color == 4):
        warning_level = ('BLACK',)
    else:
        sys.exit("Input color was wrong. (Has to be green [1], orange [2], red [3] or black [4]")

    c.execute("INSERT INTO entries VALUES (?, ?, ?, ?, ?)", (entry_id, patient_id, employee_id, ts, warning_level[0]))
    conn.commit()


def printLogEntry(color):
    '''
    Prints all the red entries
        Input:
            @color: a code of the urgency of a journal-check

        Colors:
            GREEN == 1
            ORANGE == 2
            RED == 3
            BLACK == 0
    '''

    # Make sure the color is correct and that there will be no errors
    if(color == 1):
        symbol = ('GREEN',)
    elif(color == 2):
        symbol = ('YELLOW',)
    elif(color == 3):
        symbol = ('RED',)
    elif(color == 4):
        symbol = ('BLACK',)
    else:
        sys.exit("Input color was wrong. (Has to be green [1], orange [2], red [3] or black [4]")

    # Create a connection to the log database
    conn = sqlite3.connect('log.db')
    c = conn.cursor()

    # Fetch all entries in the log with a given warning level (gree,orange,red) and print them
    print(c.fetchall())
    for row in c.execute('SELECT * FROM entries WHERE warning_level=?', symbol):
        print(row)

    # Close the connection
    conn.close()
