# trip_planner_ENSF_607_608_Group_15_testing

Authors:

## Description
- This project was created to test [trip_planner_ENSF_607_608_Group_15_development](https://github.com/ENSF-607-608-Group-15/trip_planner_ENSF_607_608_Group_15_development.git)
- The framework incorporates the following elements:
  - Behavior Driven Development (BDD) using [Behave](https://behave.readthedocs.io/en/latest/)
  - [Selenium](https://www.selenium.dev/), as testing framework (to interact with web elements)
  - [Python](https://www.python.org/doc/), as programming language
  - [Page Object Model (POM)](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/), as design pattern (commonly used with Selenium)
  - [Optional] [Allure Behave](https://allurereport.org/docs/behave/), to generate HTML reports

 _Note: This project was developed using the work done in [source link](https://github.com/arunmotoori/TutorialsNinjaBehaveBDDHybridFrameworkWithPageObjectModel) as guidance_


## Why is this a good framework?
- BDD uses gherkin syntax so our tests are written in a language very similar to plain english, which means our tests are self documented and directly translate to user requirements
- Behave allows us to use `context` to specify flexible objects / properties defined in runtime per session (scenario), which allows tests to run in parallel
- Selenium allows us to test in different browsers and platforms to ensure our app is reliable
- POM allows us to keep loose coupling and high cohesion
  - Each page (object) is separated, and all locators are constants specified per page
  - The methods are defined in the highest class (i.e., `BasePage`)
- Code is highly reusable and new tests are very simple to be created, we simply have to create a `scenario` or `feature`, define the `steps` and, if not defined, the locators in the `page` class
- The framework allows us to fully do E2E testing
- Allure Behave provides a descriptive visualization of our tests results, including screenshots whenever they fail


## How to run
1. Clone the repository to your computer
2. If testing locally, make sure the project is running locally
   1. Replace `url` in `config.ini` for the URL and port your local project is using (e.g., http://localhost:3000/) 
2. If testing in deployed version, replace `url` in `config.ini` for the deployment URL
3. Set up your Python env using the packages defined in `requirements.txt`, i.e., install required packages
   1. _Note: `allure-behave` is optional. It requires you to have `Java` installed and having a `JAVA_HOME` environment variable pointing to a JRE_
4. In a terminal, `cd` to the project location and run it using, one the following commands:
   1. `behave features`, to run all tests (i.e., all `feature` files)
   2. `behave --tags=<tag1,tag2,...,tagN>`, to run specific scenarios decorated by a tag, e.g. `behave --tags=login,anothertag`
      1. _Note: a `tag` is a decorator (using `@`) specified over a `Scenario`, e.g. `@login`_
   3. `behave -f allure_behave.formatter:AllureFormatter -o reports/ features`, to run all scenarios and generating an allure behave report
      1. Then use `allure serve reports` to visualize your results
   4. `behave -f allure_behave.formatter:AllureFormatter -o reports/ --tags=<tag1,tag2,...,tagN>`, to run specific scenarios decorated by a tag, e.g. `behave --tags=login,anothertag` and generating an allure behave report
      1. Then use `allure serve reports` to visualize your results

## How to create a test scenario
1. Create the test `Scenario`(s) using gherkin syntax in the corresponding `feature` file
2. Create the binding code, i.e., the steps, for the `Scenario`
3. Reuse available functions and locators for the corresponding page or define new ones, if needed
   1. _Note: To figure out the locators on the page for the element you want to interact with, spy on the element using the browser's dev tool_
