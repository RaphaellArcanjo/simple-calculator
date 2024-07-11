## *Simple calculator*
<p>
    This project is a calculator with basic functions in order to learn and improve my knowledge in python. I used the TKINTER library to make the project's interface. We only use three functions in the project.
</p>

### *Requirements*
- Know python and tkinter

#### *Installation*
    git clone git@github.com:RaphaellArcanjo/simple-calculator.git

### *Use*
```python
def enter_value(event):
    global all_value

    all_value = all_value + str(event)
    text_value.set(all_value)
```
###### This function is called when an event is triggered, and takes an event parameter. It is responsible for adding the event value to the global variable all_value. The event value is converted to a string before being added. The function then updates the text_value variable with the current value of all_value.

```python
def calculate():
    global all_value
    result = eval(all_value)
    text_value.set(result)
    all_value = str(result)
```
###### This function is called when you want to calculate the result of the expression stored in all_value. First, the function uses the eval() function to evaluate the expression stored in all_value and assign the result to the result variable. Then the function updates the text_value variable with the result value and converts the result to a string. Finally, the function updates all_value with the result string.
```python
def clear_screen():
    global all_value
    all_value = ''
    text_value.set('')
```
###### This function is called when you want to clear the screen. It resets the all_value global variable to an empty string and updates the text_value variable to an empty string as well. This results in the screen being cleared, removing any previously displayed values ​​or results.

### *License*
#### - The Unlicense

### *Contact*
  - Name: Raphaell Arcanjo
  - E-mail: raphaellarcanjo28@gmail.com

#### *Special thanks*
###### I took inspirations from [Lilizok4 ASMR's](https://www.youtube.com/watch?v=NhNORVxdOsc&t=2119s) youtube channel and the site [UsandoPy](https://www.usandopy.com/pt/artigo/como-fazer-calculadora-em-python/)
