# DNAdrive

`dnadrive` is a tool to convert data to and from the [openMoSS](http://openmoss.org) format.
please see the [Techinical Documentation](https://openmoss.org/docs/MoSS.pdf) for more details.

[See the demo here](https://openmoss.org/file/)

### Installation

* `pip install dnadrive`
(or)
* Please install in a virtualenv that is running python2.7 (we do **not** support python3 as of now)
* `python setup.py install` in the source directory will also install
* `pip install -r requirements.txt` if you would like to use the provided flask server. (does not install with pip)

### Usage

All supported operations are done on files
*	`-e` or `-d` encodes/decodes the file
*	`-i` and `-o` provide the input and ouput paths
*	`-v` let's you choose the openmoss variant from
*	variant is detected automatically on decode

**Variant list to choose from**

1. Cost efficiency - GCGGGGCXXXXCGGGGCG
2. Balanced - CGGGGCXXXXCGGGGC
3. Lower secondary structures - CGGGGXXXXGGGGC
4. No secondary structures - GGGGXXXXGGGG

* To Encode
```
dnadrive  -e -i input.test -o output.test -v 1
```
* To Decode
```
dnadrive  -d -i output.test -o check.test 
```
* To Generate Well File
```
dnadrive  -g -i output.test -o check.test 
```

### DOCKER
we provide a docker file for REST access to openmoss encoding/decoding service.
```
docker build -t helix-dnadrive .
docker run -d -p 5000:5000 helix-dnadrive
```

### API EXAMPLES

```
curl -X POST -F filedata=@input.png --data "variant=1" "http://localhost:5000/encode/" > out.moss

curl -X POST -F filedata=@out.moss "http://localhost:5000/decode/" > out.png
```


