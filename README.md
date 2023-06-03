# Pomodoro Project
This is a Pomodoro project implemented using Python and Tkinter.
The Pomodoro Program is a simple timer application built using Python and the Tkinter library.
It follows the Pomodoro Technique, a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Features
* Countdown timer with work and break intervals.
* Visual indication of the current timer state (work or break).
*Start and reset buttons.
* Check marks to track completed intervals.

## Dependencies
1. Python: The programming language used to build the application.
2. Tkinter: The standard Python interface to the Tk GUI toolkit, used for creating the graphical user interface.
3. Math: A Python built-in module used for mathematical calculations.

## User Interface
The program creates a graphical user interface (GUI) using Tkinter with the following elements:

* Timer label: Displays the current timer state ("Work" or "Break").
* Tomato image and timer text: Shows a tomato image and the current time remaining in the interval.
* Start button: Starts the timer.
* Reset button: Resets the timer.
* Check marks labels: Displays check marks for completed intervals.

## Installation
To use this project, follow these steps:

1. Clone the repository: `git clone https://github.com/OrCHUK23/pomodoro.git`
2. Change to the project directory: `cd pomodoro`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the program: `python main.py`

## Usage
1. Start the timer by clicking the "Start" button.
2. The timer will count down the work duration (default: 25 minutes).
3. After the work duration, a short break (default: 5 minutes) will start automatically.
4. After the short break, the work duration will start again.
5. After every 4 work sessions, a longer break (default: 15 minutes) will be taken.
6. Use the "Reset" button to reset the timer and checkmarks.
