from collections import OrderedDict


def is_leaf(identifier: str) -> bool:
    # Iterates over all categories. If the provided category identifier is referenced at least once as a parent,
    # it is not a leaf category.
    for k, v in _get_categories().items():
        try:
            parent = v['parent']
        except KeyError:
            continue
        else:
            if parent == identifier:
                return False

    return True


def list_leaves() -> list:
    categories = _get_categories()

    leaves = []

    for k, v in categories.items():
        # Let's just have is_leaf do all the hard work.
        if is_leaf(k):
            leaves.append("{} ({})".format(v['name'], k))

    # Since we're using an ordered dictionary and the categories.txt file is already sorted by ascending id,
    # there's no need to explicitly sort the data structure at this point.

    return leaves


def match(query: str) -> list:
    categories = _get_categories()

    results = []

    for k, v in categories.items():
        # Converts both query and category name to lowercase, implementing case insensitive matching.
        if query.lower() in v['name'].lower():
            results.append("{} ({})".format(v['name'], k))

    return results


def _get_categories():
    # TODO Cache the result.
    return _parse_file('categories.txt')


def _parse_file(filename: str) -> dict:
    categories = OrderedDict()

    with open(filename, 'r') as file:
        for line in file:
            stripped = line.lstrip()

            # Ignore comments
            if stripped.startswith('#'):
                continue

            identifier, attribute = _parse_line(stripped)
            attributes = categories.get(identifier, {})

            # Merges attributes dictionary with the last parsed attribute.
            categories[identifier] = {**attributes, **attribute}

    return categories


def _parse_line(line: str) -> (str, dict):
    path, value = line.split('=')
    _, identifier, attribute = path.split('.')
    return identifier, {attribute: value.rstrip()}


if __name__ == '__main__':
    print('1.')
    print("is_leaf('6140') ->", is_leaf('6140'))
    print("is_leaf('6000') ->", is_leaf('6000'))
    print()
    print('2.')
    print(list_leaves())
    print()
    print('3.')
    print("match('des') ->", match('des'))
    print("match('ár') ->", match('ár'))
    print()
