# Create the dictionary
test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}


# Function to add a new setting
def add_setting(settings, setting):
    key, value = setting

    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value

    return f"Setting '{key}' added with value '{value}' successfully!"


# Function to update an existing setting
def update_setting(settings, setting):
    key, value = setting

    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# Function to delete a setting
def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


# Function to view all settings
def view_settings(settings):
    if not settings:
        return "No settings available."

    settings_str = "Current User Settings:\n"

    for key, value in settings.items():
        settings_str += f"{key.capitalize()}: {value}\n"

    return settings_str


# Test the functions
print(add_setting(test_settings, ("VOLUME", "HIGH")))
print(update_setting(test_settings, ("THEME", "DARK")))
print(delete_setting(test_settings, "language"))
print(view_settings(test_settings))