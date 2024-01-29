#!/usr/bin/env python3
"""
 Module to contain the Server of class that paginates
a database of popular baby names.
"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ Calculate """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """ The Server class. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ The cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ The return. """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
