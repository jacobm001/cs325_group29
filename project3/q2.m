cost[tomato_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 1*tomato + .75*lettuce +
    .5*spinach + .5*carrot + .45*sunflower + 2.15*tofu + .95*chickpea + 2*oil

energy[tomato_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 21*tomato + 16*lettuce +
    40*spinach + 41*carrot + 585*sunflower + 120*tofu + 164*chickpea + 884*oil

protein[tomato_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := .85*tomato + 1.62*lettuce +
    2.86*spinach + 0.93*carrot + 23.4*sunflower + 16.00*tofu + 9.0*chickpea + 0*oil

fat[tomato_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 0.33*tomato + 0.20*lettuce +
    0.39*spinach + 0.24*carrot + 48.7*sunflower + 5*tofu + 2.6*chickpea + 100.00*oil

carbs[tomato_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 4.64*tomato + 2.37*lettuce +
    3.63*spinach + 9.58*carrot + 15.00*sunflower + 3.00*tofu + 27.0*chickpea + 0*oil

sodium[tomato_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := .009*tomato + .028*lettuce +
    .065*spinach + .069*carrot + .0038*sunflower + .120*tofu + .078*chickpea + 0*oil

data = Minimize[{energy[tomato,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil],
    tomato >= 0
    && lettuce >= 0
    && spinach >= 0
    && carrot >= 0
    && sunflower >= 0
    && tofu >= 0
    && chickpea >= 0
    && oil >= 0
    && protein[tomato,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] >= 15
    && 2 <= fat[tomato,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] <= 8
    && sodium[tomato,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] <= 200
    && carbs[tomato,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] >= 4
    && ((lettuce + spinach)/(tomato+lettuce+spinach+carrot+sunflower+tofu+chickpea+oil)) >= .40
    },
    {tomato,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil}
]

Print["Cost of salad: "]
Print[cost[tomato, lettuce, spinach, carrot, sunflower, tofu, chickpea, oil]/.data[[2]]]

Export["out.csv", data, "csv"]
