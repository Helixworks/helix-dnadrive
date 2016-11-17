import os
import binascii

class StringEmptyException(Exception):
    pass

class NotStringException(Exception):
    pass

def encode_string(s):
   """ Inputs: Argument should be a string
       Returns string of encoded DNA sequence
   """
   GCarr=['AAAAGGGGGG',
   'AAATGGGGGG',
   'AATAGGGGGG',
   'AATTGGGGGG',
   'ATAAGGGGGG',
   'ATATGGGGGG',
   'ATTAGGGGGG',
   'ATTTGGGGGG',
   'TAAAGGGGGG',
   'TAATGGGGGG',
   'TATAGGGGGG',
   'TATTGGGGGG',
   'TTAAGGGGGG',
   'TTATGGGGGG',
   'TTTAGGGGGG',
   'TTTTGGGGGG']
   if type(s)==str :
      if s=='':
         raise StringEmptyException
      dnaEnc='GGGGGG'
      for i in s:
         hexbyt=int(binascii.hexlify(i),16)
         ind = divmod(hexbyt,16)
         dnaEnc = dnaEnc + GCarr[ind[0]]+GCarr[ind[1]]
      # print dnaEnc
      return dnaEnc
   else:
      raise NotStringException

def encode_file(inp,out):
   """ Input: Arguments should be a input and output file
       Output: Writes encoded DNA sequence in output file
   """
   GCarr=['AAAAGGGGGG',
   'AAATGGGGGG',
   'AATAGGGGGG',
   'AATTGGGGGG',
   'ATAAGGGGGG',
   'ATATGGGGGG',
   'ATTAGGGGGG',
   'ATTTGGGGGG',
   'TAAAGGGGGG',
   'TAATGGGGGG',
   'TATAGGGGGG',
   'TATTGGGGGG',
   'TTAAGGGGGG',
   'TTATGGGGGG',
   'TTTAGGGGGG',
   'TTTTGGGGGG']
   if (type(inp)==str)and(type(out)==str):
      if os.path.isfile(inp):
#         print "file is going to open"
         with open(inp,'rb') as f, open(out,'w') as w:
#            print "file opened"
            dnaEnc="GGGGGG"
            for line in f:
#               print line
               for byt in line:
                  if byt == '':
                     raise Exception("Error: String is empty")
                      
                  hexbyt = int(binascii.hexlify(byt),16)
                  ind = divmod(hexbyt,16)
                  dnaEnc = dnaEnc + GCarr[ind[0]] + GCarr[ind[1]]
                  w.write(dnaEnc)
                  dnaEnc=""
#         print dnaEnc
#         with open(out,'w') as w:
#            w.write(dnaEnc)
      else: 
         raise Exception("Error: Input file doesnot exist") 
   else: 
      raise Exception("Error: Arguments should be string.") 
            
def decode_string(dna):
   """
      Input: Argument as string to be decoded
      Returns string of decoded DNA sequence
   """
   hexAT={'AAAA':'0',
      'AAAT':'1',
      'AATA':'2',
      'AATT':'3',
      'ATAA':'4',
      'ATAT':'5',
      'ATTA':'6',
      'ATTT':'7',
      'TAAA':'8',
      'TAAT':'9',
      'TATA':'a',
      'TATT':'b',
      'TTAA':'c',
      'TTAT':'d',
      'TTTA':'e',
      'TTTT':'f'}
   if type(dna)==str:
      dnaDec=""
      for i in xrange(0,len(dna),10):
         Gs,AT=dna[i:i+6],dna[i+6:i+10]
         if (Gs == "GGGGGG"):
            if AT in hexAT.keys() :
              dnaDec=dnaDec+hexAT[AT]
            elif AT == '':
              continue
            else: 
              raise Exception("Error: DNA sequence not in required format (1)")
         else: 
           raise Exception("Error: DNA sequence not in required format (2)")
      # print dnaDec
      return binascii.unhexlify(dnaDec)
   else:
      raise Exception("Error: Arguments should be string")
            
def decode_file(inp,out):
   """
   Inputs: 1st argument as input file with DNA sequence to be decoded.
             2nd argument as output file where decoded DNA seq will be written
   Output: output file with decoded DNA seq
   """
   hexAT={'AAAA':'0',
      'AAAT':'1',
      'AATA':'2',
      'AATT':'3',
      'ATAA':'4',
      'ATAT':'5',
      'ATTA':'6',
      'ATTT':'7',
      'TAAA':'8',
      'TAAT':'9',
      'TATA':'a',
      'TATT':'b',
      'TTAA':'c',
      'TTAT':'d',
      'TTTA':'e',
      'TTTT':'f'}
   if (type(inp)==str)and(type(out)==str):
      if os.path.isfile(inp):
         with open(inp,'r') as f:
            dnaSeq=f.read()
            dnaDec=""
            for i in xrange(0,len(dnaSeq),10):
               Gs,AT=dnaSeq[i:i+6],dnaSeq[i+6:i+10]
               if (Gs == "GGGGGG"):
                  # print AT
                  if AT in hexAT.keys() :
                     dnaDec=dnaDec+hexAT[AT]
                  elif AT == '\n' or AT == '':
                    continue
                  else: 
                     # print AT,int(AT)
                     raise Exception("Error: DNA sequence not in required format (3)")
               else: 
                  raise Exception("Error: DNA sequence not in required format (4)")
            with open(out,'w') as w:
               w.write(binascii.unhexlify(dnaDec))
      else:
         raise Exception("Error: File doesnot exist")
   else:
      raise Exception("Error invalid arguments")
