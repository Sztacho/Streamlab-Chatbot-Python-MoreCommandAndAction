import json
import random


class MPACore(object):
    parent = None
    settings = None
    utils = None
    twitch_un_authorize_api = "https://api.crunchprank.net/twitch/"

    def __init__(self, parent, settings):
        self.parent = parent
        self.settings = settings

    def parse_string(self, parseString, data):
        string_to_parse = str(parseString)
        if "$username" in string_to_parse:
            string_to_parse = string_to_parse.replace('$username', data.get('user', None))
        if "$target" in string_to_parse:
            string_to_parse = string_to_parse.replace('$target', data.get('target', None))
        if "$amount" in string_to_parse:
            string_to_parse = string_to_parse.replace('$amount', data.get('amount', None))
        if "$currency_name" in string_to_parse:
            string_to_parse = string_to_parse.replace('$currency_name', self.settings.data['core_currency_name'])
        if "$uptime" in string_to_parse:
            string_to_parse = string_to_parse.replace('$uptime', data.get('uptime', 'error'))
        if "$game" in string_to_parse:
            string_to_parse = string_to_parse.replace('$game', data.get('game', 'error'))
        if "$followage" in string_to_parse:
            string_to_parse = string_to_parse.replace('$followage', data.get('followage', 'error'))
        return string_to_parse

    def throw_points_at_the_another_viewer(self, thrower, target, amount=10):
        data = {
            "user": thrower,
            "target": target,
            "amount": amount
        }
        if self.parent is not None:
            message = self.parse_string(self.settings.data['throw_response'], data)
            result = self.parent.RemovePoints(thrower, int(amount))
            if result:
                self.parent.SendStreamMessage(message)

    def get_uptime_from_api(self, user):
        headers = {}
        result = self.parent.GetRequest(self.twitch_un_authorize_api + 'uptime/' + user, headers)
        return json.loads(result)

    def get_game_from_api(self, user):
        headers = {}
        result = self.parent.GetRequest(self.twitch_un_authorize_api + 'game/' + user, headers)
        return json.loads(result)

    def get_follow_age_api(self, channel, user):
        headers = {}
        result = self.parent.GetRequest(
            self.twitch_un_authorize_api + 'followage/' + channel + '/' + user + '?precision=3', headers)
        return json.loads(result)

    def stream_uptime(self):
        self.parent.Log("test", str(dir(self.parent)))
        uptime = self.get_uptime_from_api(self.parent.GetChannelName())
        data = {
            "uptime": uptime['response']
        }
        message = self.parse_string(self.settings.data['uptime_response'], data)
        self.parent.SendStreamMessage(message)

    def stream_game(self):
        game = self.get_game_from_api(self.parent.GetChannelName())
        data = {
            "game": game['response']
        }
        message = self.parse_string(self.settings.data['game_response'], data)
        self.parent.SendStreamMessage(message)

    def follow_age(self, user, other_user_id=None):
        if other_user_id is not None and len(other_user_id) > 0:
            follow_age = self.get_follow_age_api(self.parent.GetChannelName(), other_user_id)
            message = self.parse_string(self.settings.data['followage_response'],
                                        {"user": other_user_id, "followage": follow_age['response']})
        else:
            follow_age = self.get_follow_age_api(self.parent.GetChannelName(), user)
            message = self.parse_string(self.settings.data['followage_response'],
                                        {"user": user, "followage": follow_age['response']})

        self.parent.SendStreamMessage(message)

    def gamble_round(self):
        random_number = random.randint(0, 2)
        return random_number > 0

    def gamble_game(self, user, amount):
        amount = int(amount)
        if self.gamble_round():
            win_amount = amount + (amount * 0.2)
            self.parent.AddPoints(user, win_amount)
            data = {
                "user": user,
                "amount": str(win_amount)
            }
            message = self.parse_string(self.settings.data['gamble_response_win'], data)
            self.parent.SendStreamMessage(message)
        else:
            self.parent.RemovePoints(user, amount)
            data = {
                "user": user,
                "amount": str(amount)
            }
            message = self.parse_string(self.settings.data['gamble_response_loss'], data)
            self.parent.SendStreamMessage(message)

    def gamble(self, user, amount):
        user_currency = self.parent.GetPoints(user)
        if amount == 'all':
            if user_currency > 0:
                self.gamble_game(user, user_currency)
        if isinstance(int(amount), int):
            if user_currency >= int(amount):
                self.gamble_game(user, amount)
