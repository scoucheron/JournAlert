from utils import *
import os
import datetime


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
	return 0

def logEntry(patient_id, emlpoyee_id):
	'''
	Write to the log. The log consists of a @patient_id, a @employee_id and a timestamp when it was accessed.
		Input:
			@patient_id: the ID of the patient to fetch the journal from
			@employee_id: The ID for the employee which
		Output:
			An entry in the log containing @patient_id, @employee_id and a timestamp
	'''

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

	return 0


def returnAccessed(patient_id, start_date, end_date=datetime.datetime.now()):
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

	c.execute("SELECT * FROM entries WHERE patient_id = ? AND timestamp > ? AND timestamp < ?", (patient_id, start_date, end_date))
	accesses = c.fetchall()

	return accesses


def main():
	# os.remove('journalert.db')
	# os.remove('log.db')
	# initializeDatabase()
	# fillJournAlert(500, 200, 300)
	# fillLog(100, 90, 5, 5)

	patient = 124
	date = '02.05.2018 16:00'

	accesses = returnAccessed(patient, date)
	print (accesses)


if __name__ == '__main__':
	main()
