from django.contrib import admin
from apps.goods.models import Goods, GoodsImage, GoodsSKU, GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner
# Register your models here.

admin.site.register(Goods)
admin.site.register(GoodsImage)
admin.site.register(GoodsSKU)
admin.site.register(GoodsType)
admin.site.register(IndexTypeGoodsBanner)
admin.site.register(IndexPromotionBanner)
admin.site.register(IndexGoodsBanner)