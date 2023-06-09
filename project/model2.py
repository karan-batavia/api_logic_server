from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode, DateTime,ForeignKey, UniqueConstraint


class Foo(declarative_base(metadata=metadata)):
  passport_number = Column(Integer, primary_key=True)
  first_name = Column(String, index = True)


SpecieBase = declarative_base(metadata=metadata)
class Specie(SpecieBase):
    __tablename__ = 'specie'
    __table_args__ = (UniqueConstraint('name'), {})

    passport_number = Column(Integer, primary_key=True)
    first_name = Column(String, index = True)
    def __init__(self, name):
        self.name = name

def MakeClasses(metadata):

  PhylumBase = declarative_base(metadata=metadata)
  class Phylum(PhylumBase):
      __tablename__ = 'phylum'
      __table_args__ = (UniqueConstraint('name'), {})
      id = Column(Integer, primary_key=True)
      name = Column(String, index = True)
      def __init__(self, name):
          self.name = name
  
  PhylumJoinBase = declarative_base(metadata = metadata)
  class Phylum_GBIDJoin(PhylumJoinBase):
    __tablename__= 'phylum_gbidjoin'
    __table_args__ = (UniqueConstraint('gbid'), {})

    id = Column(Integer, primary_key=True)
    phylum = Column(Integer, 
                      ForeignKey('phylum.id'))
    gbid = Column(Integer,
                  ForeignKey('gbid.id')
                  , index = True)
    def __init__(self,  phylum, gbid):
      self.gbid = gbid
      self.phylum = phylum
  
  
  
  DomainBase = declarative_base(metadata=metadata)
  class Domain(DomainBase):
      __tablename__ = 'domain'

      __table_args__ = (
        UniqueConstraint('name'), {},
        {}
        )
      __table_args__ = (UniqueConstraint('name'), {})
      id = Column(Integer, primary_key=True)
      name = Column(String, nullable = False, index = True)
      def __init__(self, name):
          self.name = name
  
  DomainJoinBase = declarative_base(metadata = metadata)
  class Domain_GBIDJoin(DomainJoinBase):
    __tablename__= 'domain_gbidjoin'
    __table_args__ = (UniqueConstraint('gbid'), {})

    id = Column(Integer, primary_key=True)
    domain = Column(Integer, 
                      ForeignKey('domain.id'))
    gbid = Column(Integer,
                  ForeignKey('gbid.id'), index = True)
    def __init__(self,  domain, gbid):
      self.gbid = gbid
      self.domain = domain
  
  
  
  ClassBase = declarative_base(metadata=metadata)
  class Class(ClassBase):
      __tablename__ = 'class_tax'
      __table_args__ = (UniqueConstraint('name'), {})

      id = Column(Integer, primary_key=True, index = True)
      name = Column(String, index = True)
      def __init__(self, name):
          self.name = name
  
  ClassJoinBase = declarative_base(metadata = metadata)
  class Class_GBIDJoin(ClassJoinBase):
    __tablename__= 'class_tax_gbidjoin'
    __table_args__ = (UniqueConstraint('gbid'), {})

    id = Column(Integer, primary_key=True)
    class_tax = Column(Integer, 
                      ForeignKey('class_tax.id'))
    gbid = Column(Integer,
                  ForeignKey('gbid.id'), index = True)
    def __init__(self,  class_tax, gbid):
      self.gbid = gbid
      self.class_tax = class_tax
  
  
  
  OrderBase = declarative_base(metadata=metadata)
  class Order(OrderBase):
      __tablename__ = 'order'
      __table_args__ = (UniqueConstraint('name'), {})

      id = Column(Integer, primary_key=True)
      name = Column(String, index = True)
      def __init__(self, name):
          self.name = name
  
  OrderJoinBase = declarative_base(metadata = metadata)
  class Order_GBIDJoin(OrderJoinBase):
    __tablename__= 'order_gbidjoin'
    __table_args__ = (UniqueConstraint('gbid'), {})

    id = Column(Integer, primary_key=True)
    order = Column(Integer, 
                      ForeignKey('order.id'))
    gbid = Column(Integer,
                  ForeignKey('gbid.id'), index = True)
    def __init__(self,  order, gbid):
      self.gbid = gbid
      self.order = order
  
  
  
  FamilyBase = declarative_base(metadata=metadata)
  class Family(FamilyBase):
      __tablename__ = 'family'
      __table_args__ = (UniqueConstraint('name'), {})

      id = Column(Integer, primary_key=True)
      name = Column(String, index = True)
      def __init__(self, name):
          self.name = name
  
  FamilyJoinBase = declarative_base(metadata = metadata)
  class Family_GBIDJoin(FamilyJoinBase):
    __tablename__= 'family_gbidjoin'
    __table_args__ = (UniqueConstraint('gbid'), {})

    id = Column(Integer, primary_key=True)
    family = Column(Integer, 
                      ForeignKey('family.id'))
    gbid = Column(Integer,
                  ForeignKey('gbid.id'), index = True)
    def __init__(self,  family, gbid):
      self.gbid = gbid
      self.family = family
  
  
  
  GenusBase = declarative_base(metadata=metadata)
  class Genus(GenusBase):
      __tablename__ = 'genus'
      __table_args__ = (UniqueConstraint('name'), {})
            
      id = Column(Integer, primary_key=True)
      name = Column(String, index = True)
      def __init__(self, name):
          self.name = name
  
  GenusJoinBase = declarative_base(metadata = metadata)
  class Genus_GBIDJoin(GenusJoinBase):
    __tablename__= 'genus_gbidjoin'      
    __table_args__ = (UniqueConstraint('gbid'), {})

    id = Column(Integer, primary_key=True)
    genus = Column(Integer, 
                      ForeignKey('genus.id'))
    gbid = Column(Integer,
                  ForeignKey('gbid.id'), index = True)
    def __init__(self,  genus, gbid):
      self.gbid = gbid
      self.genus = genus
  
  

  
  SpecieJoinBase = declarative_base(metadata = metadata)
  class Specie_GBIDJoin(SpecieJoinBase):
    __tablename__= 'specie_gbidjoin'
    __table_args__ = (UniqueConstraint('gbid'), {})

    id = Column(Integer, primary_key=True)
    specie = Column(Integer, 
                      ForeignKey('specie.id'))
    gbid = Column(Integer,
                  ForeignKey('gbid.id'), index = True)
    def __init__(self,  specie, gbid):
      self.gbid = gbid
      self.specie = specie

  return dict(Domain = Domain, Phylum = Phylum, Class = Class, 
              Order = Order, Family = Family, Genus = Genus, 
              Specie = Specie,
              Domain_GBIDJoin = Domain_GBIDJoin, 
              Phylum_GBIDJoin =  Phylum_GBIDJoin,
              Class_GBIDJoin = Class_GBIDJoin, 
              Order_GBIDJoin =  Order_GBIDJoin,
              Family_GBIDJoin = Family_GBIDJoin, 
              Genus_GBIDJoin =  Genus_GBIDJoin,
              Specie_GBIDJoin =  Specie_GBIDJoin)