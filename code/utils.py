import sqlite3
from time import strftime

# conn = sqlite3.connect('journalert.db')
# c = conn.cursor()



def initializeDatabase(c):
    '''
    Initialization of the database (only have to do this once)
        ### ADD SCHEMA DESCRIPTION
    '''

    c.execute("""CREATE TABLE patients(id integer PRIMARY KEY, name text, journal text)""")
    c.execute("""CREATE TABLE employees(id integer PRIMARY KEY)""")
    c.execute("""CREATE TABLE schedule(id integer PRIMARY KEY, patient_id integer, employee_id integer, date text, timeFrom text, timeTo text,
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
        createPatient(i, c)

    for i in range(employee_number):
        createPatient(i,c)

    year        = "2018"
    month       = "05"
    day         = "01"
    hourFrom    = "00"
    minFrom     = "00"
    minTo       = "00"

    # TO DO: make employees that haas no appointments
    for i in range(schedule_number):
        # choose random patients
        patient = random.randint(0, patient_number-1)
        # choose random employee
        employee = random.randint(0, employee_number-1)

        # new day
        if int(hourFrom) == 23:
            minTo = "59"
            hourTo = hourFrom
        else:
            hourTo = str(int(hourFrom)+1)

        if int(hourFrom) <= 9 and hourFrom != "00": x = "0"
        else: x = ""

        if int(hourTo) <= 9: y = "0"
        else: y = ""

        if int(month) <= 9: z = "0"
        else: y = ""

        if int(day) <= 9: k = "0"
        else: k = ""

        date        = k + day + "." + z + month + "." + year + " "
        timeFrom    = x + str(hourFrom) + ":" + str(minFrom)
        timeTo      = y + str(hourTo) + ":" + str(minTo)

        createAppointment(patient, employee, date+timeFrom, date+timeTo)

        # Move time to next appointment
        # Assume 28 days in every month

        # New day
        if int(hourFrom) == 23:
            hourFrom = "00"
            minTo = "00"
            day = str(int(day)+1)

            # New month
            if int(day) == 28:
                day = "1"
                month = str(int(month)+1)
            # New year
            if month == "12":
                month = "1"
                year = str(int(year)+1)

        else:
            hourFrom = str(int(hourFrom) + 1)





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


    return 0

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

def createAppointment(patient_id, employee_id, timeFrom, timeTo):
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
