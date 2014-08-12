# -*- coding: utf-8 -*-
__author__ = 'soroosh'

import logging
from suds.client import Client
logging.basicConfig(level=logging.INFO)

logging.debug('creating client started')
c = Client('http://services.yaser.ir/Quran/?wsdl')
logging.debug('client created')
logging.info(c)

result = c.service.GetRandomAyeh()
print result




