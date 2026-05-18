from markdown.extensions import Extension
from markdown.extensions.tables import TableExtension, TableProcessor
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree

class CaptionInlineProcessor(InlineProcessor): 
    def handleMatch(self, m, data):
        el = etree.Element('span')
        # print(m.group(1))
        el.text = m.group(1)
        return el, m.start(0), m.end(0)
    
class CaptionExtension(Extension): 
    def extendMarkdown(self, md):
        CAPTION_PATTERN = r'\{(.*?)\}(\s*?)\[(.*?)\]'  # like {...}[...]
        md.inlinePatterns.register(CaptionInlineProcessor(CAPTION_PATTERN, md), 'caption-inline', 4)


class ExtTableProcessor(TableProcessor): 
    def run(self, parent, blocks):
        super().run(parent, blocks)

        el = etree.Element('ul')

        table = parent.find('table')
        headers = [x.text for x in table.find('thead').find('tr').findall('th')]
        
        for tRow in table.find('tbody').findall('tr'): 
            ulBody = etree.Element('ul')
            i = 0
            for tData in tRow.findall('td'): 
                li = etree.Element('li')
                
                li.text = f"<strong>{headers[i]}</strong>: {tData.text}"

                if i == 0:
                    el.append(li)
                else: 
                    ulBody.append(li)

                i += 1
            el.append(ulBody)

        parent.remove(table)
        parent.append(el)
        

class ExtTableExtension(TableExtension): 
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(ExtTableProcessor(md.parser, self.getConfigs()), 'ext-tables', 75)