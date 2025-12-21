full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # --- Name Validations ---
    
    # Check if the name is a string
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    # Check if the name is an empty string
    if name == "":
        return 'The character should have a name'
    
    # Check if the name is longer than 10 characters
    if len(name) > 10:
        return 'The character name is too long'
    
    # Check if the name contains spaces
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    # --- Stats Validations ---
    
    # Create a list of stats to check them all at once
    stats = [strength, intelligence, charisma]
    
    # Check if all stats are integers
    if not all(isinstance(s, int) for s in stats):
        return 'All stats should be integers'
    
    # Check if any stat is less than 1
    if any(s < 1 for s in stats):
        return 'All stats should be no less than 1'
    
    # Check if any stat is greater than 4
    if any(s > 4 for s in stats):
        return 'All stats should be no more than 4'
    
    # Check if the sum of the stats equals 7
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    
    # --- Output Formatting ---
    
    # Initialize a list to hold the stat bars
    bars = []
    
    # For each stat, generate a bar of 10 total dots, using full and empty dots
    for stat in stats:
        bar = full_dot * stat + empty_dot * (10 - stat)  # Full dots for the stat, empty for the remaining
        bars.append(bar)  # Append the bar for this stat
    
    # Create the final output, including the name and the bars for each stat
    output = f"{name}\nSTR {bars[0]}\nINT {bars[1]}\nCHA {bars[2]}"
    
    return output
