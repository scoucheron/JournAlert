from utils import *
import os
from datetime import datetime, timedelta
import multiprocessing

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
		print ("Not a valid employee")
		return False

	c.execute('SELECT * from journals WHERE patient_id = ?', (patient_id,))

	time_now = datetime.datetime.now().replace(microsecond=0)
	createLogEntry(patient_id, employee_id, time_now, conn2, c2, 4)

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
	for row in c_log.execute("SELECT * from entries WHERE warning_level='%s'" % 'BLACK'):
		assign_colour = ""
		no_schedules = 0;
		entryTime = row[2]
		patient_id = row[0]
		employee_id = row[1]
		entry_datetime = datetime.strptime(entryTime, "%Y-%m-%d %H:%M:%S")

		for row in c.execute("SELECT * FROM schedules WHERE patient_id = ? AND employee_id = ?", (patient_id,employee_id)):
			no_schedules = 1
			timeFrom = row[3]
			timeTo = row[4]

			time = timeFrom.split(' ')[1]
			date = timeFrom.split(' ')[0]


			appointment_datetime_from = datetime.strptime(timeFrom, "%Y-%m-%d %H:%M:%S")
			appointment_datetime_to = datetime.strptime(timeTo, "%Y-%m-%d %H:%M:%S")

			if entry_datetime >= (appointment_datetime_from - timedelta(hours=delta)) and entry_datetime <= (appointment_datetime_to + timedelta(hours=delta)):
				assign_colour = "GREEN"

			else:
				assign_colour = "YELLOW"


		if(no_schedules == 0):
			# No existing schedule --> no relation between employee and patient in schedule
			# It's RED!
			assign_colour = "RED"

		c_log.execute("UPDATE entries SET warning_level = ? WHERE patient_id = ? and employee_id = ? AND ts = ?", (assign_colour, patient_id, employee_id, entryTime))

	conn_log.commit()
	conn_log.close()

def printWarningLevels():

	greens = 0
	yellows = 0
	reds = 0
	blacks = 0

	conn = sqlite3.connect('log.db')
	c = conn.cursor()

	c.execute("SELECT * FROM entries")

	entries = c.fetchall()

	for i in entries:
		if(i[3] == "RED"):
			reds = reds + 1
		elif(i[3] == "YELLOW"):
			yellows = yellows + 1
		elif(i[3] == "GREEN"):
			greens = greens + 1
		elif(i[3] == "BLACK"):
			blacks = blacks + 1


	print("GREEN:	", greens)
	print("YELLOW:	", yellows)
	print("REDS:	", reds)
	print("BLACKS:	", blacks)

	conn.commit()
	conn.close()
	
def returnAccessed(patient_id, start_date, end_date=datetime.now().replace(microsecond=0)):
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


def main(num_client):
	# os.remove('journalert.db')
	# os.remove('log.db')

	number_request = num_client * 100

	random_ids = []

	for x in range(number_request):
		tup = (random.randint(1,1000), random.randint(1,1000))
		random_ids.append(tup)

	p = multiprocessing.Pool(num_client)
	p.starmap(fetchJournal, random_ids)



if __name__ == '__main__':
	# Find the wanted size of the cluster as a command line argument
	try:
		num_client = int(sys.argv[1])
	except:
		sys.exit("Argument is as follows \n \t number of clients \n\t \t \n Usage: python3 main.py 5")

	main(num_client)
