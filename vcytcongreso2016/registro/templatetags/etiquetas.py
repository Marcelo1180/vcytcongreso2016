from django import template
import json
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name='addattr')
def addattr(field, items):
   items = json.loads(items)
   field = field.as_widget(attrs=items)
   return field

@register.filter(name='required')
def required(field):
   return field.as_widget(attrs={"required":"true"})