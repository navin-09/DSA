def send_email(result):
    print(f"Email sent: Task result = {result}")

def process_data(data, callback):
    print("Processing data...")
    result = sum(data) / len(data)
    callback(result)  # call the callback when done

process_data([10, 20, 30], send_email)
