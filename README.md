Luna
====

Luna is a collection of Python utilies for working with the
[Selenium](http://docs.seleniumhq.org/) browser automation tool via its official 
[python library](http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html).

This includes:

* `SeleniumWrapper`, a wrapper for selenium `WebDriver` and `WebElement` objects
  which has two functions:

    *  Lets you specify a base URL for the driver so you can use only the relevant
       part of the URL in a test.

    *  Wraps all driver method calls in a loop that catches any resulting
       `NoSuchElementException` and retries the method call until it succeeds or
       the maximum retry duration is reached.

       The default is to retry every .5 seconds until 10 seconds have elapsed.
       These values can be changed by passing the `duration` and `interval`
       keyword arguments to any driver method call.

       In addition, since it can be a selenium error to find or click on a hidden
       element, and is almost certainly a test semantics error, the default
       behavior is to ensure that any `WebElement` returned by a wrapped method
       call is displayed, or else continue the retry loop until it is.  This can
       be overridden by passing `ensure_displayed=False`.

       The error message on failure can be set by passing the `msg` keyword
       argument.

* `SeleniumTestCase`, a unittest TestCase that lets you specify a browser and a
  base URL as class properties, and automatically starts and stops a selenium
  driver as part of its `setupClass()` and `tearDownClass()` classmethods.

  `__getattr__` is also overridden so you can use `self.find_element_by_id()`
  instead of `self.driver.find_element_by_id`

* A Django `manage.py seltest` command for running tests found in the `tests/selenium`
  directory of installed applications.  The same argument semantics as the
  Django default test command apply, except you may also specify the browser
  name or remote selenium driver URL as the first argument.

  These localsettings control the behavior of this command:

```python
SELENIUM_SETUP = {
    # Firefox, Chrome, Ie, or Remote
    'BROWSER': 'Chrome',

    # Necessary if using Remote selenium driver
    'REMOTE_URL': None,

    # If not using Remote, allows you to open browsers in a hidden virtual X
    # Server
    'USE_XVFB': False,
    'XVFB_DISPLAY_SIZE': (1024, 768),
}
```
