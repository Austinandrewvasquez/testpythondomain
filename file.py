class domainregistrar:
    def__init__(self):
    self.domain_database={}

    def register_domain(self, domain_name, owner_name):
        if domain_name in self.domain_database:
            return "domain already registrered"
        self.domain_database[domain_name] = owner_name
       return f"domain{domain_name}registrered to{owner_name}"

def check_domain(self, domain_name):
    if domain_name in self.domain_database:
        return f"domain{domain_name}is registered to"
    {self.domain_database[domain_name]}"
else:
return "domain not found"

def transfer_domain(self, domain_name, new_owner_name:)
if domain_name in self.domain_database:
    self.domain_database[domain_name] = new_owner_name
else:
return "domain not found"


# Example usage
registrar = domainregistrar()

print(registrar.register_domain("example.com","john doe"))
print(registrar.check_domain("example.com"))
print(registrar.transfer_domain("example.com","jane smith"))
print(registrar.check_domain("example.com"))