
class CellPhone:

    def __init__(self,ma,mo,rp):
        self.__manufact = ma 
        self.__model = mo
        self.__retail_price = rp
    
    def set_manufact(self,ma):
        self.__manufact = ma
    
    def set_model(self,mo):
        self.__model = mo

    def set_retail_price(self,rp):
        self.__retail_price = rp

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self,ma,mo,rp):
        return self.__retail_price
