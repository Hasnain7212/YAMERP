import os

# Define the base directory
base_dir = 'erp-project/src'

# Define the directories and files with their corresponding content
directories = ['components']
component_codes = {
    'DashboardComponent.vue': """
<template>
  <div class="DashboardComponent">
    <h1>Dashboard</h1>
    <p>Welcome to the Dashboard!</p>
  </div>
</template>

<script>
export default {
  name: 'DashboardComponent',
};
</script>

<style scoped>
.DashboardComponent {
  padding: 20px;
}
</style>
""",
    'CustomersComponent.vue': """
<template>
  <div class="CustomersComponent">
    <h1>Customers</h1>
    <table>
      <thead>
        <tr>
          <th>Customer ID</th>
          <th>Name</th>
          <th>Address</th>
          <th>Contact Information</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="customer in customers" :key="customer.CustomerID">
          <td>{{ customer.CustomerID }}</td>
          <td>{{ customer.Name }}</td>
          <td>{{ customer.Address }}</td>
          <td>{{ customer.ContactInformation }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'CustomersComponent',
  data() {
    return {
      customers: []
    };
  },
  created() {
    this.fetchCustomers();
  },
  methods: {
    fetchCustomers() {
      // Fetch customers from API
      this.customers = [
        { CustomerID: 1, Name: 'John Doe', Address: '123 Main St', ContactInformation: '123-456-7890' },
        { CustomerID: 2, Name: 'Jane Smith', Address: '456 Oak St', ContactInformation: '987-654-3210' }
      ];
    }
  }
};
</script>

<style scoped>
.CustomersComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'EmployeesComponent.vue': """
<template>
  <div class="EmployeesComponent">
    <h1>Employees</h1>
    <table>
      <thead>
        <tr>
          <th>Employee ID</th>
          <th>Name</th>
          <th>Position</th>
          <th>Department</th>
          <th>Salary</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.EmployeeID">
          <td>{{ employee.EmployeeID }}</td>
          <td>{{ employee.Name }}</td>
          <td>{{ employee.Position }}</td>
          <td>{{ employee.Department }}</td>
          <td>{{ employee.Salary }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'EmployeesComponent',
  data() {
    return {
      employees: []
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    fetchEmployees() {
      // Fetch employees from API
      this.employees = [
        { EmployeeID: 1, Name: 'John Doe', Position: 'Manager', Department: 'Sales', Salary: 60000 },
        { EmployeeID: 2, Name: 'Jane Smith', Position: 'Developer', Department: 'IT', Salary: 70000 }
      ];
    }
  }
};
</script>

<style scoped>
.EmployeesComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'ExpensesComponent.vue': """
<template>
  <div class="ExpensesComponent">
    <h1>Expenses</h1>
    <table>
      <thead>
        <tr>
          <th>Expense ID</th>
          <th>Expense Date</th>
          <th>Amount</th>
          <th>Category</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="expense in expenses" :key="expense.ExpenseID">
          <td>{{ expense.ExpenseID }}</td>
          <td>{{ expense.ExpenseDate }}</td>
          <td>{{ expense.Amount }}</td>
          <td>{{ expense.Category }}</td>
          <td>{{ expense.Description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ExpensesComponent',
  data() {
    return {
      expenses: []
    };
  },
  created() {
    this.fetchExpenses();
  },
  methods: {
    fetchExpenses() {
      // Fetch expenses from API
      this.expenses = [
        { ExpenseID: 1, ExpenseDate: '2023-01-01', Amount: 100, Category: 'Office Supplies', Description: 'Stationery' },
        { ExpenseID: 2, ExpenseDate: '2023-01-02', Amount: 200, Category: 'Travel', Description: 'Business Trip' }
      ];
    }
  }
};
</script>

<style scoped>
.ExpensesComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'InvoicesComponent.vue': """
<template>
  <div class="InvoicesComponent">
    <h1>Invoices</h1>
    <table>
      <thead>
        <tr>
          <th>Invoice ID</th>
          <th>Order ID</th>
          <th>Invoice Date</th>
          <th>Due Date</th>
          <th>Total Amount</th>
          <th>Payment Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="invoice in invoices" :key="invoice.InvoiceID">
          <td>{{ invoice.InvoiceID }}</td>
          <td>{{ invoice.OrderID }}</td>
          <td>{{ invoice.InvoiceDate }}</td>
          <td>{{ invoice.DueDate }}</td>
          <td>{{ invoice.TotalAmount }}</td>
          <td>{{ invoice.PaymentStatus }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'InvoicesComponent',
  data() {
    return {
      invoices: []
    };
  },
  created() {
    this.fetchInvoices();
  },
  methods: {
    fetchInvoices() {
      // Fetch invoices from API
      this.invoices = [
        { InvoiceID: 1, OrderID: 1, InvoiceDate: '2023-01-01', DueDate: '2023-01-31', TotalAmount: 1000, PaymentStatus: 'Paid' },
        { InvoiceID: 2, OrderID: 2, InvoiceDate: '2023-01-02', DueDate: '2023-02-01', TotalAmount: 500, PaymentStatus: 'Unpaid' }
      ];
    }
  }
};
</script>

<style scoped>
.InvoicesComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'OrdersComponent.vue': """
<template>
  <div class="OrdersComponent">
    <h1>Orders</h1>
    <table>
      <thead>
        <tr>
          <th>Order ID</th>
          <th>Customer ID</th>
          <th>Order Date</th>
          <th>Total Amount</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.OrderID">
          <td>{{ order.OrderID }}</td>
          <td>{{ order.CustomerID }}</td>
          <td>{{ order.OrderDate }}</td>
          <td>{{ order.TotalAmount }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'OrdersComponent',
  data() {
    return {
      orders: []
    };
  },
  created() {
    this.fetchOrders();
  },
  methods: {
    fetchOrders() {
      // Fetch orders from API
      this.orders = [
        { OrderID: 1, CustomerID: 1, OrderDate: '2023-01-01', TotalAmount: 1000 },
        { OrderID: 2, CustomerID: 2, OrderDate: '2023-01-02', TotalAmount: 500 }
      ];
    }
  }
};
</script>

<style scoped>
.OrdersComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'PaymentsComponent.vue': """
<template>
  <div class="PaymentsComponent">
    <h1>Payments</h1>
    <table>
      <thead>
        <tr>
          <th>Payment ID</th>
          <th>Invoice ID</th>
          <th>Payment Date</th>
          <th>Amount</th>
          <th>Payment Method</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="payment in payments" :key="payment.PaymentID">
          <td>{{ payment.PaymentID }}</td>
          <td>{{ payment.InvoiceID }}</td>
          <td>{{ payment.PaymentDate }}</td>
          <td>{{ payment.Amount }}</td>
          <td>{{ payment.PaymentMethod }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'PaymentsComponent',
  data() {
    return {
      payments: []
    };
  },
  created() {
    this.fetchPayments();
  },
  methods: {
    fetchPayments() {
      // Fetch payments from API
      this.payments = [
        { PaymentID: 1, InvoiceID: 1, PaymentDate: '2023-01-05', Amount: 1000, PaymentMethod: 'Credit Card' },
        { PaymentID: 2, InvoiceID: 2, PaymentDate: '2023-02-05', Amount: 500, PaymentMethod: 'Bank Transfer' }
      ];
    }
  }
};
</script>

<style scoped>
.PaymentsComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'ProductsComponent.vue': """
<template>
  <div class="ProductsComponent">
    <h1>Products</h1>
    <table>
      <thead>
        <tr>
          <th>Product ID</th>
          <th>Product Name</th>
          <th>Description</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.ProductID">
          <td>{{ product.ProductID }}</td>
          <td>{{ product.ProductName }}</td>
          <td>{{ product.Description }}</td>
          <td>{{ product.Price }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ProductsComponent',
  data() {
    return {
      products: []
    };
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
      // Fetch products from API
      this.products = [
        { ProductID: 1, ProductName: 'Product A', Description: 'Description A', Price: 100 },
        { ProductID: 2, ProductName: 'Product B', Description: 'Description B', Price: 200 }
      ];
    }
  }
};
</script>

<style scoped>
.ProductsComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'SalesComponent.vue': """
<template>
  <div class="SalesComponent">
    <h1>Sales</h1>
    <table>
      <thead>
        <tr>
          <th>Sale ID</th>
          <th>Employee ID</th>
          <th>Product ID</th>
          <th>Quantity</th>
          <th>Sale Date</th>
          <th>Total Amount</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sale in sales" :key="sale.SaleID">
          <td>{{ sale.SaleID }}</td>
          <td>{{ sale.EmployeeID }}</td>
          <td>{{ sale.ProductID }}</td>
          <td>{{ sale.Quantity }}</td>
          <td>{{ sale.SaleDate }}</td>
          <td>{{ sale.TotalAmount }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'SalesComponent',
  data() {
    return {
      sales: []
    };
  },
  created() {
    this.fetchSales();
  },
  methods: {
    fetchSales() {
      // Fetch sales from API
      this.sales = [
        { SaleID: 1, EmployeeID: 1, ProductID: 1, Quantity: 10, SaleDate: '2023-01-01', TotalAmount: 1000 },
        { SaleID: 2, EmployeeID: 2, ProductID: 2, Quantity: 5, SaleDate: '2023-01-02', TotalAmount: 500 }
      ];
    }
  }
};
</script>

<style scoped>
.SalesComponent {
  padding: 20px;
}
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 10px;
  border: 1px solid #ddd;
}
</style>
""",
    'HomePage.vue': """
<template>
  <div class="HomePage">
    <h1>Home</h1>
    <p>Welcome to the Home Page!</p>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>

<style scoped>
.HomePage {
  padding: 20px;
}
</style>
""",
}

# Create directories and update files
for directory in directories:
    dir_path = os.path.join(base_dir, directory)
    
    # Remove all existing files in the directory
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Create new files with the updated content
    for file, code in component_codes.items():
        if file.endswith('.vue'):
            file_name = file
            with open(os.path.join(base_dir, directory, file_name), 'w') as f:
                f.write(code)
