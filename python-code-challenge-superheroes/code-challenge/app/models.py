from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'hero'

    serialize_rules = ('-hero_powers.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.relationship('Hero_powers', backref='hero')

    def __repr__(self):
        return f'<hero {self.name} for {self.super_name}>'
    
    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         'name':self.name,
    #     } 



class Hero_powers(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    serialize_rules = ('-hero.hero_powers', '-powers.hero_powers',)
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    powers_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    def __repr__(self):
        return f'<Hero_powers ({self.id}) of {self.hero}>'
    
class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_rules = ('-hero_powers.powers',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.relationship('Hero_powers', backref='powers')

    def __repr__(self):
        return f'<Powers {self.name} for {self.description}>'  

    # def to_dict(self):
    #     return {
    #         'id':self.id,
    #         'name':self.name,
    #     } 

  


# add any models you may need. 