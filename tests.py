import json
import os
import unittest

from main import find_companies


class Queries(unittest.TestCase):
    def test_single_query(self):
        result = find_companies("Apple")
        json_object = json.dumps(result, ensure_ascii=True, indent=3)
        print(json_object)

    def test_loop_query(self):
        companies = ['Apple', 'Microsoft Research', 'NonExistingCompany']
        results = []
        for company in companies:
            results.append(find_companies(company))
        with open(f'{os.getcwd()}/companies.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=True, indent=3)
        print(f'\nFind the results in \"{os.getcwd()}/companies.json\"')


if __name__ == '__main__':
    unittest.main()
