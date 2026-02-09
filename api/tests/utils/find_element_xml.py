namespaces = {
    "soapenv": "http://schemas.xmlsoap.org/soap/envelope/",
    "sch": "http://www.ans.gov.br/padroes/tiss/schemas",
}


def find(xml, tag):

    return xml.find(tag, namespaces)


def find_all(xml, tag):

    return xml.findall(tag, namespaces)
