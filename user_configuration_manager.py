# Dictionary
test_settings = {
    "theme": "light",
    "volume": "medium",
    "language": "english"
}

# Add setting
def add_setting(settings, item):
    key, value = item
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


# Update setting
def update_setting(settings, item):
    key, value = item
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


# Delete setting
def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"


# View settings - FIXED VERSION
def view_settings(settings):
    if not settings:
        return "No settings available."

    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"
    
    return output
