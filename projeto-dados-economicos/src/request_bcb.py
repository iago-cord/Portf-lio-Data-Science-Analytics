from datetime import date
from functions import buscar_serie_diaria, salvar_json, buscar_serie_mensal

# Request Serie 11 - Selic Efetiva Diaria
serie11 = buscar_serie_diaria(11,date(2000,1,1), date(2026,8,31))
salvar_json('serie11', serie11)

# Request Serie 1178 - Selic Efetiva Diaria Anualizada
serie1178 = buscar_serie_diaria(1178,date(2000,1,1), date(2026,8,31))
salvar_json('serie1178', serie1178)

# Request Serie 4189 - Selic acumulada mês Anualizada
serie4189 = buscar_serie_mensal(4189,date(2000,1,1), date(2026,8,31))
salvar_json('serie4189', serie4189)

# Request Serie 432 - Meta Selic
serie432 = buscar_serie_mensal(432,date(2000,1,1), date(2026,8,31))
salvar_json('serie432', serie432)

# Request Serie 4390 - Selic acumulada mês
serie4390 = buscar_serie_mensal(4390,date(2000,1,1), date(2026,8,31))
salvar_json('serie4390', serie4390)





