from database import SessionLocal
from models import Ruta, Punto

db = SessionLocal()

puntos_data = [
    # ISLÁMICA
    {"id": 1,  "nombre": "Muralla zirí",                                        "descripcion": "Antiguo sistema defensivo del siglo XI que protegía la Granada musulmana, con restos aún visibles en el Albaicín.",                                                              "latitud": 37.182196,              "longitud": -3.594874},
    {"id": 2,  "nombre": "Puerta de Elvira",                                    "descripcion": "Principal acceso a la ciudad en época islámica, formaba parte de la muralla zirí y conectaba con la medina.",                                                                    "latitud": 37.182125,              "longitud": -3.599586},
    {"id": 3,  "nombre": "Puerta de las Pesas",                                 "descripcion": "Puerta fortificada del Albaicín donde se colgaban pesas fraudulentas como castigo público.",                                                                                     "latitud": 37.182512,              "longitud": -3.593787},
    {"id": 4,  "nombre": "Puerta del León",                                     "descripcion": "Acceso medieval al barrio del Albaicín, decorada con un relieve de león que le da nombre.",                                                                                      "latitud": 37.180912,              "longitud": -3.598159},
    {"id": 5,  "nombre": "Puerta del Castro",                                   "descripcion": "Puerta de la muralla zirí situada en la zona alta del Albaicín, cerca del antiguo castro romano.",                                                                               "latitud": 37.181927,              "longitud": -3.592942},
    {"id": 6,  "nombre": "Puerta de Monaita",                                   "descripcion": "Una de las puertas mejor conservadas de la muralla zirí, situada en el corazón del Albaicín.",                                                                                   "latitud": 37.182046,              "longitud": -3.597612},
    {"id": 7,  "nombre": "Iglesia de San José (alminar)",                       "descripcion": "Iglesia construida sobre una mezquita medieval cuyo alminar árabe del siglo XI se conserva como campanario.",                                                                    "latitud": 37.178663,              "longitud": -3.596172},
    {"id": 8,  "nombre": "El Bañuelo",                                          "descripcion": "Baños árabes del siglo XI, entre los mejor conservados de España. Sus bóvedas con lucernas estrelladas son su seña de identidad.",                                             "latitud": 37.178488,              "longitud": -3.592991},
    {"id": 9,  "nombre": "Torres Bermejas (castillo)",                          "descripcion": "Conjunto de torres defensivas de origen romano ampliadas en época nazarí, situadas en la colina de la Mauror junto a la Alhambra.",                                             "latitud": 37.175526,              "longitud": -3.593412},
    {"id": 10, "nombre": "Alcázar Genil",                                       "descripcion": "Palacio de recreo nazarí del siglo XIII situado junto al río Genil, con una de las albercas islámicas más grandes conservadas en Granada.",                                     "latitud": 37.164720,              "longitud": -3.600530},
    {"id": 11, "nombre": "Ermita de San Sebastián (antiguo morabito)",          "descripcion": "Pequeño edificio de origen islámico que sirvió de morabito y donde, según la tradición, se firmaron las capitulaciones de Granada en 1491.",                                    "latitud": 37.166295,              "longitud": -3.600021},
    {"id": 12, "nombre": "Iglesia de San Juan de los Reyes (alminar)",          "descripcion": "Templo cristiano levantado sobre una mezquita medieval que conserva su alminar original del siglo XIII como campanario.",                                                       "latitud": 37.179963,              "longitud": -3.591829},
    {"id": 13, "nombre": "Iglesia de San Salvador (patio almohade)",            "descripcion": "Iglesia del Albaicín que conserva en su interior el patio de la antigua mezquita mayor del barrio, de época almohade.",                                                         "latitud": 37.182334,              "longitud": -3.590666},
    {"id": 14, "nombre": "Cuarto Real de Santo Domingo",                        "descripcion": "Salón palatino nazarí del siglo XIII con una de las yeserías islámicas más refinadas de Granada, integrado hoy en un jardín municipal.",                                       "latitud": 37.171700,              "longitud": -3.594911},
    {"id": 15, "nombre": "Alcazaba (Alhambra)",                                 "descripcion": "La parte más antigua de la Alhambra, fortaleza militar del siglo IX ampliada en el XIII, desde cuya Torre de la Vela se domina toda Granada.",                                 "latitud": 37.177133,              "longitud": -3.591810},
    {"id": 16, "nombre": "Corral del Carbón",                                   "descripcion": "Antiguo alhóndiga nazarí del siglo XIV, el mejor conservado de la Península. Fue almacén de carbón en época cristiana y hoy es sede cultural.",                               "latitud": 37.174936,              "longitud": -3.597878},
    {"id": 17, "nombre": "Palacios Nazaríes (Alhambra)",                        "descripcion": "Conjunto palaciego nazarí de los siglos XIII y XIV, cumbre del arte islámico en Occidente, con el Patio de los Leones y el Patio de los Arrayanes como joyas principales.",   "latitud": 37.177383,              "longitud": -3.589630},
    {"id": 18, "nombre": "Generalife (Alhambra)",                               "descripcion": "Palacio de recreo y jardines de los sultanes nazaríes, declarado Patrimonio de la Humanidad junto a la Alhambra. Sus acequias y jardines son únicos en el mundo.",             "latitud": 37.176954,              "longitud": -3.585218},
    {"id": 19, "nombre": "Puerta del Vino",                                     "descripcion": "Puerta interior de la Alhambra del siglo XIV que conectaba la medina con la alcazaba. Su nombre proviene de que aquí se vendía vino exento de impuestos.",                      "latitud": 37.176674,              "longitud": -3.590740},
    {"id": 20, "nombre": "Puerta de los Siete Suelos",                          "descripcion": "Acceso meridional a la Alhambra rodeado de leyendas. Según la tradición, Boabdil abandonó la ciudad por esta puerta tras la Reconquista.",                                     "latitud": 37.174780,              "longitud": -3.586738},
    {"id": 21, "nombre": "La Madraza",                                          "descripcion": "Universidad islámica fundada en 1349 por Yusuf I, la primera de la Península Ibérica. Conserva una espléndida sala de oraciones con decoración nazarí.",                        "latitud": 37.176209,              "longitud": -3.598029},
    {"id": 22, "nombre": "Maristán",                                            "descripcion": "Hospital psiquiátrico nazarí del siglo XIV, uno de los primeros centros de salud mental del mundo. Solo se conservan restos de su patio y fuente.",                             "latitud": 37.178727,              "longitud": -3.592840},
    {"id": 23, "nombre": "Palacio de Dar al-Horra",                             "descripcion": "Palacio nazarí del siglo XV residencia de Aixa, madre de Boabdil. Es uno de los palacios islámicos mejor conservados fuera de la Alhambra.",                                  "latitud": 37.181625,              "longitud": -3.596362},
    {"id": 24, "nombre": "Dar al-Arusa",                                        "descripcion": "Pequeño palacio nazarí situado en las laderas del Generalife, con restos de decoración geométrica y vegetal de gran delicadeza.",                                               "latitud": 37.176449,              "longitud": -3.580661},
    {"id": 25, "nombre": "Puerta de Bib Rambla",                                "descripcion": "Antigua puerta de la medina nazarí que daba acceso a la plaza principal de la ciudad islámica, hoy desaparecida como estructura pero recordada en la plaza homónima.",         "latitud": 37.175545,              "longitud": -3.589992},
    {"id": 26, "nombre": "Torre del Aceituno (San Miguel Alto)",                "descripcion": "Torre defensiva nazarí integrada en el cerro de San Miguel, con vistas panorámicas excepcionales sobre el Albaicín y la Alhambra.",                                            "latitud": 37.184978,              "longitud": -3.587461},
    {"id": 27, "nombre": "Convento de San Francisco (casa de nobleza nazarí)",  "descripcion": "Antiguo palacio nazarí convertido en convento franciscano tras la Reconquista. Isabel la Católica fue enterrada aquí provisionalmente antes de ser trasladada a la Capilla Real.", "latitud": 37.175844,             "longitud": -3.587041},
    {"id": 28, "nombre": "Casa del Chapiz",                                     "descripcion": "Conjunto de dos cármenes moriscos del siglo XVI que hoy alberga la Escuela de Estudios Árabes. Ejemplo excepcional de arquitectura doméstica nazarí tardía.",                  "latitud": 37.180980,              "longitud": -3.588364},
    {"id": 29, "nombre": "Casa de Zafra",                                       "descripcion": "Casa nazarí del siglo XIV con patio central y alberca, excavada y restaurada como muestra de la arquitectura doméstica islámica del Albaicín.",                                 "latitud": 37.178851,              "longitud": -3.592543},
    {"id": 30, "nombre": "Casa del Cuerno de Oro",                              "descripcion": "Vivienda nazarí del Albaicín con elementos decorativos originales conservados, que ilustra la vida doméstica en la Granada medieval.",                                          "latitud": 37.179809,              "longitud": -3.589307},
    {"id": 31, "nombre": "Alcaicería",                                          "descripcion": "Antiguo zoco nazarí de la seda, el más importante del reino de Granada. Fue reconstruido en el siglo XIX tras un incendio, manteniendo su trazado original de callejuelas.",  "latitud": 37.175370,              "longitud": -3.599195},

    # IMPERIAL
    {"id": 32, "nombre": "Monasterio de San Jerónimo",                          "descripcion": "Primer monasterio construido en Granada tras la Reconquista, encargado por los Reyes Católicos. Alberga el sepulcro del Gran Capitán Gonzalo Fernández de Córdoba.",          "latitud": 37.179485,              "longitud": -3.603562},
    {"id": 33, "nombre": "Convento de Santa Isabel la Real",                    "descripcion": "Convento fundado por Isabel la Católica en 1501 sobre un palacio nazarí del que conserva restos en su iglesia y claustro.",                                                     "latitud": 37.181112,              "longitud": -3.596089},
    {"id": 34, "nombre": "Hospital Real de Granada",                            "descripcion": "Mandado construir por los Reyes Católicos en 1504, es uno de los hospitales renacentistas más importantes de España. Hoy sede de la Biblioteca Universitaria.",               "latitud": 37.184937,              "longitud": -3.601050},
    {"id": 35, "nombre": "Capilla Real de Granada",                             "descripcion": "Panteón real mandado construir por los Reyes Católicos para su enterramiento. Alberga sus sepulcros junto a los de Felipe el Hermoso y Juana la Loca.",                        "latitud": 37.176210,              "longitud": -3.598782},
    {"id": 36, "nombre": "Lonja de Granada",                                    "descripcion": "Edificio renacentista del siglo XVI construido junto a la Catedral para albergar las transacciones comerciales de la ciudad.",                                                   "latitud": 37.176024,              "longitud": -3.598602},
    {"id": 37, "nombre": "Catedral de Granada",                                 "descripcion": "Primera catedral renacentista de España, iniciada en 1523 sobre la antigua mezquita mayor. Destaca su monumental Capilla Mayor diseñada por Diego de Siloé.",                  "latitud": 37.176460,              "longitud": -3.599318},
    {"id": 38, "nombre": "Iglesia de San Matías",                               "descripcion": "Templo renacentista del siglo XVI levantado sobre una mezquita del barrio de la Medina, con una notable portada plateresca.",                                                  "latitud": 37.173680,              "longitud": -3.596510},
    {"id": 39, "nombre": "Palacio de Carlos V",                                 "descripcion": "Monumental palacio renacentista iniciado en 1527 en el interior de la Alhambra por orden de Carlos I. Su patio circular es único en la arquitectura española.",               "latitud": 37.176776,              "longitud": -3.590204},
    {"id": 40, "nombre": "Casa de los Tiros",                                   "descripcion": "Palacio del siglo XVI con fachada almenada y cañones decorativos que le dan nombre. Hoy alberga el Museo Casa de los Tiros con fondos sobre la historia de Granada.",         "latitud": 37.174750,              "longitud": -3.595531},
    {"id": 41, "nombre": "Puerta de las Granadas",                              "descripcion": "Arco triunfal renacentista del siglo XVI que marca el acceso al bosque de la Alhambra, coronado por tres granadas heráldicas.",                                               "latitud": 37.176039,              "longitud": -3.593074},
    {"id": 42, "nombre": "Pilar de Carlos V",                                   "descripcion": "Fuente monumental renacentista de 1545 situada a la entrada de la Alhambra, con mascarones que representan los ríos Darro, Genil y Beiro.",                                    "latitud": 37.175866,              "longitud": -3.590072},
    {"id": 43, "nombre": "Plaza Nueva",                                         "descripcion": "Primera plaza porticada construida en Granada tras la Reconquista, en el siglo XVI. Sobre ella se construyó la Real Chancillería y es hoy el centro neurálgico del barrio.",  "latitud": 37.176849,              "longitud": -3.595971},
    {"id": 44, "nombre": "Plaza de Bib-Rambla",                                 "descripcion": "Antigua plaza mayor de la Granada islámica reconvertida en espacio cristiano tras la Reconquista. Escenario de autos de fe, torneos y mercados durante los siglos XVI y XVII.", "latitud": 37.175186,             "longitud": -3.599798},
    {"id": 45, "nombre": "Palacio Arzobispal",                                  "descripcion": "Sede del Arzobispado de Granada desde el siglo XVI, con una fachada barroca del XVIII y un patio interior renacentista de gran elegancia.",                                    "latitud": 37.175716,              "longitud": -3.599616},
    {"id": 46, "nombre": "Iglesia de Santo Domingo",                            "descripcion": "Templo dominico del siglo XVI patrocinado por los Reyes Católicos, con una portada plateresca y una bella capilla funeraria.",                                                 "latitud": 37.172964,              "longitud": -3.594482},
    {"id": 47, "nombre": "Palacio de los Córdova",                              "descripcion": "Palacio renacentista del siglo XVII situado junto al Darro, hoy sede del Archivo Municipal de Granada. Su portada y patio interior son notables ejemplos del estilo.",        "latitud": 37.179798,              "longitud": -3.587165},
    {"id": 48, "nombre": "Palacio de la Madraza (Ayuntamiento Viejo)",          "descripcion": "Edificio que integra restos de la antigua madraza nazarí con reformas barrocas del siglo XVIII cuando fue sede del Ayuntamiento de Granada.",                                 "latitud": 37.176086,              "longitud": -3.598151},
    {"id": 49, "nombre": "Real Chancillería",                                   "descripcion": "Alto tribunal de justicia fundado por los Reyes Católicos en 1505, con una monumental fachada renacentista y un patio con columnas dóricas.",                                  "latitud": 37.177388,              "longitud": -3.595179},

    # BARROCA
    {"id": 50, "nombre": "Abadía del Sacromonte",                               "descripcion": "Monasterio barroco del siglo XVII fundado sobre las cuevas donde se hallaron las reliquias de San Cecilio, primer obispo de Granada. Centro de peregrinación y sede de los famosos libros plúmbeos.", "latitud": 37.183179, "longitud": -3.577104},
    {"id": 51, "nombre": "Monasterio de la Cartuja",                            "descripcion": "Cartuja del siglo XVI con uno de los interiores barrocos más exuberantes de España, obra de los siglos XVII y XVIII. Su sacristía es considerada la cumbre del barroco español.", "latitud": 37.192004,            "longitud": -3.599302},
    {"id": 52, "nombre": "Iglesia del Sagrario",                                "descripcion": "Iglesia barroca del siglo XVIII adosada a la Catedral de Granada, construida sobre la antigua mezquita mayor. Su interior es de una gran riqueza ornamental.",                "latitud": 37.175921,              "longitud": -3.599036},
    {"id": 53, "nombre": "Iglesia de San Justo y Pastor",                       "descripcion": "Templo barroco del siglo XVIII con una destacada colección de arte sacro y una fachada de gran sobriedad clasicista.",                                                         "latitud": 37.178940,              "longitud": -3.601161},
    {"id": 54, "nombre": "Basílica y monasterio de San Juan de Dios",           "descripcion": "Basílica barroca del siglo XVIII dedicada al fundador de la Orden Hospitalaria. Su interior dorado es uno de los más impresionantes del barroco granadino.",                  "latitud": 37.180974,              "longitud": -3.602460},
    {"id": 55, "nombre": "Iglesia de Nuestra Señora del Perpetuo Socorro",      "descripcion": "Templo barroco granadino con una imagen muy venerada de la Virgen del Perpetuo Socorro, sede de una de las cofradías más activas de la ciudad.",                              "latitud": 37.179951,              "longitud": -3.602287},
    {"id": 56, "nombre": "Iglesia de San Miguel Alto",                          "descripcion": "Ermita barroca del siglo XVII situada en el cerro de San Miguel, con magníficas vistas sobre Granada. Es el punto más alto del Albaicín accesible al público.",              "latitud": 37.185127,              "longitud": -3.587101},
    {"id": 57, "nombre": "Basílica de Nuestra Señora de las Angustias",         "descripcion": "Basílica barroca del siglo XVII dedicada a la patrona de Granada. Su camarín de la Virgen es una obra maestra de la decoración barroca granadina.",                          "latitud": 37.170830,              "longitud": -3.595048},
    {"id": 58, "nombre": "Iglesia del Corpus Christi",                          "descripcion": "Templo barroco situado en el sur de Granada, con una notable colección de pinturas y esculturas del siglo XVII.",                                                             "latitud": 37.156888,              "longitud": -3.595533},
    {"id": 59, "nombre": "Colegio de San Pablo",                                "descripcion": "Antiguo colegio jesuita del siglo XVI hoy integrado en la Universidad de Granada. Su iglesia barroca conserva una rica decoración interior.",                                 "latitud": 37.177662,              "longitud": -3.601755},

    # MUDÉJAR
    {"id": 60, "nombre": "Iglesia de San José",                                 "descripcion": "Una de las iglesias mudéjares más antiguas de Granada, levantada sobre la mezquita del barrio con su alminar árabe reconvertido en campanario.",                              "latitud": 37.178646,              "longitud": -3.596156},
    {"id": 61, "nombre": "Iglesia de San Gil y Santa Ana",                      "descripcion": "Iglesia mudéjar del siglo XVI a orillas del Darro, con un esbelto campanario que es uno de los más fotografiados de Granada.",                                               "latitud": 37.177526,              "longitud": -3.594460},
    {"id": 62, "nombre": "Iglesia de San Cristóbal",                            "descripcion": "Templo mudéjar del siglo XVI situado en lo alto del Albaicín, con vistas excepcionales a la Alhambra y rodeado de uno de los miradores más tranquilos del barrio.",         "latitud": 37.183585,              "longitud": -3.596459},
    {"id": 63, "nombre": "Iglesia de San Miguel Bajo",                          "descripcion": "Iglesia mudéjar que preside la plaza de San Miguel Bajo, corazón de la vida vecinal del Albaicín y punto de encuentro entre vecinos y visitantes.",                          "latitud": 37.180681,              "longitud": -3.596714},
    {"id": 64, "nombre": "Iglesia de San Ildefonso",                            "descripcion": "Templo mudéjar del siglo XVI con una torre campanario de clara influencia islámica, situado en el límite entre el Albaicín y el centro histórico.",                          "latitud": 37.183841,              "longitud": -3.599356},
    {"id": 65, "nombre": "Iglesia de San Andrés",                               "descripcion": "Iglesia mudéjar del siglo XVI con una notable torre alminar reutilizada como campanario, testimonio de la superposición religiosa tras la Reconquista.",                      "latitud": 37.181138,              "longitud": -3.599313},
    {"id": 66, "nombre": "Iglesia de San Nicolás",                              "descripcion": "Templo mudéjar del siglo XVI frente al célebre mirador de San Nicolás, con las mejores vistas de la Alhambra y Sierra Nevada como telón de fondo.",                         "latitud": 37.181352,              "longitud": -3.592519},
    {"id": 67, "nombre": "Casa de los Pisa",                                    "descripcion": "Casa señorial del siglo XVI donde murió San Juan de Dios en 1550. Hoy es museo y conserva objetos personales del santo y documentos de la época.",                           "latitud": 37.177719,              "longitud": -3.595212},

    # SIGLO XIX
    {"id": 68, "nombre": "Cementerio de San José",                              "descripcion": "Cementerio romántico del siglo XIX con panteones neogóticos y esculturas funerarias de gran valor artístico, reflejo del gusto estético de la burguesía granadina.",        "latitud": 37.169760,              "longitud": -3.578410},
    {"id": 69, "nombre": "Silla del Moro",                                      "descripcion": "Torre de vigilancia nazarí reconvertida en mirador romántico en el siglo XIX. Según la leyenda, Boabdil contemplaba desde aquí la Alhambra tras su destierro.",             "latitud": 37.178364,              "longitud": -3.583844},
    {"id": 70, "nombre": "Calle Reyes Católicos",                               "descripcion": "Gran eje urbano trazado en el siglo XIX sobre el antiguo cauce del río Darro, que transformó radicalmente la morfología del centro histórico de Granada.",                  "latitud": 37.175390,              "longitud": -3.598120},
    {"id": 71, "nombre": "Puente Verde",                                        "descripcion": "Puente de hierro del siglo XIX sobre el río Genil, ejemplo de la ingeniería industrial romántica que modernizó las infraestructuras de Granada.",                            "latitud": 37.167246,              "longitud": -3.589450},
    {"id": 72, "nombre": "Paseo del Salón",                                     "descripcion": "Paseo arbolado a orillas del Genil diseñado en el siglo XIX como espacio de recreo burgués, con fuentes, estatuas y una alameda que sigue siendo muy frecuentada.",         "latitud": 37.169266,              "longitud": -3.594852},
    {"id": 73, "nombre": "Ayuntamiento de Granada",                             "descripcion": "Edificio neoclásico del siglo XIX sede del gobierno municipal de Granada, con una fachada austera y un interior con pinturas históricas de gran valor.",                     "latitud": 37.174203,              "longitud": -3.598626},
    {"id": 74, "nombre": "Plaza de Mariana Pineda",                             "descripcion": "Plaza dedicada a la heroína liberal granadina ajusticiada en 1831. En su centro se alza una estatua en su honor, en el barrio donde vivió y fue detenida.",               "latitud": 37.172271,              "longitud": -3.597137},
    {"id": 75, "nombre": "Carmen de los Mártires",                              "descripcion": "Jardines románticos del siglo XIX en la ladera de la Alhambra, con estanques, grutas y una arquitectura paisajística que mezcla influencias árabes y europeas.",           "latitud": 37.172741,              "longitud": -3.585955},
    {"id": 76, "nombre": "Casa de Mariana Pineda",                              "descripcion": "Vivienda donde nació y vivió Mariana Pineda, heroína del liberalismo español. Hoy reconocida con una placa conmemorativa en su fachada.",                                   "latitud": 37.173126,              "longitud": -3.603095},

    # SIGLO XX
    {"id": 77, "nombre": "Gran Vía de Colón",                                   "descripcion": "Gran bulevar trazado a finales del siglo XIX e inaugurado en 1904, que transformó el tejido medieval del centro de Granada demoliendo manzanas históricas.",               "latitud": 37.182905,              "longitud": -3.601995},
    {"id": 78, "nombre": "Gobierno Civil de Granada",                           "descripcion": "Edificio institucional del siglo XX de estilo racionalista, sede histórica del gobierno provincial de Granada.",                                                              "latitud": 37.178194,              "longitud": -3.602791},
    {"id": 79, "nombre": "Puerta Real",                                         "descripcion": "Nudo urbano del centro de Granada que en el siglo XX se convirtió en el principal punto de confluencia comercial y de transporte de la ciudad.",                             "latitud": 37.173561,              "longitud": -3.599572},
    {"id": 80, "nombre": "Alhambra Palace",                                     "descripcion": "Hotel de lujo inaugurado en 1910 en estilo neoárabe, situado en la ladera de la Alhambra. Fue escenario de congresos internacionales y visitas de personalidades del siglo XX.", "latitud": 37.173972,             "longitud": -3.590134},
    {"id": 81, "nombre": "Iglesia del Sagrado Corazón",                         "descripcion": "Templo neogótico del siglo XX construido por los jesuitas en el centro de Granada, con una fachada de piedra y un interior de gran altura y luminosidad.",                 "latitud": 37.178864,              "longitud": -3.598873},
    {"id": 82, "nombre": "Fundación Rodríguez-Acosta",                          "descripcion": "Carmen-estudio del pintor granadino José María Rodríguez-Acosta, construido entre 1914 y 1930. Combina arquitectura racionalista con jardines escalonados de inspiración nazarí.", "latitud": 37.175017,            "longitud": -3.592642},
    {"id": 83, "nombre": "Huerta de San Vicente",                               "descripcion": "Casa de veraneo de la familia García Lorca donde el poeta escribió algunas de sus obras más importantes entre 1926 y 1936. Hoy es museo lorquiano.",                        "latitud": 37.170598,              "longitud": -3.609395},
    {"id": 84, "nombre": "Calle Ángel Ganivet",                                 "descripcion": "Calle peatonal del centro de Granada dedicada al escritor regeneracionista granadino Ángel Ganivet, uno de los precursores de la Generación del 98.",                       "latitud": 37.173258,              "longitud": -3.598867},
    {"id": 85, "nombre": "Parque de las Ciencias",                              "descripcion": "Museo interactivo de ciencias inaugurado en 1995, el más visitado de Andalucía. Incluye planetario, mariposas vivas y exposiciones permanentes sobre astronomía y naturaleza.", "latitud": 37.162706,             "longitud": -3.605758},
    {"id": 86, "nombre": "Museo Caja Granada",                                  "descripcion": "Edificio de arquitectura contemporánea diseñado por Alberto Campo Baeza en 2007, sede del museo de Caja Granada con colecciones de arte y memoria histórica.",               "latitud": 37.162354,              "longitud": -3.607992},
    {"id": 87, "nombre": "Centro Federico García Lorca",                        "descripcion": "Centro cultural inaugurado en 2015 dedicado a la memoria y obra del poeta granadino. Ocupa el antiguo mercado de San Agustín y alberga el archivo personal de Lorca.",      "latitud": 37.176618,              "longitud": -3.600836},

    # LORQUIANA
    {"id": 88, "nombre": "Casa Natal de Federico García Lorca (Fuente Vaqueros)","descripcion": "Casa donde nació Federico García Lorca el 5 de junio de 1898. Convertida en museo en 1986, conserva muebles originales, fotografías y documentos de la familia Lorca.",  "latitud": 37.231675,              "longitud": -3.745574},
    {"id": 89, "nombre": "Casa Museo Federico García Lorca (Valderrubio)",      "descripcion": "Casa donde pasó su infancia Lorca y que inspiró su obra La casa de Bernarda Alba. El ambiente rural de este pueblo dejó una huella profunda en toda su producción literaria.", "latitud": 37.232614,             "longitud": -3.816052},
    {"id": 90, "nombre": "Casa de Federico García Lorca (Acera del Darro)",     "descripcion": "Primera vivienda urbana de la familia García Lorca en Granada, donde Federico vivió durante su primera etapa en la ciudad antes de trasladarse a otras residencias.",        "latitud": 37.171147,              "longitud": -3.598585},
    {"id": 91, "nombre": "Casa de Federico García Lorca (Acera del Casino)",    "descripcion": "Vivienda granadina de la familia Lorca en el centro de la ciudad, desde donde el poeta frecuentaba los cafés y tertulias literarias del entorno.",                          "latitud": 37.172354,              "longitud": -3.598654},
    {"id": 92, "nombre": "Universidad de Granada - Facultad de Derecho",        "descripcion": "Facultad donde Lorca estudió Derecho y Filosofía y Letras entre 1915 y 1919, aunque su verdadera pasión era la música, la poesía y el teatro.",                             "latitud": 37.178306,              "longitud": -3.601361},
    {"id": 93, "nombre": "Café Alameda",                                        "descripcion": "Célebre café granadino frecuentado por Lorca y la intelectualidad granadina de principios del siglo XX, escenario de tertulias literarias y musicales.",                     "latitud": 37.172374,              "longitud": -3.598032},
    {"id": 94, "nombre": "Casa de Emilia Llanos",                               "descripcion": "Residencia de la mecenas granadina Emilia Llanos, amiga íntima de Lorca que le acogió durante la represión de 1936. Un espacio clave en los últimos días del poeta.",        "latitud": 37.175040,              "longitud": -3.595059},
    {"id": 95, "nombre": "Casa de Manuel de Falla",                             "descripcion": "Carmen donde vivió el compositor gaditano Manuel de Falla durante su etapa granadina entre 1921 y 1939, hoy museo. Aquí forjó su amistad con Lorca y organizaron el Concurso de Cante Jondo.", "latitud": 37.173393, "longitud": -3.588671},
    {"id": 96, "nombre": "Plaza de los Aljibes",                                "descripcion": "Plaza de la Alhambra donde Lorca y Falla organizaron el histórico Concurso de Cante Jondo de 1922, evento que marcó el renacimiento del flamenco tradicional.",              "latitud": 37.177039,              "longitud": -3.590944},
    {"id": 97, "nombre": "Casa de los Rosales",                                 "descripcion": "Casa de la familia Rosales donde Lorca se refugió en agosto de 1936 tras el inicio de la Guerra Civil. Fue detenido aquí el 16 de agosto antes de su fusilamiento.",         "latitud": 37.176190,              "longitud": -3.602610},
    {"id": 98, "nombre": "Colonia de Víznar",                                   "descripcion": "Pequeño pueblo de la Vega de Granada donde Lorca fue trasladado tras su detención. Desde aquí fue llevado al lugar de su fusilamiento en el barranco cercano.",             "latitud": 37.235761,              "longitud": -3.549536},
    {"id": 99, "nombre": "Barranco de Víznar",                                  "descripcion": "Lugar donde Federico García Lorca fue fusilado en agosto de 1936 junto a otros represaliados. Hoy es un parque memorial en su honor y el de todas las víctimas.",           "latitud": 37.240233,              "longitud": -3.543299},
    {"id": 100,"nombre": "Antiguo Gobierno Civil de Granada",                   "descripcion": "Edificio donde Lorca fue llevado tras su detención y donde quedó registrada su detención antes de ser trasladado a Víznar. Símbolo de la represión franquista en Granada.",  "latitud": 37.180848,              "longitud": -3.605540},
]

rutas_data = [
    {
        "id": 1,
        "nombre": "Granada Islámica (siglos XI-XV)",
        "descripcion": "Ruta por los principales restos de la Granada musulmana.",
        "puntos_ids": list(range(1, 32))
    },
    {
        "id": 2,
        "nombre": "Granada Cristiana e Imperial (siglos XV-XVI)",
        "descripcion": "Monumentos tras la conquista cristiana.",
        "puntos_ids": [32, 27] + list(range(33, 50))
    },
    {
        "id": 3,
        "nombre": "Granada Barroca (siglos XVII-XVIII)",
        "descripcion": "Arquitectura barroca religiosa de Granada.",
        "puntos_ids": [50, 51, 52, 37] + list(range(53, 60))
    },
    {
        "id": 4,
        "nombre": "Granada Mudéjar",
        "descripcion": "Edificios cristianos con influencia islámica.",
        "puntos_ids": list(range(60, 67)) + [40, 28, 47, 67]
    },
    {
        "id": 5,
        "nombre": "Granada del Siglo XIX",
        "descripcion": "Espacios urbanos del siglo XIX.",
        "puntos_ids": list(range(68, 77)) + [59, 43]
    },
    {
        "id": 6,
        "nombre": "Granada del Siglo XX",
        "descripcion": "Arquitectura y urbanismo contemporáneo.",
        "puntos_ids": list(range(77, 88))
    },
    {
        "id": 7,
        "nombre": "Granada Lorquiana",
        "descripcion": "Lugares vinculados a Federico García Lorca.",
        "puntos_ids": list(range(88, 97)) + [80, 83, 97, 98, 99, 100, 87]
    },
]

# Insertar puntos
#for p in puntos_data:
#    punto = Punto(**p)
#    db.merge(punto)

for r in rutas_data:
    ruta = Ruta(
        id=r["id"],
        nombre=r["nombre"],
        descripcion=r["descripcion"]
    )

    db.add(ruta)  # 🔥 IMPORTANTE: meter en sesión primero

    ruta.puntos = [
        db.get(Punto, pid) for pid in r["puntos_ids"]
        if db.get(Punto, pid) is not None
    ]

db.commit()
db.close()
print("✅ Base de datos poblada correctamente")
