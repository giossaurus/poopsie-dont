import unittest
from main import load_config

class TestDetection(unittest.TestCase):
    def test_config_loading(self):
        config = load_config()
        self.assertIn('confidence_threshold', config)

if __name__ == '__main__':
    unittest.main()