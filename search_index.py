from whoosh.index import create_in, open_dir
from whoosh.fields import *
schema = Schema(title=TEXT(stored=True), path=ID(stored=True,unique=True), isin=ID(stored=True, unique=True), content=TEXT)
#ix = open_dir("indexdir")

ix = create_in("indexdir", schema)
writer = ix.writer()
writer.update_document(title=u"First document", path=u"/a", isin='1',
                     content=u"This is the first document we've added!")
writer.update_document(title=u"Second document", path=u"/b", isin='2',
                     content=u"The second one is even more interesting!")
writer.commit()

def new_feature():
    pass

from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
     query = QueryParser("content", ix.schema).parse("first")
     results = searcher.search(query)
     results[0]
