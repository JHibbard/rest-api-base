# Internal Libraries
from rab.utils.annotations import experimental


def test_experimental():
    @experimental
    def func():
        """Documentation"""
        pass

    notice = (
        ".. Note:: Experimental: This method may change or "
        + "be removed in a future release without warning.\n"
    )

    assert func.__doc__ == (notice + """Documentation""")
