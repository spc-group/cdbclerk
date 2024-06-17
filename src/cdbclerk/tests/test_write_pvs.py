#from unittest import mock
#import pytest

#from cdbclerk.ioc_io import write_record

#@pytest.mark.asyncio
#async def test_write_record():
 #   ctx = mock.AsyncMock()
  #  ctx.get_pvs.side_effect = lambda pvs: [mock.AsyncMock() for pv in pvs]
   # # Run the function under test
    #fields = [".VELO"]
    #result = await write_record(prefix="255idcVME:m1", fields=fields, ctx=ctx)
    ## Check that the right data was stored in the results dictionary
    #assert ".VELO" in result.keys()

from unittest import mock
import pytest

from cdbclerk.ioc_io import write_record

@pytest.mark.asyncio
async def test_write_record():
    # Run the function under test
    fields = [".VELO"]
    values = [1.23]  # Provide the corresponding values
    # Set up fake PVs for testing only
    ctx = mock.AsyncMock()
    ctx.get_pvs.side_effect = lambda pvs: [mock.AsyncMock() for pv in pvs]
    pvs = await write_record(prefix="255idcVME:m1", fields=fields, values=values, ctx=ctx)
    # Check that the right data was stored in the results dictionary
    for pv, value in zip(pvs, values):
        assert pv.write.called
    