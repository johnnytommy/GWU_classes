#delimit ;

   infix
      year     1 - 20
      degree   21 - 40
      padeg    41 - 60
      madeg    61 - 80
      spdeg    81 - 100
      sex      101 - 120
      hompop   121 - 140
      income   141 - 160
      rincome  161 - 180
      speduc   181 - 200
      maeduc   201 - 220
      id       221 - 240
      commute  241 - 260
      industry 261 - 280
      sibs     281 - 300
      childs   301 - 320
      age      321 - 340
      educ     341 - 360
      paeduc   361 - 380
      ballot   381 - 400
using GSS.dat;

label variable year     "Gss year for this respondent                       ";
label variable degree   "Rs highest degree";
label variable padeg    "Fathers highest degree";
label variable madeg    "Mothers highest degree";
label variable spdeg    "Spouses highest degree";
label variable sex      "Respondents sex";
label variable hompop   "Number of persons in household";
label variable income   "Total family income";
label variable rincome  "Respondents income";
label variable speduc   "Highest year school completed, spouse";
label variable maeduc   "Highest year school completed, mother";
label variable id       "Respondent id number";
label variable commute  "Travel time to work";
label variable industry "Rs industry code   (1970)";
label variable sibs     "Number of brothers and sisters";
label variable childs   "Number of children";
label variable age      "Age of respondent";
label variable educ     "Highest year of school completed";
label variable paeduc   "Highest year school completed, father";
label variable ballot   "Ballot used for interview";


label define gsp001x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp002x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp003x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp004x
   9        "No answer"
   8        "Don't know"
   7        "Not applicable"
   4        "Graduate"
   3        "Bachelor"
   2        "Junior college"
   1        "High school"
   0        "Lt high school"
;
label define gsp005x
   2        "Female"
   1        "Male"
;
label define gsp006x
   99       "No answer"
   98       "Don't know"
;
label define gsp007x
   99       "No answer"
   98       "Don't know"
   13       "Refused"
   12       "$25000 or more"
   11       "$20000 - 24999"
   10       "$15000 - 19999"
   9        "$10000 - 14999"
   8        "$8000 to 9999"
   7        "$7000 to 7999"
   6        "$6000 to 6999"
   5        "$5000 to 5999"
   4        "$4000 to 4999"
   3        "$3000 to 3999"
   2        "$1000 to 2999"
   1        "Lt $1000"
   0        "Not applicable"
;
label define gsp008x
   99       "No answer"
   98       "Don't know"
   13       "Refused"
   12       "$25000 or more"
   11       "$20000 - 24999"
   10       "$15000 - 19999"
   9        "$10000 - 14999"
   8        "$8000 to 9999"
   7        "$7000 to 7999"
   6        "$6000 to 6999"
   5        "$5000 to 5999"
   4        "$4000 to 4999"
   3        "$3000 to 3999"
   2        "$1000 to 2999"
   1        "Lt $1000"
   0        "Not applicable"
;
label define gsp009x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp010x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp011x
   99       "No answer"
   98       "Don't know"
   97       "97+ minutes"
   -1       "Not applicable"
;
label define gsp012x
   17       "Agricultural production"
   18       "Agricultural services, except horticultural"
   19       "Horticultural services"
   27       "Forestry"
   28       "Fisheries"
   47       "Metal mining"
   48       "Coal mining"
   49       "Crude petroleum and natural gas extractions"
   57       "Nonmetallic mining and quarrying, except fuel"
   67       "General building contractors"
   68       "General contractors, except building"
   69       "Special trade contractors"
   77       "Not specified construction"
   107      "Logging"
   108      "Sawmills, planing mills, and  mill work"
   109      "Miscellaneous wood products"
   118      "Furniture fixtures"
   119      "Glass and glass products"
   127      "Cement concrete, gypsum, and  plaster products"
   128      "Structural clay products"
   137      "Pottery and related products"
   138      "Miscellaneous nonmetallic mineral and stone products"
   139      "Blast furnaces, steel works, rolling and finishing mills"
   147      "Other primary iron and steel industries"
   148      "Primary aluminum industries"
   149      "Other primary nonferrous industries"
   157      "Cutlery, hand tools, and other hardware"
   158      "Fabricated structural metal products"
   159      "Screw machine products"
   167      "Metal stamping"
   168      "Miscellaneous fabricated metal products"
   169      "Not specified metal industries"
   177      "Engines and turbines"
   178      "Farm machinery and equipment"
   179      "Construction and material handling machines"
   187      "Metalworking machinery"
   188      "Office and accounting machines"
   189      "Electronic computing equipment"
   197      "Machinery, except electrical, n.e.c."
   198      "Not specified machinery"
   199      "Household appliances"
   207      "Radio, T.V., and communication equipment"
   208      "Electrical machinery, equipment, and supplies, n.e.c."
   209      "Not specified electrical machinery, equipment, and supplies"
   219      "Motor vehicles and motor vehicle equipment"
   227      "Aircraft and parts"
   228      "Ship and boat building and repairing"
   229      "Railroad locomotives and equipment"
   237      "Mobile dwellings and campers"
   238      "Cycles and miscellaneous transportation equipment"
   239      "Scientific and controlling instruments"
   247      "Optical and health services supplies"
   248      "Photographic equipment and supplies"
   249      "Watches, clocks, and clockwork-operated devices"
   257      "Not specified professional equipment"
   258      "Ordinance"
   259      "Miscellaneous manufacturing industries"
   268      "Meat products"
   269      "Dairy products"
   278      "Canning and preserving fruits, vegetables, and sea foods"
   279      "Grain-mill products"
   287      "Bakery products"
   288      "Confectionery and related products"
   289      "Beverage industries"
   297      "Miscellaneous food preparation and kindred products"
   298      "Not specified food industries"
   299      "Tobacco manufactures"
   307      "Knitting mills"
   308      "Dyeing and finishing textiles, except wool and knit goods"
   309      "Floor coverings, except hard surface"
   317      "Yarn, thread, and fabric mills"
   318      "Miscellaneous textile mill products"
   319      "Apparel and accessories"
   327      "Miscellaneous fabricated textile products"
   328      "Pulp, paper and paperboard mills"
   329      "Miscellaneous paper and pulp products"
   337      "Paperboard containers and boxes"
   338      "Newspaper publishing and printing"
   339      "Printing, publishing, and allied industries, except newspapers"
   347      "Industrial chemicals"
   348      "Plastics, synthetics and resins, except fibers"
   349      "Synthetic fibers"
   357      "Drugs and medicines"
   358      "Soaps and cosmetics"
   359      "Paints, varnishes, and related products"
   367      "Agricultural chemicals"
   368      "Miscellaneous chemicals"
   369      "Not specified chemicals and allied products"
   377      "Petroleum refining"
   378      "Miscellaneous petroleum and coal products"
   379      "Rubber products"
   387      "Miscellaneous plastic products"
   388      "Tanned, curried, and finished leather"
   389      "Footwear, except rubber"
   397      "Leather products, except footwear"
   398      "Not specified manufacturing industries"
   407      "Railroads and railway express"
   408      "Street railways and bus lines"
   409      "Taxicab service"
   417      "Trucking service"
   418      "Warehousing and storage"
   419      "Water transportation"
   427      "Air transportation"
   428      "Pipe lines, except natural gas"
   429      "Services incidental to transportation"
   447      "Radio broadcasting and television"
   448      "Telephone (wire and radio)"
   449      "Telegraph and miscellaneous communication services"
   467      "Electric light and power"
   468      "Electric-gas utilities"
   469      "Gas and steam supply systems"
   477      "Water supply"
   478      "Sanitary services"
   479      "Other and not specified utilities"
   507      "Motor vehicles and equipment"
   508      "Drugs, chemicals, and allied products"
   509      "Dry goods and apparel"
   527      "Food and related products"
   528      "Farm products-raw materials"
   529      "Electrical goods"
   537      "Hardware, plumbing, and heating supplies"
   538      "Not specified electrical and hardware products"
   539      "Machinery equipment and supplies"
   557      "Metals and minerals, n.e.c."
   558      "Petroleum products"
   559      "Scrap and waste materials"
   567      "Alcoholic beverages"
   568      "Paper and its products"
   569      "Lumber and construction materials"
   587      "Wholesalers, n.e.c."
   588      "Not specified wholesale trade"
   607      "Lumber and building material retailing"
   608      "Hardware and farm equipment stores"
   609      "Department and mail order establishments"
   617      "Limited price variety stores"
   618      "Vending machine operators"
   619      "Direct selling establishments"
   627      "Misc. general merchandise stores"
   628      "Grocery stores"
   629      "Dairy product stores"
   637      "Retail bakeries"
   638      "Food stores, n.e.c."
   639      "Motor vehicle dealers"
   647      "Tire, battery, and accessory dealers"
   648      "Gasoline service stations"
   649      "Miscellaneous vehicle dealers"
   657      "Apparel and accessories stores, except shoe stores"
   658      "Shoe stores"
   667      "Furniture and home furnishing stores"
   668      "Household appliances, TV, and radio stores"
   669      "Eating and drinking places"
   677      "Drug stores"
   678      "Liquor stores"
   679      "Farm and garden supply stores"
   687      "Jewelry stores"
   688      "Fuel and ice dealers"
   689      "Retail florists"
   697      "Miscellaneous retail stores"
   698      "Not specified retail trade"
   707      "Banking"
   708      "Credit agencies"
   709      "Security, commodity brokerage, and investment companies"
   717      "Insurance"
   718      "Real estate, incl. real estate-insurance-law offices"
   727      "Advertising"
   728      "Services to dwellings and other buildings"
   729      "Commercial research, development, and testing labs"
   737      "Employment and temporary help agencies"
   738      "Business management and consulting services"
   739      "Computer programming services"
   747      "Detective and protective services"
   748      "Business services, n.e.c."
   749      "Automobile services, except repair"
   757      "Automobile repair and related services"
   758      "Electrical repair shops"
   759      "Miscellaneous repair services"
   769      "Private households"
   777      "Hotels and motels"
   778      "Lodging places, except hotels and motels"
   779      "Laundering, cleaning, and other garment services"
   787      "Beauty shops"
   788      "Barber shops"
   789      "Shoe repair shops"
   797      "Dressmaking shops"
   798      "Miscellaneous personal services"
   807      "Theaters and motion pictures"
   808      "Bowling alleys, billiard and pool parlors"
   809      "Miscellaneous entertainment and recreation services"
   828      "Offices of physicians"
   829      "Offices of dentists"
   837      "Offices of chiropractors"
   838      "Hospitals"
   839      "Convalescent institutions"
   847      "Offices of health practitioners,n.e.c."
   848      "Health services, n.e.c."
   849      "Legal services"
   857      "Elementary and secondary schools"
   858      "Colleges and universities"
   859      "Libraries"
   867      "Educational services, n.e.c."
   868      "Not specified educational services"
   869      "Museums, art galleries, and zoos"
   877      "Religious organizations"
   878      "Welfare services"
   879      "Residential welfare facilities"
   887      "Nonprofit membership organizations"
   888      "Engineering and architectural services"
   889      "Accounting, auditing, and bookkeeping services"
   897      "Miscellaneous professional and related services"
   907      "Postal service"
   917      "Federal public administration"
   927      "State public administration"
   937      "Local public administration"
   IAP      "Not Applicable and No Answer"
;
label define gsp013x
   99       "No answer"
   98       "Don't know"
   -1       "Not applicable"
;
label define gsp014x
   9        "Dk na"
   8        "Eight or more"
;
label define gsp015x
   99       "No answer"
   98       "Don't know"
   89       "89 or older"
;
label define gsp016x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp017x
   99       "No answer"
   98       "Don't know"
   97       "Not applicable"
;
label define gsp018x
   4        "Ballot d"
   3        "Ballot c"
   2        "Ballot b"
   1        "Ballot a"
   0        "Not applicable"
;


label values degree   gsp001x;
label values padeg    gsp002x;
label values madeg    gsp003x;
label values spdeg    gsp004x;
label values sex      gsp005x;
label values hompop   gsp006x;
label values income   gsp007x;
label values rincome  gsp008x;
label values speduc   gsp009x;
label values maeduc   gsp010x;
label values commute  gsp011x;
label values industry gsp012x;
label values sibs     gsp013x;
label values childs   gsp014x;
label values age      gsp015x;
label values educ     gsp016x;
label values paeduc   gsp017x;
label values ballot   gsp018x;


