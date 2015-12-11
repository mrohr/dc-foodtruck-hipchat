import foodtruck
import requests
import json

class Hipchat():
    def __init__(self, token, room_id):
        self.token = token
        self.room_id = room_id

    def hipchat_trucks(self, location, truck_list):
        if not truck_list:
            message = "No trucks found"
        else:
            message = "<br/>".join([str(t) for t in truck_list])
        message = "Trucks at " + location + ": <br/>" + message
        url = "https://api.hipchat.com/v2/room/%s/notification" % self.room_id
        payload = {'message': message, 'notify': True, 'color': 'random'}
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer %s' % self.token}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
