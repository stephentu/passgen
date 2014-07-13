passgen [![Build Status](https://travis-ci.org/stephentu/passgen.svg?branch=master)](https://travis-ci.org/stephentu/passgen)
=======

A simple random password generator (using either `/dev/random` or `/dev/urandom`) for various online services such as g-mail and various banking websites. 

Install
-------
Use `pip` for installation (typically in a virtual env):    
  
    pip install -r requirements.txt
    pip install .
    
    
Usage
-----
Look at `api.py` for the supported services. Please submit pull requests to add more. 

    from passgen.api import *
    g = google(max_limit=25)
    g.generate(urandom=True) # use /dev/urandom, fast but insecure entropy
    # 'u`FQM|+/3(X?Hb@[NNM G7opn'
    b = boa()
    b.generate(urandom=False) # use /dev/random, might be slowish
    # 'euwzUBLDW&uaunCu0sk%'
