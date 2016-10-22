import os
import binascii


###############################################
# Inputs 1st argument as string or file name
#        2nd argument as 's' or 'f' to indicate 
#        string or file respectively
#
# Returns string of encoded DNA sequence
###############################################
def encode(sOf,t):
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
   if type(sOf)==str:
      if t == 's':
         dnaEnc='GGGGGG'
         for i in sOf:
            hexbyt=int(binascii.hexlify(i),16)
            ind = divmod(hexbyt,16)
            dnaEnc = dnaEnc + GCarr[ind[0]]+GCarr[ind[1]]
         return dnaEnc
      elif t == 'f':
         if os.path.isfile(sOf):
            with open(sOf,'rb') as f:
               dnaEnc="GGGGGG"
               for line in f:
                  for byt in line:
                     hexbyt = int(binascii.hexlify(byt),16)
                     ind = divmod(hexbyt,16)
                     dnaEnc = dnaEnc + GCarr[ind[0]] + GCarr[ind[1]]
            return dnaEnc
         else: 
            "Error: File doesnot exist"
            return
      else: 
         print "Error: Incorrect second argument.\n It should be \'s\' or \'f\'."
         return
   else: 
      print "Error: First argument should be string."
      return


###############################################
# Inputs 1st argument as string or file name
#        2nd argument as 's' or 'f' to indicate 
#        string or file respectively
#
# Returns string of decoded DNA sequence
###############################################               
def decode(dna,t):
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
      if t == 's':
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
                 return
            else: 
              print "Error: DNA sequence not in required format (2)"
              return
         return binascii.unhexlify(dnaDec)
      elif t == 'f':
         if os.path.isfile(dna):
            with open(dna,'r') as f:
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
               return binascii.unhexlify(dnaDec)
         else:
            print "Error: File doesnot exist"
            return
      else:
         print "Error: Invalid arguments"
         return
   else:
      print "Error invalid arguments"
      return

#print encode("",'f')
#print decode("",'f')
