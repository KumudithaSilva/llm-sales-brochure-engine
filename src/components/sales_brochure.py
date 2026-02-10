from utils import base_utils

class SalesBrochure:
    
    def __init__(self):
        self.utils = base_utils.BaseUtils()
        self.env_variables = self.utils.load_env_variables()


if __name__ == "__main__":
    sales_brochure = SalesBrochure()
    print(sales_brochure.env_variables)