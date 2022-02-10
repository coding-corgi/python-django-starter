from django.db import models

# Create your models here.
class Restaurant(models.Model): # Restaurant 라는 상점을 나타내는 모델을 정의
    name = models.CharField(max_length=30)  # 이름
    address = models.CharField(max_length=200)  # 주소

    image = models.CharField(max_length=500, default=None, null=True)
    password = models.CharField(max_length=20, default=None, null=True) #기존 입력데이터에대 추가하려면 이렇게 해야함

    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)  # 저장된 레코드 수정 시 수정 시각

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # 식당 모델과의 릴레이션 정의,
    # on_delete CASCADE로 지정하면 식당이 삭제되면 같이 삭제된다.
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)



