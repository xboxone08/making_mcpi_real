class UnknownSwordTypeError(ValueError):
    """The type of sword you passed to the Sword constructor was not
    recognized.
    """
    pass


class UnknownEnchantmentError(ValueError):
    """The enchantment you tried to add doesn't exist
    """
    pass
