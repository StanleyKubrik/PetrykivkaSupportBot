import configparser
import os


class Config:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileExistsError
        self.configuration = configparser.RawConfigParser()
        self.configuration.read(path, encoding='1251')

    def get_setting(self, section, setting):
        return self.configuration.get(section, setting)

    def get_section(self, section):
        return self.configuration.options(section)

    def set_setting(self, section, setting, value):
        self.configuration.set(section=section, option=setting, value=value)

    def has_section(self, name):
        return self.configuration.has_section(name)

    def has_option(self, section, option):
        return self.configuration.has_option(section, option)
