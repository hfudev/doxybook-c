import argparse
import os

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
    parser.add_argument('-i', '--input', type=str, help='Path to doxygen generated xml folder', required=True)
    parser.add_argument('-o', '--output', type=str, help='Path to the destination folder', required=True)
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

    args = parser.parse_args()

    if args.target == 'gitbook' and args.summary and not os.path.exists(args.summary):
        raise Exception('The provided summary file does not exist!')

    if os.path.isfile(args.output):
        raise Exception('The target output directory is a file!')

    return args


def main():
    args = parse_options()
    os.makedirs(args.output, exist_ok=True)

    run(
        input=args.input,
        output=args.output,
        target=args.target,
        hints=args.hints,
        debug=args.debug,
        ignore_errors=args.ignoreerrors,
        summary=args.summary,
        link_prefix=args.link_prefix,
    )


if __name__ == '__main__':
    main()
