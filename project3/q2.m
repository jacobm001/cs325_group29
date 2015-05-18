cost[tomatoe_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 1*tomatoe + .75*lettuce + 
	.5*spinach + .5*carrot + .45*sunflower + 2.15*tofu + .95*chickpea + 2*oil

energy[tomatoe_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 21*tomatoe + 16*lettuce +
	40*spinach + 41*carrot + 585*sunflower + 120*tofu + 164*chickpea + 884*oil

protein[tomatoe_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := .85*tomatoe + 1.62*lettuce +
	2.86*spinach + 0.93*carrot + 23.4*sunflower + 16.00*tofu + 2.6*chickpea + 0*oil

fat[tomatoe_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 0.33*tomatoe + 0.20*lettuce +
	0.39*spinach + 0.24*carrot + 48.7*sunflower + 5*tofu + 2.6*chickpea + 100.00*oil

carbs[tomatoe_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 4.64*tomatoe + 2.37*lettuce +
	3.63*spinach + 9.58*carrot + 15.00*sunflower + 3.00*tofu + 27.0*chickpea + 0*oil

sodium[tomatoe_, lettuce_, spinach_, carrot_, sunflower_, tofu_, chickpea_, oil_] := 9.00*tomatoe + 28.00*lettuce +
	65.00*spinach + 69.00*carrot + 3.80*sunflower + 120.00*tofu + 78.00*chickpea + 0*oil

Minimize[{cost[tomatoe,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil],
	tomatoe >= 0
	&& lettuce >= 0
	&& spinach >= 0
	&& carrot >= 0
	&& sunflower >= 0
	&& tofu >= 0
	&& chickpea >= 0
	&& oil >= 0
	&& ((lettuce + spinach)/(tomatoe+lettuce+spinach+carrot+sunflower+tofu+chickpea+oil)) >= .4
	&& protein[tomatoe,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] >= 15
	&& fat[tomatoe,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] <= 8
	&& fat[tomatoe,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] >= 2
	&& sodium[tomatoe,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil] <= 200
	},
	{tomatoe,lettuce,spinach,carrot,sunflower,tofu,chickpea,oil}
]