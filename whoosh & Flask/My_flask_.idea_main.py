from flask import Flask,render_template,request
from whoosh.index import open_dir
from whoosh.qparser import MultifieldParser
from whoosh.fields import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/search',methods=['GET', 'POST'])
def search():
 query=request.args.get('text')
 #return query


 index_path = r"C:\Users\Abhi\Desktop\Index"
 ix = open_dir(index_path)
 mparser = MultifieldParser(["title","docno","text_data", "author_data","bibilo_text"], schema=ix.schema)
 q = mparser.parse(str(query))

 with ix.searcher() as searcher:
         result = searcher.search(q)
         if len(result)!=0:
            return render_template("search.html", results=result)
         else:
            return render_template("NotFound.html")

    #count = count + 1
     # for hit in result:
     # print(len(hit))
 #print(count)

 #return render_template('search.html')
if __name__ == '__main__':
  app.run(port=80,debug=True)