#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from functools import partial
import concurrent.futures

import html.parser
from base64 import b64encode
import requests

executor = concurrent.futures.ThreadPoolExecutor(1)
futures = []


def header(user, passwd):
    return {
        'Authorization': 'Basic %s' % b64encode(bytes(user + ':' + passwd, "utf-8")).decode("ascii"),
    }


# https://stackoverflow.com/a/1094933/1698412
def sizeof(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.data = None
        self.first = None
        self.start = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            try:
                self.links.append(dict(attrs)['href'])
            except KeyError:
                # invalid a tag
                pass
            else:
                self.start = True

    def handle_endtag(self, tag):
        if tag == "a":
            self.start = False

    def handle_data(self, data):
        if self.start:
            if self.data is None:
                self.first = data
            self.data = data


def links_reachable(html, data, root="/", parent="/", depth=0, request_kwargs={}):
        p = MyHTMLParser()
        try:
            p.feed(html)
        except TypeError:  # no html
            return

        for link in p.links:
            extern = False

            # do not follow anchors
            if "#" in link:
                continue
            # do not follow mailto
            if "mailto:" in link:
                continue
            # mark extern links
            if link.startswith("http") and not link.startswith(root):
                extern = True

            # make relative absolute
            if link[0] != "/" and not link.startswith("http"):
                link = parent.rsplit("/", 1)[0] + "/" + link
            if link[0] == "/":
                link = root + link

            # do not follow twice
            if link in data["visited"]:
                continue

            # do not follow doi redirects: if they redirect, they exist
            allow_redirects = "dx.doi.org" not in link
            # first, get only headers, and only download html
            # the dpg domain always answers 404 to head request, so we need
            # to perform a get request
            if "dpg-tagungen.de" in link:
                h = requests.get(link, allow_redirects=allow_redirects, **request_kwargs)
            else:
                h = requests.head(link, allow_redirects=allow_redirects, **request_kwargs)
            data["visited"].add(link)

            size = ""
            try:
                size = sizeof(int(h.headers['Content-Length']))
                data["reachable"].append(int(h.headers['Content-Length']))
            except KeyError:
                pass

            html = h.headers['Content-Type'].startswith("text/html")
            if h.status_code >= 400:
                data["fail"].append((h.status_code, link))

            comment = ""
            follow = False
            # do only download the body of html files for parsing links
            # but do not follow links on extern pages
            if html and not extern:
                follow = True
                r = requests.get(link, **request_kwargs)

                size = sizeof(int(r.headers['Content-Length']))

                data["downloaded"].append(len(r.content))
                if "Fatal error" in r.text:
                    comment = "PHP Error"

            display = link[len(url):] if link.startswith(url) else link
            print("  "*depth, h.status_code, comment, display, size)
            sys.stdout.flush()

            if follow:
                links_reachable(str(r.text),
                                data,
                                root=root,
                                parent=link,
                                depth=depth+1,
                                request_kwargs=request_kwargs)


if __name__ == "__main__":
    # url = sys.argv[1]
    url = "https://hendrik.schawe.me"
    user = ""
    passwd = ""

    visited = set()  # set of links that should not be followed
    fail = []        # list of dead links
    bytes_reachable = []
    bytes_downloaded = []
    data = {
        "fail": fail,
        "visited": visited,
        "reachable": bytes_reachable,
        "downloaded": bytes_downloaded
    }

    req_kwargs=dict(headers=header(user, passwd))

    start = time.time()
    r = requests.get(url, **req_kwargs)

    links_reachable(str(r.text),
                    data,
                    root=url,
                    request_kwargs=req_kwargs)

    duration = time.time() - start

    print(len(visited), "sites visited")
    print(sizeof(sum(bytes_reachable)), "bytes reachable")
    print(sizeof(sum(bytes_downloaded)), "bytes downloaded")
    print("%.2f s" % duration, "needed")

    if len(fail):
        print("Dead links:")
        for status, link in fail:
            print(status, link)
        sys.exit(1)
