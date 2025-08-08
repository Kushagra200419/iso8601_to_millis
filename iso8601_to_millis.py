# iso8601_to_millis.py

from datetime import datetime, timezone

def iso8601_to_milliseconds(iso_string):
    """
    Convert ISO 8601 date string to milliseconds since epoch.
    
    Args:
        iso_string (str): ISO 8601 date string (e.g., '2020-02-27T15:24:17.123Z')
    
    Returns:
        int: Milliseconds since Unix epoch
    """
    # Parse the ISO 8601 string into a datetime object
    dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
    
    # Convert to UTC timestamp (in seconds) and then to milliseconds
    return int(dt.timestamp() * 1000)

# Example usage
if __name__ == '__main__':
    iso_time = '2020-02-27T15:24:17.123Z'
    millis = iso8601_to_milliseconds(iso_time)
    print(f"ISO 8601: {iso_time}")
    print(f"Milliseconds since epoch: {millis}")
