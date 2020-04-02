from werkzeug.routing import BaseConverter


class MyConverter(BaseConverter):
    """自定义转换器"""
    def __init__(self, url_map, regex):
        self.regex = regex
        super().__init__(url_map)