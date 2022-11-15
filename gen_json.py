import gettext
import json

import pycountry as pc

thai = gettext.translation('iso3166', pc.LOCALES_DIR, languages=['th'])
all = [{
    **country._fields,
    'name_th': thai.gettext(country.name),
}
    for country in pc.countries
]
print(json.dumps(all, ensure_ascii=False, indent=4))
