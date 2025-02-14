from app import create_app, db
from app.models import Player, News

app = create_app()

with app.app_context():
    # 1. สร้างฐานข้อมูลและตาราง
    db.create_all()
    print("Database and tables created successfully!")

    # 2. เพิ่มข้อมูลตัวอย่าง
    player1 = Player(name='Marcus Rashford', position='Forward', goals=10)
    player2 = Player(name='Bruno Fernandes', position='Midfielder', goals=7)
    player3 = Player(name='Casemiro', position='Midfielder', goals=5)
    news1 = News(title='Manchester United wins!', content='Manchester United secured a big win last night.')
    
    db.session.add_all([player1, player2,player3 ,news1])
    db.session.commit()
    print("Sample data added successfully!")
