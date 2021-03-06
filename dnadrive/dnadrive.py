import os
import binascii
import ntpath
import datetime
from string import maketrans  

class StringEmptyException(Exception):
    pass

class NotStringException(Exception):
    pass


def check_type(typ):
   if typ==1:
      return True
   elif typ==2:
      return True
   elif typ==3:
      return True
   elif typ==4:
      return True
   else:
      return False

def type1(byt1,byt2):
   return 'GCGGGGC'+byt1+'CGGGGCG'+','+'GCCCCGC'+byt2+'CGCCCCG'+','

def type2(byt1,byt2):
   return 'CGGGGC'+byt1+'CGGGGC'+','+'GCCCCG'+byt2+'GCCCCG'+','

def type3(byt1,byt2):
   return 'CGGGG'+byt1+'GGGGC'+','+'CCCCG'+byt2+'GCCCC'+','
   
def type4(byt1,byt2):
   return 'GGGG'+byt1+'GGGG'+','+'CCCC'+byt2+'CCCC'+','


def check_seq(byt1,byt2,typ):
   if typ==1:
      GC11,AT1,GC12=byt1[:7],byt1[7:11],byt1[11:]
      GC21,AT2,GC22=byt2[:7],byt2[7:11],byt2[11:]
      if (GC11=='GCGGGGC')and(GC12=='CGGGGCG')and(GC21=='GCCCCGC')and(GC22=='CGCCCCG'):
         return True,AT1,AT2
      else:
         return False,0,0
   elif typ==2:
      GC11,AT1,GC12=byt1[:6],byt1[6:10],byt1[10:]
      GC21,AT2,GC22=byt2[:6],byt2[6:10],byt2[10:]
      if (GC11=='CGGGGC')and(GC12=='CGGGGC')and(GC21=='GCCCCG')and(GC22=='GCCCCG'):
         return True,AT1,AT2
      else:
         return False,0,0
   elif typ==3:
      GC11,AT1,GC12=byt1[:5],byt1[5:9],byt1[9:]
      GC21,AT2,GC22=byt2[:5],byt2[5:9],byt2[9:]
      if (GC11=='CGGGG')and(GC12=='GGGGC')and(GC21=='CCCCG')and(GC22=='GCCCC'):
         return True,AT1,AT2
      else:
         return False,0,0
   elif typ==4:
      GC11,AT1,GC12=byt1[:4],byt1[4:8],byt1[8:]
      GC21,AT2,GC22=byt2[:4],byt2[4:8],byt2[8:]
      if (GC11=='GGGG')and(GC12=='GGGG')and(GC21=='CCCC')and(GC22=='CCCC'):
         return True,AT1,AT2
      else:
         return False,0,0
   else:
      return False,0,0
      

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

def encode_file(inp,out,typ=1):
   """ Input: Arguments should be a input and output file
       Output: Writes encoded DNA sequence in output file
   """
   GCarr=['AAAA',
   'AAAT',
   'AATA',
   'AATT',
   'ATAA',
   'ATAT',
   'ATTA',
   'ATTT',
   'TAAA',
   'TAAT',
   'TATA',
   'TATT',
   'TTAA',
   'TTAT',
   'TTTA',
   'TTTT']

   option={1:type1,
      2:type2,
      3:type3,
      4:type4
   }
   if (type(inp)==str)and(type(out)==str):
      if(type(typ)==int)and(check_type(typ)):
         if os.path.isfile(inp):
#            print "file is going to open"
            with open(inp,'rb') as f, open(out,'w') as w:
#               print "file opened"
#               dnaEnc=""
               if os.path.getsize(inp)>0:
                  header=ntpath.basename(inp)+'@'+str(typ)+' | '+str(datetime.datetime.now()) + " | openMoSSv1.0 | helix.works" +'\n'
                  w.write(header)
                  for line in f:
#                     print line
                     for byt in line:
#                        if byt == '':
#                           raise Exception("Error: String is empty")
                         
                        hexbyt = int(binascii.hexlify(byt),16)
                        ind = divmod(hexbyt,16)
                        dnaEnc = option[typ](GCarr[ind[0]],GCarr[ind[1]])
#                        dnaEnc = dnaEnc + GCarr[ind[0]] + GCarr[ind[1]]
                        w.write(dnaEnc)
               else:
                  raise Exception("Error: File is empty")
         else: 
            raise Exception("Error: Input file doesnot exist") 
      else:
         raise Exception("Error: Type argument should be string or invalid type value.")
   else:
      raise Exception("Error: Arguments should be string.") 

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
def decode_string(dna):
   """
      Input: Argument as string to be decoded
      Returns string of decoded DNA sequence
   """
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
   if (type(inp)==str)and(type(out)==str):
      if os.path.isfile(inp):
         with open(inp,'r') as f, open(out,'w') as w:
            dnaSeq=f.read()
            moss=dnaSeq.split('\n')
            typ=moss[0].split('@')[1][0]
            dnaDec=""
            enc=moss[1].split(',')
#            print (len(enc))
            for i in range(0,len(enc)-1,2):
#               Gs,AT=dnaSeq[i:i+6],dnaSeq[i+6:i+10]
               if (check_type(int(typ))):
                  # print AT
                  GC,AT1,AT2=check_seq(enc[i],enc[i+1],int(typ))
#                  print (str(i)+AT1+AT2)
                  if GC:
                     if (AT1 in hexAT.keys())and(AT2 in hexAT.keys()) :
                        dnaDec=hexAT[AT1]+hexAT[AT2]
                        w.write(binascii.unhexlify(dnaDec))
#                     elif AT == '\n' or AT == '':
#                       continue
                     else: 
                     # print AT,int(AT)
                        raise Exception("Error: DNA sequence not in required format (3)")
                  else:
                     raise Exception("Error: DNA sequence not in required format (4)")
               else: 
                  raise Exception("Error: File header type doesnot match")
#            with open(out,'w') as w:
#            w.write(binascii.unhexlify(dnaDec))
      else:
         raise Exception("Error: File doesnot exist")
   else:
      raise Exception("Error invalid arguments")

BITLENGTH = 8
PADDING_BLOCK = "GCAACGCAGCACGCAACG"
WELL_MAPPING = {
   "GCGGGGCAAAACGGGGCG":"1",
   "GCGGGGCAAATCGGGGCG":"2",
   "GCGGGGCAATACGGGGCG":"3",
   "GCGGGGCAATTCGGGGCG":"4",
   "GCGGGGCATAACGGGGCG":"5",
   "GCGGGGCATATCGGGGCG":"6",
   "GCGGGGCATTACGGGGCG":"7",
   "GCGGGGCATTTCGGGGCG":"8",
   "GCGGGGCTAAACGGGGCG":"9",
   "GCGGGGCTAATCGGGGCG":"10",
   "GCGGGGCTATACGGGGCG":"11",
   "GCGGGGCTATTCGGGGCG":"12",
   "GCGGGGCTTAACGGGGCG":"13",
   "GCGGGGCTTATCGGGGCG":"14",
   "GCGGGGCTTTACGGGGCG":"15",
   "GCGGGGCTTTTCGGGGCG":"16",
   "GCCCCGCTTTTCGCCCCG":"17",
   "GCCCCGCTTTACGCCCCG":"18",
   "GCCCCGCTTATCGCCCCG":"19",
   "GCCCCGCTTAACGCCCCG":"20",
   "GCCCCGCTATTCGCCCCG":"21",
   "GCCCCGCTATACGCCCCG":"22",
   "GCCCCGCTAATCGCCCCG":"23",
   "GCCCCGCTAAACGCCCCG":"24",
   "GCCCCGCATTTCGCCCCG":"25",
   "GCCCCGCATTACGCCCCG":"26",
   "GCCCCGCATATCGCCCCG":"27",
   "GCCCCGCATAACGCCCCG":"28",
   "GCCCCGCAATTCGCCCCG":"29",
   "GCCCCGCAATACGCCCCG":"30",
   "GCCCCGCAAATCGCCCCG":"31",
   "GCCCCGCAAAACGCCCCG":"32",
   PADDING_BLOCK:"44", # padding well
}
   # for i in range(1,50):
   #    print '{0:04x}'.format(i)

def get_address_str(num):
   outtab = "AT"
   intab = "TA"
   trantab = maketrans(intab, outtab)

   enc = ('{0:0'+str(BITLENGTH)+'x}').format(num)
   outp = []
   for i,e in enumerate(enc,0):
      # print '>>>>>>',int(i),e,hexAT.keys()[hexAT.values().index(str(i))]
      if int(i)%2==0:
         outp.append(WELL_MAPPING.keys()[WELL_MAPPING.values().index(str(int(e,16)+1))])
      else:
         complement = hexAT.keys()[hexAT.values().index(str(e))]
         complement = complement.translate(trantab)#[::-1]
         complement = [key for key in WELL_MAPPING.keys() if int(WELL_MAPPING[key])>16 and complement in key][0]
         outp.append(complement)
   # print num,outp
   return outp

from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

def generate_well_file(inp,outp):
   
   # for n in range(1,200,350):
   #    print n,[int(WELL_MAPPING[bloc]) for bloc in list(get_address_str(n))]
   if os.path.isfile(inp):
      with open(inp,'r') as f:
         dnaSeq=f.read()
         moss=dnaSeq.split('\n')
         typ=moss[0].split('@')[1][0]
         dnaDec=""
         enc=[e for e in moss[1].split(',') if e!='']
         # print enc, len(enc)
      well_numbers = []
      well_numbers.append(33)
      for i,moss_bloc in enumerate(grouper(enc,BITLENGTH,PADDING_BLOCK),0):
         # print 'addr','{0:04x}'.format(i)
         well_numbers += [int(WELL_MAPPING[bloc]) for bloc in list(get_address_str(i))+list(moss_bloc)]
         well_numbers += [34,38]
      well_numbers += [34, 38, 35, 36]
      with open(outp,'w') as w:
         header = moss[0]
         w.write(header)
         w.write('\n')
         w.write(','.join([str(w) for w in well_numbers]))
         return outp