from selenium import webdriver


# Create a WebDriver object with the ChromeOptions object as an argument
driver = webdriver.Chrome()

# Use the get() method to load a website
driver.get('https://www.worksnaps.com/app/login.cgi?source=web&webpage_version=3&cls=1')
# Wrap all this with the schedular

    # Get the Login and password ids 

    # Pass the login and password keys from config 

    # Change the project to the organization 

    # Click the track time

    # From the drop down menu click the add time 

    # Change to pop up window of the Add time 

    # Add the time from 9 to 4 

    # Click Add 

    # Select the project and add the description

    # Select the close to see the reflected changes in the worksnap console


# Close the WebDriver object
driver.quit()