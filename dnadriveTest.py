import unittest
from dnadrive import dnadrive

class dnadriveTestCase(unittest.TestCase):

#  Test cases for encode_string
   
   def test_emptyString(self):
      self.assertRaises(dnadrive.StringEmptyException,dnadrive.encode_string,"")

   def test_intInString(self):
      self.assertRaises(dnadrive.NotStringException,dnadrive.encode_string,1)

   def test_variableInString(self):
      a='abc'
      self.assertIsNotNone(dnadrive.encode_string(a))

   def test_encodedecode(self):
      inp = "hello world"
      gene = dnadrive.encode_string(inp)
      outp = dnadrive.decode_string(gene)
      self.assertEqual(inp,outp)

   def test_encodedecodefile(self):
      inp = "input.test"
      outp = "output.test"
      check = "check.test"
      gene = dnadrive.encode_file(inp,outp)
      outp = dnadrive.decode_file(outp,check)
      # self.assertEqual(inp,outp)

# #  Test cases for encode_file

# #  Test cases for decode_string      
#    def test_emptyDecode(self):
#       self.assertRaises(dnadrive.decode_string(""))

#    def test_validString(self):
#       self.assertIsNotNone(dnadrive.decode_string("GGGGGGATATGGGGGG"))

#    def test_wrongSequenceType1(self):
#       self.assertIsNone(dnadrive.decode_string("GGGGGGATGGATGGGG"))

#    def test_wrongSequenceType2(self):
#       self.assertIsNone(dnadrive.decode_string("AKJSDFHAKJSDHAKJSDGH"))

if __name__=='__main__':
   unittest.main()