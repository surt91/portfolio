# This is the source of my personal landing page. [![Build Status](https://travis-ci.org/surt91/portfolio.svg?branch=master)](https://travis-ci.org/surt91/portfolio)

Visit it at [academic.schawe.me](https://academic.schawe.me).

## Setup

Ensure that `python3` is installed and `pip` is available. Advanced users might prefer to perform
step 4. in a python [virtual environment](https://docs.python.org/3/tutorial/venv.html).

1. `git clone https://github.com/surt91/portfolio.git`
2. `cd portfolio`
3. `git submodule update --init --recursive`
4. `pip3 install --user -r requirements.txt`
5. `make publish`
6. upload the static files in the `output` directory to some web server
    * [GitHub pages](https://pages.github.com/) using [TravisCI](https://travis-ci.org/) and [`.travis.yml`](.travis.yml)
    * [Netlify](https://www.netlify.com/) using [`build.sh`](build.sh)
    * An Apache server using the [`apache-vhost.conf`](apache-vhost.conf) example
