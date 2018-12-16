import argparse


class Arguments(object):
    def __init__(self, **kwargs):
        self._data = kwargs
        for k, v in kwargs.items():
            self._key_to_attr(k, v)

    def _key_to_attr(self, key, value):
        if hasattr(self, key):
            raise RuntimeError(f"Cannot use {key}!")
        setattr(self, key, value)

    def dict(self):
        return dict(self)

    def __getitem__(self, name):
        return self._data[name]

    def __iter__(self):
        for k, v in self._data.items():
            yield k, v

    def __repr__(self):
        repr = "Arguments("
        for k, v in self._data.items():
            repr += f"{k}={v}, "
        repr = repr[:-2]  # to remove the last ', '
        return repr + ")"


class ArgumentParser(object):
    def __init__(self, description=None):
        self._argparser = argparse.ArgumentParser(description=description)

    def _add_args(self, *options, type=None, default=None, choices=None, help=None,
                  **kwargs):
        if default is None and choices is not None:
            default = choices[0]
        if default is not None:
            if help is None:
                help = ""
            help += f"(default={default}/ type={type.__name__})"
        self._argparser.add_argument(*options, type=type, default=default,
                                     choices=choices, help=help, **kwargs)

    def add_int(self, *options,  default=None, choices=None, help=None):
        self._add_args(*options, type=int, default=default, choices=choices, help=help)

    def add_float(self, *options,  default=None, choices=None, help=None):
        self._add_args(*options, type=float, default=default, choices=choices, help=help)

    def add_str(self, *options,  default=None, choices=None, help=None):
        self._add_args(*options, type=str, default=default, choices=choices, help=help)

    def add_true(self, *options, help=None):
        if help is None:
            help = ""
        help += f"if not specified, false"
        self._argparser.add_argument(*options, action="store_true", help=help)

    def add_false(self, *options, help=None):
        if help is None:
            help = ""
        help += f"if not specified, true"
        self._argparser.add_argument(*options, action="store_false", help=help)

    def add_multi_int(self, *options,  default=None, choices=None, help=None):
        self._add_args(*options, type=int, default=default, choices=choices, nargs="+", help=help)

    def add_multi_float(self, *options,  default=None, choices=None, help=None):
        self._add_args(*options, type=float, default=default, choices=choices, nargs="+", help=help)

    def add_multi_str(self, *options,  default=None, choices=None, help=None):
        self._add_args(*options, type=str, default=default, choices=choices, nargs="+", help=help)

    def parse(self, return_unknown=False):
        known, unknown = self._argparser.parse_known_args()
        known = Arguments(**vars(known))
        if return_unknown:
            return known, unknown
        else:
            return known
