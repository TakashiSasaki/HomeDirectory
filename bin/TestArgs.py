#!/usr/bin/python3
import unittest,Args

class TestArgs(unittest.TestCase):
  def test(self):
    Args.setTemplate({"a":[]})
    Args.readArgv(["Args.py", "-a", "b", "c", "-d"])
    args = Args.getArgs()
    self.assertEqual({"a":["b"]}, args)
    ov = Args.getOrphanedValues()
    self.assertEqual(["c"], ov)
    ok = Args.getOrphanedKeys()
    self.assertEqual(["d"], ok)

if __name__ == "__main__":
  unittest.main()

   
    
