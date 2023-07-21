# DataCamp-Intermediate-Python
Python lessons during the [DataCamp](https://campus.datacamp.com/courses/intermediate-python) course.

## Matplotlib

### Plot

Matplotlib - is a packet for data visualization. We will be using its sub-packet named pyplot.

```py
import matplotlib.pyplot as plt
```

To plot some information, we use the plt.plot, as followed:

```py
year = [1950, 1970, 1991, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)  # Line plot, First argument = x-axis, second argument = y-axis
```

Python will only plot the graphic when the show method is called.

```py
plt.show() # Displays the plot
```

### Scatter plot (*Gráfico de Disperão*)

O gráfico de dispersão é uma ferramenta gráfica amplamente utilizada em estatística e outras áreas do conhecimento para visualizar a relação entre duas variáveis quantitativas. Ao plotar os pontos no gráfico, é possível detectar padrões e tendências nos dados e identificar possíveis correlações entre as variáveis. Fonte [FM2S](https://www.fm2s.com.br/blog/grafico-de-dispersao).

```py
plt.scatter(year, pop) # It will plot the dots without the line connecting it
plt.show()
```

Tip: [Python For Data Science Cheat Sheet](https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1620781328/Python_For_Data_Science_-_A_Cheat_Sheet_For_Beginners_igzrny.png).

To change the x-axis to a logarithmic scale, just ```plt.xscale('log')```. 

Next code gives colors to the dots while using a graph such as scatter:

```py
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c=col)
# I could also add the parameter alpha=0.8 to change opacity of the bubbles
```

I can also add other customizations such as:

```py
# Additional customizations
plt.text(1550, 71, 'India') # x-axis location, y-axis location, text
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(true)
```

### Histogram 

Helps to get idea about distribution. X-axis are for the bins and it defines the number of equal-width bins in the range. Bins has a default value of 10.

To get help: ```help(plt.hist)```.

```py
import matplotlib.pyplot as plt

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(value, bins=3) # Bins will be 0, 3, 6. 
plt.show()
```

* To show the bins on Y-axis use ```?```.
* ```plt.clf()``` Clean the current figure.

```py
plt.plot(x_axis, y_axis)

plt.xlabel(´X-axis Label`) 
plt.ylabel(´Y-axis Label`) 
plt.title(´Title of the Plot`)
plt.yticks([0, 2, 4, 6, 8, 10]) # Gives the values that will appear on Y-axis
plt.yticks([0, 2, 4, 6, 8, 10],
	   [´0´, ´2B´, ´4B´, ´6B´, ´8B´, ´10B´]) # This way, it will give the names fot the Y-axis

plt.show()
```

### Dictionary

```py
dict_name = { "key_1":1, "key_2",2 } # Key value pairs
dict_name["key_1"]

print(dict_name.keys()) # To print out all the key values
dict_name["key_3"] = 3 # To add more data to a dictionary
"key_3" in dict_name # To check if a key exists inside the list
dict_name["key_3"] = 4 # To change a value
del(dict_name["key_3"]) # To delete a key value pair
```
Dictionaries can contain other disctionaries inside (values are again dictionaries).

```py
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

print(europe['spain']['population']) # to show the population of spain
```

To add more data (as sub-dictionaries) on the europe dictionary, just:

```py
# Create sub-dictionary data
data = {'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

```

## Pandas

Pandas is an open source library, providing high-performance, easy-to-use data structures and data analysis tools for Python.
To use Pandas, we have to import its package first.

```py
import pandas as pd
```

### Creating a DataFrame

Pandas has advantages over Numpy, once Pandas handles better different data types in a single variable.
It creates a DataFrame.

We can create a DataFrame from a Dictionary.

```py
dict_name = { 
	"Column1":["Value10", "Value01", "Value02", "Value03"],
	"Column2":["Value20", "Value21", "Value22", "Value23"],
	"Column3":[30, 31, 32, 33] }

DataFrame_name = pd.DataFrame(dict_name)
```

Pandas automatict assigns row names (0 and forward), we can change that by adding index name to it:

```py
DataFrame_name.index = ["NameRow1", "NameRow2", "NameRow3", "NameRow4", "NameRow5"]
```

### Reading a DataFrame

We can read csv files using that! 

```py
DataFrame_name = pd.read_csv("path/to/file_name.csv")
```

Now, when we have index names on our csv file, we need to pass the ```index_col``` argument. Let's do it:

```py
DataFrame_name = pd.read_csv("path/to/file_name.csv", index_col=0)
```

Now let's index and select data. 

To print the whole column:

```py
print(DataFrame_name["Column2"])
```

But this, will return a dtype name object. If I type ```type(DataFrame_name["Column2"]``` it will retur as ```pandas.core.series.Series```.

To return the data and keep the data in a DataFrame format, we need to use double square brackets.

```py
print(DataFrame_name[["Column2"]])
```

Then when we check its type by ```type(DataFrame_name["Column2"]``` it will retur ```pandas.core.series.DataFrame```.

I can then use more columns by:

```py
print(DataFrame_name[["Column2", "Column3"]])
```

I can select the rows by using the index.

```py
print(DataFrame_name[1:3]) # index starts in 0, so we will print rows 2 to 4
```

In pandas we have:

* ```loc``` as label-based.
* ```iloc``` as integer position-based.

To use get a row using index with names:

```py
DataFrame_name.loc[["NameRow5"]] # Two brackets to retur DataFrame format
DataFrame_name.iloc[[4]] # Same result but using iloc
```

Now to get only a few rows and columns:

```py
DataFrame_name.loc[["NameRow4", "NameRow5"], ["Column1", "Column2"]] 
DataFrame_name.iloc[[3, 4], [0, 1]] # Same result but using iloc
```

To get all rows I could simply use:

```py
DataFrame_name.loc[:, ["Column1", "Column2"]] 
DataFrame_name.iloc[:, [0, 1] # Same result but using iloc
```

## Comparison Operatos

Same as C, ==, >=, <=, !=.

```py
DataFrame_name["area"] # Get pandas series to analize

is_huge = DataFrame_name["area"] > 8 # Compare each value from the serie to >8

# To show info about itens that are greate than 8, just
print(DataFrame_name[is_huge]

# Or, I can simply:

print(DataFrame_name[DataFrame_name["area"] > 8]])
```

## Boolean Operators

### Comparison Operator

Comparators works same way as in C.

* ``` x > 5 and x < 15``` for AND operator.
* ``` logical_and(x > 5, x < 15) ``` NumPy equivalent for AND.
* ``` y > 1 or y < -5``` for OR operator.
* ``` logical_or(y > 1, y < -5) ``` NumPy equivalent for OR.
* ``` not False ``` for NOT operator.
* ``` logical_not(False) ``` NumPy equivalent for NOT.

Note: Once Pandas is created based on NumPy packet, it is possible to use the boolean operators also.

* ``` np.logical_and(DataFrame_name["area"] > 8], DataFrame_name["area"] < 100]) ```
* ``` DataFrame_name[np.logical_and(DataFrame_name["area"] > 8], DataFrame_name["area"] < 100])] ```

For strings, it gets according to alphabel: 'rafaela' < 'amanda' ? The answer is False.
## Conditional Operators

### if

```py
if condition :
	expression
	# to continue the if, just use 4 spaces or tab

z = 4
if z % 2 == 0 : # True
	print("z is even")
```

### else

```py
if condition :
	expression
else :
	expression

z = 5
if z % 2 == 0 : # True
	print("z is even")
else : 
	print("z is odd")
```

### elif

```py
if condition : 
	expression
elif condition :
	expression
else : 
	expression
```

### While loop

```py
while condition : 
	espression

error = 5
while error > 1 :
	error = error / 4
	print(error)
```

### For loop

```py
for var in seq :
	expression

for index_name in list_name :
	print(index_name) # Not list_name[index_name], prints content of index

for index, index_name in enumerate(list_name) : 
	print ("index " + str(index) + ": " + str(index_name)) # index 0: value

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for a, area in enumerate(areas) :
    print("room " + str(a) + ": " + str(area))
```
### Loop dictionary

```py
dict = { "key1":1,
	"key2":2,
	"key3":3 }
for key, value in dict.items() : # it could be k, v
	print(key + " - " + str(value)) # it doen't follow any order
```

### Loop Numpy Array 

```py
value = np.array([array1, array2])
for val in value :
	print(val)

for val in np.nditer(value)
	print(Val) # each value in each line, all the array1 and then array2
```

### Loop DataFrame

```py
DataFrame_name = pd.read_csv("csv_name.csv", index_col = 0)

for label, row in DataFrame_name.iterrows():
	print(label)
	print(row)
for label, row in DataFrame_name.iterrows():
	print(label + ": " + row["column_name"])

for label, row in DataFrame_name.iterrows():
	 DataFrame_name.loc[label, "Lenght"] = len(row["column_name"])
	 DataFrame_name.loc[lab, "COLUMN_NAME"] = row["column_name"].upper()

DataFrame_name["Lenght"] = DataFrame_name["column_name"].apply(len) # returns the same as before
DataFrame_name["COLUMN_NAME"] = DataFrame_name["column_name"].apply(str.upper)
```

### More about the for loop

The for loop does not require an indexing variable to set beforehand.

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break
```

Looping Through a String:

```py
for x in "banana":
	print(x)
```

Do not print banana:

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		continue
	print(x)
```

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

```py
for x in range(6): # Goes from 0 to 6, with 1 of increment
	print(x)

for x in range(2, 6): # Goes from 2 to 6, with 1 of increment
	print(x)

for x in range(2, 30, 3): # Goes from 2 to 30, with 3 of increment
	print(x)

fot x in range(4):
	pass # for loops cannot be empty, the pass statement to avoid getting an error

```
NOTE that for using the ```random()``` method several times I had to use ```[ expression for _ in range(100) ]```.

```py
random = [random.random() for _ in range(100)] # Returns a random float number between 0 and 1.
```

Now to use it, and make it run over all the elements in the array:

```py
# Calculate logarithm for each element in the array
log_R1 = [math.log(x) for x in R1]  # R1 is a random variable with uniform distribution
```

log_R1 returns:

![image](https://github.com/Rafaelatff/DataCamp-Intermediate-Python/assets/58916022/8f79d378-42b1-4a70-bde4-34e8450e1154)

## random

There are a lot of methods to use within the random packet. Here are listed 3 that called my attention:

* ```randrange()``` # Returns a random number between the given range.
* ```randint()``` # Returns a random number between the given range -1.
* ```random()``` # Returns a random float number between 0 and 1.

```py
import random

values = np.random.randint(-10,10,1000) # Lower limit, Upper limit, number of values : <class 'numpy.ndarray'>

print('Mean: ' + str(np.float64(np.mean(values)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(values)))) # Same as before

## or to generate 100 random numbers - random() doesn't has param: number of values 
random = [random.random() for _ in range(100)] # Returns a random float number between 0 and 1.
```

More about random

```py
np.random.rand() # Pseudo-random numbers between 0 and 1
np.random.seed(123) # Gives a seed for the random generator

outcomes = [] # Initialize an empty list

for x in range(10) :
	value = np.random.randint(0,10)
	outcomes.append(value)

tails = [0]
for x in range(10) : 
	coin = np.random.randint(0,2)
	tails.append(tails[x] + coin)

        # Replace below: use max to make sure step can't go below 0
        step = max(0, step -1)
```
## Relational Databases

Based on ralational model of data. Most common are: PostgreSQL, MySQL, SQLite. SQL stands for Structured Query Language.


### Creating a database engine

We will be using the SQLite because is fast and simple. 

#### SQLAlchemy

Works with many Relational Database Management Systems. 

```py
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Nortwind.sqlite')

# To know the names of the tables 
table_names = engine.table_names()
print (table_names)

```

#### Querying relational databases 

```py
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Nortwind.sqlite')

# Now lets quere the data
con = engine.connect() # Open the connection
rs = con.execute("SELECT * FROM Orders") # Returns all columns of all rows of the table 'Orders'
df = pd.DataFrame(rs.fetchall()) # Store data in a dataframe
df.columns = rs.keys() # To retrieve columns and rows names
con.close() # Important to close the connection at the end

print(df.head()) # To print content
```

It is possibe to use the context manager to keep connection opened:

```py
with engine.connect() as con:
	rs = con.execute("SELECT OrderID, ShipName FROM Orders") # Returns all columns of all rows of the table 'Orders'
	df = pd.DataFrame(rs.fetchmany(size=5)) # Store only 5 rows of data in a dataframe
	df.columns = rs.keys() # To retrieve columns and rows names
# Doesn't need to close connection
```
It is possible to filter the records by: SELECT * FROM Customer WHERE Country = 'Canada'
