
def generateFiles(inFile):
    i_file = open(inFile,"r")
    temp = []
    files = []
    content = []

    for line in i_file:
        line = line.split("&&&")
        #print line
        #print "\n"
        filePath = line[1][1:-1]
        #print filePath
        path = "/Users/kristen/Development/nlp_project/forums/caregivers/"+ filePath + ".txt"

        #print path
        out = open(path,"w")
        out.write(line[2])

    return "done"


def queryExpansion(path):
    caregiver_files =["post_4109051.txt","post_5538310.txt","post_6581813.txt","post_7936623.txt","post_4129097.txt","post_5567258.txt","post_6592060.txt","post_7942578.txt","post_2571276.txt","post_4397231.txt","post_5567273.txt","post_6712675.txt","post_7973278.txt","post_2575681.txt","post_4406748.txt","post_5567661.txt","post_6720410.txt","post_8021034.txt","post_2579872.txt","post_4427982.txt","post_5625635.txt","post_6777016.txt","post_8028825.txt",
    "post_2613750.txt","post_4431725.txt","post_5637918.txt","post_6928010.txt","post_8036041.txt","post_2615304.txt","post_4451228.txt","post_5639429.txt","post_7010908.txt","post_8070151.txt",
    "post_2618158.txt","post_4481892.txt","post_5662928.txt","post_7124466.txt","post_8073381.txt",
    "post_2669760.txt","post_4491650.txt","post_5667582.txt","post_7127526.txt","post_8084129.txt",
    "post_2709593.txt","post_4522929.txt","post_5667871.txt","post_7179830.txt","post_8103651.txt",
    "post_2746323.txt","post_4587454.txt","post_5694587.txt","post_7181445.txt","post_8108202.txt",
    "post_2746679.txt","post_4599474.txt","post_5789094.txt","post_7191442.txt","post_8118858.txt",
    "post_2761594.txt","post_4665174.txt","post_5792594.txt","post_7198209.txt","post_8119211.txt",
    "post_2779564.txt","post_4775901.txt","post_5823700.txt","post_7232851.txt","post_8120783.txt",
    "post_2835128.txt","post_4797801.txt","post_5847402.txt","post_7277978.txt","post_8120953.txt",
    "post_2876083.txt","post_4818888.txt","post_5889887.txt","post_7277982.txt","post_8121524.txt",
    "post_2886995.txt","post_4821929.txt","post_5890491.txt","post_7296989.txt","post_8124845.txt",
    "post_3007061.txt","post_4999039.txt","post_5996431.txt","post_7322648.txt","post_8125152.txt",
    "post_3007436.txt","post_5057669.txt","post_5998002.txt","post_7394700.txt","post_8131676.txt",
    "post_3118159.txt","post_5124663.txt","post_6001473.txt","post_7426002.txt","post_8140713.txt",
    "post_3175252.txt","post_5176971.txt","post_6013188.txt","post_7489234.txt","post_8178926.txt",
    "post_3187128.txt","post_5179744.txt","post_6028216.txt","post_7493273.txt","post_8243129.txt",
    "post_3225097.txt","post_5202902.txt","post_6081429.txt","post_7556189.txt","post_8286671.txt",
    "post_3240087.txt","post_5202968.txt","post_6102641.txt","post_7654042.txt","post_8286675.txt",
    "post_3308786.txt","post_5206830.txt","post_6118159.txt","post_7665970.txt","post_8288599.txt",
    "post_3363905.txt","post_5245775.txt","post_6166835.txt","post_7672130.txt","post_8289159.txt",
    "post_3735502.txt","post_5245783.txt","post_6200763.txt","post_7737656.txt","post_8293843.txt",
    "post_3739274.txt","post_5252235.txt","post_6241319.txt","post_7750061.txt","post_8297169.txt",
    "post_3755327.txt","post_5299378.txt","post_6255798.txt","post_7755361.txt","post_8323650.txt",
    "post_3790996.txt","post_5338056.txt","post_6259053.txt","post_7775540.txt","post_8355695.txt",
    "post_3940331.txt","post_5397435.txt","post_6261824.txt","post_7783546.txt","post_8379415.txt",
    "post_3948486.txt","post_5416551.txt","post_6272747.txt","post_7800004.txt","post_8384189.txt",
    "post_3965710.txt","post_5419370.txt","post_6295444.txt","post_7804377.txt","post_8409923.txt",
    "post_3970676.txt","post_5442472.txt","post_6401174.txt","post_7845987.txt","post_8431877.txt",
    "post_3995349.txt","post_5445318.txt","post_6436163.txt","post_7858610.txt","post_8503725.txt",
    "post_3999987.txt","post_5463721.txt","post_6436792.txt","post_7918628.txt","post_8508415.txt",
    "post_4012960.txt","post_5476480.txt","post_6475443.txt","post_7922443.txt","post_8519938.txt",
    "post_4039396.txt","post_5498696.txt","post_6488222.txt","post_7923847.txt","post_8638643.txt",
    "post_4045538.txt","post_5508177.txt","post_6537528.txt","post_7928527.txt","post_8658930.txt",
    "post_4049482.txt","post_5516310.txt","post_6551745.txt","post_7929120.txt","post_8695880.txt",
    "post_4099013.txt","post_5530660.txt","post_6579535.txt","post_7936341.txt","post_8738549.txt"]


    mem_files = ["post_8229151.txt","post_8296587.txt","post_8473926.txt","post_8635256.txt","post_8243266.txt","post_8341081.txt","post_8484528.txt","post_8719051.txt",
    "post_2151949.txt","post_8245436.txt","post_8408367.txt","post_8514094.txt","post_8724088.txt",
    "post_2253851.txt","post_8271468.txt","post_8423677.txt","post_8530384.txt","post_8764925.txt",
    "post_2276735.txt","post_8273191.txt","post_8425444.txt","post_8552128.txt",
    "post_2292345.txt","post_8287466.txt","post_8439631.txt","post_8567357.txt",
    "post_5328146.txt","post_8293299.txt","post_8451808.txt","post_8607046.txt"]


    genetics_files = ["post_3297828.txt","post_4785213.txt","post_6087170.txt","post_6954234.txt",
    "post_3303311.txt","post_4786059.txt","post_6090992.txt","post_6954646.txt",
    "post_1869094.txt","post_3304984.txt","post_4792135.txt","post_6097526.txt","post_6960136.txt",
    "post_1875767.txt","post_3309133.txt","post_4797392.txt","post_6099922.txt","post_6966435.txt",
    "post_1904086.txt","post_3311181.txt","post_4802830.txt","post_6110966.txt","post_6966862.txt",
    "post_1911562.txt","post_3332826.txt","post_4814612.txt","post_6110987.txt","post_6972484.txt",
    "post_1926498.txt","post_3333605.txt","post_4816581.txt","post_6111912.txt","post_6973470.txt",
    "post_1946592.txt","post_3342877.txt","post_4819377.txt","post_6113744.txt","post_6975785.txt",
    "post_1952192.txt","post_3346582.txt","post_4822503.txt","post_6114918.txt","post_6996340.txt",
    "post_1990132.txt","post_3347083.txt","post_4823380.txt","post_6116339.txt","post_6997953.txt",
    "post_1996076.txt","post_3348112.txt","post_4826306.txt","post_6116353.txt","post_7001072.txt",
    "post_2002020.txt","post_3348734.txt","post_4826986.txt","post_6117019.txt","post_7002289.txt",
    "post_2012026.txt","post_3351966.txt","post_4828646.txt","post_6151653.txt","post_7008156.txt",
    "post_2018390.txt","post_3360464.txt","post_4850308.txt","post_6167721.txt","post_7008158.txt",
    "post_2021250.txt","post_3365228.txt","post_4852917.txt","post_6167739.txt","post_7013629.txt",
    "post_2021296.txt","post_3367186.txt","post_4854036.txt","post_6167764.txt","post_7030518.txt",
    "post_2021394.txt","post_3370116.txt","post_4854576.txt","post_6167930.txt","post_7042777.txt",
    "post_2028599.txt","post_3372058.txt","post_4857182.txt","post_6172238.txt","post_7052367.txt",
    "post_2030163.txt","post_3373282.txt","post_4859396.txt","post_6175527.txt","post_7057676.txt",
    "post_2039472.txt","post_3373463.txt","post_4861461.txt","post_6176102.txt","post_7061115.txt",
    "post_2041586.txt","post_3374574.txt","post_4884065.txt","post_6179428.txt","post_7089509.txt",
    "post_2042182.txt","post_3376660.txt","post_4886490.txt","post_6182367.txt","post_7094488.txt",
    "post_2058468.txt","post_3377158.txt","post_4909752.txt","post_6200760.txt","post_7113284.txt",
    "post_2061552.txt","post_3398585.txt","post_4922316.txt","post_6201734.txt","post_7117849.txt",
    "post_2065841.txt","post_3400725.txt","post_4936910.txt","post_6202386.txt","post_7138308.txt",
    "post_2066566.txt","post_3410271.txt","post_4946231.txt","post_6207924.txt","post_7142367.txt",
    "post_2068377.txt","post_3412073.txt","post_4948118.txt","post_6211736.txt","post_7145669.txt",
    "post_2072609.txt","post_3415914.txt","post_4957390.txt","post_6212044.txt","post_7148469.txt",
    "post_2073014.txt","post_3419907.txt","post_5032947.txt","post_6217775.txt","post_7151453.txt",
    "post_2074331.txt","post_3427034.txt","post_5040251.txt","post_6217862.txt","post_7151489.txt",
    "post_2084048.txt","post_3436312.txt","post_5055189.txt","post_6218026.txt","post_7176343.txt",
    "post_2085572.txt","post_3437274.txt","post_5056382.txt","post_6227821.txt","post_7180949.txt",
    "post_2102277.txt","post_3444280.txt","post_5059728.txt","post_6230402.txt","post_7190608.txt",
    "post_2107142.txt","post_3445288.txt","post_5062632.txt","post_6240564.txt","post_7192093.txt",
    "post_2111307.txt","post_3459614.txt","post_5065682.txt","post_6246610.txt","post_7198145.txt",
    "post_2111408.txt","post_3471289.txt","post_5070498.txt","post_6249050.txt","post_7213823.txt",
    "post_2114225.txt","post_3473358.txt","post_5080325.txt","post_6250528.txt","post_7214353.txt",
    "post_2125863.txt","post_3473723.txt","post_5092578.txt","post_6250756.txt","post_7225492.txt",
    "post_2128258.txt","post_3482674.txt","post_5095805.txt","post_6254739.txt","post_7226837.txt",
    "post_2134527.txt","post_3485444.txt","post_5107249.txt","post_6254965.txt","post_7236575.txt",
    "post_2135076.txt","post_3486328.txt","post_5115196.txt","post_6256409.txt","post_7247635.txt",
    "post_2137521.txt","post_3491111.txt","post_5120525.txt","post_6261314.txt","post_7248600.txt",
    "post_2140767.txt","post_3491464.txt","post_5122452.txt","post_6264581.txt","post_7261060.txt",
    "post_2145451.txt","post_3491951.txt","post_5130346.txt","post_6268720.txt","post_7262914.txt",
    "post_2152930.txt","post_3503653.txt","post_5138174.txt","post_6270649.txt","post_7267696.txt",
    "post_2154176.txt","post_3518624.txt","post_5148819.txt","post_6273185.txt","post_7268896.txt",
    "post_2157714.txt","post_3518693.txt","post_5154911.txt","post_6273677.txt","post_7279170.txt",
    "post_2162061.txt","post_3519746.txt","post_5160720.txt","post_6274384.txt","post_7286894.txt",
    "post_2162699.txt","post_3526164.txt","post_5161209.txt","post_6274393.txt","post_7292901.txt",
    "post_2170960.txt","post_3527409.txt","post_5162278.txt","post_6274605.txt","post_7298113.txt",
    "post_2176707.txt","post_3527963.txt","post_5172198.txt","post_6278971.txt","post_7299279.txt",
    "post_2180554.txt","post_3537250.txt","post_5172780.txt","post_6281968.txt","post_7302224.txt",
    "post_2181031.txt","post_3542314.txt","post_5172822.txt","post_6286182.txt","post_7308890.txt",
    "post_2192346.txt","post_3543172.txt","post_5174570.txt","post_6296930.txt","post_7309681.txt",
    "post_2196811.txt","post_3545520.txt","post_5178111.txt","post_6299664.txt","post_7314240.txt",
    "post_2216612.txt","post_3547076.txt","post_5187427.txt","post_6302978.txt","post_7326063.txt",
    "post_2218355.txt","post_3557405.txt","post_5191058.txt","post_6303091.txt","post_7328210.txt",
    "post_2221319.txt","post_3563301.txt","post_5191616.txt","post_6306620.txt","post_7329909.txt",
    "post_2239714.txt","post_3577733.txt","post_5193726.txt","post_6309469.txt","post_7336097.txt",
    "post_2252245.txt","post_3579082.txt","post_5195337.txt","post_6312798.txt","post_7342192.txt",
    "post_2259235.txt","post_3583265.txt","post_5200583.txt","post_6325885.txt","post_7350738.txt",
    "post_2267580.txt","post_3585047.txt","post_5201219.txt","post_6327139.txt","post_7351328.txt",
    "post_2270475.txt","post_3597110.txt","post_5210680.txt","post_6334163.txt","post_7354020.txt",
    "post_2278032.txt","post_3599244.txt","post_5213341.txt","post_6335238.txt","post_7363644.txt",
    "post_2285689.txt","post_3601532.txt","post_5214331.txt","post_6335942.txt","post_7365244.txt",
    "post_2293936.txt","post_3603126.txt","post_5215710.txt","post_6338337.txt","post_7365956.txt",
    "post_2304746.txt","post_3604268.txt","post_5225960.txt","post_6343357.txt","post_7371092.txt",
    "post_2322745.txt","post_3608244.txt","post_5236405.txt","post_6346840.txt","post_7375811.txt",
    "post_2327090.txt","post_3615836.txt","post_5236454.txt","post_6346850.txt","post_7376169.txt",
    "post_2333997.txt","post_3618230.txt","post_5240243.txt","post_6347480.txt","post_7376918.txt",
    "post_2334739.txt","post_3624718.txt","post_5240503.txt","post_6350701.txt","post_7378333.txt",
    "post_2337053.txt","post_3630685.txt","post_5260264.txt","post_6355916.txt","post_7385160.txt",
    "post_2347757.txt","post_3632116.txt","post_5263217.txt","post_6364754.txt","post_7416595.txt",
    "post_2347761.txt","post_3636394.txt","post_5264405.txt","post_6369564.txt","post_7425384.txt",
    "post_2350287.txt","post_3647458.txt","post_5267835.txt","post_6372302.txt","post_7443497.txt",
    "post_2350531.txt","post_3647632.txt","post_5272513.txt","post_6377109.txt","post_7444952.txt",
    "post_2351336.txt","post_3650964.txt","post_5278967.txt","post_6380290.txt","post_7453560.txt",
    "post_2364450.txt","post_3657659.txt","post_5284384.txt","post_6380897.txt","post_7483453.txt",
    "post_2365216.txt","post_3659960.txt","post_5285152.txt","post_6384383.txt","post_7489115.txt",
    "post_2382624.txt","post_3662818.txt","post_5286607.txt","post_6386385.txt","post_7498067.txt",
    "post_2388899.txt","post_3665682.txt","post_5295398.txt","post_6391000.txt","post_7499015.txt",
    "post_2390524.txt","post_3666186.txt","post_5295443.txt","post_6391648.txt","post_7502420.txt",
    "post_2394605.txt","post_3666453.txt","post_5296045.txt","post_6392018.txt","post_7504862.txt",
    "post_2406497.txt","post_3670164.txt","post_5310992.txt","post_6392652.txt","post_7505966.txt",
    "post_2407080.txt","post_3678803.txt","post_5319944.txt","post_6393042.txt","post_7513826.txt",
    "post_2422063.txt","post_3678911.txt","post_5321497.txt","post_6421102.txt","post_7523252.txt",
    "post_2423020.txt","post_3683837.txt","post_5323843.txt","post_6421207.txt","post_7529565.txt",
    "post_2444822.txt","post_3688688.txt","post_5337777.txt","post_6424186.txt","post_7535385.txt",
    "post_2452059.txt","post_3689662.txt","post_5342705.txt","post_6425021.txt","post_7536140.txt",
    "post_2454766.txt","post_3691518.txt","post_5342776.txt","post_6432116.txt","post_7539987.txt",
    "post_2457944.txt","post_3693592.txt","post_5343976.txt","post_6432117.txt","post_7550484.txt",
    "post_2459160.txt","post_3694606.txt","post_5347886.txt","post_6433304.txt","post_7560876.txt",
    "post_2461278.txt","post_3701195.txt","post_5354199.txt","post_6442912.txt","post_7566650.txt",
    "post_2461984.txt","post_3712494.txt","post_5357477.txt","post_6447071.txt","post_7568074.txt",
    "post_2462676.txt","post_3713011.txt","post_5361687.txt","post_6447490.txt","post_7577148.txt",
    "post_2471995.txt","post_3715489.txt","post_5369811.txt","post_6452700.txt","post_7587621.txt",
    "post_2474164.txt","post_3716395.txt","post_5370405.txt","post_6456311.txt","post_7595378.txt",
    "post_2474212.txt","post_3717550.txt","post_5373170.txt","post_6456607.txt","post_7605368.txt",
    "post_2491476.txt","post_3719623.txt","post_5386735.txt","post_6461082.txt","post_7609149.txt",
    "post_2505965.txt","post_3722521.txt","post_5396218.txt","post_6462912.txt","post_7614417.txt",
    "post_2516058.txt","post_3736754.txt","post_5399041.txt","post_6463779.txt","post_7619149.txt",
    "post_2525902.txt","post_3747839.txt","post_5413988.txt","post_6463830.txt","post_7622830.txt",
    "post_2535422.txt","post_3747956.txt","post_5415693.txt","post_6473193.txt","post_7626009.txt",
    "post_2547477.txt","post_3781883.txt","post_5419423.txt","post_6488240.txt","post_7628045.txt",
    "post_2567918.txt","post_3786611.txt","post_5419681.txt","post_6495585.txt","post_7628839.txt",
    "post_2568543.txt","post_3786977.txt","post_5427975.txt","post_6499923.txt","post_7637542.txt",
    "post_2573920.txt","post_3787562.txt","post_5436902.txt","post_6502787.txt","post_7642574.txt",
    "post_2577432.txt","post_3789774.txt","post_5439357.txt","post_6503379.txt","post_7659755.txt",
    "post_2578163.txt","post_3790368.txt","post_5445905.txt","post_6505799.txt","post_7690456.txt",
    "post_2587425.txt","post_3791418.txt","post_5454775.txt","post_6509409.txt","post_7690622.txt",
    "post_2599183.txt","post_3793828.txt","post_5460425.txt","post_6517087.txt","post_7697971.txt",
    "post_2603749.txt","post_3799544.txt","post_5461879.txt","post_6518811.txt","post_7702816.txt",
    "post_2603909.txt","post_3802744.txt","post_5466234.txt","post_6521111.txt","post_7712783.txt",
    "post_2605981.txt","post_3806950.txt","post_5479615.txt","post_6521255.txt","post_7721902.txt",
    "post_2606233.txt","post_3822382.txt","post_5486954.txt","post_6521593.txt","post_7734803.txt",
    "post_2609133.txt","post_3829287.txt","post_5490284.txt","post_6524874.txt","post_7746689.txt",
    "post_2609667.txt","post_3830662.txt","post_5492074.txt","post_6528074.txt","post_7764985.txt",
    "post_2609670.txt","post_3837838.txt","post_5493100.txt","post_6528803.txt","post_7773680.txt",
    "post_2618153.txt","post_3859274.txt","post_5493105.txt","post_6532520.txt","post_7778509.txt",
    "post_2621847.txt","post_3862017.txt","post_5502081.txt","post_6537704.txt","post_7779361.txt",
    "post_2622962.txt","post_3868024.txt","post_5505117.txt","post_6549708.txt","post_7790594.txt",
    "post_2623816.txt","post_3878712.txt","post_5506622.txt","post_6549914.txt","post_7790753.txt",
    "post_2625444.txt","post_3887589.txt","post_5507164.txt","post_6550000.txt","post_7794522.txt",
    "post_2626914.txt","post_3895399.txt","post_5507927.txt","post_6550155.txt","post_7795130.txt",
    "post_2627416.txt","post_3895401.txt","post_5508258.txt","post_6552274.txt","post_7814543.txt",
    "post_2630103.txt","post_3901202.txt","post_5508726.txt","post_6552665.txt","post_7818685.txt",
    "post_2637449.txt","post_3901884.txt","post_5509661.txt","post_6553452.txt","post_7834966.txt",
    "post_2637707.txt","post_3901895.txt","post_5512148.txt","post_6559373.txt","post_7839835.txt",
    "post_2660230.txt","post_3903581.txt","post_5512664.txt","post_6563006.txt","post_7841629.txt",
    "post_2661950.txt","post_3910703.txt","post_5517359.txt","post_6563888.txt","post_7855620.txt",
    "post_2667158.txt","post_3910714.txt","post_5517432.txt","post_6567066.txt","post_7870433.txt",
    "post_2668139.txt","post_3913021.txt","post_5519023.txt","post_6572517.txt","post_7872807.txt",
    "post_2673276.txt","post_3919122.txt","post_5522306.txt","post_6577045.txt","post_7880731.txt",
    "post_2673383.txt","post_3923638.txt","post_5533132.txt","post_6578525.txt","post_7885227.txt",
    "post_2674493.txt","post_3928921.txt","post_5534013.txt","post_6583726.txt","post_7886448.txt",
    "post_2676281.txt","post_3929675.txt","post_5540044.txt","post_6588054.txt","post_7894456.txt",
    "post_2676943.txt","post_3933821.txt","post_5551743.txt","post_6589416.txt","post_7902889.txt",
    "post_2677964.txt","post_3936365.txt","post_5551992.txt","post_6590609.txt","post_7912618.txt",
    "post_2682972.txt","post_3945840.txt","post_5554312.txt","post_6599905.txt","post_7919920.txt",
    "post_2684072.txt","post_3962047.txt","post_5566095.txt","post_6604700.txt","post_7930340.txt",
    "post_2689603.txt","post_3967988.txt","post_5581464.txt","post_6604805.txt","post_7931177.txt",
    "post_2697182.txt","post_3976021.txt","post_5581973.txt","post_6623076.txt","post_7940625.txt",
    "post_2706757.txt","post_3981391.txt","post_5582736.txt","post_6624337.txt","post_7946825.txt",
    "post_2708033.txt","post_3982578.txt","post_5591789.txt","post_6625117.txt","post_7951871.txt",
    "post_2726718.txt","post_3982804.txt","post_5598279.txt","post_6629613.txt","post_7953438.txt",
    "post_2730419.txt","post_3986087.txt","post_5602024.txt","post_6629771.txt","post_7973299.txt",
    "post_2731019.txt","post_3986263.txt","post_5602025.txt","post_6634481.txt","post_7976797.txt",
    "post_2732160.txt","post_3988543.txt","post_5604344.txt","post_6638372.txt","post_7978900.txt",
    "post_2732760.txt","post_3995113.txt","post_5631274.txt","post_6638787.txt","post_7995306.txt",
    "post_2734920.txt","post_3995134.txt","post_5633053.txt","post_6639128.txt","post_8002260.txt",
    "post_2747590.txt","post_3998676.txt","post_5639221.txt","post_6640095.txt","post_8008537.txt",
    "post_2756243.txt","post_4000695.txt","post_5645356.txt","post_6657155.txt","post_8009173.txt",
    "post_2762815.txt","post_4002272.txt","post_5655505.txt","post_6659168.txt","post_8010598.txt",
    "post_2772959.txt","post_4005742.txt","post_5656108.txt","post_6664746.txt","post_8015028.txt",
    "post_2773379.txt","post_4010619.txt","post_5658615.txt","post_6666206.txt","post_8028674.txt",
    "post_2785958.txt","post_4011158.txt","post_5661311.txt","post_6667994.txt","post_8042870.txt",
    "post_2794324.txt","post_4014224.txt","post_5666331.txt","post_6669353.txt","post_8045113.txt",
    "post_2805790.txt","post_4023882.txt","post_5673582.txt","post_6671164.txt","post_8051632.txt",
    "post_2809748.txt","post_4026990.txt","post_5676130.txt","post_6673081.txt","post_8055705.txt",
    "post_2811221.txt","post_4034348.txt","post_5686805.txt","post_6673621.txt","post_8057211.txt",
    "post_2813999.txt","post_4037142.txt","post_5699811.txt","post_6674454.txt","post_8062255.txt",
    "post_2832268.txt","post_4041562.txt","post_5714830.txt","post_6678774.txt","post_8063079.txt",
    "post_2843170.txt","post_4048990.txt","post_5723154.txt","post_6684157.txt","post_8063092.txt",
    "post_2851940.txt","post_4055632.txt","post_5729113.txt","post_6689974.txt","post_8075789.txt",
    "post_2858893.txt","post_4056170.txt","post_5751023.txt","post_6691518.txt","post_8077920.txt",
    "post_2863925.txt","post_4064802.txt","post_5752488.txt","post_6692500.txt","post_8082310.txt",
    "post_2865893.txt","post_4066077.txt","post_5752649.txt","post_6701249.txt","post_8091384.txt",
    "post_2866918.txt","post_4067670.txt","post_5752999.txt","post_6705346.txt","post_8094591.txt",
    "post_2875663.txt","post_4073076.txt","post_5758877.txt","post_6709051.txt","post_8097771.txt",
    "post_2894445.txt","post_4075829.txt","post_5758891.txt","post_6712567.txt","post_8104404.txt",
    "post_2899723.txt","post_4079364.txt","post_5764426.txt","post_6715409.txt","post_8113957.txt",
    "post_2902014.txt","post_4080982.txt","post_5764545.txt","post_6715681.txt","post_8121752.txt",
    "post_2902565.txt","post_4112597.txt","post_5768629.txt","post_6722438.txt","post_8135337.txt",
    "post_2907010.txt","post_4125542.txt","post_5776478.txt","post_6729234.txt","post_8137814.txt",
    "post_2908633.txt","post_4132639.txt","post_5776624.txt","post_6730999.txt","post_8138473.txt",
    "post_2912753.txt","post_4139509.txt","post_5777069.txt","post_6736090.txt","post_8147952.txt",
    "post_2920077.txt","post_4140856.txt","post_5778230.txt","post_6736666.txt","post_8157022.txt",
    "post_2926423.txt","post_4145587.txt","post_5778287.txt","post_6739713.txt","post_8161436.txt",
    "post_2934685.txt","post_4147587.txt","post_5780608.txt","post_6749657.txt","post_8169374.txt",
    "post_2937774.txt","post_4147745.txt","post_5781862.txt","post_6751754.txt","post_8176947.txt",
    "post_2942342.txt","post_4233228.txt","post_5782798.txt","post_6754992.txt","post_8179769.txt",
    "post_2955001.txt","post_4233240.txt","post_5808220.txt","post_6757022.txt","post_8180775.txt",
    "post_2955072.txt","post_4235135.txt","post_5811043.txt","post_6758451.txt","post_8185596.txt",
    "post_2957385.txt","post_4243233.txt","post_5812801.txt","post_6759253.txt","post_8186320.txt",
    "post_2962267.txt","post_4328370.txt","post_5818305.txt","post_6760410.txt","post_8186611.txt",
    "post_2962323.txt","post_4330050.txt","post_5822467.txt","post_6765600.txt","post_8195074.txt",
    "post_2979718.txt","post_4331980.txt","post_5830967.txt","post_6766601.txt","post_8195169.txt",
    "post_2998131.txt","post_4337592.txt","post_5834843.txt","post_6767083.txt","post_8195192.txt",
    "post_2999153.txt","post_4351478.txt","post_5850088.txt","post_6769449.txt","post_8201416.txt",
    "post_3010026.txt","post_4352274.txt","post_5854482.txt","post_6772343.txt","post_8208127.txt",
    "post_3020996.txt","post_4367446.txt","post_5855442.txt","post_6773934.txt","post_8214903.txt",
    "post_3021985.txt","post_4370008.txt","post_5861025.txt","post_6776612.txt","post_8215999.txt",
    "post_3027148.txt","post_4372957.txt","post_5866224.txt","post_6777130.txt","post_8218401.txt",
    "post_3029689.txt","post_4379863.txt","post_5866284.txt","post_6781240.txt","post_8220017.txt",
    "post_3036962.txt","post_4382941.txt","post_5874771.txt","post_6799359.txt","post_8242149.txt",
    "post_3036984.txt","post_4384461.txt","post_5883389.txt","post_6800860.txt","post_8245213.txt",
    "post_3040165.txt","post_4402615.txt","post_5885827.txt","post_6801568.txt","post_8260006.txt",
    "post_3040370.txt","post_4408569.txt","post_5886029.txt","post_6802429.txt","post_8266587.txt",
    "post_3043074.txt","post_4414643.txt","post_5899753.txt","post_6803847.txt","post_8287229.txt",
    "post_3049655.txt","post_4414849.txt","post_5902724.txt","post_6807887.txt","post_8288924.txt",
    "post_3052806.txt","post_4416893.txt","post_5912531.txt","post_6808594.txt","post_8290476.txt",
    "post_3054831.txt","post_4423643.txt","post_5915157.txt","post_6815408.txt","post_8290503.txt",
    "post_3091356.txt","post_4427006.txt","post_5918650.txt","post_6816675.txt","post_8295536.txt",
    "post_3095933.txt","post_4433606.txt","post_5924888.txt","post_6819099.txt","post_8303621.txt",
    "post_3106242.txt","post_4438180.txt","post_5928413.txt","post_6824343.txt","post_8312768.txt",
    "post_3122538.txt","post_4441118.txt","post_5934504.txt","post_6824397.txt","post_8313017.txt",
    "post_3125777.txt","post_4444669.txt","post_5939353.txt","post_6825393.txt","post_8313247.txt",
    "post_3136270.txt","post_4458981.txt","post_5943353.txt","post_6829367.txt","post_8315076.txt",
    "post_3137443.txt","post_4460043.txt","post_5966727.txt","post_6835928.txt","post_8315084.txt",
    "post_3139825.txt","post_4467730.txt","post_5966914.txt","post_6841775.txt","post_8318745.txt",
    "post_3145779.txt","post_4470919.txt","post_5983772.txt","post_6842767.txt","post_8345807.txt",
    "post_3153700.txt","post_4472930.txt","post_5985080.txt","post_6847515.txt","post_8346023.txt",
    "post_3177425.txt","post_4477946.txt","post_5985815.txt","post_6849004.txt","post_8385924.txt",
    "post_3185201.txt","post_4485348.txt","post_5986537.txt","post_6849536.txt","post_8388668.txt",
    "post_3190441.txt","post_4488623.txt","post_6001574.txt","post_6849594.txt","post_8406265.txt",
    "post_3194457.txt","post_4491012.txt","post_6006988.txt","post_6853674.txt","post_8408212.txt",
    "post_3195230.txt","post_4497016.txt","post_6012810.txt","post_6854575.txt","post_8433605.txt",
    "post_3196861.txt","post_4505460.txt","post_6014130.txt","post_6859896.txt","post_8434865.txt",
    "post_3204206.txt","post_4513358.txt","post_6014553.txt","post_6873056.txt","post_8442002.txt",
    "post_3206565.txt","post_4532511.txt","post_6016879.txt","post_6874903.txt","post_8451019.txt",
    "post_3220744.txt","post_4554097.txt","post_6018729.txt","post_6882492.txt","post_8462921.txt",
    "post_3227960.txt","post_4579040.txt","post_6019252.txt","post_6884656.txt","post_8467441.txt",
    "post_3228091.txt","post_4587592.txt","post_6022650.txt","post_6899581.txt","post_8481479.txt",
    "post_3239570.txt","post_4588136.txt","post_6031022.txt","post_6903486.txt","post_8486967.txt",
    "post_3240292.txt","post_4590625.txt","post_6031803.txt","post_6904677.txt","post_8487552.txt",
    "post_3241020.txt","post_4594900.txt","post_6044593.txt","post_6913800.txt","post_8500566.txt",
    "post_3241637.txt","post_4594908.txt","post_6045909.txt","post_6913971.txt","post_8501665.txt",
    "post_3245672.txt","post_4600681.txt","post_6049093.txt","post_6914008.txt","post_8510424.txt",
    "post_3248212.txt","post_4615566.txt","post_6052893.txt","post_6917952.txt","post_8517292.txt",
    "post_3254731.txt","post_4616697.txt","post_6055168.txt","post_6918593.txt","post_8551151.txt",
    "post_3257872.txt","post_4644342.txt","post_6057396.txt","post_6919999.txt","post_8551255.txt",
    "post_3279424.txt","post_4651536.txt","post_6059272.txt","post_6924991.txt","post_8558262.txt",
    "post_3281419.txt","post_4656549.txt","post_6059442.txt","post_6929842.txt","post_8565821.txt",
    "post_3281675.txt","post_4679343.txt","post_6073697.txt","post_6929980.txt","post_8578302.txt",
    "post_3284741.txt","post_4683419.txt","post_6074520.txt","post_6930942.txt","post_8579968.txt",
    "post_3292448.txt","post_4712384.txt","post_6078624.txt","post_6932378.txt","post_8604276.txt",
    "post_3295532.txt","post_4747876.txt","post_6079501.txt","post_6933270.txt","post_8688794.txt",
    "post_3297100.txt","post_4763590.txt","post_6082745.txt","post_6948229.txt",
    "post_3297312.txt","post_4777094.txt","post_6083714.txt","post_6949899.txt"]

    d_query = ["dementia","Dementia","DEMENTIA"]
    a_query = ["Alzheimers","alzheimer","Alzheimer","amyloid","alzheimer's disease","apoe","familial alzheimer's disease","tau","amyloid beta-peptides","FAC1 protein"]

    dementia_files = []
    alz_files = []

    for files in genetics_files:
        forum = path+files
        #print forum
        i_file = open(forum,"r")

        # if both words are present? make third tobic that is dementia and alz

        for line in i_file:
            for term in d_query:
                if term in line:
                    dementia_files.append(forum[-16:])
            for term in a_query:
                if term in line:
                    alz_files.append(forum[-16:])
    print dementia_files
    print len(dementia_files)
    print alz_files
    print len(alz_files)
    return "done"






queryExpansion("/Users/kristen/Development/nlp_project/forums/genetics/")




#generateFiles("/Users/kristen/Development/nlp_project/forums/memory_loss/MLH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/dementia/DH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/genetics/GH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/alz/ADH_text.txt")
#generateFiles("/Users/kristen/Development/nlp_project/forums/caregivers/CH_text.txt")
