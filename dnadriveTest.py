import unittest
import dnadrive

class dnadriveTestCase(unittest.TestCase):

#  Test cases for encode_string
   
   def test_emptyString(self):
      self.assertIsNotNone(dnadrive.encode_string(""))

   def test_intInString(self):
      self.assertIsNone(dnadrive.encode_string(1))

   def test_variableInString(self):
      a='abc'
      self.assertIsNotNone(dnadrive.encode_string(a))

#  Test cases for encode_file

#   def test_emptyFile(self):
#      self.assertIs

#  Test cases for decode_string      
   def test_emptyDecode(self):
      self.assertIsNone(dnadrive.decode_string(""))

   def test_validString(self):
      self.assertIsNotNone(dnadrive.decode_string("GGGGGGATATGGGGGG"))

   def test_wrongSequenceType1(self):
      self.assertIsNone(dnadrive.decode_string("GGGGGGATGGATGGGG"))

   def test_wrongSequenceType2(self):
      self.assertIsNone(dnadrive.decode_string("AKJSDFHAKJSDHAKJSDGH"))

if __name__=='__main__':
   unittest.main()