# :mortar_board: Website of my academic achievements

[![Makefile CI](https://github.com/surt91/portfolio/actions/workflows/main.yml/badge.svg)](https://github.com/surt91/portfolio/actions/workflows/main.yml)

Visit it at [academic.schawe.me](https://academic.schawe.me).

## :hammer_and_wrench: Setup

Ensure that `python3` is installed and `poetry` is available.

1. `git clone https://github.com/surt91/portfolio.git`
2. `cd portfolio`
3. `git submodule update --init --recursive`
4. `poetry install`
5. `DEBUG=1 poetry run make publish`
6. upload the static files in the `output` directory to some web server
    * [GitHub pages](https://pages.github.com/) using and [`.github/workflows/main.yml`](main.yml)
    * [Netlify](https://www.netlify.com/) using [`build.sh`](build.sh)
    * An Apache server using the [`apache-vhost.conf`](apache-vhost.conf) example
