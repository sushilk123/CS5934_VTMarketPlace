"""
vtmarketplace exceptions classes
"""


class vtmarketplaceError(Exception):
    """
    Creating user which already exist.
    """

    def __init__(self, *args, **kwargs):
        super(vtmarketplaceError, self).__init__(*args, **kwargs)
