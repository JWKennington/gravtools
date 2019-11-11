"""Tests for merger"""

import pytest
from pycbc import catalog

from gravtools import merger

SAMPLE_MERGER_SUMMARY = """
Merger GW150914:
    Mass1=35.6
    Mass2=30.6
    FinalSpin=0.69
""".strip()


class TestMerger:
    @pytest.fixture(scope='class', autouse=True)
    def m(self):
        return catalog.Merger('GW150914')

    def test_name(self, m):
        assert merger.name(m) == 'GW150914'

    def test_summary(self, m):
        assert merger.summary(m) == SAMPLE_MERGER_SUMMARY
