# test_vypercode.py
"""
Tests for VyperCode module.
"""

import unittest
from vypercode import VyperCode

class TestVyperCode(unittest.TestCase):
    """Test cases for VyperCode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VyperCode()
        self.assertIsInstance(instance, VyperCode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VyperCode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
