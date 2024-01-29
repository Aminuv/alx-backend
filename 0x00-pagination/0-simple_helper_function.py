#!/usr/bin/env python3
"""
    Module to contains the function that calculates the
start and end index for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
