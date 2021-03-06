from configobj import ConfigObj
config = ConfigObj()

config.filename = 'app/helper/config'
#
Kryptex = {
    'URL': 'https://www.kryptex.org/tr/best-gpus-for-mining',
    'XPATH': {
        'GPULIST': './html/body/main/div[2]/div/div[2]/div[1]/div/table/tbody'
        },
    'CLASS_NAME' : {
        'GPU_NAME' : 'tr-link__link'
        },
    'CSS_SELECTOR' : {
        'GPUS' : 'tr',
        'GPU_NAME' : 'a',
        'PRICE' : 'td.text-center',
        'ETH_HASHRATE' : 'td:nth-child(3)',
        'ETC_HASHRATE' : 'td:nth-child(4)',
        'EXP_HASHRATE' : 'td:nth-child(5)',
        'UBQ_HASHRATE' : 'td:nth-child(6)',
        'RVN_HASHRATE' : 'td:nth-child(7)',
        'BEAM_HASHRATE' : 'td:nth-child(8)',
        }
    }

config['Kryptex'] = Kryptex
#
Minerstat = {
    'URL': 'https://minerstat.com/hardware/gpus/',
    'XPATH': {},
    'CLASS_NAME' : {
        'GPULIST': 'tr',
        'ORDER': 'flexOrder',
        'GPU_NAME': 'flexHardware',
        'COIN' : 'coin'
        }
    }
#
config['Minerstat'] = Minerstat
#
config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///:memory:'
#
Grossbill = {
    'URL': 'https://www.grosbill.com/2-carte_graphique-cat-informatique',
    'XPATH': {
        'GPU_NAME': '//*[@id="content_product"]/div/div[4]/div[5]/div[1]/div[2]/div[1]/a/div[1]/h2/span'
    },
    'CLASS_NAME' : {
        'GPULIST': 'categorie-filtre lst_grid',
        'PRICE': 'price_prod_resp',
        'STOCK': 'prodfiche_dispo detail-stock',
        'PRODUCT_LINK' : 'prod_txt_left'
        }
    }
#
config['Grossbill'] = Grossbill
config.write()