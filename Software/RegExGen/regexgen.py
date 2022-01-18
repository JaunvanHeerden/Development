import re
import random
import string

"""
n - number
x - alphabet
(v) - capture version
"""


def to_regex_string(raw: str):
    build = raw.lower()

    results_d = re.findall('n+', raw)
    groups_d = sorted(list(set(results_d)), reverse=True)

    for group in groups_d:
        build = build.replace(group, '\d' + '{' + str(len(group)) + '}')

    results_a = re.findall('x+', raw)
    groups_a = sorted(list(set(results_a)), reverse=True)

    for group in groups_a:
        build = build.replace(group, '[a-zA-Z]' + '{' + str(len(group)) + '}')

    results_v = re.findall('v+', raw)
    groups_v = sorted(list(set(results_v)), reverse=True)

    for group in groups_v:
        build = build.replace(group, '[a-zA-Z]' + '{' + str(len(group)) + '}')

    return build


def test_random(num_tests):

    for random_test in range(num_tests):
        build = ''
        for i in range(random.randint(2, 5)):
            build += random.choice(['x', 'n']) * random.randint(1, 4) + random.choice(['-', '_', ' '])

        random_drop = random.randint(0, len(build))

        build = build[random_drop:] + \
                random.choice(['-(v)-', '-(vv)', '_(vv)', '-(v)_', '_(v)_']) + \
                build[:random_drop]

        pattern = to_regex_string(build)

        print('\n'*2)
        print('-'*50)
        print(f'Test #{str(random_test+1).zfill(len(str(num_tests)))}')
        print()
        print(f'Random Generation: {build}')
        print(f'Converted Pattern: {pattern}')

        for i in range(20):

            example = generate_example(build)

            result = re.match(pattern, example)

            if result.groups():

                print('\t' + example + '\t' + result.groups()[-1])

            else:

                print('\t' + example + '\t' + 'failed')





def generate_example(pattern):

    example = list(pattern)

    for index, value in enumerate(example):

        if value in ['x', 'v']:

            letter = random.choice(string.ascii_letters)

            example[index] = random.choice([letter.upper(), letter])

        if value == 'n':

            example[index] = str(random.randint(0, 9))

    example = ''.join(example).replace('(', '').replace(')', '')

    return example


def main():
    # to_regex_string('xxx_n-n-xnxx-(V)-xx-nx')

    test_random(100)


if __name__ == '__main__':
    main()
