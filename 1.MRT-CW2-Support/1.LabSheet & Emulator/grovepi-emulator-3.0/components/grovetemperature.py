from __future__ import absolute_import
import grovepi


from .genericanalog import *

import bisect

TEMP_LOOKUP=[
-76.96736464,-76.96736464,-70.00813344,-65.69910434,-62.52605398,-59.99467098,-57.87865926,-56.05473128,-54.44801084,
-53.00948476,-51.70525451,-50.5108642,-49.40807002,-48.38288732,-47.4243519,-46.52370286,-45.67382525,
-44.86885918,-44.10391901,-43.37488707,-42.67825964,-42.0110297,-41.3705966,-40.75469545,-40.16134126,
-39.58878428,-39.03547394,-38.50002952,-37.98121598,-37.47792404,-36.98915349,-36.51399925,-36.05163957,
-35.60132604,-35.162375,-34.73416028,-34.31610681,-33.90768521,-33.50840702,-33.11782053,-32.73550718,
-32.36107837,-31.99417261,-31.63445307,-31.28160534,-30.93533547,-30.59536824,-30.26144558,-29.93332512,
-29.61077898,-29.29359264,-28.98156382,-28.67450167,-28.37222583,-28.07456571,-27.78135978,-27.49245494,
-27.20770592,-26.92697478,-26.65013038,-26.37704799,-26.10760882,-25.84169968,-25.57921262,-25.32004459,
-25.0640972,-24.81127637,-24.56149214,-24.31465837,-24.0706926,-23.82951576,-23.59105205,-23.35522874,
-23.12197597,-22.89122666,-22.66291631,-22.43698291,-22.21336679,-21.99201048,-21.77285866,-21.55585799,
-21.34095708,-21.12810633,-20.9172579,-20.70836559,-20.50138478,-20.29627238,-20.0929867,-19.89148746,
-19.69173568,-19.49369364,-19.29732482,-19.10259387,-18.90946651,-18.71790955,-18.5278908,-18.33937904,
-18.15234398,-17.96675626,-17.78258733,-17.5998095,-17.41839587,-17.2383203,-17.05955739,-16.88208244,
-16.70587143,-16.53090102,-16.35714846,-16.18459166,-16.01320907,-15.84297975,-15.67388326,-15.50589973,
-15.33900977,-15.1731945,-15.0084355,-14.84471483,-14.68201496,-14.52031883,-14.35960977,-14.19987151,
-14.04108817,-13.88324425,-13.72632463,-13.57031451,-13.41519944,-13.26096533,-13.10759838,-12.9550851,
-12.80341232,-12.65256715,-12.50253699,-12.35330951,-12.20487265,-12.0572146,-11.91032382,-11.764189,
-11.61879908,-11.47414321,-11.33021078,-11.1869914,-11.04447488,-10.90265126,-10.76151074,-10.62104375,
-10.48124091,-10.34209299,-10.20359098,-10.06572602,-9.928489435,-9.791872703,-9.655867473,-9.520465548,
-9.385658886,-9.251439592,-9.117799919,-8.984732261,-8.852229153,-8.720283261,-8.588887387,-8.458034458,
-8.327717529,-8.197929777,-8.068664498,-7.939915105,-7.811675123,-7.683938191,-7.556698056,-7.42994857,
-7.303683688,-7.177897468,-7.052584067,-6.927737736,-6.803352823,-6.679423767,-6.555945098,-6.432911435,
-6.31031748,-6.188158022,-6.066427933,-5.945122165,-5.824235747,-5.703763788,-5.583701472,-5.464044056,
-5.34478687,-5.225925315,-5.107454861,-4.989371047,-4.871669477,-4.754345821,-4.637395813,-4.520815249,
-4.404599987,-4.288745944,-4.173249096,-4.058105478,-3.94331118,-3.828862347,-3.714755179,-3.60098593,
-3.487550904,-3.374446458,-3.261668999,-3.149214982,-3.037080911,-2.925263336,-2.813758856,-2.702564113,
-2.591675795,-2.481090634,-2.370805403,-2.26081692,-2.151122042,-2.041717667,-1.932600736,-1.823768224,
-1.715217148,-1.606944562,-1.498947558,-1.391223261,-1.283768835,-1.176581478,-1.069658424,-0.962996937,
-0.856594319,-0.750447901,-0.644555048,-0.538913156,-0.433519652,-0.328371993,-0.223467668,-0.118804193,
-0.014379114,0.089809995,0.193765531,0.297489866,0.400985341,0.504254275,0.607298956,0.710121651,
0.8127246,0.915110016,1.01728009,1.119236988,1.220982854,1.322519807,1.423849943,1.524975337,
1.62589804,1.726620083,1.827143474,1.927470201,2.027602231,2.127541511,2.227289966,2.326849504,
2.426222012,2.525409357,2.624413389,2.723235938,2.821878817,2.92034382,3.018632722,3.116747285,
3.214689248,3.312460338,3.410062262,3.507496714,3.604765367,3.701869883,3.798811905,3.895593063,
3.992214969,4.088679223,4.184987408,4.281141094,4.377141835,4.472991173,4.568690635,4.664241734,
4.759645969,4.854904828,4.950019784,5.044992297,5.139823816,5.234515775,5.329069598,5.423486696,
5.517768468,5.6119163,5.705931568,5.799815636,5.893569857,5.987195572,6.080694112,6.174066797,
6.267314935,6.360439825,6.453442755,6.546325003,6.639087837,6.731732515,6.824260285,6.916672385,
7.008970045,7.101154484,7.193226912,7.285188531,7.377040532,7.4687841,7.560420408,7.651950622,
7.743375901,7.834697394,7.92591624,8.017033573,8.108050518,8.198968191,8.289787702,8.380510151,
8.471136632,8.561668231,8.652106028,8.742451093,8.832704492,8.922867281,9.012940511,9.102925224,
9.192822459,9.282633244,9.372358604,9.461999554,9.551557106,9.641032263,9.730426023,9.819739379,
9.908973315,9.998128813,10.08720684,10.17620838,10.26513438,10.3539858,10.44276359,10.5314687,
10.62010207,10.70866463,10.79715731,10.88558104,10.97393674,11.06222532,11.15044769,11.23860475,
11.3266974,11.41472655,11.50269307,11.59059786,11.67844179,11.76622575,11.8539506,11.94161721,
12.02922644,12.11677916,12.20427622,12.29171847,12.37910676,12.46644193,12.55372482,12.64095626,
12.72813708,12.81526812,12.9023502,12.98938414,13.07637075,13.16331084,13.25020524,13.33705473,
13.42386014,13.51062225,13.59734186,13.68401977,13.77065676,13.85725363,13.94381115,14.03033011,
14.11681128,14.20325545,14.28966338,14.37603584,14.4623736,14.54867742,14.63494807,14.7211863,
14.80739287,14.89356853,14.97971403,15.06583013,15.15191757,15.23797709,15.32400943,15.41001534,
15.49599554,15.58195079,15.6678818,15.75378931,15.83967405,15.92553674,16.01137812,16.0971989,
16.1829998,16.26878154,16.35454485,16.44029043,16.526019,16.61173128,16.69742796,16.78310977,
16.8687774,16.95443158,17.04007299,17.12570234,17.21132033,17.29692767,17.38252506,17.46811318,
17.55369274,17.63926442,17.72482894,17.81038697,17.89593921,17.98148635,18.06702907,18.15256808,
18.23810405,18.32363766,18.40916962,18.49470059,18.58023127,18.66576234,18.75129447,18.83682835,
18.92236467,19.0079041,19.09344731,19.178995,19.26454783,19.35010649,19.43567164,19.52124398,
19.60682417,19.69241289,19.77801082,19.86361862,19.94923699,20.03486658,20.12050807,20.20616214,
20.29182946,20.37751071,20.46320655,20.54891766,20.63464472,20.7203884,20.80614937,20.8919283,
20.97772586,21.06354274,21.14937961,21.23523713,21.32111598,21.40701683,21.49294037,21.57888726,
21.66485818,21.75085381,21.83687481,21.92292188,22.00899567,22.09509688,22.18122617,22.26738423,
22.35357173,22.43978935,22.52603778,22.61231769,22.69862976,22.78497468,22.87135313,22.9577658,
23.04421335,23.13069649,23.2172159,23.30377226,23.39036626,23.4769986,23.56366995,23.65038102,
23.73713249,23.82392506,23.91075941,23.99763625,24.08455628,24.17152018,24.25852867,24.34558243,
24.43268218,24.51982861,24.60702242,24.69426434,24.78155505,24.86889528,24.95628572,25.0437271,
25.13122013,25.21876551,25.30636398,25.39401625,25.48172303,25.56948505,25.65730303,25.74517771,
25.8331098,25.92110004,26.00914915,26.09725788,26.18542695,26.27365711,26.3619491,26.45030365,
26.53872151,26.62720343,26.71575015,26.80436242,26.89304101,26.98178666,27.07060013,27.15948218,
27.24843358,27.33745509,27.42654748,27.51571151,27.60494796,27.69425762,27.78364124,27.87309963,
27.96263355,28.0522438,28.14193117,28.23169644,28.32154042,28.41146391,28.5014677,28.5915526,
28.68171941,28.77196896,28.86230204,28.95271949,29.04322211,29.13381074,29.22448621,29.31524933,
29.40610096,29.49704192,29.58807305,29.67919521,29.77040924,29.86171599,29.95311632,30.04461109,
30.13620117,30.22788742,30.31967071,30.41155192,30.50353194,30.59561163,30.6877919,30.78007364,
30.87245773,30.96494509,31.05753662,31.15023323,31.24303583,31.33594534,31.4289627,31.52208881,
31.61532462,31.70867107,31.8021291,31.89569965,31.98938369,32.08318216,32.17709603,32.27112626,
32.36527384,32.45953974,32.55392494,32.64843043,32.7430572,32.83780627,32.93267862,33.02767528,
33.12279726,33.21804559,33.31342128,33.40892539,33.50455894,33.60032298,33.69621858,33.79224678,
33.88840866,33.98470528,34.08113772,34.17770707,34.27441442,34.37126087,34.46824752,34.56537548,
34.66264588,34.76005984,34.85761849,34.95532297,35.05317443,35.15117402,35.24932291,35.34762227,
35.44607327,35.54467709,35.64343494,35.74234801,35.8414175,35.94064465,36.04003066,36.13957678,
36.23928424,36.3391543,36.43918821,36.53938724,36.63975267,36.74028579,36.84098787,36.94186024,
37.04290419,37.14412106,37.24551217,37.34707887,37.44882249,37.55074441,37.65284599,37.75512861,
37.85759367,37.96024255,38.06307668,38.16609747,38.26930635,38.37270477,38.47629418,38.58007605,
38.68405184,38.78822305,38.89259117,38.99715771,39.1019242,39.20689216,39.31206315,39.41743871,
39.52302043,39.62880987,39.73480864,39.84101835,39.9474406,40.05407704,40.16092932,40.26799908,
40.37528801,40.4827978,40.59053014,40.69848674,40.80666935,40.9150797,41.02371955,41.13259067,
41.24169486,41.35103391,41.46060965,41.57042391,41.68047853,41.7907754,41.90131638,42.01210338,
42.12313832,42.23442311,42.34595973,42.45775012,42.56979628,42.68210021,42.79466393,42.90748947,
43.02057889,43.13393427,43.24755771,43.3614513,43.4756172,43.59005754,43.70477451,43.81977029,
43.93504709,44.05060716,44.16645275,44.28258613,44.3990096,44.51572548,44.63273612,44.75004387,
44.86765113,44.9855603,45.10377382,45.22229416,45.34112378,45.4602652,45.57972095,45.69949358,
45.81958568,45.93999986,46.06073874,46.181805,46.30320131,46.4249304,46.54699501,46.6693979,
46.79214189,46.91522979,47.03866446,47.1624488,47.28658573,47.41107818,47.53592915,47.66114164,
47.7867187,47.9126634,48.03897886,48.16566822,48.29273466,48.42018138,48.54801165,48.67622873,
48.80483594,48.93383666,49.06323426,49.19303217,49.32323388,49.45384288,49.58486273,49.71629701,
49.84814936,49.98042343,50.11312296,50.24625169,50.37981342,50.51381199,50.64825131,50.78313529,
50.91846792,51.05425323,51.1904953,51.32719825,51.46436625,51.60200352,51.74011435,51.87870306,
52.01777404,52.1573317,52.29738055,52.43792513,52.57897004,52.72051993,52.86257953,53.0051536,
53.14824699,53.29186459,53.43601137,53.58069233,53.72591259,53.87167728,54.01799162,54.16486092,
54.31229052,54.46028586,54.60885243,54.75799581,54.90772164,55.05803566,55.20894366,55.36045152,
55.5125652,55.66529074,55.81863426,55.97260198,56.12720018,56.28243526,56.43831367,56.59484198,
56.75202684,56.90987501,57.06839333,57.22758874,57.38746828,57.5480391,57.70930845,57.87128367,
58.03397224,58.19738173,58.36151981,58.5263943,58.69201309,58.85838424,59.02551588,59.19341632,
59.36209394,59.53155729,59.70181502,59.87287596,60.04474902,60.2174433,60.39096801,60.56533251,
60.74054633,60.91661914,61.09356076,61.27138116,61.4500905,61.62969909,61.81021741,61.99165611,
62.17402602,62.35733815,62.5416037,62.72683406,62.91304079,63.10023568,63.28843071,63.47763805,
63.66787011,63.8591395,64.05145905,64.24484182,64.43930111,64.63485044,64.83150358,65.02927457,
65.22817767,65.42822742,65.62943863,65.83182638,66.03540602,66.24019321,66.44620388,66.65345428,
66.86196096,67.0717408,67.28281099,67.49518907,67.7088929,67.92394071,68.1403511,68.35814302,
68.5773358,68.79794917,69.02000327,69.24351862,69.46851621,69.69501741,69.92304409,70.15261853,
70.38376352,70.61650231,70.85085866,71.08685684,71.32452165,71.56387842,71.80495307,72.04777206,
72.29236245,72.53875192,72.78696878,73.03704197,73.28900111,73.5428765,73.79869914,74.05650078,
74.3163139,74.57817177,74.84210847,75.10815887,75.37635874,75.64674469,75.91935425,76.19422592,
76.47139912,76.75091432,77.03281299,77.31713769,77.6039321,77.89324102,78.18511045,78.47958763,
78.77672106,79.07656057,79.37915733,79.68456396,79.99283453,80.30402462,80.61819142,80.93539374,
81.25569209,81.57914875,81.90582783,82.23579536,82.56911934,82.90586984,83.24611907,83.58994146,
83.93741379,84.28861524,84.64362752,85.00253495,85.36542462,85.73238646,86.10351337,86.47890141,
86.85864984,87.24286135,87.63164219,88.02510231,88.42335557,88.82651989,89.23471747,89.64807498,
90.06672378,90.49080017,90.9204456,91.35580697,91.79703687,92.24429391,92.69774302,93.15755577,
93.62391075,94.09699395,94.57699914,95.06412836,95.55859233,96.06061097,96.57041396,97.08824128,
97.61434385,98.14898417,98.69243706,99.24499045,99.80694613,100.3786207,100.9603467,101.5524732,
102.1553674,102.7694159,103.3950254,104.032625,104.6826672,105.3456299,106.0220182,106.7123664,
107.4172405,108.1372406,108.8730036,109.625206,110.3945679,111.1818558,111.9878877,112.8135366,
113.6597365,114.5274873,115.4178616,116.3320115,117.2711766,118.236693,119.2300036,120.2526688,
121.3063806,122.3929765,123.514457,124.6730048,125.8710074,127.1110832,128.3961113,129.7292671,
131.1140636,132.5543998,134.0546185,135.6195754,137.2547211,138.9662007,140.760975,142.6469683,
144.6332514,146.7302699,148.9501301,151.3069644,153.8174,156.5011699,159.3819213,162.4883,
165.8554334,169.5269994,173.5581775,178.0199731,183.0057487,188.6414497,195.1023175,202.6416691,
211.6437932,222.7296429,236.9930127,256.6190412,286.9596509,347.6819765,347.6819765]


class GroveTemperature(GenericAnalog):
        
    def __init__(self,inputNum):
        GenericAnalog.__init__(self,inputNum)
        self.value.set(512)
        
    def title(self):
        return "A%d: Grove Temperature Sensor"%self.pin
        
    @classmethod
    def classDescription(cls):
        return "Grove Temperature Sensor"

    def initPropertyPage(self,parent):
        self.propGrid=propgrid.PropertyGrid(parent,title=self.title())        
        self.valueProperty=propgrid.FloatProperty("Centigrade",value=TEMP_LOOKUP[512])
        self.propGrid.Append( self.valueProperty )
        self.rawValueProperty=propgrid.IntProperty("Raw",value=0)
        self.propGrid.Append( self.rawValueProperty )
        self.propGrid.SetCallback(self.OnPropGridChange)
        self.propGrid.pack()
        
    def OnPropGridChange(self,property,value):
        if property=="Raw":
            self.setValue(value)
        else:
            self.setValueC(value)

    def OnSliderChange(self,event):
        self.setValue(self.value.get())
        
    def setValueC(self,cVal):
        valueSlider=bisect.bisect_left(TEMP_LOOKUP,cVal)
        self.setValue(valueSlider)
        
    def setValue(self,value):
        if value>1023: value=1023
        if value<0:value=0
        self.valueProperty.SetValue(TEMP_LOOKUP[value])
        self.rawValueProperty.SetValue(value)
        self.value.set(value)
        grovepi.anaValues[self.pin]=value

    def getCSVCode(self):
        return {"imports":["grovepi"],"reader":"grovepi.analogRead(%d)"%self.pin,"variable":"temperature%d"%self.pin}

        