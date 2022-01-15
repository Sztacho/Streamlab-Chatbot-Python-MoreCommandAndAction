import codecs
import json


class MPASettings(object):
    def __init__(self, settings_file=None):
        try:
            with codecs.open(settings_file, encoding="utf-8-sig", mode="r") as f:
                self.data = json.load(f, encoding="utf-8")
        except:
            pass

    def Reload(self, json_data):
        self.data = json.loads(json_data, encoding="utf-8")

    def Save(self, settings_file):
        try:
            with codecs.open(settings_file, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.data, f, encoding="utf-8")
            with codecs.open(settings_file.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("const settings = {0};".format(json.dumps(self.data, encoding='utf-8')))
        except:
            pass