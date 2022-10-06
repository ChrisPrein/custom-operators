import asyncio
import unittest
from unittest.mock import MagicMock, Mock, patch
from typing import Any, Coroutine, List, Dict, Tuple

from src.custom_operators.operators.true_division import allow_zero

class AllowZeroTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_allow_zero_division_by_zero_should_return_zero(self):
        assert 2 /allow_zero/ 0 == 0