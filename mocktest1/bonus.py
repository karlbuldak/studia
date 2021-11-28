def bonus(years):
    if years <= 5:
        kasa = years*100
    if years <= 8 and years > 5:
        kasa = 5*100 + (years-5) *200
    if years > 8:
        kasa = 1100 + (years-8) * 50
    return(kasa)

