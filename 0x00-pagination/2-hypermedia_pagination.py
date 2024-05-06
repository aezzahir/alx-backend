#!/usr/bin/env python3
"""
0x00. Pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    0. Simple helper function
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)


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
        1. Simple pagination
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        2. Hypermedia pagination
        """
        data = self.get_page(page, page_size)
        next_page = page + 1 if self.get_page(page=page + 1,
                                              page_size=page_size) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {"page_size": len(data), "page": page, "data": data,
                "next_page": next_page, "prev_page": prev_page,
                "total_pages": total_pages}