{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pytest\
from app.calc import add, divide\
\
def test_add():\
    assert add(2, 3) == 5\
    assert add(-1, 1) == 0\
\
def test_divide():\
    assert divide(6, 2) == 3\
    assert pytest.approx(divide(1, 3), 1e-6) == 0.3333333333333333\
\
def test_divide_by_zero():\
    import pytest\
    with pytest.raises(ValueError):\
        divide(1, 0)\
}