# Copyright (c) 2021 ICHIRO ITS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from yakusha import msg_to_json, json_to_msg
from yakusha.msg import Floats


def test_floats_msg():
    msg = Floats()

    msg.float32 = 3.1415
    msg.float64 = 3.14159265359

    parsed_msg = json_to_msg(msg_to_json(msg), Floats())

    assert parsed_msg.float32 == msg.float32
    assert parsed_msg.float64 == msg.float64


def test_floats_msg_negative():
    msg = Floats()

    msg.float32 = -3.1415
    msg.float64 = -3.14159265359

    parsed_msg = json_to_msg(msg_to_json(msg), Floats())

    assert parsed_msg.float32 == msg.float32
    assert parsed_msg.float64 == msg.float64


def test_floats_msg_from_json():
    msg_json = '''{
                    "float32": 3.1415,
                    "float64": 3.14159265359
                  }'''

    parsed_msg = json_to_msg(msg_json, Floats())

    assert parsed_msg.float32 == 3.1415
    assert parsed_msg.float64 == 3.14159265359


def test_floats_msg_from_json_negative():
    msg_json = '''{
                    "float32": -3.1415,
                    "float64": -3.14159265359
                  }'''

    parsed_msg = json_to_msg(msg_json, Floats())

    assert parsed_msg.float32 == -3.1415
    assert parsed_msg.float64 == -3.14159265359


def test_floats_msg_from_json_integer():
    msg_json = '''{
                    "float32": 10000,
                    "float64": 1000000000
                  }'''

    parsed_msg = json_to_msg(msg_json, Floats())

    assert parsed_msg.float32 == 10000.0
    assert parsed_msg.float64 == 1000000000.0
