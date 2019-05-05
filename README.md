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


## Exercise 3.04 - User Input And Looping
At the moment our alarm only works for two minutes and only once. We will now augment it to take in a user's input and loop as well as introducing you to JSON. You will be using Bootstrap's modal to take in the input, storing the input in a JSON object then triggering the alarm and running the alarm in a loop.

### Things to look up and use
- Bootstrap Modal
- HTML Forms
- JSON

### Requirements
- Using Bootstrap's grid system, split the page into different sections, whether it be vertically or horizontally there should be one part of the page which contains everything you have previously created and a new part which will contain nothing.
- You must use the Bootstrap modal to take in user input, trigger it with a button within the new section of the page you just created. 
- The form should take in the alarm's name, sound to play, and the amount of time to play it, you decide on minutes or seconds or both as well as any other parameters you deem necessary. Store all of this information within a JSON object in a variable.
- The form should be formatted nicely and use Bootstraps form components to look good!
- Change your count down function to depend on the new JSON object you have created
- Make a new function which simply plays the alarm sound for x amount of calls to the setInterval then stops the alarm sound and changes the function back to the count down. It should alternate between the two functions, displaying the count down and playing the alarm.
- Make sure to change the alarm sound depending on the option the user picks!


## Exercise 3.05 - Alarm List
At the moment we can only add one alarm. We will now display a list of alarms. 

### Things to look up and use
- Document.createElement
- element.appendChild

### Requirements
- Modify your form so that instead of setting a variable to a JSON object, hold a list of JSON objects and simply add to that list. The list should look something like 
```
[
	{
		"alarmName" : "Study",
		"alarmMinutes" : 25,
		"alarmSound" : "option 1"
	},
	{
		"alarmName" : "Break",
		"alarmMinutes" : 5,
		"alarmSound" : "option 2"
	}
]
```
- Create a new div above the add alarm button which opens the modal, using `Document.createElement` and `element.appendChild`, add a component of your choosing to display each alarm. 
- These changes can remain cosmetic for now as your next task will be to implement using this list into your loop.
- You are done when every time you input the form you successfully add to both the list of JSON objects as well as visually see the alarm in 


## Exercise 3.06 - Putting it all together
We will now add functionality to our alarm list. Cycling through it.

### Things to look up and use
- (Just for fun if you want to) FIFO Queue

### Requirements
- Add a new variable called `currentIndex` which begins at zero. The count down and alarm function will use the JSON object at the `currentIndex`. Each time the alarm ends, increment the `currentIndex` and if you implemented everything right it should cycle through the list of alarms.
- Change the color of the component currently running in the alarm list so it is clear which alarm we are on currently. You may find this difficult without some special logic.


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
