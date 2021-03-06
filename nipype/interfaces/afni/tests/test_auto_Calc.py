# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Calc


def test_Calc_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        expr=dict(
            argstr='-expr "%s"',
            mandatory=True,
            position=3,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file_a=dict(
            argstr='-a %s',
            mandatory=True,
            position=0,
        ),
        in_file_b=dict(
            argstr='-b %s',
            position=1,
        ),
        in_file_c=dict(
            argstr='-c %s',
            position=2,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        other=dict(argstr='', ),
        out_file=dict(
            argstr='-prefix %s',
            name_source='in_file_a',
            name_template='%s_calc',
        ),
        outputtype=dict(),
        overwrite=dict(argstr='-overwrite', ),
        single_idx=dict(),
        start_idx=dict(requires=['stop_idx'], ),
        stop_idx=dict(requires=['start_idx'], ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = Calc.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Calc_outputs():
    output_map = dict(out_file=dict(), )
    outputs = Calc.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
