#HelixWorks

## DNAdrive Repo

dnadrive -str 'hello world' -e 
dnadrive -str 'GGGGGGATTAGGGGGGTAAAGGGGGGATTAGGGGGGATATGGGGGGATTAGGGGGGTTAAGGGGGGATTAGGGGGGTTAAGGGGGGATTAGGGGGGTTTTGGGGGGAATAGGGGGGAAAAGGGGGGATTTGGGGGGATTTGGGGGGATTAGGGGGGTTTTGGGGGGATTTGGGGGGAATAGGGGGGATTAGGGGGGTTAAGGGGGGATTAGGGGGGATAAGGGGGG' -d

## for files, we can have multiple variants 
todo: descrive variant IDS

dnadrive  -e -i input.test -o output.test -v 1
dnadrive  -d -i output.test -o check.test 

## DOCKER

docker build -t helix-dnadrive .
docker run -d -p 5000:5000 helix-dnadrive

## CURL CHECK TO 

curl -X PUT -F filedata=@input.png "http://localhost:5000/encode/" > out.moss
curl -X PUT -F filedata=@out.moss "http://localhost:5000/decode/" > out.png


