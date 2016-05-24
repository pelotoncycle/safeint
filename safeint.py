import six


class int(int):

    def __new__(cls, value, base=None, digits=10, low=None, high=None):

        if value is None or value == '':
            return None

        if isinstance(value, six.string_types):
            if len(value) > digits:
                raise ValueError("invalid literal with base %r: %r" %
                                 (base or 10, value[:digits] + '...'))

        if base is None:
            value = super(int, cls).__new__(cls, value)
        else:
            value = super(int, cls).__new__(cls, value, base)

        if low is not None and value < low:
            raise ValueError("value=%r < low=%r" % (value, low))
        if high is not None and value > high:
            raise ValueError("value=%r > high=%r" % (value, high))
        return value
