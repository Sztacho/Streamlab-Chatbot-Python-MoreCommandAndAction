import os
import sys
import clr

clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

mpa_dir = os.path.dirname(__file__)
modules_dir = os.path.join(mpa_dir, 'modules')
sys.path.append(modules_dir)
from Mpa_Settings_Module import MPASettings
from DB_Module import MPADatabase
from Mpa_Module import MPACore

# ================ Script Information =====================
ScriptName = "MC&A"
Website = "https://twitch.tv/stachopl"
Description = "Now your viewers has new interaction and commands"
Creator = "StachoPL"
Version = "1.0.0.0"
# =========================================================

core = None
mpa_core = None
mpa_settings = None
mpa_database = None


class CoreClass:
    parent = None
    mpa_core = None
    mpa_utils = None

    def __init__(self, parent):
        self.parent = parent
        self.mpa_core = MPACore(parent, mpa_settings)

    def check_permission(self, user, permission, info):
        data = Parent.HasPermission(user, mpa_settings.data[permission], mpa_settings.data[info])
        return data

    def check_cooldown(self, command):
        data = Parent.IsOnCooldown(ScriptName, mpa_settings.data[command])
        return data

    def check_command_active(self, command_active):
        data = mpa_settings.data[command_active]
        return bool(data)

    def message_incoming(self, data):
        if data.GetParam(0).lower() == mpa_settings.data['throw_command'] and not self.check_cooldown(
                'throw_command') and self.check_permission(data.User, 'throw_permission',
                                                           'throw_info') and self.check_command_active('throw_active'):
            self.mpa_core.throw_points_at_the_another_viewer(data.User, data.GetParam(1), data.GetParam(2))
            Parent.AddCooldown(ScriptName, mpa_settings.data['throw_command'], mpa_settings.data['throw_cooldown'])

        if data.GetParam(0).lower() == mpa_settings.data['uptime_command'] and not self.check_cooldown(
                'uptime_command') and self.check_permission(data.User, 'uptime_permission',
                                                            'uptime_info') and self.check_command_active(
            'uptime_active'):
            self.mpa_core.stream_uptime()
            Parent.AddCooldown(ScriptName, mpa_settings.data['uptime_command'], mpa_settings.data['uptime_cooldown'])

        if data.GetParam(0).lower() == mpa_settings.data['game_command'] and not self.check_cooldown(
                'game_command') and self.check_permission(data.User, 'game_permission',
                                                          'game_info') and self.check_command_active('game_active'):
            self.mpa_core.stream_game()
            Parent.AddCooldown(ScriptName, mpa_settings.data['game_command'], mpa_settings.data['game_cooldown'])

        if data.GetParam(0).lower() == mpa_settings.data['followage_command'] and not self.check_cooldown(
                'followage_command') and self.check_permission(data.User, 'followage_permission',
                                                               'followage_info') and self.check_command_active(
            'followage_active'):
            self.mpa_core.follow_age(data.User, data.GetParam(1))
            Parent.AddCooldown(ScriptName, mpa_settings.data['followage_command'],
                               mpa_settings.data['followage_cooldown'])

        if data.GetParam(0).lower() == mpa_settings.data['gamble_command'] and not self.check_cooldown(
                'gamble_command') and self.check_permission(data.User, 'gamble_permission',
                                                            'gamble_info') and self.check_command_active(
            'gamble_active'):
            self.mpa_core.gamble(data.User, data.GetParam(1))
            Parent.AddCooldown(ScriptName, mpa_settings.data['gamble_command'],
                               mpa_settings.data['gamble_cooldown'])


def LoadSettingsFile():
    settings_file = os.path.join(os.path.dirname(__file__), "settings/settings.json")
    globals()['mpa_settings'] = MPASettings(settings_file)


def InitSettings():
    globals()['mpa_settings'] = MPASettings()
    directory = os.path.join(os.path.dirname(__file__), "settings")
    if not os.path.exists(directory):
        os.makedirs(directory)
    LoadSettingsFile()


def InitDatabase(directory):
    database_location = os.path.join(directory, "MPADatabase.db")
    globals()['mpa_database'] = MPADatabase(database_location)


def InitDatabaseFile():
    directory = os.path.join(os.path.dirname(__file__), "databases")
    if not os.path.exists(directory):
        os.makedirs(directory)
    InitDatabase(directory)


def Init():
    InitSettings()
    InitDatabaseFile()
    globals()['core'] = CoreClass(Parent)


def Execute(data):
    if core is not None and data.IsChatMessage():
        core.message_incoming(data)


def Tick():
    return
