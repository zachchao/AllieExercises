# Exercise 3

This exercise will be significantly longer so don't feel pressured to finish it in one go as you probably can't. If you don't know how to do something just ask or Google. 

In this exercise you will teach you how to pass functions around, make a user interface that is constantly updating and interactive which takes in user input to create and display an array of HTML elements using JavaScript. You will also be introduced to JSON format and the BootStrap grid system.

Eg - you will be making an [interval alarm](https://interval-alarm.herokuapp.com/). Feel free to look and use it as reference but try not to look at the code. 


## Exercise 3.01 - The Clock
Make the primary component - the time's display. But in this version, add a button which switches between displaying the time in the format HH:MM:SS to displaying in the format HH:MM:SS (AM|PM).

### Things to look up and use
- SetInterval method
- Date() Objects

### Requirements
- Set the interval on a function called f. Make the button change what function is assigned to f. You should never need to clear and reassign this interval.
- Update every 500 milliseconds. 
- 

## Exercise 3.02 - Some CSS
We will now make our clock a little prettier. We are learning web development after all! Not just JavaScript.

### Things to look up and use
- margin: 0 auto;
- margin-top
- HTML title tag
- Bootstrap grid system

### Requirements
- Clock must be centered in the middle of the page horizontally with some vertical padding with the button horizontally aligned below the clock.
- Use some additional CSS to make it look better and include bootstrap.
- Make the title of this HTML page be equal to "Exercise 3".
- Use [Google Fonts](https://fonts.google.com/) to choose a better looking font for our time! 


## Exercise 3.03 - Initial Alarm
We will now begin adding an alarm to our clock. Make a new button which, when pressed, displays a countdown for two minutes before playing an alarm. Try to keep this flexible! Make the 120 seconds an argument or a variable as we will later change the alarm so that it can be anytime not just two minutes.

### Things to look up and use
- HTML DOM Audio Object
- Modulo operator
- Bootstrap col-6

### Requirements
- You must use the modulo operator, do not keep separate variables for minutes and seconds, only hold seconds. You may assume sixty seconds per minute. 
- The clock should display 00:00:00 when finished and stay there. 
- When counting down, the clock must go down exactly one second every second, it may not be fast or slow.
- Make a new function for the alarm. You should not need to modify old code, you should only need to add new code as long as you made your past code flexible. 
- Place the two buttons side by side and the two should remain horizontally centered under the clock display.
- Do not use the smoke alarm as I hate the sound and anyone who does so **WILL** receive a failing grade.


## Exercise 3.04 - User Input

### Things to look up and use
- Bootstrap Modal
- Forms
- JSON
### Requirements


## Exercise 3.05 - Alarm List

### Things to look up and use
- Document.createElement
- element.appendChild
### Requirements


## Exercise 3.06 - Putting it all together

### Things to look up and use
### Requirements


## Exercise 3.07 - Adding a remove button

### Things to look up and use
### Requirements


## Exercise 3.08 - Adding an edit button

### Things to look up and use
### Requirements


## Exercise 3.09 - Changing position of alarms

### Things to look up and use
### Requirements


## Exercise 3.10 - Saving state locally

### Things to look up and use
### Requirements


## Exercise 3.11 - Finishing touches

### Things to look up and use
### Requirements
