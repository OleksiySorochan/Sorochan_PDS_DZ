class TextProcessor:
    def __init__(self):
        self.__chek_symbol = ',.!?()_-'

    def __is_punktiantion(self, symbol):
        return symbol in self.__chek_symbol

    def get_clean_string(self, text):
        # return text
        clean_text = ''
        for symbol in text:
            if self.__is_punktiantion(symbol) == False:
                clean_text += symbol
        return clean_text

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_sring = None

    def set_clean_text(self, text):
        self.__clean_sring = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print(f"Clean string: {self.__clean_sring}")
        return self.__clean_sring

class DataInterface:
    def __init__(self):
        self._data = TextLoader()

    def process_texts(self, lst):
        clean_lst = []
        for text in lst:
            self._data.set_clean_text(text)
            clean_lst.append(self._data.clean_string)
        return clean_lst

d = DataInterface()
l = ['dhfjd, sdf, sf.', 'Hello!!', 'one, and two!', 'sd ,sdf, sfd, sf.']
d.process_texts(l)



