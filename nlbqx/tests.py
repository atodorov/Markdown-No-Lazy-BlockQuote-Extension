#!/usr/bin/env python

import unittest
from markdown import Markdown


class NLBQExtensionTest(unittest.TestCase):

    # list of tuples (description, markup, expected)
    test_cases = [
(
"two quotes divided by regular text",
"""
> Quote 1

divider

> Quote 2
""",
"""
<blockquote>
<p>Quote 1</p>
</blockquote>
<p>divider</p>
<blockquote>
<p>Quote 2</p>
</blockquote>
"""),

(
"two quotes divided by newline",
"""
> Quote 1

> Quote 2
""",
"""
<blockquote>
<p>Quote 1</p>
</blockquote>
<blockquote>
<p>Quote 2</p>
</blockquote>
"""),

(
"one single quote with 1 paragraph",
"""
> Quote 1
> Quote 2
""",
"""
<blockquote>
<p>Quote 1
Quote 2</p>
</blockquote>
"""),

(
"one single quote with 2 paragraphs",
"""
> Quote 1
>
> Quote 2
""",
"""
<blockquote>
<p>Quote 1</p>
<p>Quote 2</p>
</blockquote>
"""),

]

    def setUp(self):
        self.md = Markdown(extensions=['nlbqx'])

    def runTest(self):
        for (description, markup, expected) in self.test_cases:
            self.assertEquals(self.md.convert(markup), expected.strip(), msg=description)


if __name__ == "__main__":
    unittest.main()
