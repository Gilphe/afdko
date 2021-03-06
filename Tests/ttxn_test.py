from __future__ import print_function, division, absolute_import

import os
import tempfile

from runner import main as runner
from differ import main as differ

TOOL = 'ttxn'
CMD = ['-t', TOOL]

OTF_FONT = 'OTF.otf'
OTF2_FONT = 'OTF2.otf'
OTF3_FONT = 'OTF3.otf'
TTF_FONT = 'TTF.ttf'


def _get_expected_path(file_name):
    return os.path.join(os.path.split(__file__)[0], TOOL + '_data',
                        'expected_output', file_name)


# -----
# Tests
# -----

def test_dump_otf():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'o{}'.format(save_path),
                  '-f', OTF_FONT, '-n'])
    expected_path = _get_expected_path('OTF.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_otf_no_hints():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'nh', 'o{}'.format(save_path),
                  '-f', OTF_FONT, '-n'])
    expected_path = _get_expected_path('OTF_no_hints.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_otf_gpos_only():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'tGPOS', 'o{}'.format(save_path),
                  '-f', OTF_FONT, '-n'])
    expected_path = _get_expected_path('OTF_GPOS_only.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_otf_gsub_only():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'tGSUB', 'o{}'.format(save_path),
                  '-f', OTF_FONT, '-n'])
    expected_path = _get_expected_path('OTF_GSUB_only.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_otf2_gpos_only():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'tGPOS', 'o{}'.format(save_path),
                  '-f', OTF2_FONT, '-n'])
    expected_path = _get_expected_path('OTF2_GPOS_only.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_otf2_gsub_only():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'tGSUB', 'o{}'.format(save_path),
                  '-f', OTF2_FONT, '-n'])
    expected_path = _get_expected_path('OTF2_GSUB_only.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_otf3_gpos_only():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'tGPOS', 'o{}'.format(save_path),
                  '-f', OTF3_FONT, '-n'])
    expected_path = _get_expected_path('OTF3_GPOS_only.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_otf3_gsub_only():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'tGSUB', 'o{}'.format(save_path),
                  '-f', OTF3_FONT, '-n'])
    expected_path = _get_expected_path('OTF3_GSUB_only.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True


def test_dump_ttf():
    save_path = tempfile.mkstemp()[1]
    runner(CMD + ['-o', 'o{}'.format(save_path),
                  '-f', TTF_FONT, '-n'])
    expected_path = _get_expected_path('TTF.ttx')
    assert differ([expected_path, save_path,
                   '-s', '<ttFont sfntVersion']) is True
