Expense Tracker Overview
This tool is created to help individuals better manage their financial transactions by recording, summarizing, and visualizing both income and expenses. It is aimed at simplifying the process of keeping track of small, easily overlooked transactions, which can make a big difference over time.

Key Features:
CSV File Storage:

Data Storage: All transactions are stored in a CSV file (finance_data.csv), making it easy to maintain and export the data as needed.
Portable Data: Since the file is in CSV format, users can open, edit, or analyze the data in spreadsheet software like Excel or Google Sheets.
Transaction Management:

Add Transactions: Users can add transactions by providing:
Date: The date of the transaction.
Amount: The transaction amount (positive for income, negative for expenses).
Category: Whether it's income or expense.
Description: A short description for context (e.g., "Salary," "Groceries," "Coffee").
Automatic Handling: The application handles data validation to ensure that entered data is in the correct format and calculates totals correctly.
Date-Range Filtering:

Filter by Date Range: Users can select a custom date range to filter transactions and view detailed records within that period.
Summary View: After filtering, a summary is provided, showing:
Total Income
Total Expenses
Net Savings (Income - Expenses) for the selected time range.
Data Visualization:

Line Plot: Users can generate a line plot to visualize their income and expenses over time. This helps identify trends or irregular spending patterns.
Time-Based Trends: The visualization highlights changes in financial activity, helping users understand where their money is going over a selected time period.
User-Friendly Command-Line Interface (CLI):

Simple and Intuitive: The application uses a straightforward CLI, offering easy options to add, view, and analyze financial data.
Minimalistic Design: The interface is designed to be as intuitive as possible, making it easy even for non-technical users to interact with.
How It Works:
Initialization:

When the application is first run, it checks if the CSV file (finance_data.csv) exists. If not, the program creates the file to begin recording transactions.
Add Transactions:

Users can input a new transaction through the CLI, specifying the date, amount, category, and description. The data is validated for accuracy and automatically saved to the CSV file.
View and Summarize:

Users can request a summary of their financial activity within a specific date range. The application will calculate and display:
Total income
Total expenses
Net savings for the period.
Visualize:

Users can choose to generate a plot that shows their income and expenses over time. The plot is updated dynamically based on the selected date range and provides a visual representation of their financial trends.
Example Usage:
Adding a Transaction:

User adds a transaction with a command like:
arduino
Copy code
add_transaction(2024-12-01, 1500, 'Income', 'Salary')
Filtering Transactions by Date:

User filters by a date range to see all transactions in December 2024:
arduino
Copy code
filter_by_date('2024-12-01', '2024-12-31')
Generating a Plot:

User generates a plot to visualize the income and expenses trend for the last 6 months:
arduino
Copy code
generate_plot(start_date='2024-06-01', end_date='2024-12-01')
Benefits:
Improved Financial Management: By regularly tracking income and expenses, users can gain a clearer picture of their financial situation and make better budgeting decisions.
Simplicity and Accessibility: The user-friendly CLI makes it easy to use without needing advanced technical knowledge.
Data Export and Backup: Storing data in CSV format allows users to back up or export their records for further analysis or tax purposes.
Trend Analysis: The data visualization feature helps users recognize spending patterns and income fluctuations over time.