# Pytest Selenium Python Automation Framework

## Introduction
This project is a robust Python-based automation testing framework using Selenium and Pytest. It supports efficient browser automation, test case management, and detailed reporting. The framework also integrates with a Dockerized PostgreSQL database for efficient test data management and validations.

## Key Features
**•	Cross-Browser Testing:** Supports execution on multiple browsers using Selenium WebDriver.

**•	Database Validation:** Utilizes Dockerized database services for data validation.

**•	Parallel Execution:** Enabled using Pytest-xdist for faster test execution.

**•	Headless Testing:** Configurable for CI/CD integration to run tests without a GUI.

**•	Customizable Test Data Management:** Test data can be managed externally using configuration files or data loaders.

**•	Automatic HTML Reporting:** Generates detailed HTML reports using Pytest-HTML.

**•	Fail-Safe Mechanisms:** Captures screenshots on test failures for debugging.

**•	Data-Driven Testing Approach:** Tests are designed to accept input from external files such as CSV, Excel, or JSON.


## Prerequisites
Before setting up the project, ensure you have the following prerequisites installed:

**•	Python 3.x (version 3.7 or higher)** - Required for running the automation scripts.

**•	PostgreSQL** - Installed locally or use Docker for a containerized version for database validation.

**•	Docker** - For setting up PostgreSQL containers and managing services.

**•	Selenium WebDriver** - Supports Chrome or Firefox for web automation.

**•	ChromeDriver or GeckoDriver** - Depending on your preferred browser.

**•	Pytest** - For running the test suites.

**•	Git** - For version control and managing project repositories.

**•	Pytest-xdist** - For parallel test execution.

**•	Pytest-HTML** - For generating test execution reports.

**•	Virtual Environment Tool** - Like venv or virtualenv to manage project dependencies

**•	Test Data Libraries** - Like pandas or openpyxl for handling external test data files.

## Setup and Installation
Follow these steps to set up the framework:
#### 1. Clone the Repository:
git clone https://github.com/owais2021/Pytest-Selenium-Python-AutomationFramework.git
#### 2. Set up a Virtual Environment:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
#### 3.	Installing Dependencies:
Ensure Python is Installed 
Confirm Python 3.8 or later is installed on your system.
#### 4.	Check the version using:
python –version
#### 5.	Verify Installation
Check if the dependencies are installed correctly by listing installed packages:
pip list

## Folder Structure
![image](https://github.com/user-attachments/assets/80c92b60-25ce-493f-8d57-e4403f895f25)

## Folder & File Details:
#### 1. drivers/chrome & drivers/firefox
These directories contain the WebDriver binaries (chromedriver.exe for Chrome and geckodriver.exe for Firefox) used to automate the browser actions. The corresponding driver for the browser specified in the configuration is used during the test execution.
#### 2. reports/report.html
This file stores the test run results in HTML format. It provides a summary of the test execution, including success, failure, and any captured logs or errors.
![image](https://github.com/user-attachments/assets/bbbeb5fd-0612-4b7d-88e9-b48cdccdaf69)
#### 3. resources/db_config.py
This file contains the database connection configuration for PostgreSQL, including host, user, password, and database name.
![image](https://github.com/user-attachments/assets/10365876-1594-4225-a04c-941f480d38ea)
#### 4. resources/test_config.json
This JSON file holds the configuration details for the testing environment. It includes the base URL for Amazon, the browser to be used (Chrome or Firefox), paths to the Chrome and Firefox WebDriver executables, and the path to the test data Excel file.
![image](https://github.com/user-attachments/assets/9d0b011a-fc2a-45e3-b973-5921754b8fe2)
#### 5. resources/test_data.xlsx
An Excel file that contains the test data. The data is read from this file for the search query parameters during test execution. It includes columns for the search term, category, and price range, which will be used in the product search.
#### 6. src/pages/searchProduct_page.py
This file defines the SearchProduct class responsible for interacting with the Amazon search page. It defines methods to open the page, perform a search, and click on the first product.
#### 7. test/test_searchProduct.py
This file contains the pytest test case test_searchProduct. It reads the search data from the Excel file using read_excel_data and passes it to the SearchProduct page object to perform the search.
#### 8. utils/config.py
This utility file loads the test configuration from test_config.json using Python's json module and makes it available globally via CONFIG.
#### 9. utils/data_reader.py
This utility file contains the read_excel_data function, which reads data from an Excel file using openpyxl. It allows you to extract column data from a specified sheet.
#### 10. utils/db_connection.py
This file manages the database connection for PostgreSQL, providing a fixture db_connection that sets up and tears down the connection for each test.
#### 11. utils/db_util.py
This file contains utility functions for connecting to PostgreSQL, executing queries, and fetching results.
#### 12. conftest.py
This file sets up the pytest configuration, initializing the WebDriver based on the configuration in test_config.json. It also captures screenshots on test failure.
#### 13. databaseTest/testCase_verifying_Data_Insertion.py
This test case checks that a user is correctly inserted into the database and that the data is retrievable. It also performs cleanup after the test by deleting the inserted user.
#### 14. docker-compose.yml
This file defines the services for PostgreSQL and Adminer in a Docker container. It configures the PostgreSQL container to expose its port on 5432 and connects it to a test_network.

## Dockerized Setup for Adminer and PostgreSQL
Ensure Docker is installed and running on your system before proceeding with the setup. All configurations are defined in the docker-compose.yml file, you can bring up the PostgreSQL and Adminer containers using the following commands:

#### •	Navigate to the Directory:
Ensure you are in the directory where the docker-compose.yml file is located:
**cd /path/to/your/project**

#### •	Build and Start Containers:
Run the following command to build and start the containers:
**docker-compose up -d**

#### •	Verify the Containers:
Use this command to check the status of running containers:
**docker-compose ps**

#### •	Access Adminer
Open a web browser and navigate to:
**http://localhost:8080**
The image shows the Adminer interface, a lightweight database management tool, being accessed on localhost:8080 for managing a PostgreSQL database.

![image](https://github.com/user-attachments/assets/cf5ee775-2275-42ac-b6d2-ebf9f5f4d3ab)

#### •	Login to PostgreSQL in Adminer :

**-	System**: Select PostgreSQL from the dropdown.

**-	Server:** Enter the container name or server name. Example: test_postgres_db

**-	Username:** PostgreSQL username. Example: test_user

**-	Password:** Enter the database password. Example: secret

**-	Database:** Enter the target database name. Example: test_db

#### •	Click Login.

#### •	Work with Adminer:
Once logged in:
-	You can create tables, insert data, query the database, or update records.
  
-	Use the navigation options to perform database operations.
  
-	Run SQL commands directly through the SQL Command feature.
  
## Database Validation
If using this for automation testing:

•	Execute test scripts or SQL queries to validate the database state.

•	Use tools like Pytest with PostgreSQL libraries (psycopg2) to connect and validate data.

## Running the Test Suite

#### 1.	Run All Tests:
Execute all test cases using the following command:

**pytest test/ --html=reports/report.html --self-contained-html**

#### 2.	Run Tests in Parallel:
Use pytest-xdist to enable parallel execution:

**pytest -n 4 test/ --html=reports/report.html**

#### 3.	Database Tests:
Run database-specific test cases:

**pytest databaseTest/testCase _verifying_Data_Insertion.py**

#### 4.	Run Specific Test File:

**pytest test/test_searchProduct.py**

#### 5.	Run a Specific Test Function:

**pytest test/test_searchProduct.py**

#### 6.	Generate an HTML Report:

**pytest --html=reports/report.html**

## Key Notes
•	Fail-Safe Mechanism: Screenshots will automatically be captured for failed test cases.

•	Report Generation: HTML reports will be generated in the reports/ folder.

•	Scalability: Test data can be expanded using external sources like Excel or JSON files.

