import os
import time
import typing as t

from jinja2 import (
    Environment,
    FileSystemLoader,
    PackageLoader,
    select_autoescape,
)

from doxybook.cache import (
    Cache,
)
from doxybook.doxygen import (
    Doxygen,
)
from doxybook.utils import (
    get_git_revision_hash,
)
from doxybook.xml_parser import (
    XmlParser,
)


def run(
    output: str,
    input_dir: str,
    target: str = 'single-markdown',
    debug: bool = False,
    link_prefix: str = '',
    template_dir: t.Optional[str] = None,
    template_lang: t.Optional[str] = 'c',
):
    if output.endswith('.md'):
        os.makedirs(os.path.dirname(output), exist_ok=True)
        output_filepath = output
    else:
        os.makedirs(output, exist_ok=True)
        output_filepath = os.path.join(output, 'api.md')

    options = {'target': target, 'link_prefix': link_prefix}

    cache = Cache()
    parser = XmlParser(cache=cache, target=target)
    doxygen = Doxygen(input_dir, parser, cache, options=options)

    if debug:
        doxygen.print()

    if template_dir:
        loader = FileSystemLoader(template_dir)
    else:
        loader = PackageLoader('doxybook')
    template_lang = template_lang or 'c'

    env = Environment(loader=loader, autoescape=select_autoescape())
    with open(output_filepath, 'w') as fw:
        template = env.get_template('api.jinja')
        files = doxygen.header_files.children
        common_args = {
            'files': files,
            'file_template': env.get_template(f'{template_lang}/file.jinja'),
            'table_template': env.get_template('table.jinja'),
            'detail_template': env.get_template('detail.jinja'),
            'commit_sha': get_git_revision_hash(),
            'asctime': time.asctime(),
        }
        fw.write(template.render(**common_args))

    print(f'Generated single-markdown API reference: {output_filepath}')
