# DC Foodtruck Hipchat Alert

A configurable set of scripts to run on AWS Lambda that sends notifications to a hipchat room with the current state of foodtrucks in the Washington DC area as provided by http://foodtruckfiesta.com/


## Installation
 ```sh
$ git clone https://github.com/mrohr/dc-foodtruck-hipchat.git
$ cd dc-foodtruck-hipchat
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cp config.example.json config.json
$ vim config.json 
$ ./build.sh
```

You will now have an out.zip file ready to be uploaded to a lambda function.  Once you have uploaded your zip file to a lambda function, go to the Configuration tab and set the handler to :
```
cron.notify
```
You can then set up a 'scheduled event' event source that will run this function every day to let everyone know whats for lunch!

## Config Options
- **locations** - An array of locations that should be pulled from Food Truck Fiesta.  You can view the list of locations at  http://foodtruckfiesta.com/dc-food-truck-list/
- **token** - your hipchat auth token
- **room_id** - the hipchat room id for the room you want your notifications posted
