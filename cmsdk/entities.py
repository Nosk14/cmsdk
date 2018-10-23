from dataclasses import dataclass


@dataclass
class Address(object):
    name: str
    extra: str
    street: str
    zip: str
    city: str
    country: str


@dataclass
class Name(object):
    firstName: str
    lastName: str

@dataclass
class MoneyDetails(object):
    totalBalance: float
    moneyBalance: float
    bonusBalance: float
    unpaidAmount: float
    providerRechargeAmount: float

@dataclass
class BankAccount(object):
    accountOwner: str
    iban: str
    bic: str
    bankName: str

@dataclass
class Account(object):
    idUser: int
    username: str
    country: str
    isCommercial: int
    maySell: int
    riskGroup: int
    reputation: int
    shipsFast: int
    sellCount: int
    soldIntems: int
    avgShippingTime: int
    onVacation: bool
    idDisplaylanguage: int
    name: Name
    homeAddress: Address
    email: str
    phoneNumber: str
    vat: str
    registerDate: str
    moneyDetails: MoneyDetails
    bankAccount: BankAccount
    articlesInShoppingCart: int
    unreadMessages: int
    links: dict
