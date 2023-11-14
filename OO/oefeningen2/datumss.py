from faker import Faker
fake = Faker("nl_BE")
for i in range(10):
    print(fake.first_name_nonbinary())