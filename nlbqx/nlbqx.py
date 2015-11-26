from markdown import util, Extension
from markdown.blockprocessors import BlockQuoteProcessor

class NLBQExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.parser.blockprocessors['quote'] = NLBQProcessor(md.parser)


class NLBQProcessor(BlockQuoteProcessor):

    def run(self, parent, blocks):
        block = blocks.pop(0)
        m = self.RE.search(block)
        if m:
            before = block[:m.start()]  # Lines before blockquote
            # Pass lines before blockquote in recursively for parsing forst.
            self.parser.parseBlocks(parent, [before])
            # Remove ``> `` from begining of each line.
            block = '\n'.join(
                [self.clean(line) for line in block[m.start():].split('\n')]
            )

        # no lazy blockquotes
        quote = util.etree.SubElement(parent, 'blockquote')

        # Recursively parse block with blockquote as parent.
        # change parser state so blockquotes embedded in lists use p tags
        self.parser.state.set('blockquote')
        self.parser.parseChunk(quote, block)
        self.parser.state.reset()


def makeExtension(*args, **kwargs):
    return NLBQExtension(*args, **kwargs)
