class DataXMLExecucaoSPSADT:
    def __init__(self, xml, namespaces):
        self.xml = xml
        self.namespaces = namespaces

    def find_or_error(self, tag_name):

        tag = self.xml.find(tag_name, self.namespaces)

        if tag is None:
            raise Exception(
                {
                    "message": f"Não foi possível localizar a tag {tag_name} no XML",
                    "status_code": 400,
                }
            )

        return tag

    def find_all_or_error(self, tag_name):

        tags = self.xml.findall(tag_name, self.namespaces)

        if tags is None:
            raise Exception(
                {
                    "message": f"Não foi possível localizar a tag {tag_name} no XML",
                    "status_code": 400,
                }
            )

        return tags
