from bank.models import CardBrand


bandeicaCartao = {
"credit_card_flags":[
    {
            "name":"American Express",
        "image_url":"http://test.host/assets/logos/logo-creditcard-americanexpress.png"
    },
    {
            "name":"Aura",
        "image_url":"http://test.host/assets/logos/logo-creditcard-aura.png"
    },
    {
            "name":"Avista",
        "image_url":"http://test.host/assets/logos/logo-creditcard-avista.png"
    },
    {
            "name":"BrasilCard",
        "image_url":"http://test.host/assets/logos/logo-creditcard-brasilcard.png"
    },
    {
            "name":"Cabal",
        "image_url":"http://test.host/assets/logos/logo-creditcard-cabal.png"
    },
    {
            "name":"CardBan",
        "image_url":"http://test.host/assets/logos/logo-creditcard-cardban.png"
    },
    {
            "name":"Diners Club",
        "image_url":"http://test.host/assets/logos/logo-creditcard-dinersclub.png"
    },
    {
            "name":"Elo",
        "image_url":"http://test.host/assets/logos/logo-creditcard-elo.png"
    },
    {
            "name":"FortBrasil",
        "image_url":"http://test.host/assets/logos/logo-creditcard-fortbrasil.png"
    },
    {
            "name":"Hipercard",
        "image_url":"http://test.host/assets/logos/logo-creditcard-hipercard.png"
    },
    {
            "name":"MasterCard",
        "image_url":"http://test.host/assets/logos/logo-creditcard-mastercard.png"
    },
    {
            "name":"Personal Card",
        "image_url":"http://test.host/assets/logos/logo-creditcard-personalcard.png"
    },
    {
            "name":"Pleno Card",
        "image_url":"http://test.host/assets/logos/logo-creditcard-plenocard.png"
    },
    {
            "name":"Santander",
        "image_url":"http://test.host/assets/logos/logo-creditcard-santander.png"
    },
    {
            "name":"Sicredi",
        "image_url":"http://test.host/assets/logos/logo-creditcard-sicredi.png"
    },
    {
            "name":"Sorocred",
        "image_url":"http://test.host/assets/logos/logo-creditcard-sorocred.png"
    },
    {
            "name":"ValeCard",
        "image_url":"http://test.host/assets/logos/logo-creditcard-valecard.png"
    },
    {
            "name":"Visa",
        "image_url":"http://test.host/assets/logos/logo-creditcard-visa.png"
    }
]
}

for bandeira in bandeicaCartao['credit_card_flags']:
    card = CardBrand()
    card.name = bandeira['name']
    card.urlImage = bandeira['image_url']
    card.save()
    