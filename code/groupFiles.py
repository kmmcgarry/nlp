def groupFiles():
    both = ["post_2081694.txt","post_3389045.txt","post_4451228.txt","post_5912553.txt","post_7391327.txt","post_2143067.txt","post_3492486.txt","post_4540286.txt","post_5949974.txt","post_7409910.txt","post_2292345.txt","post_3526762.txt","post_4782257.txt","post_6026102.txt","post_7522506.txt","post_2512815.txt","post_3599101.txt","post_4792524.txt","post_6034607.txt","post_7642072.txt","post_3087870.txt","post_3735783.txt","post_4886015.txt","post_6230231.txt","post_7860509.txt","post_3195838.txt","post_4062902.txt","post_5274780.txt","post_6258936.txt","post_8241681.txt","post_3223348.txt","post_4091291.txt","post_5399047.txt","post_6258940.txt","post_8260335.txt","post_3271813.txt","post_4142190.txt","post_5457700.txt","post_6824323.txt","post_3314967.txt","post_4439149.txt","post_5654284.txt","post_6935010.txt","post_3332191.txt","post_4446257.txt","post_5862970.txt","post_7363820.txt"]

    alz =["post_1995614.txt","post_3684971.txt","post_4861406.txt","post_5985372.txt","post_7147517.txt","post_1999230.txt","post_3696123.txt","post_4873436.txt","post_5985550.txt","post_7179011.txt","post_2046212.txt","post_3696798.txt","post_4874866.txt","post_5993924.txt","post_7190828.txt","post_2049425.txt","post_3712227.txt","post_4879099.txt","post_6022319.txt","post_7213353.txt","post_2072065.txt","post_3714737.txt","post_4890065.txt","post_6067363.txt","post_7229137.txt","post_2143076.txt","post_3717718.txt","post_4890389.txt","post_6078014.txt","post_7268998.txt","post_2172662.txt","post_3785064.txt","post_4892050.txt","post_6082745.txt","post_7269247.txt","post_2210910.txt","post_3838867.txt","post_4917755.txt","post_6088520.txt","post_7291951.txt","post_2218754.txt","post_3838981.txt","post_4933769.txt","post_6111402.txt","post_7323419.txt","post_2234892.txt","post_3853624.txt","post_4956203.txt","post_6114374.txt","post_7333766.txt","post_2242327.txt","post_3890635.txt","post_4963646.txt","post_6127540.txt","post_7338331.txt","post_2262174.txt","post_3898999.txt","post_4990312.txt","post_6138544.txt","post_7344861.txt","post_2283299.txt","post_3900423.txt","post_5014291.txt","post_6157196.txt","post_7355991.txt","post_2291884.txt","post_3928036.txt","post_5058816.txt","post_6158390.txt","post_7510239.txt","post_2332406.txt","post_3938984.txt","post_5071761.txt","post_6209385.txt","post_7514961.txt","post_2357972.txt","post_3947145.txt","post_5100342.txt","post_6253699.txt","post_7521966.txt","post_2373497.txt","post_3950109.txt","post_5124907.txt","post_6254507.txt","post_7526967.txt","post_2391344.txt","post_3973445.txt","post_5133930.txt","post_6257817.txt","post_7553926.txt","post_2445457.txt","post_3990942.txt","post_5138276.txt","post_6258942.txt","post_7559427.txt","post_2490747.txt","post_4002436.txt","post_5150097.txt","post_6261652.txt","post_7576021.txt","post_2495114.txt","post_4003311.txt","post_5151519.txt","post_6274384.txt","post_7587564.txt","post_2542770.txt","post_4024357.txt","post_5151919.txt","post_6274393.txt","post_7601629.txt","post_2544179.txt","post_4069198.txt","post_5160266.txt","post_6275753.txt","post_7603881.txt","post_2555771.txt","post_4086214.txt","post_5166101.txt","post_6312255.txt","post_7605114.txt","post_2625193.txt","post_4100216.txt","post_5169258.txt","post_6327011.txt","post_7648209.txt","post_2649129.txt","post_4341853.txt","post_5171871.txt","post_6332561.txt","post_7651184.txt","post_2670291.txt","post_4356235.txt","post_5172421.txt","post_6333030.txt","post_7654727.txt","post_2675470.txt","post_4372887.txt","post_5172780.txt","post_6336036.txt","post_7661362.txt","post_2753258.txt","post_4390048.txt","post_5174174.txt","post_6353656.txt","post_7672509.txt","post_2776473.txt","post_4448113.txt","post_5182098.txt","post_6370454.txt","post_7699043.txt","post_2793589.txt","post_4478669.txt","post_5182116.txt","post_6431946.txt","post_7722627.txt","post_2924232.txt","post_4479659.txt","post_5183502.txt","post_6488240.txt","post_7729005.txt","post_2933536.txt","post_4480285.txt","post_5200223.txt","post_6539400.txt","post_7764744.txt","post_3015367.txt","post_4480286.txt","post_5230265.txt","post_6570328.txt","post_7862789.txt","post_3035587.txt","post_4480850.txt","post_5257920.txt","post_6574903.txt","post_7887644.txt","post_3078259.txt","post_4515857.txt","post_5333076.txt","post_6578463.txt","post_7947654.txt","post_3078568.txt","post_4517648.txt","post_5350539.txt","post_6623651.txt","post_7948615.txt","post_3095226.txt","post_4542269.txt","post_5358986.txt","post_6649739.txt","post_8052259.txt","post_3106812.txt","post_4551702.txt","post_5379340.txt","post_6651430.txt","post_8057951.txt","post_3118159.txt","post_4558082.txt","post_5454775.txt","post_6669353.txt","post_8181522.txt","post_3174737.txt","post_4571980.txt","post_5477585.txt","post_6700613.txt","post_8196698.txt","post_3178102.txt","post_4579040.txt","post_5514082.txt","post_6726172.txt","post_8217995.txt","post_3204122.txt","post_4581342.txt","post_5591150.txt","post_6753474.txt","post_8255177.txt","post_3243872.txt","post_4601353.txt","post_5625635.txt","post_6777412.txt","post_8286671.txt","post_3249282.txt","post_4625162.txt","post_5687722.txt","post_6822388.txt","post_8389186.txt","post_3286215.txt","post_4632833.txt","post_5718652.txt","post_6823128.txt","post_8405796.txt","post_3301502.txt","post_4646770.txt","post_5772003.txt","post_6836283.txt","post_8478400.txt","post_3310765.txt","post_4647172.txt","post_5787921.txt","post_6861293.txt","post_8479565.txt","post_3382176.txt","post_4662462.txt","post_5811327.txt","post_6861582.txt","post_8526840.txt","post_3385911.txt","post_4672309.txt","post_5831997.txt","post_6863772.txt","post_8596057.txt","post_3387614.txt","post_4690227.txt","post_5835446.txt","post_6883900.txt","post_8596080.txt","post_3396064.txt","post_4694553.txt","post_5838872.txt","post_6896266.txt","post_8596101.txt","post_3463088.txt","post_4697264.txt","post_5848301.txt","post_6928869.txt","post_8596143.txt","post_3468912.txt","post_4735139.txt","post_5874970.txt","post_6958844.txt","post_8630027.txt","post_3518372.txt","post_4747883.txt","post_5876811.txt","post_6982759.txt","post_8637932.txt","post_3529142.txt","post_4776178.txt","post_5883872.txt","post_7013629.txt","post_8749909.txt","post_3550501.txt","post_4785946.txt","post_5898696.txt","post_7014832.txt","post_8757345.txt","post_3594398.txt","post_4795280.txt","post_5911103.txt","post_7062519.txt","post_8758529.txt","post_3603028.txt","post_4795347.txt","post_5914238.txt","post_7062520.txt","post_3612145.txt","post_4814612.txt","post_5916477.txt","post_7096158.txt","post_3649005.txt","post_4857580.txt","post_5939724.txt","post_7147496.txt"]
    output = ""


    dementia = ["post_1928737.txt","post_3361739.txt","post_4558172.txt","post_6422925.txt","post_7531344.txt","post_1980573.txt","post_3361933.txt","post_4559388.txt","post_6478460.txt","post_7566390.txt","post_2058641.txt","post_3429358.txt","post_4726151.txt","post_6488222.txt","post_7867311.txt","post_2077550.txt","post_3464098.txt","post_4730888.txt","post_6629578.txt","post_8114011.txt","post_2086744.txt","post_3468678.txt","post_4842372.txt","post_6699527.txt","post_8229151.txt","post_2187465.txt","post_3494708.txt","post_5044647.txt","post_6711521.txt","post_8238664.txt","post_2288398.txt","post_3509643.txt","post_5284201.txt","post_6740813.txt","post_8271468.txt","post_2331582.txt","post_3534570.txt","post_5367452.txt","post_6806525.txt","post_8289159.txt","post_2408215.txt","post_3615321.txt","post_5442472.txt","post_6868382.txt","post_8296587.txt","post_2415369.txt","post_3671474.txt","post_5463721.txt","post_6941163.txt","post_8326467.txt","post_2530989.txt","post_3931075.txt","post_5476480.txt","post_6941873.txt","post_8384189.txt","post_2575681.txt","post_3949051.txt","post_5537462.txt","post_6972484.txt","post_8408364.txt","post_2739879.txt","post_4002394.txt","post_5695673.txt","post_7021932.txt","post_8408367.txt","post_2746679.txt","post_4041467.txt","post_5764690.txt","post_7118849.txt","post_8523024.txt","post_2765497.txt","post_4070994.txt","post_5775087.txt","post_7162344.txt","post_8594360.txt","post_2824268.txt","post_4072713.txt","post_5886066.txt","post_7188799.txt","post_8660432.txt","post_2925037.txt","post_4096035.txt","post_5959764.txt","post_7198650.txt","post_8677951.txt","post_3022943.txt","post_4427982.txt","post_5984882.txt","post_7252205.txt","post_8678875.txt","post_3113185.txt","post_4432154.txt","post_6081429.txt","post_7276697.txt","post_8683622.txt","post_3193443.txt","post_4491254.txt","post_6191442.txt","post_7330416.txt","post_8717520.txt","post_3252346.txt","post_4491258.txt","post_6200763.txt","post_7452928.txt","post_3309133.txt","post_4535207.txt","post_6357072.txt","post_7459857.txt"]


    directory = "/Users/kristen/Development/nlp_project/forums_v2/alz/"
    output = ""
    for filePath in alz:
        i_file = open(directory+filePath).readlines()

        #i_file = open(directory + filePath).readlines()
        try:
            temp = i_file[0].decode('ascii')
            temp = temp.replace('"',"")
            #print temp
            output += temp
        except UnicodeDecodeError:
            print "it was not a ascii-encoded unicode string"
        else:
            print "It may have been an ascii-encoded unicode string"


    out = open("/Users/kristen/Development/nlp_project/removed-ascii/combined-alz_v2.txt","w")
    out.write(output)
    #print output



groupFiles()
