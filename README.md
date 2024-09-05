# Finance-Tracker
Finance Tracker is a Python program designed to automate the tracking and categorization of monthly expenses. It reads financial transactions from a CSV file, categorizes them based on specific criteria, and updates a Google Sheets document with the organized data for easy financial management and analysis.

Features:
  - Automated Expense Tracking: Reads transaction data from a CSV file and categorizes expenses such as 'Allowance,' 'Rent,' 'E-Transfer,' 'Refund,' 'Online Purchase,' 'Internet Banking,' and 'In-store Purchase' based on       specific rules.
  - Google Sheets Integration: Uses the Google Sheets API to connect to a Google Sheets document and automatically insert categorized transactions into a specified worksheet.
  - Customizable for Different Months: Easily adjust the script to process different months by changing the MONTH variable.
  
Requirements:
  - Python 3.x
  - gspread library for Google Sheets integration
  - Google Sheets API credentials
  
Usage:
  - Set up your Google Sheets API credentials and enable access.
  - Save your monthly transaction data as a CSV file named in the format YYYY_month.csv (e.g., 2024_august.csv).
  - Update the MONTH variable in the script to the month you want to process.
  - Run the script to automatically read, categorize, and update your transactions in Google Sheets.
