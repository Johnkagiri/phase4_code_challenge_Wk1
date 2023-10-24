# puts "🦸‍♀️ Seeding powers..."
# Power.create([
#   { name: "super strength", description: "gives the wielder super-human strengths" },
#   { name: "flight", description: "gives the wielder the ability to fly through the skies at supersonic speed" },
#   { name: "super human senses", description: "allows the wielder to use her senses at a super-human level" },
#   { name: "elasticity", description: "can stretch the human body to extreme lengths" }
# ])

# puts "🦸‍♀️ Seeding heroes..."
# Hero.create([
#   { name: "Kamala Khan", super_name: "Ms. Marvel" },
#   { name: "Doreen Green", super_name: "Squirrel Girl" },
#   { name: "Gwen Stacy", super_name: "Spider-Gwen" },
#   { name: "Janet Van Dyne", super_name: "The Wasp" },
#   { name: "Wanda Maximoff", super_name: "Scarlet Witch" },
#   { name: "Carol Danvers", super_name: "Captain Marvel" },
#   { name: "Jean Grey", super_name: "Dark Phoenix" },
#   { name: "Ororo Munroe", super_name: "Storm" },
#   { name: "Kitty Pryde", super_name: "Shadowcat" },
#   { name: "Elektra Natchios", super_name: "Elektra" }
# ])

# puts "🦸‍♀️ Adding powers to heroes..."

# strengths = ["Strong", "Weak", "Average"]
# Hero.all.each do |hero|
#   rand(1..3).times do
#     # get a random power
#     power = Power.find(Power.pluck(:id).sample)

#     HeroPower.create!(hero_id: hero.id, power_id: power.id, strength: strengths.sample)
#   end
# end

# puts "🦸‍♀️ Done seeding!"
from random import choice as rc
from sqlalchemy.orm import sessionmaker
# from faker import Faker
from flask import session
from app import app
from models import db, Hero, Hero_powers, Power

with app.app_context():
    
    Hero.query.delete()
    Power.query.delete()
    Hero_powers.query.delete()
    hero=[
      Hero( name= "Kamala Khan", super_name= "Ms. Marvel" ),
      Hero( name= "Doreen Green", super_name= "Squirrel Girl" ),
      Hero( name= "Gwen Stacy", super_name= "Spider-Gwen" ),
      Hero( name= "Janet Van Dyne", super_name= "The Wasp" ),
      Hero( name= "Wanda Maximoff", super_name= "Scarlet Witch" ),
      Hero( name= "Carol Danvers", super_name= "Captain Marvel" ),
      Hero( name= "Jean Grey", super_name= "Dark Phoenix" ),
      Hero( name= "Ororo Munroe", super_name= "Storm" ),
      Hero( name= "Kitty Pryde", super_name= "Shadowcat" ),
      Hero( name= "Elektra Natchios", super_name= "Elektra"),
    ]

    db.session.add_all(hero)
    db.session.commit()

    powerss=[        
      Power( name= "super strength", description= "gives the wielder super-human strengths" ),
      Power( name= "flight", description= "gives the wielder the ability to fly through the skies at supersonic speed" ),
      Power( name= "super human senses", description= "allows the wielder to use her senses at a super-human level" ),
      Power( name= "elasticity", description= "can stretch the human body to extreme lengths" )
        ]
    
    db.session.add_all(powerss)
    # db.session.commit()

    hero_powers=[]
    for i in range(5):
        hero_power=Hero_powers(strength=rc(["Strong", "Weak", "Average"]), hero=rc(hero ), powers=rc(powerss))
        hero_powers.append(hero_power)

    db.session.add_all(hero_powers)
    db.session.commit()    
    