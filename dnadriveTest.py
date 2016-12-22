import unittest
from dnadrive import dnadrive
import hashlib

class dnadriveTestCase(unittest.TestCase):

#  Test cases for encode_string
   
   def test_emptyString(self):
      self.assertRaises(dnadrive.StringEmptyException,dnadrive.encode_string,"")

   def test_intInString(self):
      self.assertRaises(dnadrive.NotStringException,dnadrive.encode_string,1)

   def test_variableInString(self):
      a='abc'
      self.assertIsNotNone(dnadrive.encode_string(a))

   def test_encodeDecode(self):
      inp = "hello_world"
      gene = dnadrive.encode_string(inp)
      outp = dnadrive.decode_string(gene)
      self.assertEqual(inp,outp)

   def test_encodeDecodeFile(self):
      inp = "input.test"
      outp = "output.test"
      check = "check.test"
      well = "check.well"
      gene = dnadrive.encode_file(inp,outp)
      outf = dnadrive.decode_file(outp,check)
      outp = dnadrive.generate_well_file(outp,well)
      # self.assertEqual(outp,[33, 1, 17, 1, 17, 1, 17, 1, 17, 7, 24, 7, 27, 7, 20, 7, 20, 34, 38, 1, 17, 1, 17, 1, 17, 1, 18, 7, 17, 3, 32, 8, 25, 7, 17, 34, 38, 1, 17, 1, 17, 1, 17, 1, 19, 8, 30, 7, 20, 7, 28, 1, 22, 34, 38, 34, 38, 35, 36])

   def test_encodeDecodeFileVairants(self):
      inp = "input.test"
      outp = "output"
      check = "check"
      gene = dnadrive.encode_file(inp,outp+"1.test",1)
      gene = dnadrive.encode_file(inp,outp+"2.test",2)
      gene = dnadrive.encode_file(inp,outp+"3.test",3)
      gene = dnadrive.encode_file(inp,outp+"4.test",4)

      outf = dnadrive.decode_file(outp+"1.test",check+"1.test")
      outf = dnadrive.decode_file(outp+"2.test",check+"2.test")
      outf = dnadrive.decode_file(outp+"3.test",check+"3.test")
      outf = dnadrive.decode_file(outp+"4.test",check+"4.test")

      with open(inp,'rb') as w:
         orig_hash = hashlib.md5(w.read()).hexdigest()
         with open(check+"1.test",'rb') as c1:
            hash_1 = hashlib.md5(c1.read()).hexdigest()
            self.assertEqual(orig_hash,hash_1)
         with open(check+"2.test",'rb') as c2:
            hash_2 = hashlib.md5(c2.read()).hexdigest()
            self.assertEqual(orig_hash,hash_2)
         with open(check+"3.test",'rb') as c3:
            hash_3 = hashlib.md5(c3.read()).hexdigest()
            self.assertEqual(orig_hash,hash_3)
         with open(check+"4.test",'rb') as c4:
            hash_4 = hashlib.md5(c4.read()).hexdigest()
            self.assertEqual(orig_hash,hash_4)


   # def test_encodedecodefile2(self):
   #    inp = "10000290816.png"
   #    outp = "output2.test"
   #    check = "check2.test"
   #    gene = dnadrive.encode_file(inp,outp)
   #    outp = dnadrive.decode_file(outp,check)
   #    # self.assertEqual(inp,outp)

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