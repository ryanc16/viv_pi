from src.main.main import Main
from importlib import import_module

config_module = import_module('config')
Main(config_module.SYSTEM_CONFIG)