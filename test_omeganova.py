# test_omeganova.py
"""
Tests for OmegaNova module.
"""

import unittest
from omeganova import OmegaNova

class TestOmegaNova(unittest.TestCase):
    """Test cases for OmegaNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OmegaNova()
        self.assertIsInstance(instance, OmegaNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OmegaNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
