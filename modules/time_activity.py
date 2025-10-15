from datetime import datetime, timedelta

def show_time_logs(start_date, end_date):
    """
    Display activities within a specified time range.
    Currently, this is a placeholder that simulates logs.
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return

    print(f"Showing activities from {start_date} to {end_date}:")
    # Placeholder example
    current = start
    while current <= end:
        print(f"{current.strftime('%Y-%m-%d')} - Sample activity")
        current += timedelta(days=1)
