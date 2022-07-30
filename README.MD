[![tests](https://github.com/ForsakenWing/spriteCloud-TechnicalTask/actions/workflows/tests-pipeline.yml/badge.svg?event=push)](https://github.com/ForsakenWing/spriteCloud-TechnicalTask/actions/workflows/tests-pipeline.yml)
## 1. How to run the tests locally

**Clone this repository first**
```
git clone https://github.com/ForsakenWing/spriteCloud-TechnicalTask.git
cd spriteCloud-TechnicalTask/
```
* If you already have docker-compose
```
docker-compose build
docker-compose up
```
* If you only have Python 3.6 or later
```
python3 -m venv .venv
source .venv/bin/activate
pip install docker-compose
docker-compose build
docker-compose up
```
* If you are using Ubuntu 20+
```
sudo apt install -y python3 python3-pip
sudo pip3 install docker-compose
docker-compose build
docker-compose up
```

## 2. How to run the test in a CI/CD pipeline
Send pull_request or push to master

<sub>pay attention to .github/workflows/tests-pipeline.yml</sub>

## 3. Has a link to the results in [Calliope.pro](https://app.calliope.pro/reports/140379/public/7eaac567-141d-4943-aacd-b644c1609f77)

## 4. Describe one improvement point and one new feature for the Calliope.pro platform

* Improvements point
> I would like to support for more plugins/frameworks like pytest-json-report.
> 
> Most painful was to see that plain/text is not supported. I had to remake logging logic 2 times because of this problems

* Feature point
> The best feature is to give users the opportunity to implement their custom structure of reports. It can decrease your stress and give us (users) more possibilities and flexibility while designing our tests 

## What you used to select the scenarios, what was your approach?
* Severity
> Without products in store users even cannot estimate their interest in buying pets exactly in this store. 
> But if we have to consider that unregistered users can't buy products in-store, 
> unfortunately, 3 tests won't enough for me to declare that a business at least in theory can get income.
* Priority
> Just 3 words. Opportunity/Requirement/Resources

## What could be the next steps to your project
> In the next steps I will continue working on tests because I can't even declare that product is working properly, and I'm not even speaking about user satisfaction


###### If you want to automatically send reports to calliope, you have to replace values in config_example with your own and change config_example.ini  filename to config.ini

