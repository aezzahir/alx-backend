#!/usr/bin/env python3
"""Server class to paginate a database of popular baby names.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
       Return a tuple
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get pages
        """
        try:
            type_er = "raised when page and/or page_size are not ints"
            assert isinstance(page, int), type_er
            assert isinstance(page_size, int), type_er
            assert page != 0 and page_size != 0, "raised with 0"
            assert page > 0 and page_size > 0, "raised with negative values"
        except AssertionError as e:
            raise AssertionError(e)

        pagination_range = index_range(page, page_size)
        if (pagination_range[0] >= len(self.dataset()) or
                pagination_range[1] >= len(self.dataset())):
            return []

        return self.dataset()[pagination_range[0]: pagination_range[1]]
