''' Created by Sverre Coucheron for paxos-assignment '''
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import sys, os, time
import subprocess as sp
from utils import *
from main import *

NTEST = 5

def run_correctness_test():
    # Percentages of
    number_fetches = 1000
    green_percentage = 80
    yellow_percentage = 10
    red_percentage = 10

    # The percantes above gives the following numbers
    correct_green = number_fetches*(green_percentage/100)
    correct_yellow = number_fetches*(yellow_percentage/100)
    correct_red = number_fetches*(red_percentage/100)


    # Delete log database is it already exists
    try:
        os.remove('log.db')
    except OSError:
        pass

    # Delete journalert database if it already exists
    try:
        os.remove('journalert.db')
    except OSError:
        pass


    #Initialize
    initializeJournAlertDatabase()
    initializeLogDataBase()
    fillJournAlert(50,20,30)
    fillLog(number_fetches, green_percentage, yellow_percentage, red_percentage)
    checkLog(2)
    green, yellow, red, black = printWarningLevels()

    calculated_green = correct_green - green
    calculated_yellow = correct_yellow - yellow
    calculated_red = correct_red - red

    print("Log entries: ", 10)
    print("Percentages: \n \t green [%d percent] \n\t yellow [%d percent] \n\t red [%d percent] " % (green_percentage, yellow_percentage, red_percentage))
    print("This should give the following number of colors:  \n\t green: %d \n\t yellow: %d \n\t red: %d " % (correct_green, correct_yellow, correct_red))
    print("\n\n The values we got when testing: \n\t green: %d \n\t yellow: %d \n\t red: %d " % (green, yellow, red ))
    print("With the missed calculations of :  \n\t green: %d \n\t yellow: %d \n\t red: %d " % (calculated_green, calculated_yellow, calculated_red ))

def run_stress_test(num_client):
    result_list = np.array([])
    stdR_list = np.array([])

    f = open("data.txt", "w")

    # Delete log database is it already exists
    try:
        os.remove('log.db')
    except OSError:
        pass

    # Delete journalert database if it already exists
    try:
        os.remove('journalert.db')
    except OSError:
        pass

    initializeJournAlertDatabase()
    fillJournAlert(500, 200, 300)

    # For each client 'step' we spawn a subprocess which will handle it
    for x in range(num_client):
        for each in range(NTEST):
            initializeLogDataBase()

            # Start a subprocess
            p1 = sp.Popen(['python3', 'main.py', str(x+1)])

            # Wait for above subprocess to finish running
            p1.wait()

            # check how many was logged
            conn = sqlite3.connect('log.db')
            c = conn.cursor()
            c.execute('SELECT * FROM entries ORDER BY ts ASC')
            data = c.fetchall()

            # Set the start and end time
            time1 = data[0][2]
            time2 = data[len(data)-1][2]

            # Convert the time (they are string) into a datetime object
            datetime_object1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
            datetime_object2 = datetime.datetime.strptime(time2, '%Y-%m-%d %H:%M:%S')

            # Calculate the time spent sending
            total_time = (datetime_object2-datetime_object1).total_seconds()
            throughput = int(len(data)/total_time)

            with open('data.txt', 'a') as outfile:
                outfile.write(str(throughput))
                outfile.write("\n")
            # Remove the log database for further testing
            os.remove('log.db')

        # Fetch the data from the file
        print("Fetching the data for client ", x+1)

        with open('data.txt') as datafile:
            int_list = [int(i) for i in datafile]



        #Calculate the mean value and the standardeviation
        mean, stdR = calculate_std_mean(int_list)
        time.sleep(1)

        #Append the result (mean) to the result list so it can be plotted
        result_list = np.append(result_list, mean)
        stdR_list = np.append(stdR_list, stdR)
        #Since we want to reset the file we can delete it now
        os.remove('data.txt')

    # Plot the result in PDF
    logged_employee_print(result_list, num_client, stdR_list)


def logged_employee_print(resultList, number_clients, stdR_list):
    '''
        Plot the results and save them to a file
            @ Input:
            @ Output: a graph with the given results given as a pdf-file
    '''

    # Create a list from 0 to the number of number_clients
    clients = np.arange(1, number_clients+1)

    f = plt.figure()
    ax = plt.gca()
    ax.yaxis.grid(True)

    # Label the above the figure, on x-axis and on y-axis
    plt.ylabel('Logged employee visits per second')
    plt.xlabel('# of concurrent clients')

    # Plot the result
    plt.plot(clients, resultList)

    # Force the x-axis to be only integers
    plt.xticks(clients)

    # Errorbar
    plt.errorbar(clients, resultList, stdR_list,  marker='o', color='red')

    plt.xlim(0.95, number_clients+1)
    plt.show()

    #Save the graph to a pdf
    f.savefig("logged_per_second.pdf", bbox_inches='tight')

def calculate_std_mean(data):
    '''
        Calculates the given datas mean and standardeviation
            @ Input: All the data from a given number of clients in the test to find the STD and mean
            @ Output: mean and standardeviation from the data
    '''
    # take away any values that are possibly too huge or low (extreme values)
    data.sort()
    data = data[1:-1]
    stdR = np.std(data)
    mean = np.mean(data)
    return mean, stdR


if __name__=='__main__':
    # Find the wanted size of the cluster as a command line argument
    try:
        num_client = int(sys.argv[1])
    except:
        sys.exit("Argument is as follows \n \t number of clients \n\t \t \n Usage: python3 main.py 5")

    run_correctness_test()
    # run_stress_test(num_client)
