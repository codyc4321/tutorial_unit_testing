#!/usr/bin/env python3

references = [
    "https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/",
]


LESSON_MESSAGES = [
"""
Unit testing is a method for testing software that looks at the smallest testable pieces of code, called units, which are tested for correct operation.
By doing unit testing, we can verify that each part of the code, including helper functions that may not be exposed to the user,
works correctly and as intended.

The idea is that we are independently checking each small piece of our program to ensure that it works.
This contrasts with regression and integration testing, which tests that the different parts of the program work well together and as intended.
""",

"""
Unit tests verify that the methods you write work as corrected in the future, mainly to allow you to make changes to the code and
automatically verify your code still works after you change it.

This allows you to work quickly and efficiently as the project grows, as making significant changes to a method written weeks ago
only takes about 5-10 seconds to verify.
""",

"""
Well-written unit test can save several hours often tedious and frivolous manual testing per week, such as walking through the debugger or writing throwaway print statements.

If a project grows into a very large and complex system, with numerous collaborators at the same time, unit tests can even save dozens,
or hundreds of hours of time, with a very minimal amount of investment compared with how much time debugging would take \
if you didn't have tests...would you rather spend 20 hours writing creative tests and learning while documenting your code, \
or 60 hours of boring debugger walkthroughs?

The time unit tests save you can grow exponentionally as the project codebase grows rapidly.""",

"""
Unit tests are self-documenting...if the project gets moved to a new teammate for maintainence, they can become productive immediately
by merely running your tests and seeing what they broke, or even just reviewing your tests as soon as they download the code.
This is because unit tests show a result, and an expectation, and the hard-coded expecation statements document what the method was intended to do.
""",

"""
Another key benefit of unit tests is that they help easily isolate errors.
Imagine running the entire project and receiving a string of errors. How would we go about debugging our code?

A test failure means the code can run, but the test result didn't match the expecation we gave the test.

An error running the tests means the code the test relies on actually cannot run, such as typos like

    def myfunction()):;

It may be hard to read the entire stacktrace and determine where the data got corrupted by a logic error without lots of manual debugging.
Unit tests show us exactly where our program went wrong, giving you the test file, and the test that failed for a failure.
For an error, they show you what line of code is broken.

You may still do some manual debugging, but unit tests give you a much easier and more descriptive starting point, saving very much time longterm even though you invested time initially writing your tests.
""",

"""
The 2 main Python testing frameworks are the built-in 'unittest' framework (PyUnit), and the 3rd-party Pytest

Pytest was created to overcome some shortcomings of unittest, primarily verbose assertion statements such as

    self.assertEqual(1, 1)
    
instead of 

    assert 1 == 1
    
Pytest wraps the Python 'assert' keyword, and gives detailed error messages when a test fails.
Pytest also has colorized, human readable test failure output.

I would like to convert all my tests to Pytest and only use it in the future, when I find time.
""",


]

# LESSON_MESSAGES = [introduction_message, overview_message, benefits_message, error_isolation_message]


def walk_through_lesson():
    current_index = 0
    print("\n\n")
    while current_index < len(LESSON_MESSAGES):
        print(LESSON_MESSAGES[current_index])
        print("\n\n")
        command = input()
        if command not in ["", "f", "forward", "b", "back"]:
            COMMAND_ERROR_MESSAGE = "Just hit enter or say 'f' to go forward, or say 'b' to go backwards."
        if command in ["", "f", "forward"]:
            current_index += 1
        if command in ["b", "back"]:
            if current_index == 0:
                print("\n\n**You're already at the beginning of the lesson.**")
            else:
                current_index -= 1
    print("\n\nThank you for completing this lesson!")


"""uncomment this assertion statement to show why we have to separate our tests from the code and use a testrunner"""
# assert 1 == 2

walk_through_lesson()
