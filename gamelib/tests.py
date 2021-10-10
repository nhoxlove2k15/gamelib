from django.test import TestCase

# Create your tests here.

import datetime
import hashlib
from gamelib.models import *
def delete_everything():
    Game.objects.all().delete()
    Requirement.objects.all().delete()
    Category.objects.all().delete()
    Game_Category.objects.all().delete()

    User.objects.all().delete()
    Rating.objects.all().delete()
    Like.objects.all().delete()
    Comment.objects.all().delete()

delete_everything()

list_name = [
    "FIFA 22 Legacy Edition Switch NSP",
    "Assassins Creed Valhalla Ultimate Edition",
    "Diablo 2 Resurrected",
    "Far Cry 6 Ultimate Edition",
    "GTA 5",
]

list_description = [
    "Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi FIFA 22 Legacy Edition. Trong đó FIFA 22 Legacy Edition là một tựa game hành động, phiêu lưu – thể thao cực hay và hấp dẫn. Cốt truyện FIFA 22 Legacy Edition thì bạn sẽ bắt gặp nhiều huyền thoại như David Beckham hay Thierry Henry trong đoạn phim này. Ngoài thông điệp thể hiện ngôi sao Mbappe cùng câu lạc bộ PSG sẽ là những gương mặt đại diện mới, EA cũng gửi gắm ý đồ hướng người chơi tham gia vào các chế độ khác nhiều hơn qua việc khởi tạo một cầu thủ “Avatar cá nhân” ngay trước khi bắt đầu game.",
    "Nói về gameplay Assassins Creed Valhalla thì nếu ai đã từng chơi dòng game này thì cũng không quá khó khăn để làm quen đâu nhé. Đặc biệt một trong số đó là cây kỹ năng (skill) và thiết lập tùy biến độ khó trong các yếu tố gameplay khác nhau: khám phá, chiến đấu và hành động lén lút. Người chơi và kẻ thù được phân định mạnh, yếu thông qua power, chỉ số tăng dần như cấp độ dựa trên số lượng điểm kỹ năng mà bạn cộng vào các kỹ năng cũng như tăng chỉ số của nhân vật mỗi khi “thăng cấp”. 1 điểm khá hay mà mình cực thích đó là kỹ năng Advanced Assassinations, cho phép người chơi ám sát kẻ thù “one hit one kill” thông qua QTE. Nếu bấm hụt khoảnh khắc, kẻ thù mạnh hơn về chỉ số power sẽ lồm cồm bò dậy và “chiến” với bạn tới cùng.",
    "Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Diablo II Resurrected. Đánh giá Diablo II Resurrected là đây là một tựa game hành động, phiêu lưu – chặt chém cực hay và hấp dẫn. Cốt truyện Diablo II Resurrected thì sau những biến cố đã diễn ra trong Diablo I, Chúa tể hắc ám Diablo đã bị một chiến binh vô danh tiêu diệt. Tuy nhiên, trước khao khát có được sức mạnh của Chúa tể hắc ám, người chiến binh ấy đã quyết định hấp thụ sức mạnh của Chúa tể hắc ám vào trong cơ thể của mình.Việc làm này đã vô tình khiến Chúa tể hắc ám Diablo có cơ hội thâm nhập vào cơ thể của người chiến binh và thực hiện việc biến đổi anh ta trở thành một con ác quỷ thật sự. Sau quá trình biến đổi, người chiến binh vô danh trở thành một vật chủ để những con ác quỷ bắt đầu quá trình xâm nhập vào thế giới loài người.",
    "Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Far Cry 6. Trong đó Far Cry 6 là một tựa game hành động, phiêu lưu cực hay và hấp dẫn. Cốt truyện Far Cry 6 thì game sẽ đưa chúng ta đến đảo quốc hư cấu Yara ở vùng biển Caribbean tươi đẹp. Dĩ nhiên là trong một tựa game Far Cry thì không nơi nào êm đềm: bạn sẽ tham gia vào một cuộc cách mạng tại đây, và sử dụng mọi chiến thuật mình có thể nghĩ ra để chiến thắng.",
    "Nếu các bạn đã biết thì Grand Theft Auto, cái tên gắn liền với tuổi thơ của không ít game thủ, sở hữu độ “tai tiếng” mạnh đến nỗi rất nhiều bậc phụ huynh cũng phải ái ngại khi nghe đến tên này. Nhớ khi xưa mình cũng hay trốn học ra quán nét làm vài ván Cướp Đường Phố mới về và cũng phải công nhận GTA có sức cuốn hút kì lạ mà trải qua bao năm tháng rồi giờ vẫn muốn chơi lại.", 

]

list_producer = [
    "EA Canada",
    "Ubisoft Montreal",
    "Blizzard Entertainment",
    "Ubisoft Toronto",
    "Rockstar North",
]

list_publisher = [
    "Electronic Arts",
    "Ubisoft",
    "Blizzard Entertainment",
    "Ubisoft",
    "Rockstar Games"
]

list_homepage = [
    "",
    "https://www.epicgames.com/store/en-US/p/assassins-creed-valhalla",
    "",
    "https://www.epicgames.com/store/en-US/p/far-cry-6",
    "https://store.steampowered.com/app/113020/Monaco_Whats_Yours_Is_Mine/",
]

list_image = [
    [
    "https://hadoantv.com/wp-content/uploads/2021/10/download-fifa-22-hadoan-tv-3.jpg",
    "https://hadoantv.com/wp-content/uploads/2021/10/download-fifa-22-hadoan-tv-1.jpg"
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/03/download-Assassins-Creed-Valhalla-Ultimate-Edition-hadoan-tv-808x454.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/09/download-diablo-ii-resurrected-hadoan-tv-3-scaled.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/09/download-diablo-ii-resurrected-hadoan-tv-1.jpg"
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-far-cry-6-hadoan-tv-1.jpg",

    ],
    [
        "https://hadoantv.com/wp-content/uploads/2020/11/download-GTA-V-viet-hoa-hadoan-tv-3.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/11/download-GTA-V-viet-hoa-hadoan-tv-3.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/11/download-GTA-V-viet-hoa-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-gta-online-new-survival-hadoan-tv-808x454.jpg",
    ],
]



list_graphic = [
    "Nvidia GTX 1650 Vram 4G", 
    "Ryzen 3 1200 – 3,1 Ghz / i5-4460 – 3,2 Ghz",
    "Nvidia GTX 660 / AMD Radeon HD 7850",
    "AMD RX 460 (4 GB) / Nvidia GTX 960 (4 GB)",
    "NVIDIA 9800 GT 1GB / AMD HD 4870 1GB (DX 10, 10.1, 11)",
]

list_processor = [
    "Intel Core i3-6100 @ 3.7GHz or AMD Athlon X4 880K @4GHz",
    "AMD R9 380 – 4GB / GeForce GTX 960 4GB",
    "Intel Core i3-3250 / AMD FX-4350",
    "AMD Ryzen 3 1200 – 3.1 GHz / Intel i5-4460 – 3.2 GHz",
    "Intel Core 2 Quad CPU Q6600 @ 2.40GHz (4 CPUs) / AMD Phenom 9850 Quad-Core Processor (4 CPUs) @ 2.5GHz",
]
list_category = [
        "bắn súng",
        "kinh dị",
        "phiếu lưu",
        "2d",
        "moba",
]
     
for i in range(5) :
   
    r = Requirement(
        os = "Windows",
        storage = "20GB chỗ trống khả dụng",
        ram = "8GB RAM",
        graphic = list_graphic[i] ,
        processor = list_processor[i],
    )
    r.save()
    g = Game(
        name = list_name[i],
        description = list_description[i],
        producer = list_producer[i],
        publisher = list_publisher[i],
        home_page = list_homepage[i], 
        release_date = datetime.datetime.now(),
        requirement_id = r,
        images = list_image[i]
        )
    g.save()

    c = Category(name=list_category[i])
    c.save()
    Game_Category.objects.create(game_id = g , category_id = c)

User.objects.create(full_name="Đôn Khánh Duy" , user_name = "duydon" , pass_word=str(hash("duydon")) , created_at=datetime.datetime.now())
User.objects.create(full_name="Trần Hoàng Long" , user_name = "longtran" , pass_word="longtran" , created_at=datetime.datetime.now())
User.objects.create(full_name="Lê Trọng Hiếu" , user_name = "hieule" , pass_word="hieule" , created_at=datetime.datetime.now())
User.objects.create(full_name="Nguyễn Đình Tuấn Anh" , user_name = "anhnguyen" , pass_word="anhnguyen" , created_at=datetime.datetime.now())
User.objects.create(full_name="Bùi Tiến Đạt" , user_name = "datbui" , pass_word="datbui" , created_at=datetime.datetime.now())

Comment.objects.create(user_id = User.objects.get(pk=1), game_id = Game.objects.get(pk=1) , content = "user 1 comment game 1" , created_at = datetime.datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=2), game_id = Game.objects.get(pk=1) , content = "user 2 comment game 1" , created_at = datetime.datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=3), game_id = Game.objects.get(pk=1) , content = "user 3 comment game 1" , created_at = datetime.datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=4), game_id = Game.objects.get(pk=2) , content = "user 4 comment game 2" , created_at = datetime.datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=5), game_id = Game.objects.get(pk=2) , content = "user 5 comment game 2" , created_at = datetime.datetime.now() )

Rating.objects.create(user_id = User.objects.get(pk = 1 ), game_id = Game.objects.get(pk=2), rate=[6,7,8,9,5])
Rating.objects.create(user_id = User.objects.get(pk = 2 ), game_id = Game.objects.get(pk=2), rate=[10,10,10,10,9 ])
Rating.objects.create(user_id = User.objects.get(pk = 3 ), game_id = Game.objects.get(pk=2), rate=[1,2,3,4,5 ])
Rating.objects.create(user_id = User.objects.get(pk = 1 ), game_id = Game.objects.get(pk=1), rate=[1,2,3,4,5 ])
Rating.objects.create(user_id = User.objects.get(pk = 4 ), game_id = Game.objects.get(pk=1), rate=[5,6,7,8,9 ])

# Rating.objects.create(user_id = User.objects.get(pk = 1 ), game_id = Game.objects.get(pk=2), rate=1)
# Rating.objects.create(user_id = User.objects.get(pk = 2 ), game_id = Game.objects.get(pk=2), rate=2)
# Rating.objects.create(user_id = User.objects.get(pk = 3 ), game_id = Game.objects.get(pk=2), rate=3)
# Rating.objects.create(user_id = User.objects.get(pk = 1 ), game_id = Game.objects.get(pk=1), rate=4)
# Rating.objects.create(user_id = User.objects.get(pk = 4 ), game_id = Game.objects.get(pk=1), rate=5)

Like.objects.create(user_id= User.objects.get(id=1 ), game_id =  Game.objects.get(id=1))
Like.objects.create(user_id= User.objects.get(id=1 ), game_id =  Game.objects.get(id=1))
Like.objects.create(user_id= User.objects.get(id=1 ), game_id =  Game.objects.get(id=1))
Like.objects.create(user_id= User.objects.get(id=2 ), game_id =  Game.objects.get(id=2))
Like.objects.create(user_id= User.objects.get(id=2 ), game_id =  Game.objects.get(id=2))

# Game_Category.objects.create(game_id = 1 , category_id = 2)
# Game_Category.objects.create(game_id = 1 , category_id = 3)
# Game_Category.objects.create(game_id = 2 , category_id = 5)
# Game_Category.objects.create(game_id = 3 , category_id = 4)


