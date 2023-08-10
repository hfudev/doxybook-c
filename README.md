# esp-doxybook

This is a tool that converts Doxygen XML output into a single-file API reference in MarkDown format.

## Live Demo

- C Project: https://espressif.github.io/doxybook/c_api/
- C++ Project: https://espressif.github.io/doxybook/cpp_api/

## Requirements

You need to have **python 3.7 or newer** and [Jinja2](http://jinja.pocoo.org/docs/2.10/intro/) package installed.

## Memory usage

Needs up to 100MiB of memory. Parsing super large projects can use up to 0.5GiB of memory. For example, a project consisting of 1000 Doxygen xml files can use 550MiB of memory, but I would be worried more about VuePress or GitBook memory usage while using that many files.

## Installation

**Install using Python Pip: <https://pypi.org/project/esp-doxybook/>**

## Compile the example

```bash
git clone https://github.com/espressif/doxybook.git

cd doxybook

# Install dependencies
python -m venv venv
source venv/bin/activate
pip install flit
flit install -s

# Let's take C project as an example
cd example/c
esp-doxybook -i temp/xml -o ../../docs/c_api.md

# Preview Markdown with MkDocs
cd ../../
mkdocs serve
```

Then go to `http://localhost:8000/c_api/` to see the generated documentation.

## Found a bug or want to request a feature?

[Feel free to do it on GitHub issues](https://github.com/espressif/doxybook/issues)

## Pull requests

[Pull requests are welcome](https://github.com/espressif/doxybook/pulls)

## License

```
MIT License

Copyright (c) 2019 Matus Novak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Additions Copyright (c) 2022 Espressif Systems (Shanghai) Co. Ltd.
```
