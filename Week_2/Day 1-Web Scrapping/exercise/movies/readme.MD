## Background & Objectives

- Using a package of the standard library
- Working with CSV file input

In order to read a CSV file and extract its data you can use the `csv` package that comes with python standard library.
The CSV given as an example in `lib/movies.csv` has been taken from [IMDB](http://www.imdb.com/boxoffice/alltimegross).

#### Python Standard Library

The python standard library includes all the convenient packages that come with your installation. For instance the [time](https://docs.python.org/2/library/time.html

) module, if included in your python program, enables you to manipulate dates easily. An external library is loaded at the beginning of your python file with:

```python
import time
```

There are loads more useful ones in there too, so make sure you have a read!

## Requirements

- implement `def most_successful` that returns the number of movies published prior to a given year, with associated earnings.
- **constraint**: the returned list should be a list/dic of movies. Each movie should be represented by a dictionary with keys `name`, `year` and `earnings`. Ex: `{ name: "Avatar", year: 2009, earnings: 760505847 }`

## Further suggestions & resources

- Make sure you specify the good `encoding` options for reading the CSV.
Remember, some titles are given in other languages and have special characters 😉
