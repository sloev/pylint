"""Test for special methods implemented incorrectly."""

# pylint: disable=missing-docstring, unused-argument, too-few-public-methods
# pylint: disable=invalid-name,too-many-arguments,bad-staticmethod-argument

class Invalid(object):

    def __enter__(self, other): # [unexpected-special-method-signature]
        pass

    def __del__(self, other): # [unexpected-special-method-signature]
        pass

    def __format__(self, other, other2): # [unexpected-special-method-signature]
        pass

    def __setattr__(self): # [unexpected-special-method-signature]
        pass

    def __round__(self, invalid, args): # [unexpected-special-method-signature]
        pass

    def __deepcopy__(self, memo, other): # [unexpected-special-method-signature]
        pass

    def __iter__(): # [no-method-argument]
        pass

    @staticmethod
    def __getattr__(self, nanana): # [unexpected-special-method-signature]
        pass


class Valid(object):

    def __new__(cls, test, multiple, args):
        pass

    def __init__(self, this, can, have, multiple, args, as_well):
        pass

    def __call__(self, also, trv, for_this):
        pass

    def __round__(self, n):
        pass

    def __index__(self, n=42):
        """Expects 0 args, but we are taking in account arguments with defaults."""

    def __deepcopy__(self, memo):
        pass

    def __format__(self, format_specification=''):
        pass

    def __copy__(self, this=None, is_not=None, necessary=None):
        pass

    @staticmethod
    def __enter__():
        pass

    @staticmethod
    def __getitem__(index):
        pass