from mongoengine import Document, EmbeddedDocument, fields

class Project(EmbeddedDocument):
    ProjectId = fields.StringField(max_length=10, required=True, null=False)
    projName = fields.StringField(max_length=100, required=True)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()


class Skills(EmbeddedDocument):
    tech = fields.StringField(max_length=100, required=True)
    exp = fields.IntField(max_length=100, required=True)
    level = fields.StringField(max_length=100, required=True)
    

class Employee(Document):
    empId = fields.StringField(max_length=10, required=True, null=False)
    empName = fields.StringField(max_length=255, required=True, null=True)
    workLocation = fields.StringField(max_length=255, required=False, null=True)
    projects = fields.EmbeddedDocumentListField(Project)
    skills = fields.EmbeddedDocumentListField(Skills)




