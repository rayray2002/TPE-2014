
#version 3.6;

#declare ldd_level_of_detail = 0;

#declare ldd_light_color = <255/255,255/255,255/255>;

#declare ldd_color_variance = 2.00;

#include "ldd_default_colors.inc"

#include "ldd_default_materials.inc"

#include "ldd_part_materials.inc"

#include "ldd_part_bevels.inc"

#include "ldd_part_position_variances.inc"

#include "ldd_main.bin"

#declare ldd_camera_transformation = transform { matrix <-0.99990886449813843,0,-0.013495597057044506,-0.0099204918369650841,0.67796844244003296,0.73502403497695923,0.0091495895758271217,0.73509097099304199,-0.67790675163269043,2.2915925979614258,65.0565185546875,-55.414924621582031>}
#declare ldd_camera_location = ldd_vtransform(<0, 0, 0>, ldd_camera_transformation);
#declare ldd_camera_distance = 81.052230834960937;
#declare ldd_camera_look_at = ldd_vtransform(<0, 0, -ldd_camera_distance>, ldd_camera_transformation);

#declare ldd_camera_angle = ldd_default_camera_angle;

#declare ldd_model_transformation = transform { translate <0,0,0> }

#include "ldd_76302.bin"
#include "ldd_98313.bin"
#include "ldd_75937.bin"
#include "ldd_3943.bin"
#include "ldd_6222.bin"
#include "ldd_6218.bin"
#include "ldd_60474.bin"
#include "ldd_15462.bin"
#include "ldd_2780.bin"
#include "ldd_62462.bin"
#include "ldd_4081.bin"
#include "ldd_6140.bin"
#include "ldd_4592.bin"
#include "ldd_4593.bin"
#include "ldd_3710.bin"
#include "ldd_3022.bin"
#include "ldd_6183.bin"
#include "ldd_93606.bin"
#include "ldd_3023.bin"
#include "ldd_92946.bin"
#include "ldd_50745.bin"
#include "ldd_3460.bin"
#include "ldd_87552.bin"
#include "ldd_57909.bin"
#include "ldd_3666.bin"
#include "ldd_2431.bin"
#include "ldd_60219.bin"
#include "ldd_44568.bin"
#include "ldd_3020.bin"
#include "ldd_30499.bin"
#include "ldd_4345.bin"
#include "ldd_2412.bin"
#include "ldd_30000.bin"
#include "ldd_47457.bin"
#include "ldd_3009.bin"
#include "ldd_3032.bin"
#include "ldd_44237.bin"
#include "ldd_3034.bin"
#include "ldd_3001.bin"
#include "ldd_3795.bin"
#include "ldd_47456.bin"
#include "ldd_32059.bin"
#include "ldd_15068.bin"
#include "ldd_11295.bin"
#include "ldd_2434.bin"
#include "ldd_3021.bin"
#include "ldd_30363.bin"
#include "ldd_61409.bin"
#include "ldd_3024.bin"
#include "ldd_85984.bin"
#include "ldd_10247.bin"
#include "ldd_44661.bin"
#include "ldd_99781.bin"
#include "ldd_3747.bin"
#include "ldd_51739.bin"
#include "ldd_6091.bin"
#include "ldd_98138.bin"
#include "ldd_93571.bin"
#include "ldd_87083.bin"
#include "ldd_55981.bin"
#include "ldd_60476.bin"
#include "ldd_48336.bin"
#include "ldd_3633.bin"
#include "ldd_30361.bin"
#include "ldd_30367.bin"
#include "ldd_4274.bin"
#include "ldd_4346.bin"
#include "ldd_50747.bin"
#include "ldd_6211.bin"
#include "ldd_60897.bin"
#include "ldd_6558.bin"
#include "ldd_41531.bin"
#include "ldd_43122.bin"


global_settings {
  assumed_gamma 1.4
  max_trace_level 50
  adc_bailout 0.01/2     
  radiosity {
    pretrace_start 0.08
    pretrace_end   0.005
    count 450
    nearest_count 4
    error_bound 0.05
    recursion_limit 1
    low_error_factor 0.3
    gray_threshold 0.0
    minimum_reuse 0.005
    //maximum_reuse 0.2
    brightness 1
    adc_bailout 0.005
    normal on
    media off
  }
}

background { color rgbft <255/255, 255/255, 255/255, 1, 1> }

light_source {
  <100,100,0>
  color 40/100*ldd_light_color
  area_light 5, 5, 10, 10
  adaptive 1
  jitter
  circular
  orient
  transform { ldd_camera_transformation }
}

light_source {
  <-100,100,0>
  color 40/100*ldd_light_color
  area_light 5, 5, 10, 10
  adaptive 1
  jitter
  circular
  orient
  transform { ldd_camera_transformation }
}

light_source {
  <0,100,0>
  color 40/100*ldd_light_color
  area_light 5, 5, 10, 10
  adaptive 1
  jitter
  circular
  orient
  transform { ldd_camera_transformation }
}

camera {
  right  -(image_width/image_height)*x
  location ldd_camera_location
  look_at ldd_camera_look_at
  angle ldd_camera_angle

}

#declare ldd_model = union {
ldd_76302(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,-3.7086374759674072,0.5598716139793396,-3.7011833190917969}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{-0.70710605382919312,0.7071075439453125,0,0.7071075439453125,0.70710605382919312,0,0,0,-1,-3.256657600402832,1.0115982294082642,5.7471199035644531}})
ldd_75937(array[1]{21},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-2.8081099987030029,1.4601342678070068,5.5001220703125}})
ldd_3943(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-3.1999986171722412,1.0600069761276245,3.5799713134765625}})
ldd_6222(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-3.5999991893768311,1.4600085020065308,2.6199722290039063}})
ldd_6218(array[1]{199},array[1]{0},array[1][12]{{-1,0,0,0,0,1,0,1,0,-1.1999987363815308,2.2600119113922119,-1.2200279235839844}})
ldd_6218(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-3.5999991893768311,1.4600086212158203,-1.2200279235839844}})
ldd_6222(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-3.5999991893768311,1.4600087404251099,-2.1800270080566406}})
ldd_60474(array[1]{194},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-3.5999991893768311,1.4600087404251099,-2.5000267028808594}})
ldd_15462(array[1]{138},array[1]{0},array[1][12]{{0,-1,0,1,0,0,0,0,1,-2.3999991416931152,1.8600083589553833,-0.82002639770507813}})
ldd_3943(array[1]{199},array[1]{0},array[1][12]{{0,-1,0,0,0,-1,1,0,0,-1.6000000238418579,2.660008430480957,-2.5000267028808594}})
ldd_75937(array[1]{21},array[1]{0},array[1][12]{{0,-1,0,0,0,-1,1,0,0,-2.0001275539398193,2.2681190967559814,-4.4201774597167969}})
ldd_2780(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,0,1.8600083589553833,3.2000045776367187}})
ldd_62462(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,0.799998939037323,1.4600085020065308,3.2000045776367187}})
ldd_4081(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.8005127906799316,8.0000057220458984,4.4000396728515625}})
ldd_6140(array[1]{26},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-0.39948940277099609,8.2436704635620117,4.5600123405456543}})
union { 
ldd_4592(array[1]{24},array[1]{0},array[1][12]{{0,-1,0,0,0,-1,1,0,0,3.6005141735076904,8.2436761856079102,4.2400469779968262}})
ldd_4593(array[1]{26},array[1]{0},array[1][12]{{0,-1,0,0,0,-1,1,0,0,3.6005184650421143,8.2436790466308594,3.8200454711914062}})
}
ldd_3710(array[1]{24},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,0.4005124568939209,8.3200035095214844,4.4000201225280762}})
ldd_3022(array[1]{26},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,1.2005130052566528,8.0000038146972656,4.4000277519226074}})
ldd_6183(array[1]{24},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,-0.39948558807373047,6.0800023078918457,4.4000048637390137}})
ldd_4081(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.4005126953125,8.0000028610229492,4.4000201225280762}})
ldd_93606(array[1]{24},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.0005121231079102,8.6400041580200195,4.4000353813171387}})
ldd_6183(array[1]{24},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,-0.39947891235351563,6.0800051689147949,3.6000056266784668}})
union { 
ldd_4592(array[1]{24},array[1]{0},array[1][12]{{0,-1,0,0,0,-1,1,0,0,-0.39948606491088867,8.2436714172363281,4.2400126457214355}})
ldd_4593(array[1]{26},array[1]{0},array[1][12]{{0,-1,0,0,0,-1,1,0,0,-0.39948210120201111,8.2436742782592773,3.8200111389160156}})
}
ldd_6183(array[1]{24},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,-0.39947199821472168,6.0800085067749023,2.8000025749206543}})
ldd_6183(array[1]{24},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,-0.39998388290405273,6.080012321472168,2.0000033378601074}})
ldd_3023(array[1]{21},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,2.0000147819519043,7.0400152206420898,2.0000300407409668}})
ldd_92946(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.8000168800354004,5.7600159645080566,2.0000300407409668}})
ldd_50745(array[1]{199},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.8000109195709229,4.8000125885009766,2.8000259399414063}})
ldd_3460(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,3.6005632877349854,5.7600288391113281,-1.1999626159667969}})
ldd_87552(array[1]{24},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,3.5999977588653564,3.8400070667266846,4.4000282287597656}})
ldd_57909(array[1]{199},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,3.6000182628631592,3.8400163650512695,2.000030517578125}})
ldd_3666(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,3.6000316143035889,3.5200221538543701,0.40002429485321045}})
ldd_2431(array[2]{24,0},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,3.6005628108978271,6.0800290107727051,-1.1999626159667969}})
ldd_60219(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.40001964569091797,2.5600123405456543,1.9999960660934448}})
ldd_44568(array[1]{194},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,0.40000057220458984,2.2400031089782715,4.3999977111816406}})
ldd_3020(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.0000324249267578,3.5200204849243164,0.40001285076141357}})
ldd_30499(array[1]{1},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,1.2000186443328857,3.8400135040283203,2.0000076293945313}})
ldd_4345(array[1]{194},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,3.6005523204803467,3.840022087097168,0.40002810955047607}})
ldd_2412(array[1]{21},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.200554370880127,7.680023193359375,-0.3999786376953125}})
ldd_30000(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.2005552053451538,6.7200231552124023,-0.39998340606689453}})
ldd_2412(array[1]{21},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.0005545616149902,7.6800241470336914,-0.39997220039367676}})
ldd_47457(array[1]{194},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.8005497455596924,6.080021858215332,0.40003085136413574}})
ldd_3710(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.800562858581543,5.7600278854370117,-1.1999714374542236}})
union { 
ldd_4592(array[1]{194},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.7999985218048096,3.2000057697296143,4.4000205993652344}})
ldd_4593(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.7999982833862305,3.6200063228607178,4.4000205993652344}})
}
ldd_3460(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.8000459671020508,2.8800272941589355,-1.1999826431274414}})
ldd_3009(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,3.599503755569458,4.8000192642211914,1.2000312805175781}})
ldd_3009(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,3.5995044708251953,3.8400192260742187,1.2000281810760498}})
ldd_47457(array[1]{194},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.40055537223815918,6.0800223350524902,-0.39999008178710938}})
ldd_92946(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.39949584007263184,5.7600131034851074,2.0000076293945313}})
ldd_50745(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.39949727058410645,4.8000130653381348,2.0000019073486328}})
ldd_3460(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,-0.39943695068359375,5.7600245475769043,-1.2000026702880859}})
ldd_87552(array[1]{24},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,-0.40051507949829102,3.84000563621521,3.5999889373779297}})
ldd_57909(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,-0.40050840377807617,3.8400087356567383,2.7999932765960693}})
ldd_3666(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,-0.40048789978027344,3.5200181007385254,0.39998805522918701}})
ldd_3020(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.40003204345703125,3.5200188159942627,0.4000014066696167}})
ldd_3710(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.40056371688842773,5.7600255012512207,-1.1999893188476563}})
ldd_2431(array[2]{24,0},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,-0.39943742752075195,6.0800247192382813,-1.1999969482421875}})
ldd_3032(array[1]{1},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.40004611015319824,3.2000248432159424,-1.2000007629394531}})
ldd_3460(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.40004587173461914,2.8800249099731445,-1.2000010013580322}})
union { 
ldd_4592(array[1]{194},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.39999914169311523,3.2000033855438232,4.3999977111816406}})
ldd_4593(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.39999872446060181,3.6200039386749268,4.4000015258789062}})
}
ldd_3460(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.0005903244018555,5.7600393295288086,-4.3999786376953125}})
ldd_3460(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.2005906105041504,5.7600388526916504,-4.3999824523925781}})
ldd_4345(array[1]{194},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,-0.39944148063659668,3.8400208950042725,-0.40000534057617188}})
ldd_30000(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.1999994516372681,1.2800097465515137,2.8000030517578125}})
ldd_44237(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.0000021457672119,0.32000446319580078,4.3999977111816406}})
ldd_3034(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,1.9999990463256836,2.2400074005126953,3.6000025272369385}})
ldd_3001(array[1]{199},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,1.9999990463256836,1.2800135612487793,1.9999998807907104}})
ldd_3795(array[1]{199},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.0000016689300537,0,3.5999984741210937}})
ldd_47456(array[1]{199},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,2.0005760192871094,6.4000339508056641,-2.7999730110168457}})
ldd_3795(array[1]{24},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.2005972862243652,6.0800418853759766,-5.1999812126159668}})
ldd_32059(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,3.6005589962005615,3.5200252532958984,-0.39997482299804688}})
ldd_3009(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,3.6005642414093018,4.8000283241271973,-1.1999664306640625}})
ldd_3009(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,3.6005651950836182,3.8400282859802246,-1.1999690532684326}})
ldd_15068(array[1]{24},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.200589656829834,6.7200393676757812,-4.3999786376953125}})
ldd_11295(array[1]{199},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.8000261783599854,2.5600183010101318,1.2000159025192261}})
ldd_2434(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,2.0005724430084229,3.8400297164916992,-1.9999828338623047}})
ldd_3021(array[1]{194},array[1]{0},array[1][12]{{0,0,-1,1,0,0,0,-1,0,2.4005739688873291,4.5600299835205078,-1.9999780654907227}})
ldd_30363(array[1]{199},array[1]{0},array[1][12]{{0,1,0,1,0,0,0,0,-1,2.720573902130127,4.5600299835205078,-1.9999747276306152}})
ldd_61409(array[1]{199},array[1]{0},array[1][12]{{0,0,1,1,0,0,0,1,0,4.000575065612793,4.5600318908691406,-1.9999618530273437}})
ldd_3024(array[1]{41},array[1]{0},array[1][12]{{0,0,-1,1,0,0,0,-1,0,3.680574893951416,4.5600314140319824,-1.9999666213989258}})
ldd_85984(array[1]{21},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.2000534534454346,2.8800284862518311,-1.9999961853027344}})
ldd_10247(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.0005970001220703,6.4000430107116699,-5.1999721527099609}})
ldd_3021(array[1]{194},array[1]{0},array[1][12]{{0,0,-1,-1,0,0,0,1,0,0.80057084560394287,5.3600287437438965,-1.9999885559082031}})
ldd_44661(array[1]{24},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.0005967617034912,6.7200431823730469,-5.1999702453613281}})
ldd_30000(array[1]{199},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,1.1999958753585815,1.2800278663635254,-1.9999923706054687}})
ldd_30363(array[1]{199},array[1]{0},array[1][12]{{0,-1,0,-1,0,0,0,0,-1,0.48057103157043457,5.3600282669067383,-1.9999904632568359}})
ldd_61409(array[1]{199},array[1]{0},array[1][12]{{0,0,-1,-1,0,0,0,1,0,-0.79942846298217773,4.5600271224975586,-2.0000061988830566}})
ldd_3024(array[1]{48},array[1]{0},array[1][12]{{0,0,1,-1,0,0,0,-1,0,-0.47942829132080078,4.5600266456604004,-2.0000028610229492}})
ldd_99781(array[1]{194},array[1]{0},array[1][12]{{0,1,0,1,0,0,0,0,-1,2.4005947113037109,4.5600390434265137,-4.3999786376953125}})
ldd_10247(array[1]{199},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,1.2005898952484131,6.4000391960144043,-4.3999786376953125}})
ldd_3747(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,1.9999983310699463,0.3200230598449707,-0.40000152587890625}})
ldd_44661(array[1]{24},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,0.40059661865234375,6.7200412750244141,-5.1999859809875488}})
ldd_51739(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,2.8005859851837158,3.5200369358062744,-3.5999774932861328}})
ldd_61409(array[1]{21},array[1]{0},array[1][12]{{-1,0,0,0,0,-1,0,-1,0,2.3205990791320801,5.360041618347168,-4.9599742889404297}})
ldd_99781(array[1]{194},array[1]{0},array[1][12]{{0,-1,0,-1,0,0,0,0,-1,0.80059170722961426,5.3600378036499023,-4.3999881744384766}})
ldd_61409(array[1]{21},array[1]{0},array[1][12]{{-1,0,0,0,0,-1,0,-1,0,0.88059628009796143,5.3600397109985352,-4.9599876403808594}})
ldd_6091(array[1]{21},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.0000152587890625,6.7200150489807129,2.0000264644622803}})
ldd_6091(array[1]{21},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,1.200015664100647,6.7200140953063965,2.0000185966491699}})
ldd_2412(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,2.8005423545837402,6.0800189971923828,1.2000308036804199}})
ldd_2412(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,1.2005420923233032,6.08001708984375,1.2000155448913574}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,2.8005025386810303,8.2436714172363281,5.5200386047363281}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,0.40050309896469116,8.2436685562133789,5.52001953125}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,2.0005030632019043,8.2436704635620117,5.5200309753417969}})
ldd_93571(array[1]{26},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,4.8000130653381348,4.4000153541564941,2.400043249130249}})
ldd_87083(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,6.4000134468078613,4.4000153541564941,5.1200447082519531}})
ldd_55981(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,-1,0,0,0,1,6.4000139236450195,4.4000167846679687,4.4000434875488281}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,1.2005033493041992,8.2436695098876953,5.5200271606445313}})
ldd_60476(array[1]{194},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,1.2000002861022949,1.2800036668777466,4.4000053405761719}})
ldd_48336(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,0.00083324842853471637,0.99999964237213135,0,0.99999964237213135,-0.00083324842853471637,2.7999980449676514,1.0397032499313354,4.9527130126953125}})
ldd_3633(array[1]{26},array[1]{0},array[1][12]{{1,0,0,0,0.00083324842853471637,0.99999964237213135,0,-0.99999964237213135,0.00083324842853471637,0.39999794960021973,1.0399717092514038,5.2727108001708984}})
ldd_48336(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,0.00083324842853471637,0.99999964237213135,0,0.99999964237213135,-0.00083324842853471637,1.1999993324279785,1.0397045612335205,4.9527149200439453}})
ldd_60476(array[1]{194},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,2.0000011920928955,1.280005931854248,4.4000015258789062}})
ldd_30361(array[2]{24,24},array[1]{0},array[1][12]{{0,1,0,0,0,-1,-1,0,0,0.00053781270980834961,7.3000144958496094,1.540008544921875}})
ldd_30367(array[6]{24,24,24,0,0,0},array[5]{0,0,0,0,0},array[1][12]{{-1,0,0,0,0,-1,0,-1,0,0.40055450797080994,6.900022029876709,-0.37998926639556885}})
ldd_4274(array[1]{23},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,0.00055074691772460938,7.300020694732666,0}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,-1,0,-1,0,0,0,0,-1,-0.79944896697998047,7.3000187873840332,0}})
ldd_4346(array[1]{194},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,3.6005518436431885,3.8400225639343262,0.40002822875976563}})
ldd_50747(array[2]{40,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,2.7999935150146484,3.2880051136016846,4.83203125}})
ldd_30361(array[2]{24,24},array[1]{0},array[1][12]{{0,-1,0,0,0,-1,1,0,0,3.2005379199981689,7.300018310546875,1.5400352478027344}})
ldd_30367(array[6]{24,24,24,0,0,0},array[5]{0,0,0,0,0},array[1][12]{{1,0,0,0,0,-1,0,1,0,2.8005542755126953,7.7000250816345215,-0.37996697425842285}})
ldd_4274(array[1]{23},array[1]{0},array[1][12]{{0,0,-1,0,-1,0,-1,0,0,3.2005512714385986,7.3000240325927734,3.814697265625E-005}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,1,0,1,0,0,0,0,-1,4.0005507469177246,7.300025463104248,4.1961669921875E-005}})
ldd_93571(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,0,1,0,1,0,-1.600504994392395,4.4000110626220703,2.399986743927002}})
ldd_87083(array[1]{199},array[1]{0},array[1][12]{{-1,0,0,0,-1,0,0,0,1,-3.2005054950714111,4.4000110626220703,5.119987964630127}})
ldd_55981(array[1]{24},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,-3.2005057334899902,4.4000091552734375,4.3999862670898437}})
ldd_62462(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.3999989032745361,1.4600101709365845,3.2000007629394531}})
ldd_2780(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,3.1999990940093994,1.860010027885437,3.2000007629394531}})
ldd_75937(array[1]{21},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,5.1918840408325195,1.4601541757583618,5.5001220703125}})
ldd_3943(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,4.7999954223632812,1.0600268840789795,3.5799713134765625}})
ldd_6222(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,4.3999948501586914,1.4600284099578857,2.6199722290039063}})
ldd_6218(array[1]{199},array[1]{0},array[1][12]{{-1,0,0,0,0,1,0,1,0,6.7999958992004395,2.2600317001342773,-1.2200279235839844}})
ldd_6218(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,4.3999948501586914,1.4600285291671753,-1.2200279235839844}})
ldd_6222(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,4.3999948501586914,1.4600286483764648,-2.1800270080566406}})
ldd_60474(array[1]{194},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,4.3999948501586914,1.4600286483764648,-2.5000267028808594}})
ldd_15462(array[1]{138},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,5.5999960899353027,1.860027551651001,-0.82002639770507813}})
ldd_3943(array[1]{199},array[1]{0},array[1][12]{{1,0,0,0,0,-1,0,1,0,4.7999954223632812,2.6600265502929687,-2.5000267028808594}})
ldd_75937(array[1]{21},array[1]{0},array[1][12]{{1,0,0,0,0,-1,0,1,0,5.1918845176696777,2.2598991394042969,-4.4201774597167969}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,5.9918842315673828,2.2601571083068848,5.8201217651367188}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,5.1918840408325195,2.2601571083068848,5.8201179504394531}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,5.9918842315673828,1.4601579904556274,5.8201217651367188}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{0.70710611343383789,-0.70710748434066772,0,-0.70710748434066772,-0.70710611343383789,0,0,0,-1,6.4484052658081055,2.7164311408996582,5.7471199035644531}})
ldd_76302(array[1]{26},array[1]{0},array[1][12]{{1,0,0,0,-1,0,0,0,-1,6.9003849029541016,3.1681578159332275,-3.7011833190917969}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{-0.70710635185241699,0.7071073055267334,0,-0.70710724592208862,-0.70710635185241699,0,0,0,1,6.448401927947998,2.7161760330200195,-4.6671848297119141}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,5.1918840408325195,1.4601579904556274,5.8201217651367188}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{-0.70710629224777222,-0.70710742473602295,0,-0.7071073055267334,0.70710635185241699,0,0,0,-1,6.4404082298278809,1.0116181373596191,5.7471237182617187}})
ldd_76302(array[1]{26},array[1]{0},array[1][12]{{1,0,0,0,1,0,0,0,1,6.8923912048339844,0.55963623523712158,4.7811241149902344}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{0.70710605382919312,0.70710760354995728,0,-0.7071075439453125,0.70710611343383789,0,0,0,1,6.4404120445251465,1.0113629102706909,-4.6671772003173828}})
ldd_2780(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,3.1999952793121338,1.8600286245346069,-1.5999946594238281}})
ldd_62462(array[1]{26},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.3999950885772705,1.4600287675857544,-1.5999946594238281}})
ldd_6211(array[2]{21,21},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,5.5999956130981445,3.4600286483764648,-1.5999908447265625}})
ldd_4274(array[1]{23},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,5.5999946594238281,2.6600286960601807,-1.5999947786331177}})
ldd_60897(array[1]{199},array[1]{0},array[1][12]{{0,0,1,1,0,0,0,1,0,3.6805737018585205,5.3600316047668457,-1.9999618530273437}})
ldd_4346(array[1]{194},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,-0.39944133162498474,3.8400216102600098,-0.4000091552734375}})
ldd_60897(array[1]{199},array[1]{0},array[1][12]{{0,0,-1,-1,0,0,0,1,0,-0.47942915558815002,5.3600273132324219,-2}})
ldd_62462(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,0.79999560117721558,1.4600270986557007,-1.5999908447265625}})
ldd_2780(array[1]{26},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,0,1.8600269556045532,-1.5999908447265625}})
ldd_6558(array[1]{23},array[1]{0},array[1][12]{{0,0,-1,0,1,0,1,0,0,0.80059355497360229,6.3400402069091797,-4.7999820709228516}})
ldd_41531(array[1]{24},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,-2.3994033336639404,6.3400387763977051,-5.2000102996826172}})
ldd_43122(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,1,0,0,0,-1,-2.3994033336639404,6.3400387763977051,-5.2000102996826172}})
ldd_4274(array[1]{23},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,-3.1994068622589111,6.3400363922119141,-4.8000164031982422}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,0,1,-1,0,0,0,-1,0,-3.999406099319458,6.340031623840332,-4.8000240325927734}})
ldd_6558(array[1]{23},array[1]{0},array[1][12]{{0,0,1,0,1,0,-1,0,0,2.4005930423736572,6.3400421142578125,-4.7999687194824219}})
ldd_41531(array[1]{24},array[1]{0},array[1][12]{{1,0,0,0,-1,0,0,0,-1,5.6005959510803223,6.3400492668151855,-5.1999416351318359}})
ldd_4274(array[1]{23},array[1]{0},array[1][12]{{0,-1,0,0,0,1,-1,0,0,6.4005923271179199,6.3400483131408691,-4.7999343872070312}})
ldd_98138(array[2]{40,0},array[1]{0},array[1][12]{{0,0,1,1,0,0,0,1,0,7.200592041015625,6.3400530815124512,-4.7999286651611328}})
ldd_43122(array[1]{26},array[1]{0},array[1][12]{{1,0,0,0,-1,0,0,0,-1,5.6005959510803223,6.3400492668151855,-5.1999416351318359}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,-2.8081099987030029,1.4601380825042725,5.8201217651367188}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,-2.0081098079681396,1.4601380825042725,5.8201217651367188}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,-2.8081099987030029,2.2601370811462402,5.8201179504394531}})
ldd_98138(array[2]{1,0},array[1]{0},array[1][12]{{0,1,0,0,0,1,1,0,0,-2.0081098079681396,2.2601370811462402,5.8201217651367188}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{0.70710623264312744,0.70710748434066772,0,0.70710736513137817,-0.70710629224777222,0,0,0,-1,-3.2486608028411865,2.7164103984832764,5.7471237182617187}})
ldd_76302(array[1]{26},array[1]{0},array[1][12]{{-1,0,0,0,-1,0,0,0,1,-3.70064377784729,3.1683924198150635,4.7811241149902344}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{-0.70710599422454834,-0.70710766315460205,0,0.70710760354995728,-0.70710605382919312,0,0,0,1,-3.2486646175384521,2.7166657447814941,-4.6671772003173828}})
ldd_6211(array[2]{21,21},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-2.3999993801116943,3.4600086212158203,-1.5999946594238281}})
ldd_4274(array[1]{23},array[1]{0},array[1][12]{{1,0,0,0,0,1,0,-1,0,-2.3999991416931152,2.6600086688995361,-1.5999947786331177}})
ldd_98313(array[1]{26},array[1]{0},array[1][12]{{0.70710629224777222,-0.70710736513137817,0,0.7071073055267334,0.70710629224777222,0,0,0,1,-3.2566545009613037,1.0118534564971924,-4.6671848297119141}})
}

ldd_model

ldd_statistics()