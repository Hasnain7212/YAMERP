import os

# Define the base directory
base_dir = 'my-project/src'

# Define the directories and files
directories = ['components', 'views']
files = ['Dashboard.vue', 'Customers.vue', 'Products.vue', 'Orders.vue', 'Invoices.vue', 'Payments.vue', 'Employees.vue', 'Sales.vue', 'Expenses.vue', 'AIAnalysis.vue', 'Home.vue', 'App.vue', 'main.js', 'router.js']

# Create the directories
for directory in directories:
    os.makedirs(os.path.join(base_dir, directory), exist_ok=True)

# Create the files
for file in files:
    # Determine the directory based on the file name
    if file.endswith('.vue'):
        directory = 'components' if file != 'Home.vue' else 'views'
    else:
        directory = ''

    # Create the file
    with open(os.path.join(base_dir, directory, file), 'w') as f:
        pass
