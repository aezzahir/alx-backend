#!/usr/bin/env python3
"""
0. Simple helper function
"""


def index_range(page, page_size):
    """
       Return a tuple
    """
    return ((page - 1) * page_size, page * page_size)
