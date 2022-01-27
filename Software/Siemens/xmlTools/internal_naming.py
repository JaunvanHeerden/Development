import re


CHECK = re.compile(r'(?P<project>\d{4})(?:.(?P<subproject>\d+))?[-_](?P<discipline>[A-Z]{1,2})[-_](?P<type>[A-Z]{1,'
                   r'4})[-_](?P<unique>\d{3})(?:[-_](?P<sheet>\d{2}))?[-_](?P<revision>\w{1,2})')


examples = """•	1008-E-DR-005-01_A	Electrical Drawing 5, sheet 1, Rev A for the project 1008
•	1008-E-DR-005-02_A	Electrical Drawing 5, sheet 2, Rev A for the project 1008
•	2219.0001-B-CLM-001_0	Project claim sheet 1 for project 2291.0001"""


for element in CHECK.finditer(examples):

    print(element.group())
    for group, value in element.re.groupindex.items():
        print(f'{group}\t{value}')
