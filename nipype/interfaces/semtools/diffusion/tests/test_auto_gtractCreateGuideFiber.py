# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..gtract import gtractCreateGuideFiber


def test_gtractCreateGuideFiber_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        inputFiber=dict(argstr='--inputFiber %s', ),
        numberOfPoints=dict(argstr='--numberOfPoints %d', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputFiber=dict(
            argstr='--outputFiber %s',
            hash_files=False,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        writeXMLPolyDataFile=dict(argstr='--writeXMLPolyDataFile ', ),
    )
    inputs = gtractCreateGuideFiber.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_gtractCreateGuideFiber_outputs():
    output_map = dict(outputFiber=dict(), )
    outputs = gtractCreateGuideFiber.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
