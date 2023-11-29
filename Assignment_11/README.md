# Assignment 11
In this section, exercises are done to familiarize and understand **object-oriented programming** in Python.

## 11.1 Fraction

In this exercise, a **class** is defined for fractions using object orientation.

```python
class Fraction:
    def __init__ (self)
        #properties
        ...
    #methods
    def method_1(self):
        ...
    def method_2(self):
        ...
```
#### properties in this class:

```python
#properties
self.numerator = num1
self.denominator = num2
```

Two numbers that are the **numerator** and **denominator** of the fraction.

#### methods in this class:

```python
#methods
def sum_fraction (self, fraction):
    ...
def mul_fraction (self, fraction):
    ...
def sub_fraction (self, fraction):
    ...
def div_fraction (self, fraction):
    ...
def fraction_to_number (self):
    ...
def sim_fraction (self):
    ...
def show_fraction (self):
    ...
```
Seven functions that perform `addition`, `multiplication`, `subtraction`, `division` between **two fractions** and `converting` the fraction to a number, `simplifying` the fraction and `displaying` the fraction, respectively.

## 11.2 Time

In this exercise, a **class** is defined for time using object orientation.

```python
class Time:
    def __init__ (self)
        #properties
        ...
    #methods
    def method_1(self):
        ...
    def method_2(self):
        ...
```
#### properties in this class:

```python
#properties
self.hour = hour
self.minute = minute
self.second = second
self.fix ()
```
The three numbers that are **hour**, **minute** and **second** of the time and calling the `fix()` to modify the time.

#### methods in this class:

```python
#methods
def show_time (self):
    ...
def sum_time (self, time):
    ...
def sub_time (self, time):
    ...
def second_to_time (self, second):
    ...
def time_to_second(self, time):
    ...
def GMT_to_tehran_time(self, GMT):
    ...
def fix (self):
    ...
```
Seven functions that perform `displaying` the time, `addition`, `subtraction` between **two times** and `converting` "the second to time", "time to second" and "GMT time to Tehran's time" and `fix` the time respectively.



## 11.3 Complex numbers

In this exercise, a **class** is defined for complex numbers using object orientation. 


```python
class Complex_numbers:
    def __init__ (self)
        #properties
        ...
    #methods
    def method_1(self):
        ...
    def method_2(self):
        ...
```
#### properties in this class:

```python
#properties
self.real= real
self.image= image
```
Two numbers, **real** and **image**, which form a complex number.

#### methods in this class:

```python
#methods
def show_complex (self):
    ...
def sum_complex (self, complex):
    ...
def sub_complex (self, complex):
    ...
def mul_complex (self, complex):
    ...
```
Four functions that perform `displaying` the complex number, `addition`, `multiplication`, and `subtraction` between **two complex numbers** respectively.