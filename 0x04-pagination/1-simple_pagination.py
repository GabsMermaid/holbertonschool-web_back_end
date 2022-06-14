#!/usr/bin/env python3

""" Copy index_range from the previous task and
the following class into your code """

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Find the correct indexes to paginate the dataset correctly and return
    the appropriate page of the dataset (i.e. the correct list of rows) """

    start = (page-1) * page_size
    end = page * page_size
    # end = start + page_size
    i_range = (start, end)
    return i_range


class Server:
    """ Server class to paginate the
    database for popular baby names """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Verify that both arguments are integers greater than 0. """

        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        gp_range = index_range(page, page_size)
        gp_start = gp_range[0]
        gp_end = gp_range[1]
        return self.dataset()[gp_start:gp_end]
