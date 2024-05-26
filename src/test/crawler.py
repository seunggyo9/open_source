import unittest
from mycrawler import fetch_page, parse_titles

class TestCrawler(unittest.TestCase):
    
    def test_fetch_page(self):
        html = fetch_page('')
        self.assertIsNotNone(html)
    
    def test_parse_titles(self):
        html = "<html><body><h1>Title 1</h1><h1>Title 2</h1></body></html>"
        titles = parse_titles(html)
        self.assertEqual(titles, ['Title 1', 'Title 2'])

if __name__ == '__main__':
    unittest.main()
