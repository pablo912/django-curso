from django.db import models

from apps.base.models import BaseModel

# Create your models here.


class MeasureUnit(BaseModel):

    description = models.CharField('Description', max_length=50, blank = False, null = False, unique = True )


    class Meta:

        verbose_name = 'Unidad de medidad'
        verbose_name_plural = 'Unidad de medidad'

    def __str__(self):

        return self.description



class CategoryProduct(BaseModel):

    description = models.CharField('Description', max_length=50, blank = False, null = False )
    measure_unit = models.ForeignKey( MeasureUnit, on_delete=models.CASCADE, verbose_name = 'Unidad de Medida' )

    class Meta:

        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categoria de productos'

    def __str__(self):

        return self.description
    

class Indicador(BaseModel):

    discount_value = models.PositiveSmallIntegerField( default = 0)
    category_product = models.ForeignKey( CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de ofertas' )
     
    class Meta:

        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de ofertas'

    def __str__(self):

        return f'Oferta de la categoria { self.category_product } : { self.discount_value }'
    
    