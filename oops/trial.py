class Phone():
    def specs(self, name, ram, storage, processor):
        self.name = name
        self.ram = ram
        self.storage = storage
        self.processor = processor
    def display(self):
        print(self.name)
        print(self.ram)
        print(self.storage)
        print(self.processor,"\n")

p1 = Phone()
p2 = Phone()
p3 = Phone()

p1.specs("S25 Ultra", "12GB", "512GB", "SD 8 Elite")
p2.specs("S23 Ultra", "12GB", "256GB", "SD 8 Gen 3")
p3.specs("17 Pro max", "12GB", "512GB", "A18 Bionic Chip")

p1.display()
p2.display()
p3.display()