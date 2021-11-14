from io import StringIO
from rest_framework.schemas import AutoSchema, coreapi

class CustomSchema(AutoSchema):
    def __init__(self):
        super(CustomSchema, self).__init__()
    def get_manual_fields(self, path, method):
        extra_fields = [
            coreapi.Field('command', required=True, location='form', schema=StringIO(), description='', type='', example=''),
            coreapi.Field('params', required=False, location='form', schema=StringIO(), description='', type='', example=''),
        ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields