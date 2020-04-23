from app import db
from models import Pet

db.drop_all()
db.create_all()

jones = Pet(name="Jones", species="dog", photo_url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/funny-dog-captions-1563456605.jpg", age=2, notes="Infinity cute!")
sally = Pet(name="Sally", species="dog", photo_url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-captions-for-instagram-1563456770.jpg", age=5, notes="Loves walks")
jupiter = Pet(name="Jupiter", species="dog", photo_url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-dog-captions-1563456568.jpg", age=1, notes="Eats lots")
gumbo = Pet(name="Gumbo", species="hamster", photo_url="https://www.catster.com/wp-content/uploads/2020/04/2005_Hiding-in-box_getty950329090.png", age=2, notes="Loves to run on his wheel")
commander = Pet(name="Commander", species="cat", photo_url="https://www.rd.com/wp-content/uploads/2019/05/shutterstock_1031164915.jpg", age=1, notes="Chases yarn", available=False)
leah = Pet(name="Leah", species="cat", photo_url="https://www.rd.com/wp-content/uploads/2019/05/British-Blue-Silver-Kitten.jpg", age=2, notes="Fluffball")
stinky = Pet(name="Stinky", species="pig", photo_url="https://thenypost.files.wordpress.com/2019/10/giant-pigs-china-01.jpg?quality=90&strip=all&w=1236&h=820&crop=1", age=10, notes="Great company")
lightning = Pet(name="Lightning", species="dog", photo_url="https://www.petmd.com/sites/default/files/Acute-Dog-Diarrhea-47066074.jpg", age=7, notes="Eats meatballs", available=False)
thunder = Pet(name="Thunder", species="dog", photo_url="https://www.guidedogs.org/wp-content/uploads/2019/11/website-donate-mobile.jpg", age=3, notes="Chases balls")
carrots = Pet(name="Carrots", species="rabbit", photo_url="https://www.humanesociety.org/sites/default/files/styles/1441x612/public/2019/03/rabbit-475261_0.jpg?h=c855054e&itok=nUp2e27x", age=2, notes="Might bite")

everyone = db.session.add_all([jones, sally, jupiter, gumbo, commander, leah, stinky, lightning, thunder, carrots])
db.session.commit()