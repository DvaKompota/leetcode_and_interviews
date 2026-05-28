# QA Eng Lead Tech Challenge

0.0 The objective of this challenge is to provide an architectural solution to the problems below.

0.1 You should be able to explain each aspect of your architecture in depth, including how you would implement it.

0.2 You do not, however, need to implement anything.

## 1.0 Background

1.0 Review a relatively complex, but not unusual, network [Topology of an Iris Room](https://miro.com/app/board/uXjVI7_Ykhc=/?share_link_id=652752866832):
![Topology](./image.png)

1.1 The "Studio", is the frontend app that the user interacts with, it is a React application. It is deployed both to the web and an electron app. The "Bridge" is a Go application, it handles the actual media publishing and routing. The studio commands the bridge by updating the "state" of the bridge. Devices can be added/removed by updating the state and device settings can also be manipulated through this. The "state" for the bridge is a universal schema that is shared between the bridge and the studio projects.

1.2 Every "Bridge" is a part of a "Room". A "Room" can have multiple bridges, allowing users to horizontally scale hardware and balance load across hardware.

1.3 Every "Bridge" is unaware of every other bridge in the "Room", they exist in parallel and the "Studio" ties the experience together for the user. The execption to this is inter bridge media sharing, which is when we route media from one bridge to another (usually for output, switching, or recording).

1.4 This topology, is one of many that our users will encounter. They may have a single bridge and studio running on the same device. They may have entire control rooms of studios that require load sharing to prevent loading duplicate streams over the cloud.

## 2.0 Task

2.1 Design an automated QA Achitecture that provides "Crawl", "Walk", "Run" approach to automating the QA of a platform like Iris.

2.2 The "Crawl" approach should provide BASIC integration tests for Iris, should be able to deployed nearly immediately and iteratively improved, and ideally be able to rapidly scale tasks for a more junior team to take over. These tests should test the concept of multi bridge, however it can be simple setups.

2.3 The "Walk" approach should consider things like Unit testing, and what we should consider there.

2.4 The "Run" approach should be able to consider the topology documented in the above miro, as well as many others. It should be trivial to deploy these environments. It should be always running and putting Iris through its paces. It should test embedded software on a hardware array.

2.5 If you would like to include a "Fly" approach I would consider a technology like Auto Tracking, and how one might even begin to create automated tests for it, when it involves algorithsm that are responsible for coordinating motion with the camera.


## 3.0 Assumptions and Disclaimers

3.1 Communication with bridges and cameras is done via http requests (grpc will require some additional witchcraft)

3.2 Both Studio and Bridge are light enough apps, that can be compiled into binaries (this assumption is based on Studio being available as an Electron app, and Bridge being a Go-based backend), that can be launched by individual tests in parallel, in under 5 seconds, e.g. using [Testcontainers](https://testcontainers.com/).  
If it takes longer — consider deploying them in Docker once, and then share/reuse the containers across tests.

3.3 The "unit" tests mentioned in the "Walk" stage are feature-based E2E (UI+API) tests, not unit tests in the traditional sense. They cover separate functionality (features) of the Studio and Bridge applications, and can be run against deployed instances of the said applications. Traditional unit tests (run without deploying, provide code coverage, etc.) are implemented in the Studio and Bridge applications themselves, with tools like Jest, Storybook, Go testing, etc. They are not part of this challenge.

3.4 The speed and effectiveness of moving to "Walk", and especially to "Run" is somewhat dependent on the availability of a skilled DevOps engineer who can set up the necessary infrastructure and CI/CD pipelines. In the absence of such an engineer, the transition is still viable but may take longer and may end up being less efficient than the highest industry standards.


## 4.0 Foundational Principles

4.1 [TA Commandments](https://www.linkedin.com/feed/update/urn:li:activity:7308975051494633472/) FTW

4.2 General architecture should be based on the [Page / API Object Model](https://github.com/DvaKompota/FETA-TS-Playwright)

4.3 Tests should be runnable against any environment: local, dockerized, on-demand in CI/CD, or pre-deployed (staging, production, etc.), and not depend on any pre-existing data or state

4.4 Any and all tests should be able to run in parallel, not depending or interfering with each other, including the ability to run the same test in parallel threads (e.g. --repeat-each=100) to check for flakiness. The number of parallel workers/shards should be limited only by the available hardware resources, and not by the test framework or CI/CD configuration.

4.5 Acceptable level of flakiness is 0%, with a maximum number of retries set to 1 (to mitigate any external factors like network issues, etc.). If a test fails, it should be investigated and fixed, not retried.

4.6 Integrations that cannot be fully controlled (e.g. external APIs, third-party services, etc.) should be mocked to ensure consistent test results during development cycle. For RC validation real integrations can be used, if they are stable and reliable enough.


## 5.0 Proposed Architecture

5.1 The architecture is based on the [Page / API Object Model](https://github.com/DvaKompota/FETA-TS-Playwright). 
Framework is written in TypeScript (optionally can be also done in Python or Go, but the rollout will be slower), uses Playwright as the test runner, and is designed to be fast, reliable, modular, and easy to maintain. Framework is designed to reside in the same repository as the main application-under-test — this will be increasingly important starting from the "Walk" stage, and absolutely critical going forward.

5.2 **Fixtures**: represent application-under-test (Studio's UI, API, and optionally DB), and its dependencies (e.g. Bridge, Camera, etc.).
- **UiFixture**: contains all the framework's page objects to interact with the Studio's UI;
- **ApiFixture**: contains all the framework's API objects to interact with the Studio's APIs;
- **DbFixture**: contains a database connection, methods to interact with the database, and typical DB queries used in tests (e.g. to create data, validate changes, clean up, etc.);
- **BridgeFixture**: contains all the API objects to interact with the Bridge's APIs; can spin up Bridge instance(s), use pre-deployed one(s), or mock the Bridge's APIs;
- **CameraFixture**: mocks the camera's APIs, or, in some cases, can connect to real pre-deployed cameras; can be separate fixtures for different camera models, if needed.

5.3 **TestData**: represents the data classes used in tests: to create, update and validate synthetic test data, enabling full tests' independence from any pre-existing data and from each other.

5.4 **Utils**: are utility functions that can be used in tests, fixtures, and data classes to simplify the code and make it more reusable.

5.5 **Tests**: are generally written [like this](https://github.com/DvaKompota/FETA-TS-Playwright/blob/main/tests/example.test.ts); They can be grouped into `describe` blocks, separate files, or even separate directories/projects, depending on their scope and complexity of the setup they require. Each test can be devided into `test.step` blocks to make them more readable in the code and in the reports.

5.6 **Reporting**: can be done using the built-in Playwright reporters, can be extended with open source solutions like [ReportPortal](https://reportportal.io/) or [Allure](https://allurereport.org/), or commercial solutions like [TestRail](https://www.testrail.com/). Reports should include detailed information about each test, including its status, duration, and any errors or failures encountered during the test run, with all the attached artifacts (e.g. screenshots, videos, logs, etc.). Any third-party reporting solution used should be able to demonstrate test results over time, including trends, historical data, and other metrics that can help identify patterns and areas for improvement.


## 6.0 Implementation

6.1 **Crawl** (runnable in 1-2 days): 
- Implement basic Page / API Object Model architecture.
- Runs against pre-deployed local or cloud-based Studio and Bridge instances, via provided URLs/ports.
- Includes 1-10 simple "Smoke" tests that cover the most basic functionality of the Studio and Bridge. 
- Tests are workflow-based, i.e. they cover the most common/simple user journeys through the Studio and validate overall success rather than individual elements or features.
- Tests can be written with the [Playwright Test generator](https://playwright.dev/docs/codegen) to speed up the initial setup, with immediate refactoring to POM/APIOM after that.
- If one instance of Studio and Bridge can support multiple tests at the same time — runs tests in parallel, otherwise runs them sequentially.
- Synthetic test data generation is welcomed, but not required.
- No dockerization or CI/CD setup is done at this stage
Success criteria: 
- any developer on the team can run the tests locally against a pre-deployed Studio and Bridge instances, and can see the results in the console or Playwright HTML report

6.2 **Walk** (runnable in 2-4 weeks):
- All tests are refactored to use the Page / API Object Model architecture.
- Tests can run against any pre-deployed environment (local, staging, production, etc.) or, if the nature of the applications allows — each tests can launch its own instance(s) of Studio(s) and Bridge(s) in parallel, run against them, and then tear them down. 
- 50+ Most critical feature-based "Sanity" tests are implemented for the most used features of the Studio and Bridge, covering both UI and API interactions.
- All tests can run in parallel (with multiple workers on the same machine), not depending or interfering with each other, using 100% synthetic test data.
- Implementation of CI/CD pipelines within the said time frame can be dependent on the availability of a skilled DevOps engineer, but also can be done by the QA team with a little help and less strict time requirements. If implemented, it should support full dockerization, multiple parallel shards, and run tests on every commit, pull request, or on schedule.  
- Dev team is given basic training on how to write new E2E tests and can start contributing to the test suite, with the QA team providing guidance and support
Success criteria:
- any developer on the team can run the tests locally against pre-deployed Studio and Bridge instances (locally or in the cloud)
- if CI/CD is implemented at this stage — every commit, pull request, and release candidate is automatically tested by the full set of tests, with 100% pass rate being required for any merge to the main branch, let alone any release.


6.3 **Run** (runnable in 2-4 months):
- All tests are fully automated and can be run against any environment (local, dockerized, pre-deployed, CI/CD, etc.) without any pre-existing conditions or data.
- 100+ "Full Regression" end-to-end tests covering all major features of the Studio and Bridge applications, including multi-bridge setups, inter-bridge media sharing, etc.
- Every major integration is covered either by real pre-deployed instances of such integrations, or by mocks that simulate their behavior.
- All tests can run in parallel (multiple workers on multiple shards), providing full regression test coverage of every commit, PR or RC, with 0% flakiness under 5 minutes (provided that CI/CD infrastructure resources are sufficient).
- Every developer on the team can write new E2E tests to cover new features, bug fixes, and code changes they introduce — every PR, that introduces behavior changes, should include new/updated E2E tests to cover the changes. QA team can help with adjusting the testing strategy, expanding the coverage, and improving the tests' quality.
- Advanced reporting is implemented, providing detailed information about each test run, including trends, historical data, and other metrics that can help identify patterns and areas for improvement. Dev team is trained on how to read and interpret the reports, in case they are facing issues with their code or tests.
Success criteria:
- Every commit, PR, and RC is automatically tested via full regression test suite, that includes all major features and integrations, running in CI/CD in under 5 minutes, with 0% flakiness.
- Every PR with behavior changes includes new/updated E2E tests to cover the changes, and needs to be reviewed and approved by the QA team.


6.4 **Fly** (6+ months):
- E2E tests provide 100% feature coverage of the Studio and Bridge applications, including all integrations, and edge cases.
- Physical hardware is used to test embedded software and integrations with cameras for RC validation (e.g. camera light-boxes with calibration matrices, remote-controlled lights, etc.).
- Auto-tracking can be tested by mocking video streams and validating camera behavior based on the mocked data, or by using real cameras against pre-defined video feeds (e.g. against remote-controlled screens with pre-recorded videos).
- If time and resources allow, an AI-driven system that automatically generates comprehensive test suites by transforming Jira tickets and feature descriptions into executable Playwright tests, Page Objects, and API Objects with minimal human intervention can be developed. Such system should be able to reduce the time and effort required to write new tests at least by 50%, and should be able to generate tests that are as good as those written by experienced QA engineers.