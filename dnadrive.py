import os
import binascii

###############################################
# Inputs: Argument should be a string
#
# Returns string of encoded DNA sequence
###############################################

def encode_string(s):
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
         print "Error: String is empty"
         return
      dnaEnc='GGGGGG'
      for i in s:
         hexbyt=int(binascii.hexlify(i),16)
         ind = divmod(hexbyt,16)
         dnaEnc = dnaEnc + GCarr[ind[0]]+GCarr[ind[1]]
      print dnaEnc
      return dnaEnc
   else:
      print "Error: Incorrect argument. argument should be 'str'"
      return


###############################################
# Input: Arguments should be a input and
#        output file
#
# Output: Writes encoded DNA sequence in 
#         output file
###############################################

def encode_file(inp,out):
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
         with open(inp,'rb') as f:
#            print "file opened"
            dnaEnc="GGGGGG"
            for line in f:
#              print line
               for byt in line:
                  if byt == '':
                     print "Error: file is empty"
                     return 
                  hexbyt = int(binascii.hexlify(byt),16)
                  ind = divmod(hexbyt,16)
                  dnaEnc = dnaEnc + GCarr[ind[0]] + GCarr[ind[1]]
#         print dnaEnc
         with open(out,'w') as w:
            w.write(dnaEnc)
      else: 
         print "Error: Input file doesnot exist"
   else: 
      print "Error: Arguments should be string."
      return


###############################################
# Input: Argument as string to be decoded
#
# Returns string of decoded DNA sequence
###############################################               
def decode_string(dna):
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
              print "Error: DNA sequence not in required format (1)"
#              return
         else: 
           print "Error: DNA sequence not in required format (2)"
#           return
      return binascii.unhexlify(dnaDec)
   else: print "Error: Arguments should be string"



###############################################
# Inputs: 1st argument as input file with DNA 
#         sequence to be decoded.
#         2nd argument as output file where
#         decoded DNA seq will be written
#
# Output: output file with decoded DNA seq
###############################################               
def decode_file(inp,out):
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
                  if AT in hexAT.keys() :
                     dnaDec=dnaDec+hexAT[AT]
                  elif AT == '\n' :
                    continue
                  else: 
                     print "Error: DNA sequence not in required format (3)",AT
                     return
               else: 
                 print "Error: DNA sequence not in required format (4)"
                 return
            with open(out,'w') as w:
               w.write(binascii.unhexlify(dnaDec))
      else:
         print "Error: File doesnot exist"
         return
   else:
      print "Error invalid arguments"
      return