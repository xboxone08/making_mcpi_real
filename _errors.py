class UnknownSwordError(ValueError):
    """The type of sword you passed to the Sword constructor was not
    recognized.
    """

    def __init__(self, sword=None):
        if sword is not None:
            super(UnknownSwordError, self).__init__(
                f"There is no such sword as {sword}")


class UnknownEnchantmentError(ValueError):
    """The enchantment you tried to add doesn't exist
    """

    def __init__(self, enchantment=None):
        if enchantment is not None:
            super(UnknownEnchantmentError, self).__init__(
                f"There is no such enchantment with id {enchantment}")
