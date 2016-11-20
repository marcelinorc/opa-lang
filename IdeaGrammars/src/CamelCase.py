from dragonfly import Text


class CamelCase(Text):

    def __init__(self, spec=None, static=False, pause=Text._pause_default,
                 autofmt=False):
        super(CamelCase, self).__init__(spec, static, pause, autofmt)

    def _parse_spec(self, spec):
        spec = spec.title()
        spec = spec.replace(" ", "")
        return super(CamelCase, self)._parse_spec(spec)