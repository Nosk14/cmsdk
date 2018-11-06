from dataclasses import dataclass


class BaseEntity:

    @classmethod
    def from_json(cls, json):
        return cls(**json)


@dataclass
class Address(BaseEntity):
    name: str
    extra: str
    street: str
    zip: str
    city: str
    country: str


@dataclass
class Name(BaseEntity):
    firstName: str
    lastName: str


@dataclass
class MoneyDetails(BaseEntity):
    totalBalance: float
    moneyBalance: float
    bonusBalance: float
    unpaidAmount: float
    providerRechargeAmount: float


@dataclass
class BankAccount:
    accountOwner: str
    iban: str
    bic: str
    bankName: str

    @classmethod
    def from_json(cls, json):
        return BankAccount(**json)


@dataclass
class Account(BaseEntity):
    idUser: int
    username: str
    country: str
    isCommercial: int
    maySell: int
    sellerActivation: int
    riskGroup: int
    lossPercentage: str
    reputation: int
    shipsFast: int
    sellCount: int
    soldItems: int
    avgShippingTime: int
    onVacation: bool
    idDisplayLanguage: int
    name: Name
    homeAddress: Address
    email: str
    phoneNumber: str
    vat: str
    legalInformation: str
    registerDate: str
    isActivated: bool
    moneyDetails: MoneyDetails
    bankAccount: BankAccount
    articlesInShoppingCart: int
    unreadMessages: int

    @classmethod
    def from_json(cls, json):
        sub_entities = {
            'name' : Name.from_json(json['name']),
            'homeAddress' : Address.from_json(json['homeAddress']),
            'moneyDetails' : MoneyDetails.from_json(json['moneyDetails']),
            'bankAccount' : BankAccount.from_json(json['bankAccount'])
        }
        return Account(**{**json, **sub_entities})
