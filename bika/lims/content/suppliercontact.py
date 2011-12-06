"""The contact person at a reference supplier organisation.
"""
from AccessControl import ClassSecurityInfo
from AccessControl.Permissions import manage_users
from Products.Archetypes.public import *
from bika.lims.content.person import Person
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName
from bika.lims.interfaces import IGenerateUniqueId
from bika.lims.config import PROJECTNAME
from bika.lims import bikaMessageFactory as _
from zope.interface import implements

schema = Person.schema.copy()

schema['JobTitle'].schemata = 'default'
schema['Department'].schemata = 'default'

schema['id'].schemata = 'default'
schema['id'].widget.visible = False
# Don't make title required - it will be computed from the Person's
# Fullname
schema['title'].schemata = 'default'
schema['title'].required = 0
schema['title'].widget.visible = False

class SupplierContact(Person):
    implements(IGenerateUniqueId)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

registerType(SupplierContact, PROJECTNAME)
