import connexion
import json
import requests
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.company import Company  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server import util

import xml.etree.ElementTree as ET

def companies_id_get(id_):  # noqa: E501
    """companies_id_get

     # noqa: E501

    :param id: Company ID
    :type id:

    :rtype: Union[Company, Tuple[Company, int], Tuple[Company, int, Dict[str, str]]
    """
    response = requests.get(f"https://raw.githubusercontent.com/MiddlewareNewZealand/evaluation-instructions/main/xml-api/{int(id_)}.xml")
    if response.status_code == 200:
        try:
            xmldoc = ET.fromstring(response.text)
            return Company(id=int(xmldoc.find('id').text), name=xmldoc.find('name').text, description=xmldoc.find('description').text)
        except:
            return Error(error="Errorish", error_description="It's a bloody error").__str__()
    else:
        return Error(error="404", error_description="No such company")

    return false
