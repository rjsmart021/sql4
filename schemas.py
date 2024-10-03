from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from API_MINI import app
ma = Marshmallow()
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Bakery as BakeryModel, Product as productModel, product_genres, db
from sqlalchemy.orm import Session
