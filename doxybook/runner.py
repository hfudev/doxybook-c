import os
import time

from jinja2 import select_autoescape, Environment, PackageLoader

from doxybook.cache import Cache
from doxybook.constants import Kind, PACKAGE_DIR
from doxybook.doxygen import Doxygen
from doxybook.generator import Generator
from doxybook.utils import get_git_revision_hash
from doxybook.xml_parser import XmlParser

import typing as t


def run(
    output: str,
    input: str,
    target: str = 'gitbook',
    hints: bool = True,
    debug: bool = False,
    ignore_errors: bool = False,
    summary: str = None,
    link_prefix: str = '',
    template_dir: t.Optional[str] = None,
    template_lang: t.Optional[str] = 'c',
):
    os.makedirs(output, exist_ok=True)

    options = {'target': target, 'link_prefix': link_prefix}

    cache = Cache()
    parser = XmlParser(cache=cache, target=target, hints=hints)
    doxygen = Doxygen(input, parser, cache, options=options)

    if debug:
        doxygen.print()

    generator = Generator(ignore_errors=ignore_errors, options=options)

    if target == 'single-markdown':
        template_dir = template_dir or PACKAGE_DIR
        template_lang = template_lang or 'c'

        env = Environment(loader=PackageLoader(template_dir), autoescape=select_autoescape())
        with open(os.path.join(output, 'api.md'), 'w') as fw:
            template = env.get_template(f'{template_lang}/api.jinja')
            files = doxygen.header_files.children
            fw.write(
                template.render(
                    files=files,
                    file_template=env.get_template(f'{template_lang}/file.jinja'),
                    table_template=env.get_template(f'{template_lang}/table.jinja'),
                    detail_template=env.get_template(f'{template_lang}/detail.jinja'),
                    commit_sha=get_git_revision_hash(),
                    asctime=time.asctime(),
                )
            )
        return

    generator.annotated(output, doxygen.root.children)
    generator.fileindex(output, doxygen.files.children)
    generator.members(output, doxygen.root.children)
    generator.members(output, doxygen.groups.children)
    generator.files(output, doxygen.files.children)
    generator.namespaces(output, doxygen.root.children)
    generator.classes(output, doxygen.root.children)
    generator.hierarchy(output, doxygen.root.children)
    generator.modules(output, doxygen.groups.children)
    generator.pages(output, doxygen.pages.children)
    generator.relatedpages(output, doxygen.pages.children)
    generator.index(
        output,
        doxygen.root.children,
        [Kind.FUNCTION, Kind.VARIABLE, Kind.TYPEDEF, Kind.ENUM],
        [Kind.CLASS, Kind.STRUCT, Kind.INTERFACE],
        'Class Members',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.FUNCTION],
        [Kind.CLASS, Kind.STRUCT, Kind.INTERFACE],
        'Class Member Functions',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.VARIABLE],
        [Kind.CLASS, Kind.STRUCT, Kind.INTERFACE],
        'Class Member Variables',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.TYPEDEF],
        [Kind.CLASS, Kind.STRUCT, Kind.INTERFACE],
        'Class Member Typedefs',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.ENUM],
        [Kind.CLASS, Kind.STRUCT, Kind.INTERFACE],
        'Class Member Enums',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.FUNCTION, Kind.VARIABLE, Kind.TYPEDEF, Kind.ENUM],
        [Kind.NAMESPACE],
        'Namespace Members',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.FUNCTION],
        [Kind.NAMESPACE],
        'Namespace Member Functions',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.VARIABLE],
        [Kind.NAMESPACE],
        'Namespace Member Variables',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.TYPEDEF],
        [Kind.NAMESPACE],
        'Namespace Member Typedefs',
    )
    generator.index(
        output,
        doxygen.root.children,
        [Kind.ENUM],
        [Kind.NAMESPACE],
        'Namespace Member Enums',
    )
    generator.index(output, doxygen.files.children, [Kind.FUNCTION], [Kind.FILE], 'Functions')
    generator.index(output, doxygen.files.children, [Kind.DEFINE], [Kind.FILE], 'Macros')
    generator.index(
        output,
        doxygen.files.children,
        [Kind.VARIABLE, Kind.UNION, Kind.TYPEDEF, Kind.ENUM],
        [Kind.FILE],
        'Variables',
    )

    if target == 'gitbook' and summary:
        generator.summary(
            output,
            summary,
            doxygen.root.children,
            doxygen.groups.children,
            doxygen.files.children,
            doxygen.pages.children,
        )
