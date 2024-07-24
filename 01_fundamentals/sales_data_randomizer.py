import csv
import random
import time
import shutil
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='shuffle_log.log', level=logging.INFO,
                    format='%(asctime)s = %(levelname)s - %(message)s')

# Configuration
csv_file_path = 'sales_data.csv'
backup_directory = 'backups'
backup_interval = 10 # in seconds for demostration purposes

# Ensure the backup director exists
os.makedirs(backup_directory, exist_ok=False)

def read_csv(csv_file_path):
    with open(csv_file_path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        rows = list(reader)
    return header, rows

def write_csv(csv_file_path, header, rows):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def shuffle_csv(csv_file_path):
    try:
        # Read the original CSV
        header, rows = read_csv(csv_file_path)

        # Create a backup
        backup_path = os.path.join(backup_directory, f'{datetime.now().strftime("%Y%m%d%H%M%S")}_sales_data.csv')
        shutil.copy(csv_file_path, backup_path)
        logging.info(f'Backup created: {backup_path}')

        # Shuffle the rows
        random.shuffle(rows)

        # Write the shuffled data back to the original file
        write_csv(csv_file_path, header, rows)
        logging.info(f'CSV file {csv_file_path} shuffled successfully.')

    except Exception as e:
        logging.error(f'Error occurred while shuffling CSV: {e}')

def main():
    while True:
        shuffle_csv(csv_file_path)
        time.sleep(backup_interval)

if __name__ == "__main__":
    main()
 



