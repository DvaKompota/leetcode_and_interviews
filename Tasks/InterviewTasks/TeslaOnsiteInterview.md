# What You’ll Do

### Invent methods and build technology to execute tests and evaluate results efficiently and repeatedly
I wrote hundreds of automated test for various FE and BE applications.<br>
I know how to run them in repetitive, scheduled, or conditional manner in CI/CD or on their own.<br>
I have integrated different reporting tools, like TestRail, Cucumber, Robot Framework, etc. for visible results evaluation.<br>
<br>

### Specify, design, develop, integrate and maintain test automation frameworks and tools
I have designed and built 7 different test automation frameworks using Selenium, Cypress, and Playwright, as the main driver<br>
and frameworks like Robot Framework, Pytest, and Cucumber as a wrapper around such driver for running, parallelization, and reporting.<br>
I not only do this for work, but also in my free time, searching for an ideal combination of tools for testing.<br>
<br>

### Implement and execute test strategies on all supported platforms and languages to help improve overall quality and test code coverage.
I know how to build OS-independent test automation frameworks with multi-browser support to test apps in all possible combinations.<br>
I can write both in Python and TypeScript, and able to read Angular and React code, e.g. to add test-ids for test automation<br>
<br>

### Write backend integration tests as well as end-to-end tests for RESTful APIs, websockets, grpc, etc
I wrote a lot of backend tests for our FETA PyTest library when I wos working at BlueOwl, used mocks, provided 100% code coverage.<br>
I have experience in writing API tests using Robot Framework, PyTest, Cypress, Playwright, and Postman.<br>
I often use API calls within my FE test automation frameworks to perform setup steps or to speed-up test execution.<br>
<br>

### Design and develop integration, regression, and stress tests using industry standard tools.
My typical strategy for every framework that I've written is to use different sets of tests for different purposes<br>
and then use tags like `@smoke`, `@regression`, etc. to run specifically those sets depending on the task.<br>
<br>

### Collaborate with Business Analyst and Developers to understand requirements and translate them into test cases or need for additional test tooling
Starting with my very first job in software industry I've learned that trusting human connection and good chemistry<br>
with Development and Product team members is at least 50% of success for a QA engineer.<br>
Since then I always put additional effort into building such connections and chemistry in every team I work with.<br>
And it ALWAYS pays off.<br>
<br>

### Good knowledge of Web/UI testing.
Testing UI and UX of Web applications is my main specialty: in all companies I worked at in the last 4 years I was mostly testing Web apps<br>
<br>

### Define, implement, and maintain test plans, test specifications and test suites.
In every project that I worked on in the last 4 years I was the main (and mostly the only) person who defined test strategies,<br>
wrote test plans, test suites and test scenarios and then implemented all that in test automation on every level:<br>
from the highest abstractions to low-level interactions with browsers and APIs<br>
<br>

### Provide technical leadership, driving and performing engineering best practices to initiate, plan, and execute large-scale, cross-functional, and company-wide critical programs.
I am a strong advocate of clean and DRY code.<br>
I encourage project ownership approach.<br>
I prefer to build scalable, parallelizable, modular projects from start, even if necessity for that is not clear in the beginning.<br>
I have 4 years of team management experience (up to 7 team members).<br>
<br>

### Improve existing vehicle testing strategies.
I am an effectiveness maniac — have a strong internal drive to improve and optimize processes, that I am involved in.<br>
Tests failing for an unknown reason drive my crazy until I find the reason and fix it.<br>
For me an acceptable percentage of flaky tests is 0%<br>
<br>

### Track our automation testing progress with weekly reports.
I have a track record of building/tuning/integrating several reporting systems for daily/weekly/monthly visual reports of tests' performance.<br>
I am familiar with reporting tools like TestRail and Allure, and built-in reports of Cucumber, Robot Framework, Cypress, and Playwright.<br>
<br>

### Execute functional and regression tests as a part of release testing and triage results.
I've been doing that as my daily/weekly/bi-weekly/monthly routine for the last 4 years: both manually and through test automation.<br>
<br>

### Help identify software bugs through manual testing, automated scripting, and report investigation.
I've been doing that as my daily/weekly/bi-weekly/monthly routine for the last 4 years: both manually and through test automation.<br>
<br>



# Tell me about the hardest engineering problem you solved 

I can name 3 — all of them were pretty complicated for me at the time, but for different reasons:

### Building my first test automation framework using Robot Framework at AppZen
I was only 3 months into profession of a manual QA with 0 automation experience<br>
I needed to build a full-fetched FE test automation framework from scratch<br>
The framework was to have ~100 automated functional test cases that I was executing manually at the time<br>
This was in addition to manual validation of every new feature and every bi-weekly release coming to the app.<br>
I had only 3 months to complete the task.<br>
<br>
I finished 2.5 weeks early. The framework had less than 5% of flakiness (compared to ~15% my peers had),<br>
and finished 100+ FE tests in under 30 minutes (compared to ~4.5 hours for ~150 tests my peers had).<br>
<br>

### Building FETA Framework library to unify 3 separate Pytest frameworks at BlueOwl
It was a big refactoring project with lots of legacy code (mostly not clean) with little to no documentation.<br>
The project was performed jointly by 3 different SDETs (including me), which I never did before that.<br>
Almost every refactored function was slightly different in those 3 frameworks — we needed to satisfy all their use cases.<br>
All the new code was to be written in a very clean code manner (which I was not familiar at the time) and very documented per PEP-8.<br>
The entire library was to have 100% code coverage by unit tests, with heavy use of mocks (which I never heard of before that).<br>
The end result was to satisfy 5 different SDETs that used those 3 frameworks to test 3 very different applications.<br>
<br>
It did.<br>
<br>

### Building an integration of FETA Framework with TestRail reporting portal at BlueOwl
It was my solo task to build this integration from scratch to a turn-key solution that would fit all 3 Pytest frameworks (and liked by 5 SDETs).<br>
The only things I had available were PyTest documentation and TestRail public APIs — everything else I had to figure out myself.<br>
<br>
The solution I built was reporting tests live as they were executed (not at the end of the whole run), having logs and screenshots attached.<br>
It worked both with local and cloud-based test runs, supported our complicated tag system, and made beautiful reports, very easy to triage.<br>
