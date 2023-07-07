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

### Comparison Operators

For strings, it gets according to alphabel: 'rafaela' < 'amanda' ? The answer is False.
Comparators works same way as in C.
