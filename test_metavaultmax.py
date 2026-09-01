# test_metavaultmax.py
"""
Tests for MetaVaultMax module.
"""

import unittest
from metavaultmax import MetaVaultMax

class TestMetaVaultMax(unittest.TestCase):
    """Test cases for MetaVaultMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaVaultMax()
        self.assertIsInstance(instance, MetaVaultMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaVaultMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
