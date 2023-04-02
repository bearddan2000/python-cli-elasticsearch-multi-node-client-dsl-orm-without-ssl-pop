from elasticsearch_dsl import Document,Text,Keyword,Long,Double,Integer

class DbModel(Document):
    id=Long()
    name=Text()
    color=Keyword()
    price=Double()
    quanty=Integer()

    class Index:
        name='pop-demo' #index will be created automatically

    def __init__(self, id, name, color, price) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.color = color
        self.price = price
        self.quanty = int(id)*10
