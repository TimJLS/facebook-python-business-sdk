# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ExtendedCreditApplication(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isExtendedCreditApplication = True
        super(ExtendedCreditApplication, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        billing_country = 'billing_country'
        city = 'city'
        cnpj = 'cnpj'
        country = 'country'
        duns_number = 'duns_number'
        id = 'id'
        invoice_email_address = 'invoice_email_address'
        legal_entity_name = 'legal_entity_name'
        phone_number = 'phone_number'
        postal_code = 'postal_code'
        product_type = 'product_type'
        registration_number = 'registration_number'
        run_id = 'run_id'
        state = 'state'
        status = 'status'
        street1 = 'street1'
        street2 = 'street2'
        submitter = 'submitter'
        tax_id = 'tax_id'
        terms = 'terms'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=ExtendedCreditApplication,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'billing_country': 'string',
        'city': 'string',
        'cnpj': 'string',
        'country': 'string',
        'duns_number': 'string',
        'id': 'string',
        'invoice_email_address': 'string',
        'legal_entity_name': 'string',
        'phone_number': 'string',
        'postal_code': 'string',
        'product_type': 'string',
        'registration_number': 'string',
        'run_id': 'string',
        'state': 'string',
        'status': 'string',
        'street1': 'string',
        'street2': 'string',
        'submitter': 'User',
        'tax_id': 'string',
        'terms': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info

