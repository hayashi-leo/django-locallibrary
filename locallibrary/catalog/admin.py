# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# lin,leo - if you register your models under admin,
# you can use admin portal to add/edit/remove model instances

from . models import Author, Genre, Book, BookInstance


### this is the simplest way to use admin to configure/edit your model's data

## myModels = [Author, Genre, Book, BookInstance]

## for model in myModels:
##    admin.site.register(model)

### lin,leo - you can also extend the way admin presents your model data
### like so,


# extending ModelAdmin for Author model
class AuthorAdmin(admin.ModelAdmin):
    # pass  ## uncomment to use default admin presentation style
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    ### the 'fields' attribute list just those files that are to be display on the admin form,
    ### in order.  Fields are display vertically by default, but will display horizontally if you
    ### further ground them in a tuple (as shown below).
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# now register Admin new model
admin.site.register(Author, AuthorAdmin)

# extending ModelAdmin for BookInstance model
## we use here a decorator to register BookInstance and BookInstanceAdmin
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    ## this creates a section view of BookInstance details
    fieldsets = (
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Availability Section',{
            'fields':('status', 'due_back')
        }),
    )
### now register BookInstance new model
#admin.site.register(BookInstance, BookInstanceAdmin) # commented out!, use decorator instead


# extending ModelAdmin for Book model
### Associates records at the same time.
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # pass ## uncomment to use default admin presentation style
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
