import re

def calculate_reading_time(text:str, reading_speed:int=200)->float:
    """Calculates reading time
    """
    # Remove any non-word characters (e.g., punctuation)
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    # Split the text into words
    words = cleaned_text.split()

    # Calculate the estimated reading time in minutes
    estimated_time = len(words) / reading_speed

    # Return the estimated reading time rounded to the nearest whole number
    return round(estimated_time)