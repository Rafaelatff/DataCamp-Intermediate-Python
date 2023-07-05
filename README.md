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

list_name = { "key_1":1, "key_2",2 } # Key value pairs
list_name["key_1"]
