import argparse
import os
from shutil import copytree

from doxybook.constants import DEFAULT_TEMPLATES_DIR, SUPPORTED_LANGS
from doxybook.runner import run


def parse_options():
    parser = argparse.ArgumentParser(description='Convert doxygen XML output into GitBook or Vuepress markdown output.')
    parser.add_argument(
        '-t',
        '--target',
        choices=['gitbook', 'vuepress', 'docsify', 'mkdocs', 'single-markdown'],
        help='markdown type',
        default='single-markdown',
    )
    parser.add_argument('-i', '--input', help='Path to doxygen generated xml folder')
    parser.add_argument('-o', '--output', help='Path to the destination folder')
    parser.add_argument(
        '-s',
        '--summary',
        type=str,
        help='Path to the summary file which contains a link to index.md in the folder pointed by --input (default: false)',
    )
    parser.add_argument(
        '-l',
        '--link-prefix',
        type=str,
        help='Adds a prefix to all links. You can use this to specify an absolute path if necessary. Docsify might need this. (default: "")',
        default='',
    )
    parser.add_argument(
        '-d', '--debug', type=bool, help='Debug the class hierarchy (default: false)', required=False, default=False
    )
    parser.add_argument(
        '--hints',
        type=bool,
        help='(Vuepress only) If set to true, hints will be generated for the sections note, bug, and a warning (default: true)',
        default=True,
    )
    parser.add_argument(
        '--ignoreerrors',
        type=bool,
        help='If set to true, will continue to generate Markdown files even if an error has been detected (default: false)',
        default=False,
    )
    parser.add_argument(
        '--template-dir',
        help='Would use this template dir instead of the default one if set. '
        'Suggest use "doxygen generate-templates" at first to generate the defaults template dir, '
        'and then make your own changes on it.',
    )
    parser.add_argument(
        '--template-lang',
        choices=SUPPORTED_LANGS,
        default='c',
        help='specifies your project\'s main language.',
    )
    action = parser.add_subparsers(dest='action')
    generate_templates = action.add_parser('generate-templates')
    generate_templates.add_argument(
        'output_dir', nargs='?', default=os.getcwd(), help=f'generate default template files. (Default: {os.getcwd()})'
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_options()
    if args.action:
        if os.path.isfile(args.output_dir):
            raise Exception('The [OUTPUT_DIR] should be a directory')

        output_dir = os.path.join(args.output_dir, 'templates')
        if os.path.exists(output_dir):
            raise ValueError(f'{output_dir} folder already exists')

        copytree(DEFAULT_TEMPLATES_DIR, output_dir)
        print(f'Copied the default template files to {output_dir}')
        return

    if args.input is None or args.output is None:
        raise ValueError('-i/--input and -o/--output are required')

    if args.target == 'gitbook' and args.summary and not os.path.exists(args.summary):
        raise Exception('The provided summary file does not exist!')

    os.makedirs(args.output, exist_ok=True)
    run(
        input_dir=args.input,
        output=args.output,
        target=args.target,
        hints=args.hints,
        debug=args.debug,
        ignore_errors=args.ignoreerrors,
        summary=args.summary,
        link_prefix=args.link_prefix,
        template_dir=args.template_dir,
        template_lang=args.template_lang,
    )


if __name__ == '__main__':
    main()
