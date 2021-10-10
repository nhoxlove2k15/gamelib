from gamelib.models import *
import datetime
import hashlib
# create 

# User(full_name="Nguyễn Văn A" , user_name="nhoxlove" , pass_word=str(hash("123456")) , created_at = datetime.datetime.now()).save()
# User(full_name="Nguyễn Văn B" , user_name="nhoxlove" , pass_word=str(hash("123456")) , created_at = datetime.datetime.now()).save()

#User(full_name="Nguyễn Văn A" , user_name="nhoxlove123" , pass_word=str(hash("123456")) , created_at = datetime.datetime.now()).save()
User(full_name="Nguyễn Văn E" , user_name="nhox" , pass_word=hashlib.md5("123456".encode()).hexdigest() , created_at = datetime.datetime.now()).save()
User(full_name="Nguyễn Văn  f" , user_name="nhoxlv" , pass_word=hashlib.md5("123456".encode()).hexdigest(), created_at = datetime.datetime.now()).save()

# #  read

# user = User.objects.get(full_name="Nguyễn Văn A")
# print(user.user_name)

# # update 

# user = User.objects.get(full_name="Nguyễn Văn A")
# user.full_name = "Nguyễn Quang Trường"
# user.pass_word = "truong123"
# user.save()

# # delete

# User.objects.filter(user_name="nhoxlove").delete()

