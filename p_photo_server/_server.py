import argparse
import logging
import asyncio

def parse_args():

    return


class logger:
    def __init__(self, file_location, name) -> None:
        self._file_location = file_location
        self._name = name
        pass

    def create_log(self) -> None:
        logging.basicConfig(filename=self._name)

    def log_item(self, time, item: str) -> None:
        logging.info(str(time)+item)