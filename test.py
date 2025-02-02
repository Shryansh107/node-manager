from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import json

PRIVATE_KEY = """-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFJTBPBgkqhkiG9w0BBQ0wQjAhBgkrBgEEAdpHBAswFAQIsPoFqf9JlHwCAkAA
AgEIAgEBMB0GCWCGSAFlAwQBAgQQbm45Uz7mJueH4JsD7DEd5gSCBNBxqUBvH0iT
gGIEMaa0xhWdBPnzt15mgEul2xs0ZxtCwnHnFc4ZxArMXsFpF5zlXdxMWRYQh2Cb
D1QmcULOUPB72yaglqCHDzjlubmNxOeM4MoSiSHlPFNUSOhZEBSjk+ndyhHmfxPP
mvtCn0d2cLCyYA4g7p6/jm4QVq/77ptL1fdqfgMJZIJfM0o4kPhqhycb1zvcfbao
mnL7UysASBpJiq3MaxaEOd3Y1s9iKJHt7tbiHPabictV45hWOK0bbhL72fc8yo4s
RkojuAs/H2xqIV9UlWBrlLl18rrC+HEOfmIdcIwk+jgXZF5N6qLKcCjJDWjZRMbq
E/NwqoD9Z1Y3fDb2eYHvAXRx0vCvae0i3ApoO5QNDzurnYbksbLrcMW89POoL7+g
fq1aSm5Kv6RTxfiu+QoFiZg2W5vYVaLFBIJlliTFV5ZFEKOCO4vkiViVH5S3MA95
CMVSRz5lQOjledZqayQwl+WPOAjeEVyLXsaEc8nDx2II/D2cTqECIvJ9EXzuWQXU
Xpv3eRdCtTs8jaWyQzVA+SVa236d+RILuQP61Yc+Nm/ufcYkb7j9vRU8vaY3zo1Y
lhl0++h4V/JUjyNuw+kCc5M1sz0PN20BtK0oCTSHfFNLr5CW0ivOIbEzRLNLqsUN
hhgYJjPg+rCfIgWeoS2rVemnxk+vPGRIPO62eZTFe0ZctfrBg1pCrIyBeTtmVYQV
Ma9hSJZlUZ1i79zw6BkiJiCOCdeAFB9vJZmuD6rtUSw8Z9o5MlL1pAQcjQQZuwrQ
eCtfLnWJsELGtKi9GWznWzaLoYRq10XjsFpfLv5hlGntRO+nzUSz7LbTPX/9Tb2P
dYO4YLzeKGR3VB+CFBt3FmvMjFXqF2FyMR9HFnPegPLqL/WH5VdWf5S8O0Vwo82S
osW9wJ3xG+UX24OGKxWta5h3tw49Do2NrdMDLUuZmMdqm0rtx0IXeR3oGkiFuV0Y
aNf5RAhZAPyX41sxfQHYG6fuc2FkO6Rs7G4AKcBA/KjBIPFxLnjX7dMvsuvGM9eu
2mlzIa/dSaUdsLd06Osx84NcMufQH/558EyqLK6M9QZZ0MeRsucAP63qYD051X25
EJlwUyizN2KJe3EZ+IJ6jHSHIugG1lTrreR/nsGtX99pRzlO28cYrkGoMsJyXLxu
tRqzOHwmPWfu5auxBl/tI3Jcaebw5w/QmYpdD95cGRvQdXOHyCAZ176CP8BKLz/x
vX6zAGCFmGE7bEULhyi0XHnMVDFKpew6B5h+Q2EfjR0yvGvP9KFV7bAn+VpmFQIs
50OW3ameYKEUGghjjz/VKni8Sq/kxFgZ9LTL9trsADmKQCnY/vkxop2jdDpC0s48
Y3AIQCQJf+k4oNvF8nG3AntAdktKowYkWFavQpJfO7CqxtEAGfjBFqKz6y2FlsPj
Rqy3a3XVxehPKLvuj4Kc8sd/f2tZUFGq3HRDzdHmaYQ2Sw7BOkeuQzcVjgvsXj+a
ije4wvxhXTOTwAmK/llWfoY0GkEbIBGFcOqHncxX2gIZziLrh0MzDpOBYFk3nTHR
3zSDRgdE2GuKwgL9U6ak0I2IFCrqpoCV9z9h+dTPcMibp1EHUz5e2FuNvv6TzW6y
aTiebQSrI8RFyGhjjZevkS6JHgjTfbGz+Q==
-----END ENCRYPTED PRIVATE KEY-----"""

PASSPHRASE = "H7bc:<-wi&nj'5Ls"

data = {"a": "b"}

data = json.dumps(data)

data_hash = SHA256.new(data.encode("utf-8"))

rsa_key = RSA.import_key(PRIVATE_KEY, PASSPHRASE)

signature = pkcs1_15.new(rsa_key).sign(data_hash)

signature = base64.b64encode(signature).decode()

print(signature)


