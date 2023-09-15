import os
from enum import (
    Enum,
)

OVERLOAD_OPERATORS = [
    'operator=',
    'operator+',
    'operator-',
    'operator*',
    'operator/',
    'operator+=',
    'operator-=',
    'operator*=',
    'operator/=',
    'operator==',
    'operator%',
    'operator%=',
    'operator++',
    'operator--',
    'operator==',
    'operator!=',
    'operator<=',
    'operator>=',
    'operator>',
    'operator<',
    'operator!',
    'operator&&',
    'operator||',
    'operator~',
    'operator&',
    'operator|',
    'operator^',
    'operator<<',
    'operator>>',
    'operator~=',
    'operator&=',
    'operator|=',
    'operator^=',
    'operator<<=',
    'operator>>=',
    'operator[]',
    'operator*',
    'operator&',
    'operator->',
    'operator->*',
]

PACKAGE_DIR = os.path.dirname(__file__)
DEFAULT_TEMPLATES_DIR = os.path.join(PACKAGE_DIR, 'templates')


class Kind(Enum):
    NONE = 'none'
    ROOT = 'root'
    NAMESPACE = 'namespace'
    CLASS = 'class'
    STRUCT = 'struct'
    UNION = 'union'
    FUNCTION = 'function'
    VARIABLE = 'variable'
    DEFINE = 'define'
    TYPEDEF = 'typedef'
    ENUM = 'enum'
    ENUMVALUE = 'enumvalue'
    FRIEND = 'friend'
    FILE = 'file'
    DIR = 'dir'
    PAGE = 'page'
    EXAMPLE = 'example'
    GROUP = 'group'
    INTERFACE = 'interface'

    def is_function(self) -> bool:
        return self == Kind.FUNCTION

    def is_variable(self) -> bool:
        return self == Kind.VARIABLE

    def is_namespace(self) -> bool:
        return self == Kind.NAMESPACE

    def is_class(self) -> bool:
        return self == Kind.CLASS

    def is_struct(self) -> bool:
        return self == Kind.STRUCT

    def is_enum(self) -> bool:
        return self == Kind.ENUM

    def is_interface(self) -> bool:
        return self == Kind.INTERFACE

    def is_class_or_struct(self) -> bool:
        return self in (Kind.CLASS, Kind.STRUCT, Kind.INTERFACE)

    def is_typedef(self) -> bool:
        return self == Kind.TYPEDEF

    def is_define(self) -> bool:
        return self == Kind.DEFINE

    def is_union(self) -> bool:
        return self == Kind.UNION

    def is_group(self) -> bool:
        return self == Kind.GROUP

    def is_root(self) -> bool:
        return self == Kind.ROOT

    def is_friend(self) -> bool:
        return self == Kind.FRIEND

    def is_file(self) -> bool:
        return self == Kind.FILE

    def is_dir(self) -> bool:
        return self == Kind.DIR

    def is_page(self) -> bool:
        return self == Kind.PAGE

    def is_language(self) -> bool:
        LANGUAGE = [
            Kind.FUNCTION,
            Kind.VARIABLE,
            Kind.NAMESPACE,
            Kind.DEFINE,
            Kind.CLASS,
            Kind.STRUCT,
            Kind.TYPEDEF,
            Kind.ENUM,
            Kind.ENUMVALUE,
            Kind.UNION,
            Kind.INTERFACE,
            Kind.FRIEND,
        ]

        if self in LANGUAGE:
            return True
        return False

    def is_parent(self) -> bool:
        return self in (
            Kind.NAMESPACE,
            Kind.CLASS,
            Kind.STRUCT,
            Kind.UNION,
            Kind.INTERFACE,
        )

    def is_member(self) -> bool:
        return self.is_language() and not self.is_parent()

    @staticmethod
    def from_str(s: str) -> 'Kind':
        try:
            return Kind(s)
        except Exception:
            return Kind.NONE


class Visibility(Enum):
    PUBLIC = 'public'
    PROTECTED = 'protected'
    PRIVATE = 'private'


SUPPORTED_LANGS = ['c', 'cpp']
