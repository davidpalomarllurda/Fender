1-Install Python 2.7.6   (This has been the version used to test the scripts)

2-Install PIP for this version of python

3-If windows version set the system path to call python/pip from command line

4-Install selenium libraries with pip ---- pip install selenium 

5- Dowload the chromedriver corresponding for your OS from http://chromedriver.storage.googleapis.com/index.html?path=2.22/

For example with windows, place chromedriver.exe inside this same folder since it will be called by the script.

6- Install behave BDD framework with pip ------- pip install behave

7- To execute the tests navigate through the command line to the folder where this readme.txt file is place and type: behave




**Note1: When opening a new browser session, which is the case of the tests,  it appears to be some bug on the fender page doing 
redirections, i.e when we go to update the location from en-IE to en-US, the new path is /GB-US/en_US which does not exists. So I added a workaround
to go back and forth in order to get to the US web page.

**Note2: Make sure that when running the tests, the mouse pointer is away from the web browser since this may activate some javascript
on the web page that may interfer witht the actual testing. 

Enhancements:

This exercise was done with the purpose of showing BDD approach using Gherking language. It was my first time using the BEHAVE framework and I had
to spend some time troubleshooting to get it to work properly (I think there is some issue on Windows machines when creating feature files and encodign in UTF-8)

Anyways, in this exercise, we are usign at a very high level a GIVEN, WHEN, THEN steps. This could have written more modular either making the scenarios smaller or
using more steps using Given this and this and this, when this and this and this, then this and this and this.

I normally map BDD from requirements, and as the requierements from the exercise sheet where high level I decided each step to have several actions, this can be broken down into many steps
as we wanted.

I added 5 scenarios to buy 5 different models of guitar, you will see in the feature file I have written the 5 scenarios, there are ways to parametrize all the guitar models, but due
to the encoding issue I found on windows, I had to write the 5 scenarios separately, this should be fixed using a unix/linux machine to create the feature files or
troubleshooting further the encoding issue creating feature files in windows.

For this exercise, I had to input quite a lot of time.sleeps to get better synchronization, I'd like to spend more time putting in place a better synch system
possibly using selenium explicit waits/expected conditions and also understanding why when using this framework I ran into some synch issues that required me
to put the time.sleeps in place


I'd like to do some more code refactoring and possibly add more comments, since we are using the same calls as in First_Selenium_Sequential folder. 

I'd like to do some refactoring of a couple of xpath queries I have used.


Obviously these are separated tests written in a short amount of time, the best way to do it would be building a test framework with methods
that would encapsulate all the selenium code and calling these methods from within the steps
