from utils import *
import os



def fetchJournal(patient_id, employee_id):
	'''
	Fetches the journal for a given patient. Only allowed if the given employee_id is an actual employee.
	If the journal is fetched it has to be written to the log
		Input:
			@patient_id: the ID of the patient to fetch the journal from
			@employee_id: The ID for the employee which
		Output:
			A journal from a patient (fetches the ID)
	'''
	conn = sqlite3.connect('journalert.db')
	c = conn.cursor()

	conn2 = sqlite3.connect('log.db')
	c2 = conn2.cursor()


	c.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
	data = c.fetchone()

	if data is None:
		print ("not a valid employee")
		return False

	c.execute('SELECT * from journals WHERE patient_id = ?', (patient_id,))

	time_now = datetime.datetime.now().replace(microsecond=0)
	createLogEntry(patient_id, employee_id, time_now, conn2, c2, 4)

	print ("log entry created")


	return 0



def checkLog():
	'''
	Goes through the log and checks if it si a red, orange or green entry.
	A green entry: the entry was ok (Nothing wrong)
	An orange entry: the journal was accessed, but not within the scheduled time (Something might be wrong)
	A red entry: The journal was accessed when there was no relation between the patient and employee (Something was wrong)

	Output:
		Prints the number of green, orange and red entries
	'''

	greens 	= 0
	yellows 	= 0
	reds 	= 0

	conn = sqlite3.connect('log.db')
	c = conn.cursor()

	for row in c.execute("SELECT * from entries WHERE warning_level='%s'" % "GREEN"):
		greens = greens + 1
	for row in c.execute("SELECT * from entries WHERE warning_level='%s'" % "YELLOW"):
		yellows = yellows + 1
	for row in c.execute("SELECT * from entries WHERE warning_level='%s'" % "RED"):
		reds = reds + 1


	print("GREEN: ", greens)
	print("YELLOW: ", yellows)
	print("RED: ", reds)
	return 0


def returnAccessed(patient_id, start_date, end_date=datetime.datetime.now().replace(microsecond=0)):
	'''
	Fetches a patients accessed journal and who has accessed them
		Input:
			@patient_id: the ID of a patient
			@start_date: Check accesses back to this date
			@end_date: Check accesses up to this date
		Output:
			Every access of the journal and who accessed it
	'''
	conn = sqlite3.connect('log.db')
	c = conn.cursor()


	c.execute("SELECT * FROM entries WHERE patient_id = ? AND ts BETWEEN ? AND ?", (patient_id, start_date, end_date))
	accesses = c.fetchall()

	return accesses


def main():
	# os.remove('journalert.db')
	# os.remove('log.db')
	# initializeDatabase()
	# fillJournAlert(500, 200, 300)
	# fillLog(100, 90, 5, 5)
	#
	# start = '2018-05-03'
	# stop = '2018-05-03 17:00:00'
	# patient = 299
	# accesses = returnAccessed(patient, start, stop)
	# print (accesses)

	checkLog()


if __name__ == '__main__':
	main()
