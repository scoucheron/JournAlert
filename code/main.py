from utils import *
import os
from datetime import datetime, timedelta
import time

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


def checkLog(delta):
	'''
		Goes through the log and checks if it si a red, orange or green entry.
		A green entry: the entry was ok (Nothing wrong)
		An orange entry: the journal was accessed, but not within the scheduled time (Something might be wrong)
		A red entry: The journal was accessed when there was no relation between the patient and employee (Something was wrong)
		Input:
			Number of hours accepted-->yellow
		Output:
			Prints the number of green, orange and red entries
	'''


	conn_log = sqlite3.connect('log.db')
	c_log = conn_log.cursor()
	conn = sqlite3.connect('journalert.db')
	c = conn.cursor()

	count = 0
	no_schedules = 0;
	for row in c_log.execute("SELECT * from entries WHERE warning_level='%s'" % 'BLACK'):
		entryTime = row[2]
		patient_id = row[0]
		employee_id = row[1]
		print(entryTime + ":00")
		entry_datetime = time.strptime(entryTime, "%d.%m.%Y %H:%M")
		# print(entry_datetime)
		# entry_datetime.tm_hour =  12
		# print(deltaFrom)
		# deltaTo = 0
		print("NOW:",datetime.now() + timedelta(hours = 2))

		# print(entry_datetime + timedelta(hours=2))

		for row in c.execute("SELECT * FROM schedules WHERE patient_id = ? AND employee_id = ?", (patient_id,employee_id)):
			no_schedules = 1
			timeFrom = row[3]
			timeTo = row[4]

			appointment_datetime_from = time.strptime(timeFrom, "%d.%m.%Y %H:%M")
			appointment_datetime_to = time.strptime(timeTo, "%d.%m.%Y %H:%M")

			if entry_datetime >= appointment_datetime_from and entry_datetime <= appointment_datetime_to:
				 # It's GREEN!
				 print("GREEN")

			# if entry_datetime >= (appointment_datetime_from + delta) and entry_datetime <= (appointment_datetime_to + delta):
			# 	# it's YELLOW
			# 	print("YELLOw")

		if(no_schedules == 1):
			# No existing schedule
			# It's RED!
			print("RED")







def returnAccessed(patient_id):
	'''
	Fetches a patients accessed journal and who has accessed them
		Input:
			@patient_id: the ID of a patient
		Output:
			Every access of the journal and who accessed it
	'''

	return 0


def main():
	# os.remove('journalert.db')
	# os.remove('log.db')
	# initializeDatabase()
	# fillJournAlert(500, 200, 300)
	# fillLog(100, 90, 5, 5)
	checkLog(24)


if __name__ == '__main__':
	main()
