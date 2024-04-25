import os
import re
# added hashtags to lines 395-405 of numpydoc/docscrape.py
# to remove value error caused by

from pathlib import Path
from pydoc_markdown.interfaces import Context
# file python.py changed: line 76, to ignore_when_discovered added "docs"
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.contrib.renderers.markdown import MarkdownRenderer
from pydoc_markdown.contrib.processors.numpy import NumpyProcessor


directory = ''
for i in os.path.abspath(os.curdir).split('/')[:-3]:
    directory += '/' + i
directory = directory[1:]
print(directory)

context = Context(directory=directory)
loader = PythonLoader(search_path=['Algorithms'])
renderer = MarkdownRenderer(render_module_header=False)

loader.init(context)
renderer.init(context)

modules = loader.load()
string = renderer.render_to_string(modules)

assert 'two_dim_array_count_sort' in string


def format_section_title(title):
    """Formats section titles to Markdown headers."""
    return f'## {title}\n'


def format_items(section):
    """Format items within sections to list or table format if applicable."""
    items_pattern = re.compile(r'^(\s*\w+[\s\w]*?)\s*:\s*(.*)$', re.MULTILINE)
    def replace(match):
        item = match.group(1).strip()
        description = match.group(2).strip()
        return f'- **{item}**: {description}\n'
    return items_pattern.sub(replace, section)


def process_docstring(docstring):
    """Convert docstring sections to Markdown format."""
    # Define sections to convert to markdown headers
    sections = ["Parameters", "Returns", "Attributes", "Methods",
                "Raises", "Examples", "Notes", "See Also"]
    for section in sections:
        pattern = re.compile(rf'(?m)^\s*({section})\s*$\n(?:-+\s*$)?', re.MULTILINE)
        docstring = pattern.sub(lambda match: format_section_title(
            match.group(1)), docstring)
        # Format section content
        docstring = re.sub(rf'(?m)(## {section}\n)(.*?)^\s*##',
                           lambda match: match.group(1) +
                           format_items(match.group(2)), docstring,
                           flags=re.DOTALL)

    # Ensure we capture the end of the document for the last section
    if '##' in docstring:
        split_docs = re.split(r'(## .+?\n)', docstring)
        new_doc = []
        capture = False
        for part in split_docs:
            if capture:
                part = format_items(part)
            if part.startswith('##'):
                capture = True
            new_doc.append(part)
            capture = True if part.startswith('##') else False
        docstring = ''.join(new_doc)
    else:
        docstring = format_items(docstring)

    return docstring


def render_markdown(file_content):
    """Converts entire file of plain docstrings to Markdown format."""
    # Assuming docstrings are separated by a consistent pattern or
    # are in a continuous block
    docstrings = re.split(r'\n{2,}', file_content)
    # Adjust based on your file's structure
    markdown_output = [process_docstring(doc) for doc in docstrings if doc.strip()]
    return '\n\n'.join(markdown_output)

string = render_markdown(string)

with open('docs.md', 'w') as f:
    f.write(string)

module_pattern = re.compile(r'(?P<name>^[A-Za-z0-9_ ]+)\n=+\n(?P<description>(?:.|\n)+?)(?=\n[A-Za-z0-9_ ]+\n=+|\Z)', re.MULTILINE)
modules = module_pattern.finditer(string)
output_dir = Path(directory + '/Algorithms/python_solutions/docs')
output_dir.mkdir(exist_ok=True)
for module in modules:
    module_name = module.group('name').strip().replace(' ', '_').lower()
    module_description = module.group('description').strip()
    filename = module_name.lower().replace(' ', '_')
    output_file_path = output_dir / f'{filename}.md'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(f'# {module_name}\n\n{module_description}')
