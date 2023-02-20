#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    if page <= 1:
        return (0, page_size)

    else:
        return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)