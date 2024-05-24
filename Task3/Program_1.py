import datetime
def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def create_timestamp_file(file_path):
    try:
        timestamp = get_current_timestamp()
        with open(file_path, 'w') as file:
            file.write(f"Current Timestamp: {timestamp}")
        print(f"File '{file_path}' created successfully with the current timestamp.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    output_file_path = 'timestamp.txt'
    create_timestamp_file(output_file_path)