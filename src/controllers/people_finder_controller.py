from typing import Dict

class PeopleFinderController:
    def find_by_name(self, person_finder_information: Dict) -> Dict:
        try:
            self.__validate_fields(person_finder_information)
            #person = Buscar em banco de dados
            response = self.__format_response(None)
            return { "success": True, "message": response }
        except Exception as exception:
            return { "success": False, "error": exception }

    def __validate_fields(self, person_finder_information: Dict) -> None:
        if not isinstance(person_finder_information["name"], str):
            raise Exception('Campo nome inválido!')
        
    def __format_response(self, person: any) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "infos": {
                "name": "meu nome teste"
            }
        }
