# :mortar_board: Website of my academic achievements

[![Makefile CI](https://github.com/surt91/portfolio/actions/workflows/main.yml/badge.svg)](https://github.com/surt91/portfolio/actions/workflows/main.yml)

Visit it at [academic.schawe.me](https://academic.schawe.me).

## :hammer_and_wrench: Setup

Ensure that `python3` is installed and `pip` is available. Advanced users might prefer to perform
step 4. in a python [virtual environment](https://docs.python.org/3/tutorial/venv.html).

1. `git clone https://github.com/surt91/portfolio.git`
2. `cd portfolio`
3. `git submodule update --init --recursive`
4. `pip3 install --user -r requirements.txt`
5. `make publish`
6. upload the static files in the `output` directory to some web server
    * [GitHub pages](https://pages.github.com/) using and [`.github/workflows/main.yml`](main.yml)
    * [Netlify](https://www.netlify.com/) using [`build.sh`](build.sh)
    * An Apache server using the [`apache-vhost.conf`](apache-vhost.conf) example

## Update

To calculate new dependencies

Do 1-3 from above
4. `python3 -m venv .`
5. `source bin/activate`
6. `sed -i '' 's/[~=]=/>=/' requirements.txt; pip install -U -r requirements.txt; pip freeze | sed 's/==/~=/' > requirements.txt`
7. run `build.sh` to test 
