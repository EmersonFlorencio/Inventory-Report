from abc import ABC, abstractclassmethod


class Importer(ABC):
    @abstractclassmethod
    def import_data(file_doc):
        raise NotImplementedError
