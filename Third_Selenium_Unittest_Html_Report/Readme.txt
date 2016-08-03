1-Install Python 2.7.6   (This has been the version used to test the scripts)

2-Install PIP for this version of python

3-If windows version set the system path to call python/pip from command line

4-Install selenium libraries with pip ---- pip install selenium

5- Dowload the chromedriver corresponding for your OS from http://chromedriver.storage.googleapis.com/index.html?path=2.22/

For example with windows, place chromedriver.exe inside this folder since it will be called by the script.

New steps for this exercise:

6- Navigate to http://tungwaiyip.info/software/HTMLTestRunner.html and download HTMLTestRunner.py, place this file into C:/Python27/Lib folder


7- From the command line navigate to the path where the file for this exercises are stored, then run Fender_Smoke_Tests.py, 
then wait for the tests to end and open SmokeTest.html  results report.


**Note: When opening a new browser session, which is the case of the tests,  it appears to be some bug on the fender page doing 
redirections, i.e when we go to update the location from en-IE to en-US, the new path is /GB-US/en_US which does not exists. So I added a workaround
to go back and forth in order to get to the US web page.

**Note2: Make sure that when running the tests, the mouse pointer is away from the web browser since this may activate some javascript
on the web page that may interfer witht the actual testing. 