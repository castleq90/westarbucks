from django.db import models
from django.db.models.base import Model

# table 명: menus
# columns: id -> name -> VARCHAR(50)

class Menu(models.Model): 
    # 장고 클래스를 상속 받아 오기 때문에 
    # id가 자동 생성되어 작성해줄 필요 없다 
    # 아래에 컬럼만 적어주면 OK
    name = models.CharField(max_length = 50)
    # VARCHAR(50) -> models.CharField(50) 
    # 바차는 sql데이터 타입이고 -> 장고 모델에서는 검색을 활용해 
    # 바꿔서 입력해줘야 한다.

    class Meta:
        db_table = 'menus'
        # 내가 원하는 테이블 명 설정이 가능

class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # 상위 카테고리의 FK를 참조하고 데이터가 지워지면 같이 사라진다

    class Meta:
        db_table = 'products_category'

class Drinks(models.Model):
    name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_drinks'

class Allergy(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'products_allergy'

class AllergyDrinks(models.Model):
    Allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    Drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_allergydrinks'

class Images(models.Model):
    image_url = models.CharField(max_length=500)
    Drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_image'