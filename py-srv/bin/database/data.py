import os
from database.model import DbModel
from database.schema import COLUMN_NAME

INDEX_NAME = os.environ["INDEX_NAME"]

DOC = [
    DbModel(0, "Orange",["orange"], 0.99),
    DbModel(1, "Grape",["purple"], 1.89),
    DbModel(2, "Blueberry",["blue"], 0.55),
    DbModel(3, "Strawberry",["red"], 1.19),
    DbModel(4, "Orange",["orange","green"], 2.29),
    DbModel(5, "Blume",["red-orange"], 1.49),
    DbModel(6, "Orange",["orange","yellow"], 2.99),
    DbModel(7, "Strawberry",["red"], 1.19)
]