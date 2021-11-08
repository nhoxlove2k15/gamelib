from django.test import TestCase

# Create your tests here.
from django.contrib.auth import authenticate 

import hashlib
from gamelib.models import *
from datetime import datetime

def delete_everything():
    Game.objects.all().delete()
    Requirement.objects.all().delete()
    Category.objects.all().delete()
    #Game_Category.objects.all().delete()
    User.objects.all().delete()
    Rating.objects.all().delete()
    Like.objects.all().delete()
    Comment.objects.all().delete()

delete_everything()

list_name = [
    #1->5
    "FIFA 22 Legacy Edition Switch NSP",
    "Assassins Creed Valhalla Ultimate Edition",
    "Diablo 2 Resurrected",
    "Far Cry 6 Ultimate Edition",
    "GTA 5",
    #5->10
    "Journey Of Life",
    "Slow living with Princess",
    "Blood and Bacon Online",
    "I am an Air Traffic Controller 4",
    "Sherlock Holmes Crimes and Punishments",
    #10->15
    "DAYS GONE",
    "HITMAN 3",
    "Cyberpunk 2077",
    "THE LEGEND OF ZELDA BREATH OF THE WILD",
    "ARK SURVIVAL EVOLVED",
    #15->20
    "DOOM Eternal The Ancient Gods Part Two",
    "Uncrashed FPV Drone Simulator",
    "Shelter Manager",
    "Stonedeep",
    "Nine Parchments + Online",
    #20->25
    "Invisigun Reloaded",
    "Gas Station Simulator",
    "Force of Nature",
    "Crashlands",
    "Mount & Blade II Bannerlord",
    #25->30
    "Tales of Arise Sao Collaboration",
    "Titanfall 2 Ultimate Edition",
    "LEGO BUILDERS JOURNEY",
    "Valiant Hearts The Great War",
    "Bombernauts",
]
list_category = [
        "hành động", #1
        "bắn súng", #2
        "phiêu lưu", #3
        "sinh tồn",#4
        "thể thao",#5
        "đối kháng",#6
        "chiến thuật",#7
        "kinh dị",#8
        "nhập vai",#9
        "offline", #10
        "online",#11
        "mô phỏng"#12
        
]
list_description = [
    #1->5
    """
    Cốt truyện hấp dẫn

Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi FIFA 22 Legacy Edition. Trong đó FIFA 22 Legacy Edition là một tựa game hành động, phiêu lưu – thể thao cực hay và hấp dẫn. Cốt truyện FIFA 22 Legacy Edition thì bạn sẽ bắt gặp nhiều huyền thoại như David Beckham hay Thierry Henry trong đoạn phim này. Ngoài thông điệp thể hiện ngôi sao Mbappe cùng câu lạc bộ PSG sẽ là những gương mặt đại diện mới, EA cũng gửi gắm ý đồ hướng người chơi tham gia vào các chế độ khác nhiều hơn qua việc khởi tạo một cầu thủ “Avatar cá nhân” ngay trước khi bắt đầu game.

    Gameplay hấp dẫn
Nói về gameplay, FIFA 22 Legacy Edition thì tốc độ trong FIFA 22 cũng được cải thiện để nhịp độ trận đấu chậm hơn, giống với ngoài đời thật hơn. Tất nhiên những cầu thủ có tốc độ (pace) cao vẫn có những lợi thế nhất định, nhưng những cầu thủ pace thấp không hoàn toàn “phế” như các bản trước. AI của những cầu thủ ngôi sao được thể hiện tốt hơn, đặc biệt là các trung vệ khi những CB hàng top như Chielini, Ramos, Van Dijk có thể chặn các đường chuyền và cú sút cực kỳ “ảo”. Nếu như mọi năm, chỉ cầu thủ bạn điều khiển mới được tập trung về các cử động vật lý thì ở FIFA 22 next-gen, toàn bộ 22 cầu thủ trên sân đều có những chuyển động, cử chỉ, dáng chạy riêng biệt. Bạn có thể cảm nhận được trong quá trình chơi game, animation của cầu thủ đã chân thực hơn rất nhiều. Đặc biệt là ở tư thế xoạc bóng, sút bóng, chặn bóng hay các chuyển động cản phá của thủ môn.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Assassins Creed Valhalla. Đánh giá Assassins Creed Valhalla là tựa game hành động, chặt chém – thế giới mở cực hay. Cốt truyện Assassins Creed Valhalla thì đây là phiên bản mới nhất trong chuỗi series dài tập của Assassins Creed. Đến với bản này, game sẽ đưa người chơi đến với các chiến binh người Viking trong bối cảnh vào khoảng cuối thế kỷ thứ 8. Bạn sẽ được nhập vai vào nhân vật chính Eivor và bạn có thể lựa chọn giới tính giống như Assassin’s Creed Odyssey. Evior cùng với anh trai Sigurd rời quê nhà đi tìm giàu sang phú quý ở nơi xứ người bằng việc cướp bóc và xâm chiếm, mở rộng mối giao hảo với bốn vương quốc: Mercia, East Anglia Northumbria và Wessex. Những gì cướp bóc được nơi xứ người lại được dùng xây dựng vương quốc của bạn sánh vai cùng các “cường quốc” khác. Kết cục ra sao bạn cần tải Assassins Creed Valhalla về trải nghiệm sẽ rõ nhé.

    Gameplay hấp dẫn:
Nói về gameplay Assassins Creed Valhalla thì nếu ai đã từng chơi dòng game này thì cũng không quá khó khăn để làm quen đâu nhé. Đặc biệt một trong số đó là cây kỹ năng (skill) và thiết lập tùy biến độ khó trong các yếu tố gameplay khác nhau: khám phá, chiến đấu và hành động lén lút. Người chơi và kẻ thù được phân định mạnh, yếu thông qua power, chỉ số tăng dần như cấp độ dựa trên số lượng điểm kỹ năng mà bạn cộng vào các kỹ năng cũng như tăng chỉ số của nhân vật mỗi khi “thăng cấp”. 1 điểm khá hay mà mình cực thích đó là kỹ năng Advanced Assassinations, cho phép người chơi ám sát kẻ thù “one hit one kill” thông qua QTE. Nếu bấm hụt khoảnh khắc, kẻ thù mạnh hơn về chỉ số power sẽ lồm cồm bò dậy và “chiến” với bạn tới cùng.

    Đồ họa Asassin’s Creed Valhalla
Nói về đồ họa của Asassin’s Creed Valhalla có phần tươi sáng trong phần lớn trải nghiệm, tương phản với cốt truyện ngày càng tăm tối về sau. Bạn cần phải chơi và để ý sẽ thấy chiến thuyền rồng drakar thon dài (longship) mang tính biểu tượng của người Viking, đưa đoàn quân của bạn đi cướp bóc và xâm chiếm khắp nơi trong thế giới game. Những ngôi nhà dài nổi tiếng của người Viking thường phục vụ cho mục đích chè chén cũng xuất hiện trong Asassin’s Creed Valhalla. Đây quả thực là dụng ý rất lớn khi muốn tái hiện chân thực nhất quang cảnh game cho người chơi thêm phần hứng thú mà nhà sản xuất đã đem tới

    Cấu hình Assassins Creed Valhalla
Cấu hình chạy Assassins Creed Valhalla thì các bạn cũng không quá lo khi các bạn cần 1 cone CPU Core i5 đời thứ 4 là đủ chạy nhưng card màn hình của bạn cần ít nhất là 4G Vram để game có thể chạy mượt nhé.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Diablo II Resurrected. Đánh giá Diablo II Resurrected là đây là một tựa game hành động, phiêu lưu – chặt chém cực hay và hấp dẫn. Cốt truyện Diablo II Resurrected thì sau những biến cố đã diễn ra trong Diablo I, Chúa tể hắc ám Diablo đã bị một chiến binh vô danh tiêu diệt. Tuy nhiên, trước khao khát có được sức mạnh của Chúa tể hắc ám, người chiến binh ấy đã quyết định hấp thụ sức mạnh của Chúa tể hắc ám vào trong cơ thể của mình.Việc làm này đã vô tình khiến Chúa tể hắc ám Diablo có cơ hội thâm nhập vào cơ thể của người chiến binh và thực hiện việc biến đổi anh ta trở thành một con ác quỷ thật sự. Sau quá trình biến đổi, người chiến binh vô danh trở thành một vật chủ để những con ác quỷ bắt đầu quá trình xâm nhập vào thế giới loài người.

    Gameplay hấp dẫn
Nói về gameplay Diablo II Resurrected thì đến với Diablo II: Resurrected, bạn sẽ nhập vai trở thành những nhà thám hiểm và lần theo dấu của Dark Wanderer. Hành trình của bạn sẽ được chia thành nhiều chương với mỗi chương bao gồm nhiều nhiệm vụ khác nhau. Bạn cùng những người đồng đội của mình sẽ cần phải vượt qua những nhiệm vụ cũng như thử thách để tiến đến chương tiếp theo của trò chơi.

Cấu hình để chơi Diablo II: Resurrected khá nhẹ nhàng khi so sánh với các bom tấn khác ở thời điểm hiện tại. Ở chế độ đồ họa thấp, game thủ chỉ cần sở hữu PC cũ với phần cứng khoảng 7 – 8 năm tuổi. CPU Intel Core i3-3250, card đồ họa GTX 660 và RAM 8 GB là đủ để chơi tốt.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Far Cry 6. Trong đó Far Cry 6 là một tựa game hành động, phiêu lưu cực hay và hấp dẫn. Cốt truyện Far Cry 6 thì game sẽ đưa chúng ta đến đảo quốc hư cấu Yara ở vùng biển Caribbean tươi đẹp. Dĩ nhiên là trong một tựa game Far Cry thì không nơi nào êm đềm: bạn sẽ tham gia vào một cuộc cách mạng tại đây, và sử dụng mọi chiến thuật mình có thể nghĩ ra để chiến thắng.

    Gameplay hấp dẫn
Nói về gameplay Far Cry 6 thì điểm mình ấn tượng nhất chính là thành phố Esperanza, thủ đô của Yara sẽ rất rộng lớn so với những làng mạc, thị trấn mà bạn từng thấy trong các tựa game Far Cry trước, và sầm uất giống với các đô thị trong các bản Assassin’s Creed gần đây. Bạn sẽ có thể khám phá thành phố này theo phương thẳng đứng, chiến đấu trên các mái nhà cao tầng, sử dụng những con hẻm chật hẹp để thực hiện những pha hành động đẹp, đem lại sự độc đáo và mới mẻ cho trò chơi. Ngoài ra bạn nhập vai vào là một chiến binh du kích thực thụ, có thể giấu súng vào người để hòa lẫn vào đám đông và tự do khám phá Esperanza hay các địa điểm dân sự khác mà không lo ngại các binh sĩ của Castillo nổ súng. Đây thực sự là một thay đổi rất lớn, khiến game thủ có thời gian để nghĩ về những cách tiếp cận mục tiêu mới thay vì cứ lao vào nổ súng như các bản trước đây.

Một điều rất thú vị khác là các trợ thủ của người chơi nay chỉ toàn là động vật. Bạn có thể tìm thấy một chú chó bị liệt tên Chorizo, một con cá sấu Guapo, và có lẽ là nhiều loài động vật khác nữa. Bạn sẽ có thể nựng nịu tất cả những sinh vật này, một điều làm tác giả rất hài lòng. Trong khi đó, chiến hữu người sẽ chỉ xuất hiện trong một số nhiệm vụ cố định chứ không còn lập tức xuất hiện mỗi khi bạn gọi họ như trong Far Cry 5.

Nói về vũ khí Far Cry 6 sẽ có rất nhiều vũ khí cho bạn sử dụng, từ những khẩu súng quen thuộc nhưng được mod loạn xạ bằng các vật phẩm thường ngày đến các loại đồ chơi phi lý như dàn phóng tên lửa đeo lưng, súng điện hay máy bắn đĩa CD. Hơn nữa nhiều loại phương tiện cơ giới cũng sẽ xuất hiện để game thủ sử dụng, trong đó bao gồm cả xe tăng và máy bay.

    Cấu hình chơi Far Cry 6
Game sẽ chỉ chạy trên Win 10 với phiên bản 20h1 mới nhất trở lên và bạn cần chip core i5 đời thứ 4 trở lên và ít nhất Vram card màn hình là 4G để có thể chơi mượt mà tựa game này. Mình đã thử với Vram 2G thì khá lag nhưng vẫn có thể load được chứ không phải không nhé. Các bạn cũng nên cân nhắc vấn đề card màn hình khi chơi nhé.
    """,
    """
    Đánh giá GTA V Việt Hóa là phiên bản mới nhất và được cập nhật các DLC mới nhất giúp các bạn trải nghiệm game ổn định và đầy đủ hơn. Hơn nữa phiên bản do HaDoanTV làm đã kèm các bản Mod Full đồ họa đẹp nhất, đảm bảo các bạn sẽ thích mê khi trải nghiệm bản Full.

Nếu các bạn đã biết thì Grand Theft Auto, cái tên gắn liền với tuổi thơ của không ít game thủ, sở hữu độ “tai tiếng” mạnh đến nỗi rất nhiều bậc phụ huynh cũng phải ái ngại khi nghe đến tên này. Nhớ khi xưa mình cũng hay trốn học ra quán nét làm vài ván Cướp Đường Phố mới về và cũng phải công nhận GTA có sức cuốn hút kì lạ mà trải qua bao năm tháng rồi giờ vẫn muốn chơi lại.

 
    Đặc điểm hấp dẫn game:
Bối cảnh game ngay từ những giây phút đầu tiên trong Grand Theft Auto V, Los Santos đã hoàn toàn “hớp hồn” người viết, không phải bởi vì nó “lộng lẫy” theo phong cách “next-gen”, mà là vì nó mang đến một cảm giác “tương phản” rõ rệt ở từng địa danh, cùng với một sức sống lạ lùng khó có thể tìm thấy được ở bất cứ tựa game thế giới mở nào khác.

Phía đông Los Santos, cũng là “quê nhà” của một trong ba nhân vật chính – Franklin Clinton, toát lên sự nhếch nhác và tồi tàn: những căn nhà xập xệ chỉ với một tầng, các băng đảng đường phố lảo rảo trên khắp các nẻo đường, nhạc rap ầm ĩ đến chói cả tai…

Và vẫn còn đó đường ray xe lửa ngăn cách hai khu phố chính, những con đường quen thuộc và khu phố Groove Streets vẫn chưa thay đổi nhiều kể từ khi Carl Johnson “làm loạn” tại đây 23 năm về trước.

Ngoài ra GTA V còn có tới 3 nhân vật có thể chơi được sẽ cuốn bạn theo câu chuyện của họ để khám phá Los Santos theo những góc nhìn khác nhau. Các nhiệm vụ đa dạng và có chiều sâu cũng là một trong những điểm cuốn hút lớn nhất của tựa game này. Ngoài các nhiệm vụ chính mà bạn phải làm để đi theo cốt truyện, bạn cũng có thể quên chúng đi để tham gia vào những hoạt động bên lề như chơi golf, tennis hoặc “hít cần”. Bạn cũng có thể chỉ đơn giản là lấy một chiếc xe nào đó rồi đi khám phá cả thế giới mở rộng lớn đầy thú vị của GTA 5.

Nếu bao nhiêu đó vẫn là chưa đủ đối với bạn thì bạn cũng có thể tham gia vào các server GTA Online để chơi trực tuyến cùng người chơi khác với đủ các thế loại từ đua xe đến battle royale hay thậm chí là các bản mod cho phép bạn hóa thân thành Superman, Ironman, Thanos… Để quậy tưng bừng cả thành phố. Gần đây, bản cập nhật GTA Casino đã bổ sung một sòng bạc trực tuyến khổng lồ vào Los Santos với rất nhiều minigames, nhiệm vụ mới và hàng tá điều thú vị khác.
    """,
    
   
    # 5->10
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Journey Of Life. Đánh giá Journey Of Life là tựa game hành động, phiêu lưu – sinh tồn cực hay và hấp dẫn. Nếu bạn chưa biết thì cốt truyện Journey Of Life kể về một người đàn ông mất đi tài sản của mình và quyết định sống xa xứ, và xây dựng một cái gì đó cho chính mình.
    Gameplay hấp dẫn:
Nói về gameplay thì đây là trò chơi sinh tồn, trong đó người chơi thấy mình đang ở trên một hòn đảo, buộc phải xây dựng ngôi nhà của mình từ đầu. Để xây dựng một ngôi làng, bạn cũng cần tạo ra nhiều trạm để xử lý các vật liệu tìm thấy trên đảo thành các thành phần được sử dụng để chế tạo công cụ và vũ khí cần thiết cho sự sống còn. Bạn cần xây dựng một bến tàu trên bờ biển để có thể đóng một con tàu được sử dụng để đi thuyền giữa các hòn đảo. Trước khi có khả năng khởi hành, bạn cũng cần nạp đầy tài nguyên như thức ăn và nước cho con tàu để sống sót trong vùng biển bão!

    """, 
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Slow living with Princess. Đánh giá Slow living with Princess là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Slow living with Princess thì đã ba năm kể từ cuộc xâm lược của Chúa quỷ Taraxon – kẻ thống trị Lục địa Bóng tối. Chỉ trong ba năm, một nửa lục địa Avalon đã rơi vào tay Chúa quỷ. Tưởng chừng như con người không thể chống lại hắn… Lúc này, một cô gái tên Ruti Ragnason đã đứng lên chỉ huy quân đội và đánh bại đội quân của Chúa quỷ.
   Gameplay hấp dẫn
Nói về gameplay Slow living with Princess thì Red đã bị đuổi khỏi nhóm của nữ anh hùng đang phiêu lưu đánh bại Chúa quỷ. Anh từ giã chiến tuyến và mở một tiệm thuốc ở biên giới có tên là Zoltan. Giờ đây, cuộc sống mới hạnh phúc của anh phụ thuộc vào mối quan hệ với cựu công chúa tsundere (tính cách nóng lạnh) và cô em gái dễ thương của anh, Ruti, người mà cả thế giới chỉ hy vọng đánh bại Chúa quỷ với tư cách là nữ anh hùng. 
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giói thiệu tới các bạn phiên bản mới nhất của trò chơi Blood and Bacon. Nếu ai chưa biết thì Blood and Bacon là trò chơi FPS nhiều người chơi (Lên đến 6P) giúp người chơi được trang bị vũ khí mạnh chống lại xác chết khi bạn cố gắng giết thịt theo cách của mình thông qua hơn 100 cấp độ điên cuồng và co giật. Ở cấp độ ngày và đêm, người chơi sẽ đối đầu với 25 loại kẻ thù và nhiều con trùm, như quái vật khổng lồ được đặt tên trìu mến, ‘Công chúa Blubbergut’ và Minibosses cứ sau 10 ngày khi bạn khám phá, bắn và chạy lấy mạng mình trước sự tấn công của những quái vật quái vật như heo

    Gameplay hấp dẫn:
Trò chơi phân phối một cách sáng tạo những chiếc xe nhặt được thông qua một máy xay thịt, từ chính những sinh vật bạn đang giết. Hộp đạn, Adrenaline, Lựu đạn, Tên lửa và các tên lửa đẩy kỳ lạ khác. Tự hào với hơn 15 giờ chơi trò chơi và khả năng chiến đấu với hơn 500 sinh vật undead đáng kinh ngạc (hoặc run rẩy) cùng một lúc, “Blood and Bacon”
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi I am an Air Traffic Controller 4. Đánh giá I am an Air Traffic Controller 4 là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện I am an Air Traffic Controller 4 thì kể từ khi phát hành vào năm 1998, trò chơi kiểm soát không lưu này đã trở thành một game bán chạy lâu dài, được sự ủng hộ mạnh mẽ của đông đảo người dùng cả trong và ngoài fandom hàng không. Để máy bay bay an toàn, kiểm soát viên không lưu đóng một vai trò quan trọng. Nhà sản xuất tập trung vào nhiệm vụ của những bộ điều khiển này trong các kịch bản trò chơi.

    Gameplay hấp dẫn
Nói về gameplay I am an Air Traffic Controller 4 thì để hoàn thành các màn chơi, người chơi nên chỉ đường với tư cách là người điều khiển tháp để máy bay bay an toàn và hiệu quả. Thao tác khá đơn giản, chỉ cần chọn một chiếc máy bay và nhấp vào nút Hướng dẫn. Tuy nhiên, khi tình hình liên tục thay đổi theo chỉ đạo được ban hành và thời điểm, việc dọn sân luôn đòi hỏi sự phán đoán chính xác và đúng đắn. Ngay cả sau khi trò chơi kết thúc, bạn có thể tiếp tục chơi lại từ giữa trò chơi.

    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Sherlock Holmes Crimes and Punishments. Đánh giá Sherlock Holmes Crimes and Punishments là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Sherlock Holmes Crimes and Punishments thì nếu bạn yêu thích thể loại phiêu lưu khám phá, từng đọc qua bộ truyện hay xem 1 bộ phim nói về thám tử lừng danh Sherlock Holmes, muốn 1 lần thử trí thông minh và tài phán đoán của mình thì hãy tham gia trải nghiệm ngay series về Sherlock Holmes. Nói qua 1 chút về nội dung game thì người chơi sẽ vào vai ngài siêu thám tử để tìm ra thủ phạm trong tám vụ án liên quan đến giết người hàng loạt, mất tích, trộm cắp… và có tổng cộng 8 vụ tất cả. Đặc biệt, game sẽ xuất hiện sự lựa chọn đạo đức mà mỗi quyết định cả người chơi sẽ danh tiếng của thám tử Sherlock Holmes và cùng với đó là những cái kết mở. Dù đã được chuyển thể thành phim hay game thì Sherlock Homes vẫn luôn giữ được sự hấp dẫn của nó

    Gameplay hấp dẫn
Nói về gameplay Sherlock Holmes Crimes and Punishments thì với bản game này, Crimes & Punishments (Tội ác & sự trừng phạt) bạn có thể tự do phá án theo bất cứ cách nào mà bạn cảm thấy phù hợp nhất. Sử dụng 14 kỹ năng phán xét nổi tiếng của Sherlock như định hướng điều tra, phỏng vấn nghi phạm, loại trừ các khả năng, đặt tên các nhóm tội … bạn có thể quyết định số phận của những tên tội phạm. Mỗi vụ án trong game đều rất phức tạp ,hóc búa và không dễ để đi đến quyết định cuối cùng. Tuy nhiên, một khi bạn đã đưa ra quyết định rồi thì mọi điều có thể xảy ra, bạn sẽ nhận được sự đồng tình nhờ vào danh tiếng của mình hay là một hậu quả nghiêm trọng sẽ xảy ra khi vào lúc mà bạn ít ngờ đến nó nhất ?Liệu bạn sẽ đi theo tiếng gọi của đạo đức và lương tâm hay chỉ đơn thuần thi hành theo đúng pháp luật ? Hãy cùng khám phá thêm trong tựa game này nhé. Game đã được mình update trọn bộ DLC cùng các hot fix mới nhất nên các bạn cứ yên tâm tải về trải nghiệm nhé
    """,

    #10->15
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Days Gone. Đánh giá Days Gone là một trò chơi hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Days Gone thì game sẽ diễn ra ở thế giới hậu tận thế, khi một cơn dịch bệnh bí ẩn quét qua nước Mỹ và biến hầu hết dân số tại đây thành những sinh vật điên loạn gọi là Freakers. Về cơ bản thì Freakers vẫn “sống” nhưng không còn tính người và hành động hoàn toàn bản năng như dã thú, chúng săn đuổi những người còn sót lại suốt ngày đêm. Nhân vật chính của Days Gone là một “Racing Man” có tên là Deacon, anh ta đã mất vợ của mình vào cái đêm mà dịch bệnh bùng nổ, giờ đây Deacon gần như đã mất đi mục đích sống và trở thành một kẻ bất cần đời trong thế giới này.

    Gameplay hấp dẫn:
Nói về gameplay Days Gone thì Days Gone xoay quanh những diễn biến tâm lý của Deacon, cách mà anh ta vẫn tiếp tục bám víu vào quá khứ, trở thành cái gai trong mắt với mọi người và cư xử hệt như một thằng khốn đúng nghĩa. Trong tựa game này có 1 điểm mình thích nhất đó là những đàn Freakers với số lượng lên tới hàng trăm con thực sự xuất hiện, chúng được gọi là The Horde và xuất hiện thường xuyên trên bản đồ. Ngoài Freakers ra thì Deacon còn phải chống lại những con thú bị nhiễm bệnh hay các tên cướp đường, hay nguy hiểm nhất là những kẻ điên vô pháp luật tự lập ra những phe phái riêng chuyên đi giết người ở thế giới hậu tận thế này. Hơn hết nhân vật chính của chúng ta cưỡi con ngựa sắt là chiếc mô-tô hầm hố cực ngầu. Đây vừa là phương tiện di chuyển, Fast Travel, chứa đạn và cả điểm save trong game, nó quan trọng tới mức bạn sẽ gần như không bao giờ rời khỏi xe trừ khi đang làm nhiệm vụ hoặc đánh nhau. Theo thời gian chiếc mô-tô này có thể độ đủ thứ từ tăng tốc độ, thêm độ bền, bám đường và cả lắp ống phóng khí nén vào để chạy cho bốc.

Đặc biệt thế giới của Days Gone xoay quanh các khu vực riêng biệt với điểm mốc là các khu trại khác nhau, theo tiến trình cốt truyện người chơi sẽ được tiếp xúc với những quần thể cư dân còn sót lại trên thế giới.

Đồ họa Days Gone thì chắc bạn khỏi chế vì tất cả đều được làm chi tiết và sắc nét đến ngạc nhiên. Mình đã thử bật lên 4K và hoàn toàn bất ngờ về độ chân thực game mang lại. Hơn nữa lồng tiếng và âm nhạc của game tương đối tốt, đặc biệt các câu thoại trong game rất có ý nghĩa nếu bạn để tâm theo dõi chúng, cũng như phần nhạc nền theo kiểu cao bồi rất phù hợp khi rong ruổi trên xe.

Cấu hình chơi Days Gone thì bạn cần tới chip core i5 thế hệ thứ 2 trở lên, điều này đồng nghĩa với việc những bạn nào đang sử dụng cấu hình mới bây giờ như các chip core i3 đời thứ 8 thì hoàn toàn chạy mượt mà. Ngoài ra nhà sản xuất khuyến nghị các bạn nên chạy trên card màn hình có Vram từ 3G trở lên, nhưng theo thử nghiệm thực tế thì với những card Vram 2G chúng ta vẫn có thể chơi được ở mức Low setting toàn bộ nhé. Chưa hết khi bạn cũng cần trang bị cho mình 1 ổ SSD dung lượng trên 70G hoặc HDD cũng không sao, nhưng tốt nhất vẫn là SSD vì game cần truy xuất dữ liệu nhanh nhé.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi HITMAN 3. Đánh giá HITMAN 3 là phần chơi mới nhất trong series game bắn súng hành động lén lút HITMAN đình đám. Cốt truyện HITMAN 3 được nhiều chuyên gia khen ngợi bởi lối tiếp cận mở kèm với thiết kế màn chơi tuyệt đỉnh. Với mức đánh giá trên các chuyên trang công nghệ lên tới 9/10 thì chắc chắn game sẽ không làm các bạn thất vọng. Nhưng có 1 tin cũng hơi buồn đối với Fan Steam rằng Hitman 3 sẽ chỉ phát hành độc quyền trên Epic Games Store. Điều đó có nghĩa bạn không thể chơi tựa game bắn súng đỉnh cao này nếu không sử dụng thông qua Epic Games Store. Hitman 3 sẽ có nhiều nhiệm vụ trong thế giới mở trong cốt truyện mới. Hơn hết game sẽ mang tính chơi lại cao khiến bạn không hề nhàm chán.

    Gameplay hấp dẫn:
Nói về gameplay thì HITMAN 3 thì giờ đây trò chơi đã có nhiều đổi mới so với các phiên bản cũ trước đây. Hitman 3 sẽ cung cấp một số nhiệm vụ phức tạp và thú vị nhất trong lịch sử trò chơi được phát hành. Game có một số cảnh mở đầu rất điện ảnh, khiến người chơi ngay từ phút đầu đã cảm thấy mãn nhãn. Phần mình yêu thích khi chơi Hitman 3 bao gồm phần giải quyết một bí ẩn giết người gợi nhớ đến Knives Out năm 2019 và chơi trò mèo vờn chuột với một nhóm sát thủ khác cũng vui không kém. Sau đó bạn sẽ nhận được phần thưởng cho việc khám phá các màn chơi và hoàn thành nhiệm vụ ám sát. Mỗi nhiệm vụ có một vài tình huống ám sát được xác định trước, nhưng bạn có thể tự do tiếp cận mỗi lần tiêu diệt tùy ý. Đầu độc mục tiêu của bạn, tạo ra một vụ tai nạn hoặc sử dụng súng bắn loạn lên miễn sao bạn hoàn thành nhiệm vụ là được. Điểm mới của Hitman 3 là bạn sẽ được cung cấp một chiếc máy ảnh cho phép đặc vụ 47 của chúng ta thu thập thông tin và điều khiển các cửa ra vào và cửa sổ bị khóa, cũng như các phím tắt khác giúp bạn dễ dàng trong việc điều khiển các thiết bị ngoại vi trong game hơn. Ngoài ra mỗi nhiệm vụ cũng có một loạt các thử thách giúp người chơi kiếm được số điểm kinh nghiệm để mở khóa nhiều tùy chọn hơn cho các lần chơi lại nhiệm vụ. Hitman 3 sẽ có sáu cấp độ khó và mỗi lần bạn chơi lại sẽ không giống nhau đâu nhé.

1 điểm mình khá thích đó chính là việc bạn có thể nhập các nhiệm vụ và chế độ từ Hitman và Hitman 2, cũng như tiến trình của bạn từ Hitman 2 trực tiếp vào Hitman 3 miễn là bạn từng chơi và sở hữu các trò chơi này trước đó.

    Hình ảnh – Âm thanh quá đẹp và chi tiết:
Về hình ảnh game chắc khỏi phải chê vì quang cảnh hiện lên quá chi tiết với những hình ảnh cùng màu sắc tươi sáng, chân thực nhất. Âm thanh cũng là điểm cộng lớn khi được lồng ghép hiệu ứng quá chi tiết. Chỉ nghe thôi các bạn cũng đủ thấy như đang nhập vai vào câu chuyện được kể trong Hitman 3 vậy.

    Cấu hình chạy Hitman 3
Về cấu hình chạy Hitman 3 thì bạn cũng khỏi lo vì game yêu cầu không quá cao khi Ram 8G và 1 card rời với Vram 2G là đã đủ để chạy game. Test thử trên GT730 của Nvidia thì cũng khá ngon ở mức setting thấp nhé, nhưng bạn cần 1 CPU Core I5 đời thứ 2 trở lên để có thể gánh tốt game
    """,
    """
    Cốt truyện hấp dẫn
Nói đến Cyberpunk 2077 là các bạn sẽ mường tượng ra 1 tựa game thế giới mở vô cùng hào nhoáng. Hơn nữa đây còn là một câu chuyện phiêu lưu hành động, thế giới mở lấy bối cảnh ở Thành phố đêm, một siêu đại nhân
bị ám ảnh bởi sức mạnh, sự quyến rũ và sự thay đổi cơ thể. Bạn vào vai V, một lính đánh thuê sống ngoài vòng pháp luật đang theo đuổi một bộ phận cấy ghép độc nhất vô nhị, chìa khóa dẫn đến sự bất tử. Bạn có thể tùy chỉnh phần mềm điều khiển mạng, bộ kỹ năng và lối chơi của nhân vật, đồng thời khám phá một thành phố rộng lớn, nơi những lựa chọn bạn đưa ra sẽ định hình câu chuyện và thế giới xung quanh bạn.

    Gameplay hấp dẫn:
Là một tựa game lấy bối cảnh viễn tưởng tương lai, hệ thống vũ khí trong Cyberpunk 2077 cũng có nhiều điểm đặc biệt, rất khác với những tựa game bắn súng thông thường. Ngoài các loại vũ khí quen thuộc như súng ngắn cầm tay, awp, shotgun, phóng lựu… Cyberpunk 2077 còn có cả những vũ khí của tương lai như súng thông minh, đạn tự truy đuổi hay các loại hỏa lực tự gắn vào cơ thể… Với hệ thống vũ khí đặc biệt như vậy, Cyberpunk 2077 chắc chắn sẽ đem đến nhiều thú vị cho người chơi.

    Điểm mình thích nhất ở tựa game này đó chính là tính năng tùy chỉnh cho nhân vật của mình do nhà sản xuất đưa ra. Từ vóc dáng, màu ra, khuôn mặt, kiểu tóc cho đến màu mắt, chiều dài chân và cả số đo 3 vòng. Hơn nữa game cho mình tùy chỉnh cả răng của nhân vật nữa đấy ạ. Nghe có vẻ buồn cười nhỉ nhưng bạn cần chơi mới thấy phải tùy chỉnh từng chi tiết nhỏ như thế mới tạo nên cá tính riêng của từng nhân vật được chứ

    Có 1 điều thú vị mà mình biết được đó chính là trong Cyberpunk 2077 sẽ có hẳn một con phố “đèn đỏ” được gọi là Jig Jig Street, nơi đường phố tràn ngập đôi trai gái, cả nam và nữ, tất cả đều khơi gợi nhân vật chính một đêm mặn nồng. Và thậm chí, nếu người chơi cho phép nhân vật chính V làm “chuyện ấy” tại Jig Jig Street, người chơi thậm chí còn được xem những phân cảnh khá nóng bỏng tại đây. Không chỉ vậy, các cửa hàng trên phố Jig Jig còn bán tất cả các loại đồ chơi người lớn và thậm chí người chơi có thể mua được.

    Nếu các bạn chưa biết nữa thì Cyberpunk 2077 còn có rất nhiều loại xe khác nhau và được chia thành nhiều lớp xe, một số mẫu xe trông giống như thiết kế tiên tiến của xe hơi trong thế giới thực ngày nay.

    Về Đồ họa game:
Nếu các bạn có ý định trải nghiệm boom tấn này thì chỉ cần tới một CPU Core i5 thế hệ thứ 3 i5-3570k kèm theo 8GB RAM và một chiếc card đồ họa cũ như Nvidia GTX 780 3GB hay AMD Radeon RX 470 là đã có thể chơi được một cách mượt mà nhưng chất lượng hình ảnh không được đẹp và chi tiết. Dung lượng ổ cứng yêu cầu sẽ chỉ cần 70GB nhưng đó phải là ổ cứng SSD. Còn nếu muốn chơi bom tấn Cyberpunk 2077 ở mức thiết đặt đồ họa cao nhất, Max Setting 1080p60fps, các bạn cũng sẽ chỉ cần một CPU Core i7-4790 với 4 nhân 8 luồng hay chỉ cần một CPU giá rẻ AMD là Ryzen 3 3200G đã có thể chiến mượt. Yêu cầu về bộ nhớ thì chỉ cần 12GB RAM và chiếc card đồ họa quốc dân Nvidia GTX 1060 6GB là đã có thể thoải mái chơi bom tấn Cyberpunk 2077 rồi nhé.
    """,
    """
    Cốt truyện cực cuốn hút
Cốt truyện Breath of the Wild sẽ cho chúng ta nhập vai vào hiệp sĩ Link, người đã được thức tỉnh sau 100 năm để đánh bại chúa quỷ Calamity Ganon trước khi binh đoàn quỷ dữ của hắn hủy diệt vương quốc Hyrule kỳ ảo. Ngoài ra với phiên bản Breath of the Wild này sẽ mang các bạn đến vương quốc Hyrule. Nơi này đang phải gồng mình chống lại thế lực quỷ dữ Calamity Ganon. Mỗi lần Ganon phát động các cuộc tấn công, binh đoàn quỷ của hắn luôn bị đánh bại bởi Công chúa Zelda, người thừa kế sức mạnh vĩ đại đến từ Nữ thần Hylia cùng sự trợ giúp của các hiệp sĩ dũng mãnh.

Mình sẽ nói kĩ hơn cho các bạn thấy cốt truyện game hấp dẫn ra sao khi trải qua nhiều thời đại, vương quốc Hyrule đã xây dựng nên một nền văn minh tiên tiến. Bằng cách sử dụng công nghệ kỹ thuật hiện đại, họ quyết định tạo ra 4 cỗ máy khổng lồ có hình dạng giống động vật để hợp nhất sức mạnh chống lại chúa quỷ Ganon, 4 cỗ máy này có tên gọi là Divine Beast. Bên cạnh Divine Beast còn có một lực lượng vũ trang tự động khác được gọi là Guardian. 4 Hiệp sĩ mạnh nhất được trao danh hiệu Anh hùng và có quyền điều khiển Divine Beast để tấn công chúa quỷ Ganon.
    """,
    """
    Cốt truyện hấp dẫn
ARK: Survival Evovled là một tựa game lấy đề tài sinh tồn khá hấp dẫn. Game lấy bối cảnh vào thời tiền sử, khi con người sẽ phải cùng chung sống với lũ khủng long gớm ghiếc.Trong ARK: Survival Evovled, sẽ không chỉ có các loài khủng long mà bên cạnh đó, người chơi còn sẽ phải đối mặt với các loài sinh vật khác, ví dụ như những con voi Ma Mút, những con hổ nanh dài sẵn sàng tấn công người chơi khi di chuyển lại gần.
 
    Gameplay hấp dẫn:
Ngay từ đầu trò chơi, người chơi sẽ được chào đón với phần tùy biến nhân vật quen thuộc. Sau khi kết thúc việc tạo nhân vật là bạn vào thẳng trò chơi. Ark: Survival Evolved bắt đầu với màn hướng dẫn khá chi tiết, hướng dẫn người chơi phải bắt đầu sinh tồn như thế nào sau khi nhân vật thức dậy ở một hòn đảo hoang vắng. Điều đáng khen là thay vì siết chặt trải nghiệm sinh tồn và buộc bạn phải lao đầu vào cuộc sinh tồn trước mắt, trò chơi dành khá nhiều thời gian để người chơi bắt đầu khám phá và làm quen với thế giới trong đó ít nhất vài tiếng trải nghiệm ban đầu.

Đầu tiên, nhiệm vụ của người chơi sẽ là cố gắng thật nhanh chế tạo ra các loại vũ khí, dụng cụ cơ bản như rìu chặt cây, rìu chặt đá, đơn giản vì khi dùng tay để chặt cây, người chơi sẽ bị thương. Danh sách các loại vật phẩm, trang bị có thể thu lượm và chế tạo được liệt kê rõ ràng để người chơi tiến hành thu thập.
    """,
    #15->20
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi DOOM Eternal: The Ancient Gods. Đánh giá DOOM Eternal: The Ancient Gods là tựa game hành động, phiêu lưu – mô phỏng hay và hấp dẫn. Cốt truyện DOOM Eternal: The Ancient Gods thì game sẽ mang đến cho người chơi “cái kết hoành tráng cho câu chuyện của Doom Slayer”. “Bạn đã phủ nhận các vị thần và đánh thức một cái ác cổ đại từ xa xưa” đó cũng là cốt truyện mở đầu đến từ Studio phát triển Doom Eternal chia sẻ.. “Lúc này việc tập hợp các đội quân Sentinel đã được triển khai, họ bao vây pháo đài cuối cùng của Địa ngục, phá vỡ các bức tường của pháo đài và đối mặt với chính Dark Lord’s.

    Gameplay hấp dẫn
Nói về gameplay DOOM Eternal: The Ancient Gods thì đối mặt với những biến thể mới, chết chóc của ma quỷ. Nam tước Thiết giáp mặc áo giáp đặc biệt và sử dụng đòn tấn công bằng nắm đấm tích điện. Stone Imp sở hữu lớp ẩn nấp gần như bất khả xâm phạm và thích cận chiến. Screecher là một thây ma có khả năng truyền sức mạnh cho những con quỷ xung quanh khi bị giết. The Cursed Prowler là một dạng đột biến với những chiếc móng vuốt có nọc độc và bị nguyền rủa. Khai thác điểm yếu của họ để tiêu diệt chúng.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Uncrashed FPV Drone Simulator. Đánh giá Uncrashed FPV Drone Simulator là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Uncrashed FPV Drone Simulator thì từ những phi công không có kinh nghiệm thực tế đến những phi công có kinh nghiệm muốn nâng cao kỹ năng của mình, Uncrashed sẽ mang đến cho bạn cơ hội lái máy bay không người lái FPV trong một mô phỏng thực tế, đẹp mắt. Thực hiện cuộc đua đến cấp độ tiếp theo mà không có nguy cơ phá vỡ máy bay không người lái hoặc tài khoản ngân hàng của bạn.

    Gameplay hấp dẫn
Nói về gameplay Uncrashed FPV Drone Simulator thì cho dù là dành cho huấn luyện tự do hay đua, nhiều bản đồ lớn và đa dạng đã được thiết kế bởi một nhóm có kiến ​​thức FPV sâu rộng để mang đến cho bạn trải nghiệm bay tốt hơn. Từ công viên đến những nơi bỏ hoang tốt nhất, bạn chưa bao giờ nhìn thấy những điểm tuyệt đẹp như vậy dành cho máy bay không người lái FPV.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Shelter Manager. Đánh giá Shelter Manager là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Shelter Manager thì chúng ta đang sống trong một thế giới đầy rắc rối. Virus, xung đột quân sự – bạn không bao giờ biết được thế giới sẽ phải đối mặt với nguy cơ nào vào ngày mai. Đã đến lúc chuẩn bị ngay! Lãnh đạo một mạng lưới boongke và bắt đầu phát triển xã hội sau thảm họa toàn cầu.

    Gameplay hấp dẫn
Nói về gameplay Shelter Manager thì từ một cuộc chiến tranh hạt nhân đến đại dịch toàn cầu hoặc cuộc tấn công thiên thạch, hãy chọn kịch bản ngày tận thế của bạn trong một hộp cát mở rộng. Trong chế độ chiến dịch, bạn sẽ học cách sống sót. Chọn từ một số nhiệm vụ để tìm hiểu cách điều hành một boongke hiệu quả. Xây dựng các hầm trú ẩn dưới lòng đất được trang bị tất cả các tiện nghi hiện đại để sống sót sau ngày tận thế. Bạn sẽ cần nhiều loại vật phẩm để tồn tại trong thế giới khắc nghiệt bên ngoài. Yêu cầu những người định cư của bạn cướp phá và cướp phá các boongke khác để mang về nhà tất cả các loại vật tư thiết yếu.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Stonedeep. Đánh giá Stonedeep là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Stonedeep thì đây là một công cụ xây dựng thành phố ngầm 2,5D. Người lùn thu thập tài nguyên, xây dựng và chống lại quái vật. Các thuộc địa có thể chuyên môn hóa về văn hóa, sản xuất, quân sự và buôn bán. Khi bắt đầu, người lùn cần đồ uống và nghỉ ngơi.

    Gameplay hấp dẫn
Nói về gameplay Stonedeep thì đào sâu vào lòng đất và tìm các nguồn tài nguyên để xây dựng và phát triển vương quốc của bạn. Nền văn minh của bạn càng phát triển, bạn càng phải mở rộng đường hầm của mình. Stonedeep hiện bao gồm hơn 80 tài nguyên, 5 quần xã sinh vật khác nhau, hơn 70 tòa nhà, 9 cấp độ văn minh và 8 loại kẻ thù với các biến thể khác nhau và 4 loài động vật.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Nine Parchments. Đánh giá Nine Parchments là tựa game hành động, phiêu lưu – chặt chém hay và hấp dẫn. Cốt truyện Nine Parchments thì đây là một trò chơi nổ tung hợp tác về tình trạng lộn xộn ma thuật từ Frozenbyte, những người sáng tạo ra loạt phim Trine!Các pháp sư tập sự của Runaway nắm bắt cơ hội để hoàn thành cuốn sách thần chú của họ bằng cách truy tìm Nine Parchments bị mất.

    Gameplay hấp dẫn
Nói về gameplay Nine Parchments thì vì các pháp sư tương lai sẽ nhanh chóng có được những phép thuật mới mạnh mẽ mà không cần học các biện pháp an toàn thích hợp, quá trình tiến bộ vội vàng của họ tự nhiên dẫn đến nhiều tai nạn chết người …Nine Parchments kết hợp hành động bắn bùa chú trong thời gian thực với các yếu tố RPG – nâng cấp nhân vật của bạn và thu thập chiến lợi phẩm ma thuật, lấp đầy tủ quần áo của bạn với vô số mũ phù thủy và cây gậy mạnh mẽ.
    """,
    #20->25
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Invisigun Reloaded. Đánh giá Invisigun Reloaded là tựa game hành động, phiêu lưu – chiến thuật hay và hấp dẫn. Cốt truyện Invisigun Reloaded thì thử thách bản thân trong Hành trình của anh hùng: các chiến dịch anh hùng được điều chỉnh riêng với các phòng giải đố, thử thách kỹ năng và đấu trùm. Các khả năng độc đáo có toàn bộ hành trình được xây dựng đặc biệt để dạy bạn sử dụng đúng cách chơi của anh hùng đó – tất cả trong khi nghệ thuật tàng hình và thành thạo di chuyển trở thành bản chất thứ hai.

    Gameplay hấp dẫn
Nói về gameplay Invisigun Reloaded thì với 12 anh hùng khác nhau – mỗi anh hùng có khả năng riêng biệt – có một chiến lược hoàn hảo cho mọi lối chơi. Từ lén lút tỉ mỉ đến hung hãn tàn nhẫn, hãy tìm khả năng yêu thích của bạn và gây sốc cho bạn bè khi bạn xuất hiện ngoài luồng gió mỏng và khiến họ bất ngờ!
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Gas Station Simulator. Đánh giá Gas Station Simulator là game hành động, phiêu lưu – mô phỏng cực hay. Cốt truyện Gas Station Simulator thì mua một trạm xăng bị bỏ hoang và khôi phục lại nó về thời kỳ huy hoàng. Cải tạo, nâng cấp và mở rộng các dịch vụ được cung cấp để đáp ứng nhu cầu của khách hàng.

    Gameplay hấp dẫn
Nói về gameplay Gas Station Simulator thì Gas Station Simulator là tất cả về việc cải tạo, mở rộng và vận hành một trạm xăng dọc theo đường cao tốc ở giữa sa mạc. Tự do lựa chọn và nhiều cách tiếp cận để điều hành doanh nghiệp của bạn và đối phó với áp lực là những thành phần quan trọng trong trò chơi này. Bạn có thể mở rộng trạm xăng của mình để có thể phục vụ được nhiều khách hàng hơn. Ngoài ra, một trạm xăng không chỉ là nơi bán nhiên liệu. Bạn có thể mở rộng phạm vi dịch vụ mà bạn cung cấp cho khách hàng và do đó thu hút ngày càng nhiều khách hàng đa dạng hơn.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Force of Nature. Đánh giá Force of Nature là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Force of Nature thì là một trò chơi Sandbox kết hợp các thể loại Hành động, Phiêu lưu, Nhập vai, Chiến lược và Quản lý.

    Gameplay hấp dẫn
Nói về gameplay Force of Nature thì người chơi sẽ khám phá hơn 10 khu khác nhau, mỗi khu đều có hệ động thực vật độc đáo. Bạn có thể thu thập và khai thác tài nguyên, tạo vũ khí và quần áo, xây nhà, các bàn chế tạo khác nhau, phòng thí nghiệm và mài giũa nhân vật của mình. Tìm kiếm các loại cây có ích, trồng chúng trên luống hạt và thuần hóa động vật để có được nguồn cung cấp thức ăn ổn định. Xây dựng các cổng để di chuyển nhanh hơn trên khắp thế giới và sử dụng bản đồ để không bị lạc.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Crashlands. Đánh giá Crashlands là tựa game hành động, phiêu lưu – kinh dị hay và hấp dẫn. Cốt truyện Crashlands thì Crashlands mang câu chuyện đầy màu sắc diễn ra giữa vũ trụ bao la rộng lớn. Ở đó, game thủ sẽ song hành với nữ phi công tên Flux – nhân viên thuộc biên chế Cục vận chuyển thiên hà. Trong một chuyến đưa hàng hóa, Flux bất ngờ bị chặn lại bởi một thực thể quái lạ và khiến con tàu nổ tung trong khi cô phải hạ cánh khẩn xuống hành tinh bên dưới. Độc thân giữa thế giới hoang dã, nay Flux sẽ phải làm mọi thứ để sống sót và chờ đợi cậu viện…

    Gameplay hấp dẫn
Nói về gameplay Crashlands thì lối chơi của Crashlands sẽ đặt game thủ vào một thế giới rộng lớn với quyền chu du tự do mọi lúc mọi nơi. Ở đó, nhiệm vụ duy nhất mà chúng ta phải hướng tới là xây dựng trạm phát sóng nhằm gửi đi tín hiệu cầu viện. Nhưng mọi chuyện không đơn giản đến thế vì nay Flux không có bất cứ công nghệ tân tiến nào trong tay và mọi công cụ hỗ trợ đều đã nổ tan tành cùng con tàu không gian.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Mount & Blade II: Bannerlord. Đánh giá Mount & Blade II: Bannerlord là tựa game hành động chặt chém thế giới mở cực hay và được rất nhiều người yêu thích. Mount & Blade II: Bannerlord lấy bối cảnh 200 năm trước những sự kiện của phiên bản đầu tiên. Trò chơi xuyên suốt thời kỳ suy tàn của Đế quốc Calradian và sự thành lập các vương quốc vốn đã từng xuất hiện trong những phiên bản trước đây. Quá trình suy vong của Đế quốc Calradian cũng tương tự như sự sụp đổ của Đế quốc La Mã và sự hình thành của các vương quốc sơ khai ở Trung Đông, Bắc Phi và châu Âu. Áo giáp, vũ khí và kiến trúc lấy cảm hứng từ năm 600 đến năm 1100.

    Gameplay hấp dẫn:
Nói về gameplay thì bạn sẽ có rất nhiều phe phái lớn nhỏ khi nhà sản xuất ưu ái tới sáu phe phái chính, mỗi bên bao gồm các gia tộc thù nghịch với những mục tiêu của riêng họ, cũng như các phe nhóm vũ trang như lính đánh thuê. Các phe cánh Northern, Western, và Southern Empire đều sử dụng một đội hình cần bằng gồm toàn kỵ binh nặng, lính cầm giáo và cung thủ. Nếu như bạn chưa biết thì Mount & Blade II: Bannerlord phiên bản mới đã bao gồm các tính năng mới như xây dựng thành phố theo thời gian thực, công thành và chế đồ. Cử động của quân lính cũng được mô phỏng lại bằng công nghệ mo-cap khiến cho các trận chiến trở nên chân thực hơn trước.

Ngoài ra bạn sẽ được tham gia chiến trường và trải nghiệm sự tàn khốc của cuộc chiến thời trung cổ ở góc nhìn thứ nhất hoặc thứ ba với hàng trăm đơn vị trên màn hình, mỗi đơn vị đều có AI chi tiết của riêng chúng. Một điểm mình khá thích đó chính là hình ảnh game đã đẹp và lôi cuốn người chơi đến lạ lùng. Khi bạn đẩy cao độ phân giải thì ôi thôi tất cả chi tiết quần áo nhân vật hiển thị sắc nét. Game cũng được ưu ái khi nhà sản xuất làm riêng bộ âm thanh độc quyền, giúp cho khi chơi tạo cảm hứng rất nhiều, nhất là những trận chiến ngoài sa trường.
    """,
    #25->30
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Tales of Arise. Đánh giá Tales of Arise là một game hành động, phiêu lưu – chặt chém hay và hấp dẫn. Cốt truyện Tales of Arise thì Tales of Arise là phiên bản thứ 17 trong loạt game đình đàm Tales. Ngoài 2 nhân vật chính Alphen và Shionne, bạn sẽ gặp nhiều nhân vật khác và có thể mời họ vào đội của mình. Một số nhân vật tiêu biểu có thể kể tên như Rinwell – pháp sư quyền năng, Law – chiến binh mạnh mẽ, Dohalim – khả năng điều khiển kỹ thuật, khống chế thần kinh và thích nghi tốt trước mọi đối thủ, Kisara – nữ chiến binh sử dụng rìu và khiên điêu luyện. Tales of Arise lấy bối cảnh hai thế giới Dahna thời trung cổ và Rena tân tiến bị chia cắt. Nhờ sự phát triển vượt trội về công nghệ và phép thuật, Rena tự cho phép họ nắm quyền sinh sát thế giới Dahna trong tay, cướp lấy tài nguyên và xem người dân ở đây như nô lệ.

    Gameplay hấp dẫn
Nói về gameplay Tales of Arise thì người chơi có thể điều khiển được trong Tales of Arise, bao gồm Alphen, Shionne, Rinwell và cuối cùng là Law. Alphen có thể nói là một kiếm sĩ có khả năng sử dụng hai thanh kiếm (một thanh kiếm lửa và một thanh kiếm thường) cùng một lúc để tung ra những đòn chặt chém cực kỳ nguy hiểm. Tiếp đến là Shionne, một cô nàng xinh đẹp bị nguyền rủa bởi một thứ gọi là “Thorn”. Nhân vật thứ ba trong Tales of Arise là nàng phù thuỷ Rindwell. Và cuối cùng là Law, một võ sư chuyên nghiệp kiêm thành viên của Biệt đội Cảnh sát Bí mật tên là Bull’s Eye.Có rất nhiều cải tiến và thay đổi trong cơ chế chiến đấu của Tales of Arise so với những phiên bản trước. Mặc dù chỉ có 4 nhân vật ở trong một trận chiến, tuy nhiên bạn có thể gọi đòn tấn công phụ trợ từ cả 6 nhân vật (tính cả nhân vật đang điều khiển luôn) mỗi khi thanh tấn công phụ trợ đầy. Trò chơi cũng đưa vào một số cơ chế mới lạ như đòn kết liễu địch thủ, hay cơ chế “tích nộ”, khi nhân vật chính anh chàng Alphen của chúng ta có thể đổi máu để gây thêm sát thương cho địch.

    Cấu hình chơi Tales of Arise
Để chạy được game này bạn cần cài đặt Win 10 64bit và 1 card rời Vram 2G để có thể chạy mượt mà nhé. Ngoài ra bạn cũng cần có 1 CPU Core i5 đời thứ 2 trở lên để có thể chạy được.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Titanfall 2 Ultimate Edition. Đánh giá Titanfall 2 Ultimate Edition là tựa game hành động, phiêu lưu – bắn súng hay và hấp dẫn. Cốt truyện Titanfall 2 Ultimate Edition thì câu chuyện về tay súng Jack Cooper, người bất ngờ bị kẹt lại trên hành tinh Typhon sau khi phi thuyền của anh bị phục kích bất ngờ bởi tập đoàn quân hắc ám mega-corp IMC.Ở phần chơi này, người xem sẽ được chứng kiến mối quan hệ “bất đắc dĩ” nhưng đầy gắn bó giữa bộ đôi người lính Jack Cooper và cỗ máy Titan khổng lồ BT-7274. Một người sống với ước mơ trở thành Pilot, một cỗ máy vừa mất đi Pilot cũ của mình, cả hai sẽ phải phối hợp cùng nhau và bất chấp hiểm nguy để tồn tại.

    Gameplay hấp dẫn
Nói về gameplay Titanfall 2 Ultimate Edition thì Titanfall 2 vẫn giữ nguyên lối chơi đã tạo nên thành công ở phiên bản trước, đó là hành động tốc độ cao với những pha Parkour, đu tường, nhảy cao (Double Jump) cùng với việc sử dụng những Titan với các kỹ năng khác nhau tùy loại. Titanfall 2 cũng có những cải tiến về mặt lối chơi và đồ họa. Giờ đây, số lượng Pilot cũng như Titan được gia tăng đáng kể, với những điểm mạnh và điểm yếu khác nhau tạo nên sư đa dạng trong chiến thuật. Tốc độ di chuyển của nhân vật cũng được thay đổi cho phù hợp với người mới. Bên cạnh những màn đấu súng nảy lửa, những robot khổng lồ với tên gọi Titan cũng là một điểm nhấn không thể bỏ qua của Titanfall 2. Sẽ có 6 loại Titan đồng hành cũng bạn trong game. Không chỉ khác nhau về tên gọi, ngoại hình hay vũ khí, sáu Titan trong Titanfall 2 còn có cho mình sự khác biệt trong cả bốn kĩ năng tấn công (ordnance), chiến thuật (tactical), phòng ngự (defensive) và đặc biệt (core). Không gì khác, đây chính là những yếu tố chính yếu tạo nên sức mạnh của các Titan cũng như quyết định đâu sẽ là người bạn to con lý tưởng nhất của bạn trong game.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi LEGO BUILDERS JOURNEY. Đánh giá LEGO BUILDERS JOURNEY là tựa game hành động, phiêu lưu hấp dẫn. Cốt truyện LEGO BUILDERS JOURNEY là cuộc hành trình Builder’s Journey là một câu đố thú vị trong thế giới của LEGO®, chứa đầy các chi tiết LEGO® được render rất chuẩn và chưa từng ra mắt trên màn ảnh rộng. Thật tuyệt vời khi được trải nghiệm một thế giới ngoạn mục với đủ loại khối gạch trên các bản nhạc nền êm dịu.

    Gameplay hấp dẫn
Nói về gameplay LEGO BUILDERS JOURNEY thì nguời chơi được dẫn dắt bằng giọng kể truyền cảm, game sẽ có nhiều cung bậc cảm xúc, thử thách và cả các màn ăn mừng chiến thắng. Hãy dành thời gian để khám phá, và quan trọng hơn cả, trải nghiệm chơi Builder’s Journey chính là con đường để tìm hiểu xem chúng ta là ai và đóng vai trò gì.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Valiant Hearts The Great War. Đánh giá Valiant Hearts The Great War là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Valiant Hearts The Great War thì hôm nay mình sẽ hướng dẫn các bạn tải và cài đặt Việt Hóa tựa game được đánh giá thang điểm 10/10 trong mọi bảng xếp hạng đó chính là tựa game như các bạn đang nhìn trên màn hình đây. Game kể lại hành trình của năm con người những tưởng không quen biết, nhưng vì một mục đích cao cả mà đã chung tay kết nối hai nửa trái tim xa cách bởi những cuộc chiến lạnh lùng vô cảm. Họ là Emile – một người nông dân Pháp, đầu quân để tìm lại con rể lưu lạc nhưng vô tình rơi vào tay quân Đức. George – Phi công thuộc quân đội Anh, người nói dối rằng mình biết lái máy bay. Freddie – Anh chàng lính Mỹ liều lĩnh xông pha biển lửa với ánh mắt luôn hướng về linh hồn người vợ quá cố. Ana – cô lính cứu thương mang lòng bao dung, luôn phải chứng kiến những bi kịch về cái chết. Sau cuối là Karl, nhân vật chính trong mối tình chia ly, người mà cô con gái của Emile mong mỏi ngày về.

    Gameplay hấp dẫn
Nói về gameplay Valiant Hearts The Great War thì game sẽ đưa người chơi làm quen với phong cách của một tựa game phiêu lưu giải đố, nơi mỗi nhân vật sẽ sở hữu một khả năng chuyên trách cho từng tình huống cụ thể. Bằng cách phối hợp những con người này với nhau, game thủ sẽ cho mình cơ hội tiếp bước trên hành trình rộng mở phía trước. Về mặt câu đố, game hoàn toàn cho thấy tính hợp lý khi đặt ra thử thách cho người chơi, vừa đủ độ khó để động não nhưng không quá phức tạp để phải đứt mạch cốt truyện. Âm thanh tiếp tục là một điểm sáng khác của game với những khúc nhạc nhộn nhịp trước chiến trận, những lời ca buồn khi chuyển màn chơi hay sư trầm ấm trong giọng dẫn chuyện. Bên cạnh đó, những tiếng nói không ra câu chữ khi các nhân vật giao tiếp có lẽ cũng sẽ khiến bạn bật cười vì sự ngây ngô mà họ thể hiện.
    """,
    """
    Cốt truyện hấp dẫn
Hôm nay mình sẽ giới thiệu tới các bạn phiên bản mới nhất của trò chơi Bombernauts. Đánh giá Bombernauts là tựa game hành động, phiêu lưu hay và hấp dẫn. Cốt truyện Bombernauts là một trò chơi chiến đấu nhiều người chơi trực tuyến bùng nổ với địa hình voxel có thể phá hủy hoàn toàn. Ném những quả bom ngu ngốc để thổi bay những người bạn robot của bạn trên thế giới vào dung nham chết chóc bên dưới, nơi họ chắc chắn sẽ chết một cách rực lửa

    Gameplay hấp dẫn
Nói về gameplay Bombernauts thì game sẽ có hơn 100 bản đồ để chơi với các ô đặc biệt thú vị như gỗ dễ cháy, suối nước nóng, băng trượt, bùn dính, và hơn thế nữa. Hàng chục sức mạnh có thể xếp chồng lên nhau để tạo ra những sức mạnh siêu mới độc đáo!

    """,

]

list_producer = [
    # 1-> 5
    "EA Canada",
    "Ubisoft Montreal",
    "Blizzard Entertainment",
    "Ubisoft Toronto",
    "Rockstar North",
    # 5->10
    "Hyperion Studio Limited",
    "KADOKAWA, TSUKURITE",
    "Big Corporation",
    "TechnoBrain",
    "Frogwares",
    # 10-15
    "Bend Studio",
    "IO Interactive A/S",
    "CD PROJEKT RED",
    "Nintendo",
    "Studio Wildcard, Instinct Games",
    #15->20
    "id Software",
    "Louis Rochette",
    "Hamsters Gaming",
    "Direfang",
    "Frozenbyte",
    #20->25
    "Sombr Studio",
    "DRAGO entertainment",
    "A.Y.std",
    "Butterscotch Shenanigans",
    "TaleWorlds Entertainment",
    #25->30
    "BANDAI NAMCO Studios Inc",
    "Respawn Entertainment",
    "Light Brick Studio",
    "Ubisoft Montpellier",
    "Eyebrow Interactive",


    
]

list_publisher = [
    # 1->5
    "Electronic Arts",
    "Ubisoft",
    "Blizzard Entertainment",
    "Ubisoft",
    "Rockstar Games",
    # 5->10
    "Hyperion Studio Limited",
    "0UP GAMES",
    "Grunge Games LTD",
    "TechnoBrain",
    "Frogwares",
    # 10->15
    "PlayStation Mobile, Inc",
    "IO Interactive A/S",
    "CD PROJEKT RED",
    "Nintendo",
    "Studio Wildcard",
    # 15->20
    "Bethesda Softworks",
    "Louis Rochette",
    "Hamsters Gaming",
    "Direfang, Smuttlewerk interactive",
    "Frozenbyte",
    #20->25
    "Sombr Studio",
    "Movie Games S.A., HeartBeat Games",
    "A.Y.std",
    "Butterscotch Shenanigans",
    "TaleWorlds Entertainment",
    #25->30
    "BANDAI NAMCO Entertainment",
    "Electronic Arts",
    "LEGO® Games",
    "Ubisoft",
    "Eyebrow Interactive",
    

]

list_homepage = [
    # 1->5
    "",
    "https://www.epicgames.com/store/en-US/p/assassins-creed-valhalla",
    "",
    "https://www.epicgames.com/store/en-US/p/far-cry-6",
    "https://store.steampowered.com/app/113020/Monaco_Whats_Yours_Is_Mine/",
    # 5->10
    "https://store.steampowered.com/app/794490/Journey_Of_Life/",
    "https://store.steampowered.com/app/1581800/Slow_living_with_Princess/",
    "https://store.steampowered.com/app/434570/Blood_and_Bacon/",
    "https://store.steampowered.com/app/1348390/I_am_an_Air_Traffic_Controller_4/",
    "https://store.steampowered.com/app/241260/Sherlock_Holmes_Crimes_and_Punishments/",
    # 10->15
    "https://store.steampowered.com/app/1259420/Days_Gone/",
    "https://www.epicgames.com/store/en-US/product/hitman-3",
    "https://store.steampowered.com/app/1091500/Cyberpunk_2077",
    "",
    "https://store.steampowered.com/app/346110/ARK_Survival_Evolved/",
    # 15->20
    "https://store.steampowered.com/app/1098293/DOOM_Eternal_The_Ancient_Gods__Part_Two/",
    "https://store.steampowered.com/app/1682970/Uncrashed__FPV_Drone_Simulator/",
    "https://store.steampowered.com/app/1256830/Shelter_Manager/",
    "https://store.steampowered.com/app/1094760/Stonedeep/",
    "https://store.steampowered.com/app/471550/Nine_Parchments/",
    #20->25
    "https://store.steampowered.com/app/375750/Invisigun_Reloaded/",
    "https://store.steampowered.com/app/1149620/Gas_Station_Simulator/",
    "https://store.steampowered.com/app/568570/Force_of_Nature/",
    "https://store.steampowered.com/app/391730/Crashlands/",
    "https://store.steampowered.com/app/261550/Mount__Blade_II_Bannerlord/",
    #25->30
    "https://store.steampowered.com/app/740130/Tales_of_Arise/",
    "https://store.steampowered.com/app/1237970/Titanfall_2/",
    "https://store.steampowered.com/app/1544360/LEGO_Builders_Journey/",
    "https://store.steampowered.com/app/260230/Valiant_Hearts_The_Great_War__Soldats_Inconnus__Mmoires_de_la_Grande_Guerre/",
    "https://store.steampowered.com/app/246920/Bombernauts",

]

list_image = [
    #1->5
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
    # 5->10
    [
        "https://hadoantv.com/wp-content/uploads/2021/02/download-Journey-Of-Life-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/02/download-Journey-Of-Life-hadoan-tv-3.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/02/download-Journey-Of-Life-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/02/download-Journey-Of-Life-hadoan-tv-2.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-slow-living-with-princess-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-slow-living-with-princess-hadoan-tv-1.jpg",   
        "https://hadoantv.com/wp-content/uploads/2021/10/download-slow-living-with-princess-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-slow-living-with-princess-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Blood-and-Bacon-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Blood-and-Bacon-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Blood-and-Bacon-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-I-am-an-Air-Traffic-Controller-4-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-I-am-an-Air-Traffic-Controller-4-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-I-am-an-Air-Traffic-Controller-4-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-I-am-an-Air-Traffic-Controller-4-hadoan-tv-3.jpg",
        
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Sherlock-Holmes-Crimes-and-Punishments-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Sherlock-Holmes-Crimes-and-Punishments-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Sherlock-Holmes-Crimes-and-Punishments-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Sherlock-Holmes-Crimes-and-Punishments-hadoan-tv-3.jpg",
    ],
    #10->15
    [
        "https://hadoantv.com/wp-content/uploads/2021/04/download-Days-Gone-hadoan-tv-808x454.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/04/download-Days-Gone-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/04/download-Days-Gone-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/04/download-Days-Gone-hadoan-tv-3.jpg",
        
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Hitman-3-hadoan-tv-808x454.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Hitman-3-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Hitman-3-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Hitman-3-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Cyberpunk-2077-hadoan-tv-808x454.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Cyberpunk-2077-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Cyberpunk-2077-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Cyberpunk-2077-hadoan-tv-3.jpg",

    ],
    [
        "https://hadoantv.com/wp-content/uploads/2020/12/download-Cyberpunk-2077-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/11/download-THE-LEGEND-OF-ZELDA-BREATH-OF-THE-WILD-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/11/download-THE-LEGEND-OF-ZELDA-BREATH-OF-THE-WILD-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/11/download-THE-LEGEND-OF-ZELDA-BREATH-OF-THE-WILD-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2020/12/download-ARK-Survival-Evolved-hadoan-tv-808x454.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-ARK-Survival-Evolved-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-ARK-Survival-Evolved-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2020/12/download-ARK-Survival-Evolved-hadoan-tv-3.jpg",
    ],
    # 15->20
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-DOOM-Eternal-The-Ancient-Gods-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-DOOM-Eternal-The-Ancient-Gods-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-DOOM-Eternal-The-Ancient-Gods-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-DOOM-Eternal-The-Ancient-Gods-hadoan-tv-3.jpg",

    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Uncrashed-FPV-Drone-Simulator-hadoan-tv-4.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Uncrashed-FPV-Drone-Simulator-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Uncrashed-FPV-Drone-Simulator-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Uncrashed-FPV-Drone-Simulator-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Shelter-Manager-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Shelter-Manager-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Shelter-Manager-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Shelter-Manager-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-stonedeep-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-stonedeep-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-stonedeep-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-stonedeep-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Nine-Parchments-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Nine-Parchments-hadoan-tv-3.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Nine-Parchments-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Nine-Parchments-hadoan-tv-2.jpg",
    ],
    #20->25
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Invisigun-Reloaded-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Invisigun-Reloaded-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Invisigun-Reloaded-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Invisigun-Reloaded-hadoan-tv-3.jpg",
    ],
    [   "https://hadoantv.com/wp-content/uploads/2021/09/download-gas-station-simulator-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/09/download-gas-station-simulator-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/09/download-gas-station-simulator-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/09/download-gas-station-simulator-hadoan-tv-3.jpg",

    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Force-of-Nature-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Force-of-Nature-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Force-of-Nature-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Force-of-Nature-hadoan-tv-3.jpg",

    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Crashlands-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Crashlands-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Crashlands-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Crashlands-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Mount-and-Blade-II-Bannerlord-hadoan-tv-808x454.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Mount-and-Blade-II-Bannerlord-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Mount-and-Blade-II-Bannerlord-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/01/download-Mount-and-Blade-II-Bannerlord-hadoan-tv-3.jpg",
    ],
    #25->30
    [
        "https://hadoantv.com/wp-content/uploads/2021/09/download-Tales-of-Arise-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/09/download-Tales-of-Arise-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/09/download-Tales-of-Arise-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/09/download-Tales-of-Arise-hadoan-tv-3.jpg",

    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Titanfall-2-hadoan-tv-808x454.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Titanfall-2-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Titanfall-2-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Titanfall-2-hadoan-tv-3.jpg",

    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/06/download-LEGO-BUILDERS-JOURNEY-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/06/download-LEGO-BUILDERS-JOURNEY-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/06/download-LEGO-BUILDERS-JOURNEY-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/06/download-LEGO-BUILDERS-JOURNEY-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Valiant-Hearts-The-Great-War-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Valiant-Hearts-The-Great-War-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Valiant-Hearts-The-Great-War-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Valiant-Hearts-The-Great-War-hadoan-tv-3.jpg",
    ],
    [
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Bombernauts-hadoan-tv.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Bombernauts-hadoan-tv-1.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Bombernauts-hadoan-tv-2.jpg",
        "https://hadoantv.com/wp-content/uploads/2021/10/download-Bombernauts-hadoan-tv-3.jpg",
    ],
]
list_releasedate = [
    #1->5
    "30/09/2021",
    "10/11/2020",
    "24/09/2020",
    "07/10/2021",
    "14/04/2015",

    # 5->10
    "15/04/2018",
    "07/10/2021",
    "01/02/2016",
    "15/10/2020",
    "30/09/2014",
    
    #10->15
    "19/05/2021",
    "20/1/2021",
    "10/12/2020",
    "03/03/2017",
    "28/08/2017",

    #15->20
    "18/03/2021",
    "01/09/2021",
    "09/10/2021",
    "11/10/2021",
    "10/10/2021",

    #20->25
    "09/02/2017",
    "15/09/2021",
    "13/12/2016",
    "21/01/2016",
    "30/03/2020",

    #25->30
    "10/9/2021",
    "28/10/2016",
    "22/06/2021",
    "26/06/2014",
    "30/12/2017",

]
list_os = [ 
    # 1->5
    "Windows 10 – 64-Bit",
    "Windows 10 (chỉ 64-bit)",
    "Windows 10",
    "Windows 10 (20H1 or newer) – 64 bit only",
    "Windows 10 64 Bit, Windows 8.1 64 Bit, Windows 8 64 Bit, Windows 7 64 Bit Service Pack 1",
    # 5->10
    "Windows 7 trở lên",
    "Windows 8.1 trở lên",
    "Windows Vista, Windows 7, Windows 8 trở lên",
    "Windows 10 64bit",
    "WINDOWS VISTA SP2/WINDOWS 7/WINDOWS 8",
    # 10->15
    "Windows 10 64-bits",
    "Windows 7/8/10 64bit",
    "Windows 7/8/10 64bit",
    "Windows Vista, 7, 8 Pro+, 10 64bit",
    "Windows® 7, Windows® 8.1, Windows® 10 (64bit)",
    #15->20
    "(64 bit) Windows 10/8/7",
    "Windows 7 64-bit, Windows 8.1, Windows 10",
    "Windows 7/8/10",
    "Windows 7 trở lên",
    "(64 bit) Windows 10/8/7",
    #20->25
    "Windows XP SP2+ trở lên",
    "Windows 7 (64-bit) or 10 (64-bit)",
    "Windows XP, Vista, 7, 8/8.1, 10",
    "Windows 8 / 8.1, 10",
    "Windows 7, 8, 10 64bit",
    #25->30
    "Windows 10 (Chỉ 64-bit)",
    "Win 7/8/8.1/10 64bit",
    "Windows 10",
    "Windows XP SP3 or Windows Vista SP2 or Windows 7 SP1 or Windows 8 (both 32/64bit versions)",
    "Windows 7 trở lên",


]
list_processor = [
    # 1->5
    "Intel Core i3-6100 @ 3.7GHz or AMD Athlon X4 880K @4GHz",
    "AMD R9 380 – 4GB / GeForce GTX 960 4GB",
    "Intel Core i3-3250 / AMD FX-4350",
    "AMD Ryzen 3 1200 – 3.1 GHz / Intel i5-4460 – 3.2 GHz",
    "Intel Core 2 Quad CPU Q6600 @ 2.40GHz (4 CPUs) / AMD Phenom 9850 Quad-Core Processor (4 CPUs) @ 2.5GHz",
    # 5->10
    "Intel Core i5 2500k / AMD FX 4100",
    "Intel Core i3-4340 or above",
    "1.2 GHz Pentium 4 Minimum",
    "Intel 4th Gen Core i3 2.4GHz",
    "AMD/INTEL DUAL-CORE 2.4 GHZ",
    # 10->15
    "Intel Core i5-2500K@3.3GHz or AMD FX 6300@3.5GHz",
    "Intel CPU Core i5-2500K 3.3GHz / AMD CPU Phenom II X4 940",
    "Intel Core i5-3570K or AMD FX-8310",
    "1.2GHZ CPU",
    "Intel Core i5-2400/AMD FX-8320 or better",
    # 15->20
    "Intel Core i5 @ 3.3 GHz or better, or AMD Ryzen 3 @ 3.1 GHz or better",
    "Intel Core i5 2.6Ghz or better",
    "1.8 GHz",
    "Intel(R) Core(TM) i7-6567U CPU @ 3.30GHz 3.30 GHZ",
    "CPU Intel Core i3 / i5 / i7 1,8 GHz lõi kép. AMD 2.0 GHz lõi kép.",
    #20->25
    "Intel Core™ Duo+ (SSE2)",
    "Intel Core i3 3.0 GHz",
    "1.6GHz+",
    "2.0 Ghz",
    "Intel® Core ™ i3-8100 / AMD Ryzen ™ 3 1200",
    #25->30
    "Intel Core i5-2300 hoặc AMD Ryzen 3 1200",
    "Intel Core i3-6300t or equivalent [4 or more hardware threads]",
    "Intel Core i3-3470 / AMD FX-8350 or equivalent",
    "Intel Pentium IV 630 @ 3.0 GHz or AMD Athlon64 3000 + @ 1.8 GHz",
    "Core 2 Duo",




]
list_graphic = [
    # 1->5
    "Nvidia GTX 1650 Vram 4G", 
    "Ryzen 3 1200 – 3,1 Ghz / i5-4460 – 3,2 Ghz",
    "Nvidia GTX 660 / AMD Radeon HD 7850",
    "AMD RX 460 (4 GB) / Nvidia GTX 960 (4 GB)",
    "NVIDIA 9800 GT 1GB / AMD HD 4870 1GB (DX 10, 10.1, 11)",
    #5->10
    "GTX 960 / AMD R9 Fury",
    "OpenGL compatible, VRAM 1 GB or above",
    "Shader Model 3.0, Direct3D , Hardware Acceleration",
    "Intel HD Graphics 4400 series",
    "256 MB 100% DIRECTX 9 COMPATIBLE AMD RADEON HD 3850/NVIDIA GEFORCE 8600 GTS OR HIGHER",
    #10->15
    "Nvidia GeForce GTX 780 (3 GB) or AMD Radeon R9 290 (4 GB)",
    "NVIDIA GeForce GTX 660 / Radeon HD 7870",
    "NVIDIA GeForce GTX 780 or AMD Radeon RX 470",
    "Card On HD4000",
    "NVIDIA GTX 670 2GB/AMD Radeon HD 7870 2GB or better",
    #15->20
    "NVIDIA GeForce GTX 1050Ti (4GB), GTX 1060 (3GB), GTX 1650 (4GB) or AMD Radeon R9 280(3GB), AMD Radeon R9 290 (4GB), RX 470 (4GB)",
    "GTX770 – 2GB video card memory",
    "Card On HD4000",
    "Intel(R) Iris(R) Graphics 550",
    "RAM 1 GB Video – NVIDIA GeForce 500 Series / Radeon HD 6000 Series",
    #20->25
    "DirectX / OpenGL, 512+ MB VRAM",
    "NVidia GeForce GTX 660 2GB VRAM",
    "256 Mb Video Memory, Shader Model 3.0",
    "Bộ nhớ video 128mb",
    "Intel® UHD 630 / NVIDIA® GeForce® GTX 660 2GB / AMD Radeon ™ HD 7850 2GB",
    #25->30
    "GeForce GTX 760 hoặc Radeon HD 7950",
    "NVIDIA Geforce GTX 660 2GB or AMD Radeon HD 7850 2GB",
    "NVIDIA GeForce GTX 960 / Radeon R7 260X",
    "nVidia GeForce 8800 GT or AMD Radeon HD2900 XT (512MB VRAM)",
    "Discreet video card, Shader Model 3+",

]


list_ram = [
    #1->5
    "8GB RAM",
    "2GB RAM",
    "4GB RAM",
    "8GB RAM",
    "1GB RAM",
    #5->10
    "4GB RAM",
    "8GB RAM",
    "1GB RAM",
    "8GB RAM",
    "2GB RAM",
    #10->15
    "8GB Ram",
    "8GB RAM",
    "8GB RAM",
    "4GB RAM",
    "8GB RAM",
    #15->20
    "8GB RAM",
    "4GB RAM",
    "6GB RAM",
    "6GB RAM",
    "4GB RAM",
    #20->25
    "2GB RAM",
    "4GB RAM",
    "2GB RAM",
    "2.5GB RAM",
    "6GB RAM",
    #25->30
    "8GB RAM",
    "8GB RAM",
    "8GB RAM",
    "2GB RAM",
    "4GB RAM",

]   
list_storage = [
    #1->5
    "70GB chỗ trống khả dụng",
    "80GB chỗ trống khả dụng",
    "70GB chỗ trống khả dụng",
    "10GB chỗ trống khả dụng",
    "220GB chỗ trống khả dụng",
    #5->10
    "5GB chỗ trống khả dụng",
    "1GB chỗ trống khả dụng",
    "4GB chỗ trống khả dụng",
    "3GB chỗ trống khả dụng",
    "14GB chỗ trống khả dụng",
    #10->15
    "70GB chỗ trống khả dụng",
    "80GB chỗ trống khả dụng",
    "70GB chỗ trống khả dụng",
    "10GB chỗ trống khả dụng",
    "220GB chỗ trống khả dụng",
    #15->20
    "80GB chỗ trống khả dụng",
    "22GB chỗ trống khả dụng",
    "2GB chỗ trống khả dụng",
    "5GB chỗ trống khả dụng",
    "7GB chỗ trống khả dụng",
    #20->25
    "5GB chỗ trống khả dụng",
    "10GB chỗ trống khả dụng",
    "5GB chỗ trống khả dụng",
    "5GB chỗ trống khả dụng",
    "60GB chỗ trống khả dụng",
    #25->30
    "45GB chỗ trống khả dụng",
    "50GB chỗ trống khả dụng",
    "5GB chỗ trống khả dụng",
    "2GB chỗ trống khả dụng",
    "2GB chỗ trống khả dụng",
] 
# create game & requirement
for i in range(len(list_name)) :  
    r = Requirement(
        os = list_os[i],
        storage = list_storage[i],
        ram = list_ram[i],
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
        release_date = datetime.strptime(list_releasedate[i] , "%d/%m/%Y").date(),
        requirement_id = r,
        images = list_image[i]
        )
    g.save()
User.objects.create(full_name="Đôn Khánh Duy" , user_name = "duydon" , pass_word=hashlib.md5("duydon".encode()).hexdigest() , created_at=datetime.now())
User.objects.create(full_name="Trần Hoàng Long" , user_name = "longtran" , pass_word=hashlib.md5("longtran".encode()).hexdigest() , created_at=datetime.now())
User.objects.create(full_name="Lê Trọng Hiếu" , user_name = "hieule" , pass_word=hashlib.md5("hieule".encode()).hexdigest() , created_at=datetime.now())
User.objects.create(full_name="Nguyễn Đình Tuấn Anh" , user_name = "anhnguyen" , pass_word=hashlib.md5("anhnguyen".encode()).hexdigest(), created_at=datetime.now())
User.objects.create(full_name="Bùi Tiến Đạt" , user_name = "datbui" , pass_word=hashlib.md5("datbui".encode()).hexdigest() , created_at=datetime.now())

Comment.objects.create(user_id = User.objects.get(pk=1), game_id = Game.objects.get(pk=1) , content = "user 1 comment game 1" , created_at = datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=2), game_id = Game.objects.get(pk=1) , content = "user 2 comment game 1" , created_at = datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=3), game_id = Game.objects.get(pk=1) , content = "user 3 comment game 1" , created_at = datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=4), game_id = Game.objects.get(pk=2) , content = "user 4 comment game 2" , created_at = datetime.now() )
Comment.objects.create(user_id = User.objects.get(pk=5), game_id = Game.objects.get(pk=2) , content = "user 5 comment game 2" , created_at = datetime.now() )

Rating.objects.create(user_id = User.objects.get(pk = 1 ), game_id = Game.objects.get(pk=2), rate=[6,7,8,9,5])
Rating.objects.create(user_id = User.objects.get(pk = 2 ), game_id = Game.objects.get(pk=2), rate=[10,10,10,10,9 ])
Rating.objects.create(user_id = User.objects.get(pk = 3 ), game_id = Game.objects.get(pk=2), rate=[1,2,3,4,5 ])
Rating.objects.create(user_id = User.objects.get(pk = 1 ), game_id = Game.objects.get(pk=1), rate=[1,2,3,4,5 ])
Rating.objects.create(user_id = User.objects.get(pk = 4 ), game_id = Game.objects.get(pk=1), rate=[5,6,7,8,9 ])

Like.objects.create(user_id= User.objects.get(id=1 ), game_id =  Game.objects.get(id=1))
Like.objects.create(user_id= User.objects.get(id=1 ), game_id =  Game.objects.get(id=1))
Like.objects.create(user_id= User.objects.get(id=1 ), game_id =  Game.objects.get(id=1))
Like.objects.create(user_id= User.objects.get(id=2 ), game_id =  Game.objects.get(id=2))
Like.objects.create(user_id= User.objects.get(id=2 ), game_id =  Game.objects.get(id=2))

c = ["none"]
# create category
for i in range(len(list_category)):
    c.append(Category.objects.create(name=list_category[i]))
print(len(list_category))
#game 30 Bombernauts
Game.objects.get(pk=30).categories.add( c[1] , c[6] , c[11])
#game 29 Valiant Hearts
Game.objects.get(pk=29).categories.add(c[1],c[3],c[6],c[10])
# #game 28 lego builder journey
Game.objects.get(pk=28).categories.add(c[1],c[3],c[10])
# #game 27 titanfall 2
Game.objects.get(pk=27).categories.add(c[1],c[2],c[3],c[10])
# #game 26 Tales of Arise
Game.objects.get(pk=26).categories.add(c[1],c[3],c[9],c[10])
# #game 25 Mount & Blade 2
Game.objects.get(pk=25).categories.add(c[1],c[9],c[10],c[11])
# #game 24 crashlands
Game.objects.get(pk=24).categories.add(c[1],c[3],c[10],c[11])
# #game 23 force of nature
Game.objects.get(pk=23).categories.add(c[1],c[3],c[4],c[10],c[11])
#game 22 gas station simulator
Game.objects.get(pk=22).categories.add(c[1],c[3],c[10],c[12])
# #game 21 Invisigun reloaded
Game.objects.get(pk=21).categories.add(c[1],c[3],c[7],c[10],c[11])
# #game 20 nine parchments
Game.objects.get(pk=20).categories.add(c[1],c[3],c[7],c[9],c[11])
# #game 19 stonedeep
Game.objects.get(pk=19).categories.add(c[1],c[3],c[7],c[10])
# #game 18 shelter manager 
Game.objects.get(pk=18).categories.add(c[4],c[10],c[12])
# #game 17 drone simulator
Game.objects.get(pk=17).categories.add(c[1],c[3],c[10],c[12])
# #game 16 Doom eternal
Game.objects.get(pk=16).categories.add(c[1],c[2],c[3],c[8],c[10])
# #game 15 ark survival
Game.objects.get(pk=25).categories.add(c[1],c[3],c[4],c[10])
# #game 14 tthe legend of zelda
Game.objects.get(pk=14).categories.add(c[1],c[3],c[9],c[10])
# #game 13 cyberpunk 2077
Game.objects.get(pk=13).categories.add(c[1],c[3],c[9],c[10])
# #game 12 hitman 3 
Game.objects.get(pk=12).categories.add(c[1],c[2],c[7],c[9],c[10])
# #game 11 day gone 
Game.objects.get(pk=11).categories.add(c[1],c[3],c[10])
# #game 10 Sherlock Holmes Crimes and Punishments
Game.objects.get(pk=10).categories.add(c[1],c[3],c[10])
# #game 9 I am an air traffic controller 4
Game.objects.get(pk=9).categories.add(c[1],c[3],c[7],c[10],c[11],c[12])
# #game 8 blood and bacon online
Game.objects.get(pk=8).categories.add(c[1],c[2],c[3],c[4],c[8],c[11])
# #game 7 slow living with princess
Game.objects.get(pk=7).categories.add(c[1],c[3],c[7],c[9],c[10])
# #game 6 Journey of life
Game.objects.get(pk=6).categories.add(c[3],c[4],c[10],c[12])
# #game 5 GTA 5
Game.objects.get(pk=5).categories.add(c[1],c[3],c[4],c[9],c[11])
# # game 4 far cry
Game.objects.get(pk=4).categories.add(c[1],c[2],c[3],c[4],c[9],c[10])
# # game 3 diablo
Game.objects.get(pk=3).categories.add(c[1],c[3],c[4],c[7],c[11])
# #game 2 assasincreed
Game.objects.get(pk=2).categories.add(c[1],c[3],c[4],c[10])
# # game 1 fifa
Game.objects.get(pk=1).categories.add(c[1],c[5],c[10],c[11])



