from configparser import ConfigParser


def read_config(category, key):
    """
    Reads a configuration value from a specified category and key in the config file.

    :param category: The section in the config file from which to read the value.
    :param key: The key within the section whose value is to be retrieved.
    :return: The value associated with the specified key in the given category.
    """
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category, key)