class GoogleTranslator:
    def __init__(self):
        from deep_translator import GoogleTranslator
        self.translator = GoogleTranslator()

    def translate(self, data):
        data['content'] = self.__remove_quotas(data).apply(
            lambda x: self.translator.translate(x, source='auto', target_lang="en"))
        return data

    @staticmethod
    def __remove_quotas(data):
        import re
        return data['content'].apply(lambda x: re.sub('"', '', str(x)))
