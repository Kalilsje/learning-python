class PubCompany:
    def __init__(self, name_company, cnpj) -> None:
        self.name_company = name_company
        self.cnpj = cnpj
    
    def get_cnpj(self):
        return self.cnpj

class Book:
    def __init__(self, title: str, pub_company: PubCompany) -> None:
        self.title = title
        self.pub_company = pub_company

pub_company_saraiva = PubCompany("Saraiva", "12234")
book = Book("Livro_1", pub_company_saraiva)
print(book.pub_company.get_cnpj())
print(pub_company_saraiva.get_cnpj())