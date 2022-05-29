from django.db import models

# Create your models here.
class Image(models.Model):
    '''
    model to handle images
    '''
    img = models.ImageField(upload_to='images/',default='1')
    name = models.CharField(max_length =30)
    description = models.TextField()
    category = models.ForeignKey( 'Category', on_delete=models.CASCADE,default=1)
    location = models.ForeignKey( 'Location', on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

    def save_image(self):
        '''
        method to save an image
        '''
        self.save()

    def delete_image(self):
        '''
        method to delete an image
        '''
        self.delete()
    @classmethod
    def search_by_category(cls, search_term):
            picha = cls.objects.filter(category__icontains=search_term)
            return picha
                
            # result = cls.objects.filter(category__name__contains=category) #images assoc w/ this cat
            # return result

    @classmethod
    def filter_by_location(cls ,location):
        '''
        method to retrive images by their locations
        '''
        data = Image.objects.filter(location__city__contains=location)
        return data
    @classmethod
    def get_image_by_id(cls, id):
       
        retrieved = Image.objects.get(id = id)
        return retrieved
    
    def update_image(self, new_url):
      
        try:
            self.image_link = new_url
            self.save()
            return self
        except self.DoesNotExist:
            print('Image entered does not exist.Please enter another image.')


class Category(models.Model):
    '''
    model to handle category
    '''
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
    def save_category(self):
        '''
        method to save a category
        '''
        self.save()

    def delete_category(self):
        '''
        method to delete a category
        '''
        self.delete()
    def update_category(cls, search_term , new_cat):
        '''
        method to update a category
        '''
        try: