# Codebook
This table describes all the head columns used in the intermediate and processed data.


Tags | Type | Unit | Description | Data files | Sources
--- | --- | --- | --- | --- | ---
Cantons | string | - | Official designation of canton with two uppercase chars | cantons_surf_pop.csv, cantons_surf_edu.csv, cantons_surf_pop_edu.csv | https://en.wikipedia.org/wiki/Cantons_of_Switzerland
UnivEdu | float | nb persons | Estimated number of persons holding a university degree or equivalent ("haute école") | cantons_surf_edu.csv, cantons_surf_pop_edu.csv | T_02_02_1_01.xls
SurfHabAndInf | float | square km | Habitable and infrastructures surface of cantons | cantons_surf_pop.csv, cantons_surf_pop_edu.csv | su-f-40.02.15.08.03-2016.xlsx
SurfTotal | float | square km | Surface of the cantons | cantons_surf_pop.csv, cantons_surf_pop_edu.csv | su-f-40.02.15.08.03-2016.xlsx
PopTotal | integer | nb persons | Pupulation of the canton | cantons_surf_pop.csv, cantons_surf_pop_edu.csv | su-f-40.02.15.08.03-2016.xlsx
PopBySurfHabAndInf | float |  -  | Ratio PopTotal/SurfHabAndInf | cantons_surf_pop_edu.csv | su-f-40.02.15.08.03-2016.xlsx
PopBySurfTotal | float |  -  | Ratio of PopTotal/SurfTotal | cantons_surf_pop_edu.csv | su-f-40.02.15.08.03-2016.xlsx
RatPopUnivLevel | float |  -  | Ratio of UnivEdu/PopTotal | cantons_surf_pop_edu.csv | T_02_02_1_01.xls, su-f-40.02.15.08.03-2016.xlsx
