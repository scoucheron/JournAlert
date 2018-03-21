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

	# Find the journal of the given patients
		# SELECT * FROM journals WHERE patient_id=? (patient_id,)


	# Take the time it is fetched


	# Write to a log -> HOW TO LOG? Log has: patient_id, journal_id (?), employee_id, timeStamp (Time fetched)


	# Returns the journal

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


def returnAccessed(patient_id):
	'''
	Fetches a patients accessed journal and who has accessed them
		Input:
			@patient_id: the ID of a patient
		Output:
			Every access of the journal and who accessed it
	'''

	return 0

def main(num_client):
	return 0


if __name__ == '__main__':
	# Find the wanted size of the cluster as a command line argument
	try:
		num_client = int(sys.argv[1])
	except:
		sys.exit("The arguments are as follows (both as given as integers): \n \t size: the size of the paxos cluster \n \t treshold: upper threshold of concurrent clients\n\n  Example: ./env 3 4 \t will run the evaluation with a cluster size of 3 and threshold 4")

	main(num_client)
