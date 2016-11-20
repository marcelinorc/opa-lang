__author__ = 'marodrig'

from dragonfly import (MappingRule, Text)


class JavaKeyWordsRule(MappingRule):
    """
    Rule class to express the reserved keywords of Java
    """

    keyMap = {
        "abstract": Text("abstract"),
        "assert": Text("assert"),
        "boolean": Text("boolean"),
        "break": Text("break"),
        "byte": Text("byte"),
        "case": Text("case"),
        "catch": Text("catch"),
        "char": Text("char"),
        "class": Text("class"),
        "const": Text("const"),
        "continue": Text("continue"),
        "default": Text("default"),
        "do": Text("do"),
        "double": Text("double"),
        "else": Text("else"),
        "enum": Text("enum"),
        "extends": Text("extends"),
        "final": Text("final"),
        "finally": Text("finally"),
        "float": Text("float"),
        "for": Text("for"),
        "goto": Text("goto"),
        "if": Text("if"),
        "implements": Text("implements"),
        "import": Text("import"),
        "instanceof": Text("instanceof"),
        "int": Text("int"),
        "interface": Text("interface"),
        "long": Text("long"),
        "native": Text("native"),
        "new": Text("new"),
        "package": Text("package"),
        "private": Text("private"),
        "protected": Text("protected"),
        "public": Text("public"),
        "return": Text("return"),
        "short": Text("short"),
        "static": Text("static"),
        "strictfp": Text("strictfp"),
        "super": Text("super"),
        "switch": Text("switch"),
        "synchronized": Text("synchronized"),
        "this": Text("this"),
        "throw": Text("throw"),
        "throws": Text("throws"),
        "transient": Text("transient"),
        "try": Text("try"),
        "void": Text("void"),
        "volatile": Text("volatile"),
        "while": Text("while"),
    }

    def __init__(self, extras=None, defaults=None, exported=None, context=None):
        super(JavaKeyWordsRule, self).__init__("Java keywords", self.keyMap, extras, defaults, exported, context)
