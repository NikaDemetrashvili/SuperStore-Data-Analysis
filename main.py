import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


filename = "C:/Users/User/Desktop/datasets/Superstore.csv"
data = pd.read_csv(filename, encoding='windows-1252')
print(data.head())
print(data.shape)
print(data.info)
print(data.isnull().sum())
print(data.describe())

# Change String To DateTime
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

print(type(data['Order Date'].iloc[0]))
print(type(data['Ship Date'].iloc[0]))
print(data.head(3))


# Total Sales For Each Region
plt.figure(figsize=(30, 10))
grouped_profit_region = data.groupby('Region').sum()[['Sales']].reset_index().sort_values(by='Sales', ascending=True)
profit_bar_region = sns.barplot(data=grouped_profit_region, x='Sales', y='Region', palette='Paired', hue='Region')
profit_bar_region.set_title("Total Sales For Each Region")
plt.show()


# Total Profit For Each Region
plt.figure(figsize=(30, 10))
grouped_profit_region = data.groupby('Region').sum()[['Profit']].reset_index().sort_values(by='Profit',
                                                                                              ascending=True)
profit_bar_region = sns.barplot(data=grouped_profit_region, x='Profit', y='Region', palette='rocket', hue='Region')
profit_bar_region.set_title("Total Profit For Each Region")
plt.show()


# Total sales for each state
plt.figure(figsize=(30, 10))
grouped_sale_state = data.groupby('State').sum()[['Sales']].reset_index().sort_values(by='Sales', ascending=False)
state_bar_profit = sns.barplot(data=grouped_sale_state, x='Sales', y='State', palette='dark')
state_bar_profit.set_title('Total Sales For Each State')
plt.show()


# Total Profit For Each State
plt.figure(figsize=(30, 10))
grouped_profit_state = data.groupby('State').sum()[['Profit']].reset_index().sort_values(by='Profit', ascending=False)
profit_bar_state = sns.barplot(data=grouped_profit_state, x='Profit', y='State', palette='rocket')
profit_bar_state.set_title("Total Profit For Each State")
plt.show()


# Total Profits by State per Customer Segment
grouped_profit_customer = data.groupby(['State', 'Segment']).agg({'Profit': 'sum'}).reset_index()
grouped_profit_customer = grouped_profit_customer.pivot(index='State', columns='Segment', values='Profit').reset_index()
grouped_profit_customer['All Customer'] = grouped_profit_customer['Consumer'] + grouped_profit_customer['Corporate'] \
                                          + grouped_profit_customer['Home Office']

grouped_profit_customer = grouped_profit_customer.sort_values(by='All Customer', ascending=False)
grouped_profit_customer.drop(columns='All Customer', inplace=True)
grouped_profit_customer.head()
grouped_profit_customer.set_index('State').plot(kind='bar', stacked=True,
                                                color=['darkorange', 'blue', 'gold'], figsize=(20, 10))
plt.title("Total Profits by State per Customer Segment")
plt.ylabel("Profit")
plt.show()


# Total Sales by State per Customer Segment
grouped_sales_customer = data.groupby(['State', 'Segment']).agg({'Sales': 'sum'}).reset_index()
grouped_sales_customer = grouped_sales_customer.pivot(index='State', columns='Segment', values='Sales').reset_index()
grouped_sales_customer['All Customer'] = grouped_sales_customer['Consumer'] + grouped_sales_customer['Corporate'] \
                                         + grouped_sales_customer['Home Office']

grouped_sales_customer = grouped_sales_customer.sort_values(by='All Customer', ascending=False)
grouped_sales_customer.drop(columns='All Customer', inplace=True)
grouped_sales_customer.head()
grouped_sales_customer.set_index('State').plot(kind='bar', stacked=True,
                                               color=['darkblue', 'deepskyblue', 'darkorange'], figsize=(20, 10))
plt.title("Total Sales by State per Customer Segment")
plt.ylabel("Profit")
plt.show()


# Total Profit by State per Product Category
category_profit = data.groupby(['State', 'Category']).agg({'Profit': 'sum'}).reset_index()
category_profit = category_profit.pivot(index='State', columns='Category', values='Profit').reset_index()
category_profit['All Category'] = category_profit['Technology'] + category_profit['Furniture'] + \
                                  category_profit['Office Supplies']
category_profit = category_profit.sort_values(by='All Category', ascending=False)
category_profit.drop(columns='All Category', inplace=True)
category_profit.set_index('State').plot(kind='bar', stacked=True, color=['steelblue', 'red', 'green'],
                                        figsize=(20, 10))
plt.title = "Total Profit by State per Product Category"
plt.ylabel = "Total Profit"
plt.show()


# Total Sales by State per Product Category
category_sales = data.groupby(['State', 'Category']).agg({'Sales': 'sum'}).reset_index()
category_sales = category_sales.pivot(index='State', columns='Category', values='Sales').reset_index()
category_sales['All Category'] = category_sales['Technology'] + category_sales['Furniture'] + \
                                 category_sales['Office Supplies']
category_sales = category_sales.sort_values(by='All Category', ascending=False)
category_sales.drop(columns='All Category', inplace=True)
category_sales.set_index('State').plot(kind='bar', stacked=True, color=['orange', 'red', 'blue'],
                                       figsize=(20, 10))
plt.title = "Total Sales by State per Product Category"
plt.ylabel = "Total Sales"
plt.show()

# Total Sales by State per Sub-Category
sub_category_sales = data.groupby(['State', 'Sub-Category']).agg({'Sales': 'sum'}).reset_index()
sub_category_sales = sub_category_sales.pivot(index='State', columns='Sub-Category', values='Sales').reset_index()
sub_category_sales['All Sub-Category'] = sub_category_sales['Appliances'] + sub_category_sales['Accessories'] + \
                                         sub_category_sales['Binders'] + sub_category_sales['Art'] + \
                                         sub_category_sales['Bookcases'] \
                                         + sub_category_sales['Chairs'] + sub_category_sales['Envelopes'] \
                                         + sub_category_sales['Fasteners'] + sub_category_sales['Furnishings'] \
                                         + sub_category_sales['Labels'] + sub_category_sales['Machines'] + \
                                         sub_category_sales['Paper'] + sub_category_sales['Phones'] + \
                                         sub_category_sales['Storage'] \
                                         + sub_category_sales['Supplies'] + sub_category_sales['Tables']

sub_category_sales = sub_category_sales.sort_values(by='All Sub-Category', ascending=False)
sub_category_sales.drop(columns='All Sub-Category', inplace=True)
sub_category_sales.set_index('State').plot(kind='bar', stacked=True, figsize=(30, 10))
plt.ylabel = "Total Sales"
plt.title = "Total Sales by State per Sub-Category"
plt.show()


# Sales & Profits over time
fig = plt.figure(figsize=(20, 10))
sales_profit_time = data[['Order Date', 'Sales', 'Profit']].sort_values(by='Order Date')
sales_profit_time = sales_profit_time.groupby('Order Date').agg({'Profit': 'mean', 'Sales': 'mean'})
plt.plot(sales_profit_time.index, sales_profit_time['Profit'], color='darkred', label='Profit')
plt.plot(sales_profit_time.index, sales_profit_time['Sales'], color='darkgreen', label='Sales')
plt.legend(fontsize=10)
plt.xlabel('Order Date')
plt.ylabel = "Sales/Profit Average"
plt.title = "Sales & Profits Over Time"
plt.show()


# Sales and Profit by Region (Pie Charts)

figure, ax = plt.subplots(1, 2)
region_sales_profit_data = data.groupby('Region').agg({'Sales': 'sum', 'Profit': 'sum'})

sales_pie = region_sales_profit_data.plot.pie(y='Sales', figsize=(10, 10), ax=ax[0])
sales_pie.set_title('Sales')
sales_pie.set_ylabel(None)
profit_pie = region_sales_profit_data.plot.pie(y='Profit', figsize=(10, 10), ax=ax[1])
profit_pie.set_title('Profit')
profit_pie.set_ylabel(None)
plt.show()


# Sales and Profit by Category (Pie Charts)

figure, ax = plt.subplots(1, 2)
region_sales_profit_data = data.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'})
my_explode = (0.1, 0, 0)
sales_pie = region_sales_profit_data.plot.pie(y='Sales', figsize=(10, 10), ax=ax[0], explode=my_explode)
sales_pie.set_title('Sales')
sales_pie.set_ylabel(None)
profit_pie = region_sales_profit_data.plot.pie(y='Profit', figsize=(10, 10), ax=ax[1], explode=my_explode)
profit_pie.set_title('Profit')
profit_pie.set_ylabel(None)
plt.show()



