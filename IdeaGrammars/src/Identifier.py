from dragonfly import Text


class Identifier(Text):

    def __init__(self, spec=None, static=False, pause=Text._pause_default,
                 autofmt=False):
        super(Identifier, self).__init__(spec, static, pause, autofmt)

    def _parse_spec(self, spec):
        spec = spec.title()
        spec = spec.replace(" ", "")
        spec = spec[:1].lower() + spec[1:]
        return super(Identifier, self)._parse_spec(spec)