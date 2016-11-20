from CamelCase import CamelCase
from Identifier import Identifier

__author__ = 'marodrig'

from dragonfly import (MappingRule, Dictation, Key, Text, IntegerRef)


def get_idea_rules():

    literals = MappingRule(
        name="literals",
        mapping={
            "cos":Text("\"") + Key("space"),
            "num":Text("%(n)d"),
        },
        extras=[
            IntegerRef("n", 1, 1000000),
            Dictation("text"),
        ]
    )

    capitalization = MappingRule(
        name="capitalization",
        mapping={
            "var <identifier>": Identifier("%(identifier)s"),
            "camel <identifier>": CamelCase("%(identifier)s"),
            "speak <identifier>": Text("%(identifier)s"),
        },
        extras=[
            Dictation("identifier"),
        ]
    )

    class_rules = MappingRule(
        name="clas_rules",
        mapping={
            "new": Text("new "),
            "pum [<identifier>]": Text("public void ") + Identifier("%(identifier)s() { \n"),
            "puma [<identifier>]": Text("public abstract void ") + Identifier("%(identifier)s() { \n"),
            "pum static [<identifier>]": Text("public static void ") + Identifier("%(identifier)s() { \n"),
            "pim  [<identifier>]": Text("private void ") + Identifier("%(identifier)s() { \n"),
            "pima [<identifier>]": Text("private abstract void ") + Identifier("%(identifier)s() { \n"),
            "pim static [<identifier>]": Text("private void ") + Identifier("%(identifier)s() { \n"),
            "pom [<identifier>]": Text("protected void ") + Identifier("%(identifier)s() { \n"),
            "poma [<identifier>]": Text("protected abstract void ") + Identifier("%(identifier)s() { \n"),
            "pom static [<identifier>]": Text("protected static void ") + Identifier("%(identifier)s() { \n"),
            "pufu [<class_name>] [var <identifier>]": Text("public ") + CamelCase("%(class_name)s") + Text(" ") +
                                                      Identifier("%(identifier)s() { \n"),
            "pifi [<class_name>] [var <identifier>]": Text("private ") + CamelCase("%(class_name)s") + Text(" ") +
                                                      Identifier("%(identifier)s() { \n"),
            "pofo [<class_name>] [var <identifier>]": Text("protected ") + CamelCase("%(class_name)s") + Text(
                " ") + Identifier("%(identifier)s() { \n"),
            "test [<identifier>]": Key("c-n, enter") + Text("test"),
            "override": Key("c-n") + Key("down:6") + Key("enter"),
            "return": Text("return"),
            "static": Text("static"),
            "abstract" : Text("abstract"),
        },
        extras=[
            Dictation("identifier"),
            Dictation("class_name"),
        ]
    )

    binary_operators = MappingRule(
        name="binary_operators",
        mapping={
            "star": Key("asterisk"),
            "sum | plus": Key("plus"),
            "min": Key("minus"),
            "and": Text("&&"),
            "or": Text("||"),
        },
        extras=[
            Dictation("identifier"),
        ]
    )

    types = MappingRule(
        name="types",
        mapping={
            "flag | bool | boolean": Text("boolean "),
            "long [<identifier>]": Text("long ") + Identifier("%(identifier)s"),
            "int [<identifier>]": Text("int ") + Identifier("%(identifier)s"),
            "double [<identifier>]": Text("double ") + Identifier("%(identifier)s"),
            "float [<identifier>]": Text("float ") + Identifier("%(identifier)s"),
            "string [<identifier>]": Text("String ") + Identifier("%(identifier)s"),
            "Integer [<identifier>]": Text("Integer ") + Identifier("%(identifier)s"),
            "class float [<identifier>]": Text("float ") + Identifier("%(identifier)s"),
            "class double [<identifier>]": Text("double ") + Identifier("%(identifier)s"),
            "list": Text("List<"),
            "collection | col": Text("Collection<"),
            "hash": Text("HashMap<"),
            "set": Text("HashSet<"),
        },
        extras=[
            Dictation("identifier"),
        ]
    )

    editing_chars = MappingRule(
        name="editing_chars",
        mapping={
            "slap": Key("enter"),
            "tab": Key("tab"),
            "pa": Key("space"),
        },
        extras=[
            Dictation("text"),
        ]
    )

    symbols = MappingRule(
        name="symbols",
        mapping={
            "this": Text("this"),
            "shasha": Text("//"),
            "cha": Text("/"),
            "comments [<text>]": Text("/**") + Key("enter") + Text("%(text)s \n"),
            "doh | dot": Key("dot"),
            "del": Key("del"),
            "se | semicolon": Text(";"),
            "koh | colon": Key("colon"),
            "ma": Key("comma"),
            "rak": Text("{"),
            "kar": Text("}"),
            "opa": Text("("),
            "apo": Text(")"),
            "brak": Text("["),
            "krak": Text("]"),
        },
        extras=[
            Dictation("text"),
        ]
    )

    ide_basic_commands = MappingRule(
        name="ide_basic",
        mapping={
            "what | mimi": Key("c-space"),
            "reformat": Key("a-f8") + Key("enter"),
            "make class [<text>]": Key("a-f") + Key("a-insert") + Key("enter") + CamelCase("%(text)s"),
            "rename": Key("s-f6"),
        },
        extras=[
            Dictation("text"),
        ]
    )

    return [binary_operators, types, symbols, ide_basic_commands, editing_chars, capitalization, class_rules, literals]