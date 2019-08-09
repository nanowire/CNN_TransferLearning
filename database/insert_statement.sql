UPDATE properties prt
SET (status, listprice, soldprice, listdate, solddate, expireddate, dom, dto, address, city, state, zip, area, beds,
     baths, sqft, age, lotsize, agentname, officename, officephone, showinginstructions, remarks, style, level, garage,
     heating, cooling, elementaryschool, juniorhighschool, highschool, otherfeatures, proptype, streetname, housenum1,
     housenum2, photourl) = (SELECT status
                                  , listprice
                                  , soldprice
                                  , listdate
                                  , solddate
                                  , expireddate
                                  , dom
                                  , dto
                                  , address
                                  , city
                                  , state
                                  , zip
                                  , area
                                  , beds
                                  , baths
                                  , sqft
                                  , age
                                  , lotsize
                                  , agentname
                                  , officename
                                  , officephone
                                  , showinginstructions
                                  , remarks
                                  , style
                                  , floorlevel
                                  , garage
                                  , heating
                                  , cooling
                                  , elementaryschool
                                  , juniorhighschool
                                  , highschool
                                  , otherfeatures
                                  , proptype
                                  , streetname
                                  , housenum1
                                  , housenum2
                                  , photourl
                                FROM (SELECT mlsnum
                                           , status                                                          status
                                           , REPLACE(listprice, ',', '') :: NUMERIC(12, 2)                   listprice
                                           , REPLACE(soldprice, ',', '') :: NUMERIC(12, 2)                   soldprice
                                           , listdate
                                           , solddate
                                           , expireddate
                                           , SUBSTRING(dom, '([0-9]{1,4})')::INTEGER::INTEGER                dom
                                           , SUBSTRING(dto, '([0-9]{1,4})')::INTEGER                         dto
                                           , INITCAP(address)                                                address
                                           , INITCAP(city)                                                   city
                                           , upper(state)                                                    state
                                           , zip::INTEGER                                                    zip
                                           , area
                                           , beds::INTEGER                                                   beds
                                           , baths::NUMERIC(5, 2)                                            baths
                                           , REPLACE(sqft, ',', '')::NUMERIC(12, 2)                          sqft
                                           , CASE
                                                WHEN replace(age, ',', '')::NUMERIC < 0 THEN NULL
                                                ELSE age::INTEGER END                                        age
                                           , REPLACE(lotsize, ',', '')::NUMERIC(12, 2)                       lotsize
                                           , agentname
                                           , officename
                                           , officephone
                                           , showinginstructions
                                           , initcap(remarks)                                                remarks
                                           , initcap(style)                                                  style
                                           , (CASE WHEN level > '99' THEN '-1' ELSE level END)::INTEGER      floorlevel
                                           , SUBSTRING(garage, '([0-9]{1,4})')::INTEGER                      garage
                                           , heating
                                           , cooling
                                           , elementaryschool
                                           , juniorhighschool
                                           , highschool
                                           , otherfeatures
                                           , CASE WHEN LENGTH(proptype) > 2 THEN NULL ELSE proptype END      proptype
                                           , INITCAP(streetname)                                             streetname
                                           , (CASE
                                                 WHEN housenum1 > '99999' THEN NULL
                                                 ELSE SUBSTRING(housenum1, '([0-9]{1,4})') END) :: INTEGER   housenum1
                                           , housenum2
                                           , photourl
                                           , row_number() OVER (PARTITION BY mlsnum ORDER BY CASE
                                                                                                WHEN status IN ('SLD', 'UAG', 'CTG')
                                                                                                   THEN 1
                                                                                                WHEN status IN ('PCG')
                                                                                                   THEN 2
                                                                                                WHEN status IN ('ACT', 'NEW', 'BOM')
                                                                                                   THEN 3
                                                                                                ELSE 4 END ) row_number
                                         FROM load_properties lpr
                                         WHERE LENGTH(proptype) = 2
                                           AND lpr.status IS NOT NULL
                                           AND lpr.mlsnum = prt.mlsnum
                                           AND EXISTS(SELECT 1
                                                         FROM properties prt
                                                         WHERE prt.mlsnum = lpr.mlsnum)) lists
                                WHERE lists.row_number = 1)
   WHERE EXISTS(SELECT 1
                   FROM load_properties lpr
                   WHERE prt.mlsnum = lpr.mlsnum
                     AND LENGTH(proptype) = 2
                     AND lpr.status IS NOT NULL);

INSERT INTO properties
   ( mlsnum, status, listprice, soldprice, listdate, solddate, expireddate, dom, dto, address, city, state, zip, area
   , beds, baths, sqft, age, lotsize, agentname, officename, officephone, showinginstructions, remarks, style, level
   , garage, heating, cooling, elementaryschool, juniorhighschool, highschool, otherfeatures, proptype, streetname
   , housenum1, housenum2, photourl)
SELECT mlsnum
     , status
     , listprice
     , soldprice
     , listdate
     , solddate
     , expireddate
     , dom
     , dto
     , address
     , city
     , state
     , zip
     , area
     , beds
     , baths
     , sqft
     , age
     , lotsize
     , agentname
     , officename
     , officephone
     , showinginstructions
     , remarks
     , style
     , floorlevel
     , garage
     , heating
     , cooling
     , elementaryschool
     , juniorhighschool
     , highschool
     , otherfeatures
     , proptype
     , streetname
     , housenum1
     , housenum2
     , photourl
   FROM (SELECT mlsnum
              , status                                                                       status
              , replace(listprice, ',', '') :: NUMERIC(12, 2)                                listprice
              , replace(soldprice, ',', '') :: NUMERIC(12, 2)                                soldprice
              , listdate
              , solddate
              , expireddate
              , SUBSTRING(dom, '([0-9]{1,4})')::INTEGER::INTEGER                             dom
              , SUBSTRING(dto, '([0-9]{1,4})')::INTEGER                                      dto
              , INITCAP(address)                                                             address
              , INITCAP(city)                                                                city
              , upper(state)                                                                 state
              , zip::INTEGER                                                                 zip
              , area
              , beds::INTEGER                                                                beds
              , baths::NUMERIC(5, 2)                                                         baths
              , replace(sqft, ',', '')::NUMERIC(12, 2)                                       sqft
              , CASE WHEN replace(age, ',', '')::NUMERIC < 0 THEN NULL ELSE age::INTEGER END age
              , replace(lotsize, ',', '')::NUMERIC(12, 2)                                    lotsize
              , agentname
              , officename
              , officephone
              , showinginstructions
              , initcap(remarks)                                                             remarks
              , initcap(style)                                                               style
              , (CASE WHEN level > '99' THEN '-1' ELSE level END)::INTEGER                   floorlevel
              , SUBSTRING(garage, '([0-9]{1,4})')::INTEGER                                   garage
              , heating
              , cooling
              , elementaryschool
              , juniorhighschool
              , highschool
              , otherfeatures
              , CASE WHEN LENGTH(proptype) > 2 THEN NULL ELSE proptype END                   proptype
              , INITCAP(streetname)                                                          streetname
              , (CASE
                    WHEN housenum1 > '99999' THEN NULL
                    ELSE SUBSTRING(housenum1, '([0-9]{1,4})') END) :: INTEGER                housenum1
              , housenum2
              , photourl
              , row_number() OVER (PARTITION BY mlsnum ORDER BY CASE
                                                                   WHEN status IN ('SLD', 'UAG', 'CTG') THEN 1
                                                                   WHEN status IN ('PCG') THEN 2
                                                                   WHEN status IN ('ACT', 'NEW', 'BOM') THEN 3
                                                                   ELSE 4 END )              row_number
            FROM load_properties lpr
            WHERE LENGTH(proptype) = 2
              AND NOT EXISTS(SELECT 1
                                FROM properties prt
                                WHERE prt.mlsnum = lpr.mlsnum)) lists
   WHERE lists.row_number = 1;
