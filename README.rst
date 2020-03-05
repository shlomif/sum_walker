==============================================================================
Sum walker.  Iterate over sums of a certain number of elements
==============================================================================
:Info: This is the README file for Sum walker.
:Author: Shlomi Fish <shlomif@cpan.org>
:Copyright: © 2020, Shlomi Fish.
:Date: 2020-02-25
:Version: 0.6.1

.. index: README
.. image:: https://travis-ci.org/shlomif/sum_walker.svg?branch=master
   :target: https://travis-ci.org/shlomif/sum_walker

PURPOSE
-------

The sum_walker PyPI distribution allows one to iterate over increasing
sums of a certain number (e.g: 2 or 3) of elements out of a stream of
increasing integers.

INSTALLATION
------------

pip3 install sum_walker

USAGE
-----

::

    # Finding sums of two powers of 3 (= i**3 ) in two or more
    # different ways:
    #
    # https://en.wikipedia.org/wiki/Taxicab_number
    from sum_walker import DWIM_SumWalker

    seq = [0, 1]
    reached = 2

    def request_more():
        nonlocal reached
        nonlocal seq
        seq.append(reached ** 3)
        reached += 1

    it = DWIM_SumWalker(2, seq, request_more)
    for sum_, coords in it:
        len_ = len(coords)
        if len_ > 1:
            print("{}	{}	{}".format(
                len_, sum_, " ; ".join(
                    [" + ".join(["{} ** 3".format(x) for x in c])
                     for c in coords])))

NOTES
-----

COPYRIGHT
---------
Copyright © 2020, Shlomi Fish.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions, and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither the name of the author of this software nor the names of
   contributors to this software may be used to endorse or promote
   products derived from this software without specific prior written
   consent.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.