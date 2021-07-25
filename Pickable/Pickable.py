import pickle


def dump(obj, file_name, *args, **kwargs):
    """Writes the pickled representation of obj to a file."""
    with open(file_name, "wb") as fp:
        pickle.dump(obj, fp, *args, **kwargs)


def dumps(obj, *args, **kwargs):
    """Alias of pickle.dumps"""
    return pickle.dumps(obj, *args, **kwargs)


def load(file_name, *args, **kwargs):
    """Loads data from file."""
    with open(file_name, "rb") as fp:
        obj = pickle.load(fp, *args, **kwargs)
    return obj


def loads(bytes_object, *args, **kwargs):
    """Alias of pickle.loads"""
    return pickle.loads(bytes_object, *args, **kwargs)


class Pickable(object):
    """Add `dump[s]` and `load[s]` methods to object"""

    def dump(self, file_name, *args, **kwargs):
        """Writes the pickled representation of self to a file."""
        dump(self, file_name, *args, **kwargs)

    def dumps(self, *args, **kwargs):
        """Returns the pickled representation of self."""
        return dumps(self)

    @staticmethod
    def load(file_name, *args, **kwargs):
        """Returns a Pickable object loaded from a file."""
        return load(file_name)

    @staticmethod
    def loads(bytes_object, *args, **kwargs):
        """Returns a Pickable object loaded from bytes."""
        return loads(bytes_object)
