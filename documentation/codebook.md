# Codebook
This table describe all the head columns of are used in the processed_data and intermediate data.


|Tags           |Type    |Unit      | Description  |
|---------------|--------|----------|---|
|Cantons|string|-|Official designation of canton with two uppercase chars|
|UnivEdu|float|nb persons|Calculated estimation of number of person with a university diploma or equivalent ("haute école")|
|SurfHabAndInf|float|square km|Surface in square km of the habitable and of the infrastructures of the canton|
|SurfTotal|float|square km|Surface in square km of the canton|
|PopTotal|integer|nb persons|Pupulation of the canton|
|PopBySurfHabAndInf|float| - |Ratio PopTotal/SurfHabAndInf|
|PopBySurfTotal|float| - |Ratio of PopTotal/SurfTotal|
|RatPopUnivLevel|float| - |Ratio of UnivEdu/PopTotal|
