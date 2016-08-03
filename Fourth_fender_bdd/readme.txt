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