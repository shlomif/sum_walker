#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the terms of the MIT license.
#
# This program finds numbers that are expressible as the sum of two integer
# cubes in two or more ways.
#
# See:
# https://en.wikipedia.org/wiki/Taxicab_number

from six import print_

from sum_walker import DWIM_SumWalker


def main():
    seq = [0, 1]
    reached = 2

    def request_more():
        nonlocal reached
        nonlocal seq
        seq.append(reached ** 3)
        reached += 1

    it = DWIM_SumWalker(2, seq, request_more)
    while True:
        sum_, coords = next(it)
        len_ = len(coords)
        if len_ > 1:
            print_("{}\t{}\t{}".format(
                len_, sum_, " ; ".join(
                    [" + ".join(["{} ** 3".format(x) for x in c])
                     for c in coords])))


main()
