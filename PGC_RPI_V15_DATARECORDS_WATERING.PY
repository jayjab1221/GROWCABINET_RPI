#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:07:09 2019

@author: jayjab1221
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:53:04 2019

@author: jayjab1221
"""




#one function to tell me the type of growth cycle used (chosen by input from user); One function to tell me the crop or plant
#being grown; another function to pull ideal conditions from that plant, function for ideal on/off morning times.

#################################################################################################    
#################################################################################################
################################Watering Conditions Setup########################################



def WateringConditions():
    
    global WateringInterval
    global WateringFlag
    global WateringDayStamp
    global WateringLength
      

    while True:
        try:
          print('Input Watering Interval in unit of days.  Ex: 1 = every day, 2 = every two days.')
          WateringInterval = int(input())
        except ValueError:
            print("Input not recognized, try again.")
            continue
        if type(WateringInterval) != int:
            print('Input value is not and interger.  Please try again.')
            continue
        else:
            break
    
    while True:
        try:
            print('Input Watering Length in unit of minutes.  Ex: 1 = minute.')
            WateringLength = int(input())
        except ValueError:
            print("Input not recognized, try again.")       
        if type(WateringLength) != int:
            print('Input value is not and interger.  Please try again.')
            continue
        else:
            break     
    
    WateringFlag = 0
    WateringDayStamp = 0
    WateringLength = WateringLength * 60 ##conversion to seconds









#################################################################################################  
#################################################################################################
#################################################################################################
#################################################################################################    
#################################################################################################
###################################Growth Cycle Functions########################################
def CycleTypeFunc():
    global CycleType
    CycleType = None
    
    while (CycleType is None or (CycleType != 'F' or CycleType != 'V' or CycleType != 'SB')):
        print('Please identify cycle type, [Vegetative], [Flowering], or [Speed Breeding]. (V/F/SB)')
        CycleType = input().upper()
        if CycleType == 'V':
            print('Vegetative cycle entered.')
            break
        elif CycleType == 'F':
            print('Flowering cycle entered.')
            break
        elif CycleType == 'SB':
            print('Speed Breeding cycle entered.')
            break
        
##################################################################################################   
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
###################################Crop Identification Function###################################           
def CropIdentification():
    global CropType
    CropType = None
    while (CropType is None or (CropType != 'PE' or CropType != 'CS')):
        print('Please identify crop type: [Pepper] (PE), [Cannabis] (CS)')
        CropType = input().upper()
        if CropType == 'PE':
            print('Peppers entered.')
            global PE_Dict
            PE_Dict = {'DayMaxTemp': 22,
                       'DayMinTemp': 16,
                       'NightMaxTemp': 18,
                       'NightMinTemp': 14,
                       'VHours': 16,
                       'FHours':16,
                       'SBHours': 20}
            break
        
        elif CropType == 'CS':
            print('Cannabis entered.')
            global CS_Dict
            CS_Dict = {'DayMaxTemp': 25,
                       'DayMinTemp': 16,
                       'NightMaxTemp': 25,
                       'NightMinTemp': 16,
                       'VHours': 16,
                       'FHours':12,
                       'SBHours': 20}
            break
        
##################################################################################################           
##################################################################################################
##################################################################################################
##################################################################################################
###################################Ideal Growing Conditions Function##############################
##################################################################################################            
##################################################################################################
def IdealGrowingCond():
    
    global DayMaxTemp
    global DayMinTemp
    
    global NightMaxTemp
    global NightMinTemp 
    
    global DayLength
    global NightLength
    
    global DailyCycleStart
    global DailyCycleEnd
    
    global ResearchDayCycleLength
    global ResearchNightCycleLength

    if ResearchFlag == False: #new addition, can drop out and unindent below code to revert to normal.
        
        DailyCycleStart = None #default
        DayMaxTemp = None
        DayMinTemp = None
        NightMaxTemp = None
        NightMinTemp = None
        
        DayMaxTemp = eval(CropType+'_Dict')['DayMaxTemp']
        DayMinTemp = eval(CropType+'_Dict')['DayMinTemp']
        NightMaxTemp = eval(CropType+'_Dict')['NightMaxTemp']
        NightMinTemp = eval(CropType+'_Dict')['NightMinTemp']
        DayLength = eval(CropType+'_Dict')[CycleType+'Hours']
        NightLength = 24 - eval(CropType+'_Dict')[CycleType+'Hours']
        
        while True:
            try:
                print('Enter hour to start Day cycle (interger)')
                DailyCycleStart = int(float(input()))
            except ValueError:
                print("Input not recognized, try again.")
                continue           
            else:
                #Input ok
                break
            
        while (int(DailyCycleStart) + int(DayLength)) <= 24:
            DailyCycleEnd = int(DailyCycleStart) + int(DayLength)
            print('Day Cycle Start = ',DailyCycleStart)
            print('Day Cycle End = ',DailyCycleEnd)
            break
            
        while (int(DailyCycleStart) + int(DayLength)) > 24:
                TempDailyCycleEnd = int(DailyCycleStart) + int(DayLength)
                print('Day Cycle Start + optimal Day Length > 24 hours.  Optimal Day Length =',DayLength,' hours')
                print('Chosen Day Cycle Start = ',DailyCycleStart)
                print('Calculated Day Cycle End = ',TempDailyCycleEnd)
                print('Auto adjust (A) or manaul adjust (M)')
                UserInputUpdateMethod = input()
                
                if UserInputUpdateMethod.upper() == 'A':
                    DailyCycleStart = int(24) - int(DayLength)
                    DailyCycleEnd = int(DailyCycleStart) + int(DayLength)
                    print('Day Cycle Start adjusted to ',DailyCycleStart)
                    print('Day Cycle End adjusted to ',DailyCycleEnd)
                    break
                
                elif UserInputUpdateMethod.upper() == 'M':
                    print('Enter hour to calculate Day/Night cycle (interger).  Remember, Optimal Day Lenth = ',DayLength, ' hours')
                    DailyCycleStart = int(input())
                    DailyCycleEnd = int(DailyCycleStart) + int(DayLength)
                    print('Day Cycle Start adjusted to ',DailyCycleStart)
                    print('Day Cycle End adjusted to ',DailyCycleEnd)
                    #break
                
                elif (UserInputUpdateMethod.upper() != 'M' or UserInputUpdateMethod.upper() != 'A'):
                    print('Retry Entry')
                    
                else:
                    print('Standard Cycle Broke')
                    break
    
    elif ResearchFlag == True:#New code, can drop out all code below this to revert back to normal.
        
        while True:
            try:
                print('Input maxiumum temperature for "Day" cycle (Celcius).')
                DayMaxTemp = int(float(input()))
            except ValueError:
                print("Input not recognized, try again.")
                continue
            if type(DayMaxTemp) != int:
                print("Input value is not and interger, try again.")
                continue
            else:
                #Input ok
                break            
        
        while True:
            try:
                print('Input minimum temperature for "Day" cycle (Celcius).')
                DayMinTemp = int(float(input()))
            except ValueError:
                print("Input not recognized, try again.")     
                continue
            if type(DayMinTemp) != int:
                print("Input value is not and interger, try again.")
                continue
            else:
                #Input ok
                break        
        #print('Is "Night" cycle max/min temperatures the same as day.')
        while True:
            try:
                print('Input maxiumum temperature for "Night" cycle (Celcius).')
                NightMaxTemp = int(float(input()))
            except ValueError:
                print("Input not recognized, try again.")
                continue
            if type(NightMaxTemp) != int:
                print("Input value is not and interger, try again.")
                continue
            else:
                #Input ok
                break

        while True:
            try:            
                print('Input minimum temperature for "Night" cycle (Celcius).')
                NightMinTemp = int(float(input()))        
            except ValueError:
                print("Input not recognized, try again.") 
                continue
            if type(NightMinTemp) != int:
                print("Input value is not and interger, try again.")
                continue
            else:
                #Input ok
                break 
            
        #research cycle temp QC
        while DayMaxTemp < DayMinTemp:
            try:
                print('Max "Day" temperature is less than or equal to min temperature. Please input new maximum and minimum temperature.')
                print('')
                print('Input maxiumum "Day" temperature (Celcius).')
                DayMaxTemp = int(float(input()))
    
                print('Input minimum "Day" temperature (Celcius).')
                DayMinTemp = int(float(input())) 
                
            except ValueError:
                print("Input not recognized, try again.")
                DayMinTemp = 999999999999
                continue
        
        while NightMaxTemp < NightMinTemp:
            try:
                print('Max "Night" temperature is less than or equal to min temperature. Please input new maximum and minimum temperature.')
                print('')
                print('Input maxiumum "Night" temperature (Celcius).')
                NightMaxTemp = int(float(input()))
        
                print('Input minimum "Night" temperature (Celcius).')
                NightMinTemp = int(float(input())) 

            except ValueError:
                print("Input not recognized, try again.")
                NightMinTemp = 999999999999
                continue
        
        while True:
            try:         
                print('Input day cycle length (hours in a 24 hour day)')
                ResearchDayCycleLength = int(float(input()))
            except ValueError:
                print("Input not recognized, try again.")
                continue
            if type(ResearchDayCycleLength) != int:
                print("Input value is not and interger, try again.")
                continue
            else:
                #Input ok
                break

        while True:
            try: 
                print('Input night cycle length (hours in a 24 hour day)')
                ResearchNightCycleLength = int(float(input()))
            except ValueError:
                print("Input not recognized, try again.")
                continue
            if type(ResearchNightCycleLength) != int:
                print("Input value is not and interger, try again.")
                continue
            else:
                #Input ok
                break
            
        while True:
            try:     
                print('Enter hour to start Day cycle (interger)')
                DailyCycleStart = int(float(input()))
            except ValueError:
                print("Input not recognized, try again.")
                continue
            if type(DailyCycleStart) != int:
                print("Input value is not and interger, try again.")
                continue
            elif DailyCycleStart > 24:
                print("Start time over 24 in a 24 hour day, try again.")
            else:
                #Input ok
                break
            
    else:
        print('Research Cycle Broke')


#IdealGrowingCond()
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
###########################To Define Standard vs. Research Capabilities###########################
##################################################################################################
def StandardVsResearch():
    global UserInputStandardVsResearch
    global ResearchFlag
    
    UserInputStandardVsResearch = None
    ResearchFlag = None
    UserInputStandardVsResearch = "N/A"
    
#    print('Choose [STANDARD] or [RESEARCH] for growth cycling options. Research allows personalized day length and standard uses optimal options for crop.')
#    UserInputStandardVsResearch = str(input().upper())
    
    while UserInputStandardVsResearch != 'R' or UserInputStandardVsResearch != 'RESEARCH' or UserInputStandardVsResearch != 'S' or UserInputStandardVsResearch != 'STANDARD':
        print('Choose [STANDARD] or [RESEARCH] for growth cycling options. Research allows personalized day length and standard uses optimal options for crop.')
        UserInputStandardVsResearch = str(input().upper())
        if (UserInputStandardVsResearch == 'STANDARD' or UserInputStandardVsResearch == 'S'):
            ResearchFlag = False
            print('Standard cycling options chosen.')
            break
        
        elif (UserInputStandardVsResearch == 'RESEARCH' or UserInputStandardVsResearch == 'R'):
            ResearchFlag = True
            print('Research cycling options chosen.')
            break
        


#StandardVsResearch()
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##########################################Import Necessar Packages################################
##################################################################################################

####importing as a function does not make the imports global.  Best practice is to do at top of the program

#def ImportNecessaryPackages():
#    import RPi.GPIO as GPIO #need to comment out 
#    import time
#    from w1thermsensor import W1ThermSensor
#    import datetime
#    import threading
    #from multiprocessing import Process
    #import ow

##################################################################################################
####################NEED DS18B20 code to pull temperatures.
##################################################################################################


# Typical reading
# 73 01 4b 46 7f ff 0d 10 41 : crc=41 YES
# 73 01 4b 46 7f ff 0d 10 41 t=23187
def TemperatureMonitoring():
    
    global Sensor_Dict
    global CurMaxTemp
    global CurMaxTemp
    global CurMinTemp
    
    Sensor_Dict = {}
        
    try:
    #while True:
        for sensor in W1ThermSensor.get_available_sensors():
            
            Sensor_Dict[sensor.id] = sensor.get_temperature()
            
        CurMaxTemp = max(Sensor_Dict.values())
        CurMinTemp = min(Sensor_Dict.values())
#            print("Current Max Temp is %s" % (CurMaxTemp))     

    except KeyboardInterrupt:
        print('Quitter! GPIO cleaned up')
        GPIO.cleanup() #GPIO cleanup here
        
        
        
        
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
#####################Request Set Name and Create File#############################################
##################################################################################################
##################################################################################################


def DataCollectionGrowCabinet():
    #global GrowSetName
    GrowSetName = None
    #global SetNameInputVerification
    SetNameInputVerification = None
    
    while (GrowSetName is None or GrowSetName == ""):
        print('Please define set name for data tracking purposes. Ex: "ThaiHotPepper_CY2020"')
        GrowSetName = input().upper()
        
        while (GrowSetName is not None and GrowSetName != ""):
            print('You entered ',GrowSetName,'. Is this correct? (Y/N)')
            SetNameInputVerification = input().upper()
            if (SetNameInputVerification != 'Y' and SetNameInputVerification != 'N'):
                print('Incorrect entry provided.  Please enter "Y" or "N".')
                #SetNameInputVerification = input().upper()
                continue
            elif SetNameInputVerification == 'Y':
                print('Set name entered. Set name is',GrowSetName,'.')
                break
            elif SetNameInputVerification == 'N':
                GrowSetName = None
                continue
            else:
                print('Error in set name creation.')
                break
    GrowSetFileName = GrowSetName+".csv"
    GrowSetTempFile = open(GrowSetFileName, "a")
    GrowSetTempFile.close()







##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
#####################Data Recording Code##########################################################
##################################################################################################
##################################################################################################


def DataWriteToSet():

    CabinetDataFrame = {
            'SetName':[GrowSetName], 
            'TimeStamp': [time.time()], 
            'CurMaxTemp': [CurMaxTemp], 
            'CurMinTemp': [CurMinTemp], 
            'NDVI': [None], 
            'DailyCycleStart': [DailyCycleStart],
            'SetDayLength': [DayLength],
            'SetNightLength': [NightLength], 
            'SetDayMaxTemp': [DayMaxTemp],
            'SetDayMinTemp': [DayMinTemp],
            'SetNightMaxTemp': [NightMaxTemp],
            'SetNightMinTemp': [NightMinTemp]
            }
    
    df = pd.DataFrame.from_dict(CabinetDataFrame,orient='columns')
    FileEmpty = os.stat(GrowSetFileName).st_size == 0
    
    if FileEmpty:
         
        with open(GrowSetFileName, "a") as GrowSetTempFile:
            df.to_csv(GrowSetTempFile, index=None, sep=',', mode='a')
            GrowSetTempFile.close()
        
    elif FileEmpty == False:
        with open(GrowSetFileName, "a") as GrowSetTempFile:
            df.to_csv(GrowSetTempFile,header = None, index=None, sep=',', mode='a')
            GrowSetTempFile.close()
        
    else:
         print('Data Recording Code Broke')









        
        
##################################################################################################
##############################################Environmental Analysis Code#########################
#################################################Day_Cycle########################################
def EnvironmentalMonitoring():

    time.sleep(SleepTime)
    try: ####Need to update if elif statements to remove time
        
        #while True:
            
            #used to be while
            if ResearchFlag == False and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd:
                
                if CurMaxTemp >= DayMaxTemp and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd:
                    GPIO.output(22,1) #Fans turn on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
                    FanOnTime = int(time.time()) + 60
                    FanTimeCheck = 1
    #                print('Too Hot, Fan ON!!!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print('')
                   
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp > DayMinTemp and FanTimeCheck - 1 == 0 and time.time() < FanOnTime and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd: # and time.time() < FanOnTime:
                    GPIO.output(22,1) #Fans stay on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
    #                print('Cool down phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print('')
                    
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp > DayMinTemp and FanTimeCheck - 1 == 0 and time.time() >= FanOnTime and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd:# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
    #                FanTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print('')
                    
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp >= DayMinTemp and FanTimeCheck == 0 and HeatTimeCheck == 0 and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd:
                    GPIO.output(22,0) #Fans turn off
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print('')
                  
                elif CurMaxTemp < DayMinTemp and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd:
                    GPIO.output(22,0) #Fans turn off        
                    GPIO.output(17,1) #Heater turns on
                    GPIO.output(27,1) #lights on
                    HeatOnTime = int(time.time()) + 30
                    HeatTimeCheck = 1
    #                print('Brrr. Too cold, heat on!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print('')
        
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp >= DayMinTemp and HeatTimeCheck - 1 == 0 and time.time() < HeatOnTime and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd: # and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans stay off
                    GPIO.output(17,1) #Heater stays on until heat time expired
                    GPIO.output(27,1) #lights on
    #                print('Warm up phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print('')
        
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp >= DayMinTemp and HeatTimeCheck - 1 == 0 and time.time() >= HeatOnTime and time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < DailyCycleEnd:# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
                    HeatTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print('')
        
                else:
                    print('Standard Day Broke!')
                    
                #time.sleep(SleepTime)
        #####################################################Night_Cycle####################################################3
            elif ResearchFlag == False and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart):
            
                if CurMaxTemp >= NightMaxTemp and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart):
                    GPIO.output(22,1) #Fans turn on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
                    FanOnTime = int(time.time()) + 60
                    FanTimeCheck = 1
    #                print('Too Hot, Fan ON!!!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print('')
                   
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and FanTimeCheck - 1 == 0 and time.time() < FanOnTime and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart): # and time.time() < FanOnTime:
                    GPIO.output(22,1) #Fans stay on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
    #                print('Cool down phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print('')
                    
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and FanTimeCheck - 1 == 0 and time.time() >= FanOnTime and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart):# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
                    FanTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print('')
                    
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and FanTimeCheck == 0 and HeatTimeCheck == 0 and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart):
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print('')
                  
                elif CurMaxTemp < NightMinTemp and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart):
                    GPIO.output(22,0) #Fans turn off         
                    GPIO.output(17,1) #Heater turns on
                    GPIO.output(27,0) #lights off
                    HeatOnTime = int(time.time()) + 30
                    HeatTimeCheck = 1
    #                print('Brrr. Too cold, heat on!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print('')
        
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and HeatTimeCheck - 1 == 0 and time.time() < HeatOnTime and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart): # and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans stay off
                    GPIO.output(17,1) #Heater stays on
                    GPIO.output(27,0) #lights off
    #                print('Warm up phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print('')
        
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and HeatTimeCheck - 1 == 0 and time.time() >= HeatOnTime and (time.localtime().tm_hour >= DailyCycleEnd or time.localtime().tm_hour < DailyCycleStart):# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
                    HeatTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print('')
            
                else:
                    print('Standard Night Broke!')

                #time.sleep(SleepTime)


    ####################################Research Cycle Start Determination##################################################################
    ########################################################################################################################################                
            elif ResearchFlag == True and DayFlag == 'N/A' and ResearchCycleStartFlag == 'N/A':
                
                
                if time.localtime().tm_hour < DailyCycleStart:
                    
                    ResearchCycleStartFlag = 'N/A'
                    DayFlag = 'N/A'
                    DayTimer = 'N/A'
                    NightFlag = 'N/A'
                    NightTimer = 'N/A'
                    
                elif time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour < (DailyCycleStart+ ResearchNightCycleLength) and DayFlag == 'N/A' and ResearchCycleStartFlag == 'N/A':
                    
                    ResearchCycleStartFlag = 1
                    DayFlag = 1
                    DayTimer = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, DailyCycleStart, 0, 0, 0).timestamp() + (ResearchDayCycleLength * 3600)
                    NightFlag = 0
                    NightTimer = 0

                    
                elif time.localtime().tm_hour >= DailyCycleStart and time.localtime().tm_hour > (DailyCycleStart + ResearchNightCycleLength) and time.localtime().tm_hour < (DailyCycleStart + ResearchNightCycleLength + ResearchDayCycleLength) and DayFlag == 'N/A' and ResearchCycleStartFlag == 'N/A':    

                    ResearchCycleStartFlag = 1
                    DayFlag = 0
                    DayTimer = 0 
                    NightFlag = 1
                    NightTimer = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, DailyCycleStart + ResearchNightCycleLength, 0, 0, 0).timestamp() + (ResearchNightCycleLength * 3600)
                   
                else: 
                    
                    time.sleep((datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday+1, DailyCycleStart, 0, 0, 0))-time.localtime())    
                    DayTimer = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, DailyCycleStart, 0, 0, 0).timestamp() + (ResearchDayCycleLength * 3600)
                    ResearchCycleStartFlag = 1
                    DayFlag = 1
                    NightFlag = 0
                    NightTimer = 0
     
                #time.sleep(SleepTime)    
     ####################################Research Cycle Start Monitoring##################################################################    
              
            elif ResearchFlag == True and ResearchCycleStartFlag == 1:
                
    ######Day Research Cycle Monitoring          
                if CurMaxTemp >= DayMaxTemp and time.time() <= DayTimer and time.time() > NightTimer and DayFlag == 1:
                    GPIO.output(22,1) #Fans turn on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
                    FanOnTime = int(time.time()) + 60
                    FanTimeCheck = 1
    #                print('Too Hot, Fan ON!!!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                   
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp > DayMinTemp and FanTimeCheck - 1 == 0 and time.time() < FanOnTime and time.time() <= DayTimer and time.time() > NightTimer and DayFlag == 1: # and time.time() < FanOnTime:
                    GPIO.output(22,1) #Fans stay on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
    #                print('Cool down phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                    
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp > DayMinTemp and FanTimeCheck - 1 == 0 and time.time() >= FanOnTime and time.time() <= DayTimer and time.time() > NightTimer and DayFlag == 1:# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
                    FanTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                    
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp >= DayMinTemp and FanTimeCheck == 0 and HeatTimeCheck == 0 and time.time() <= DayTimer and time.time() > NightTimer and DayFlag == 1:
                    GPIO.output(22,0) #Fans turn off
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                  
                elif CurMaxTemp < DayMinTemp and time.time() <= DayTimer and time.time() > NightTimer and DayFlag == 1:
                    GPIO.output(22,0) #Fans turn off        
                    GPIO.output(17,1) #Heater turns on
                    GPIO.output(27,1) #lights on
                    HeatOnTime = int(time.time()) + 30
                    HeatTimeCheck = 1
    #                print('Brrr. Too cold, heat on!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
        
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp >= DayMinTemp and HeatTimeCheck - 1 == 0 and time.time() < HeatOnTime and time.time() <= DayTimer and time.time() > NightTimer and DayFlag == 1: # and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans stay off
                    GPIO.output(17,1) #Heater stays on until heat time expired
                    GPIO.output(27,1) #lights on
    #                print('Warm up phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
        
                elif CurMaxTemp < DayMaxTemp and CurMaxTemp >= DayMinTemp and HeatTimeCheck - 1 == 0 and time.time() >= HeatOnTime and time.time() <= DayTimer and time.time() > NightTimer and DayFlag == 1:# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,1) #lights on
                    HeatTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights on')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
        
    #            else:
    #                print('Broke!')
    #                    
    #            time.sleep(SleepTime)           

    ######Night Research Cycle Monitoring
                
                elif CurMaxTemp >= NightMaxTemp and time.time() > DayTimer and time.time() <= NightTimer and NightFlag == 1:
                    GPIO.output(22,1) #Fans turn on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
                    FanOnTime = int(time.time()) + 60
                    FanTimeCheck = 1
    #                print('Too Hot, Fan ON!!!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                   
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and FanTimeCheck - 1 == 0 and time.time() > DayTimer and time.time() <= NightTimer and NightFlag == 1: # and time.time() < FanOnTime:
                    GPIO.output(22,1) #Fans stay on
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
    #                print('Cool down phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                    
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and FanTimeCheck - 1 == 0 and time.time() >= FanOnTime and time.time() > DayTimer and time.time() <= NightTimer and NightFlag == 1:# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
                    FanTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                    
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and FanTimeCheck == 0 and HeatTimeCheck == 0 and time.time() > DayTimer and time.time() <= NightTimer and NightFlag == 1:
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
                  
                elif CurMaxTemp < NightMinTemp and time.time() > DayTimer and time.time() <= NightTimer and NightFlag == 1:
                    GPIO.output(22,0) #Fans turn off         
                    GPIO.output(17,1) #Heater turns on
                    GPIO.output(27,0) #lights off
                    HeatOnTime = int(time.time()) + 30
                    HeatTimeCheck = 1
    #                print('Brrr. Too cold, heat on!')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
        
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and HeatTimeCheck - 1 == 0 and time.time() < HeatOnTime and time.time() > DayTimer and time.time() <= NightTimer and NightFlag == 1: # and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans stay on
                    GPIO.output(17,1) #Heater turns off
                    GPIO.output(27,0) #lights off
    #                print('Warm up phase')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')
        
                elif CurMaxTemp < NightMaxTemp and CurMaxTemp >= NightMinTemp and HeatTimeCheck - 1 == 0 and time.time() >= HeatOnTime and time.time() > DayTimer and time.time() <= NightTimer and NightFlag == 1:# and time.time() < FanOnTime:
                    GPIO.output(22,0) #Fans turn off 
                    GPIO.output(17,0) #Heater turns off
                    GPIO.output(27,0) #lights off
                    HeatTimeCheck = 0
    #                print('Temp Just Right')
    #                print(('Fan Time Left {} s').format(max(0,round((FanOnTime - time.time()),0))))
    #                print(('Heater Time Left {} s').format(max(0,round((HeatOnTime - time.time()),0))))
    #                print('Lights off')
    #                print("DayTimer = %s seconds" % (max(0,round((DayTimer - time.time()),0))))
    #                print("NightTimer = %s seconds" % (max(0,round((NightTimer - time.time()),0))))
    #                print('')

                elif time.time() > DayTimer and time.time() > NightTimer and DayFlag == 1 and NightFlag == 0:
                    
                    DayFlag = 0
                    NightFlag = 1
                    
                    NightTimer = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, time.localtime().tm_hour, time.localtime().tm_min, 0, 0).timestamp() + (ResearchNightCycleLength * 3600)
                    DayTimer = 0
            
                elif time.time() > DayTimer and time.time() > NightTimer and DayFlag == 0 and NightFlag == 1:
                    
                    DayFlag = 1
                    NightFlag = 0
                    
                    NightTimer = 0
                    DayTimer = datetime.datetime(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, time.localtime().tm_hour, time.localtime().tm_min, 0, 0).timestamp() + (ResearchDayCycleLength * 3600)           
            
            
                else:
                    print('Research Cycle Broke!')

                #time.sleep(SleepTime)


    except KeyboardInterrupt:
        print('Quitter! GPIO cleaned up')
        GPIO.cleanup() #GPIO cleanup here



##################################################################################################           
##################################################################################################
##################################################################################################
##################################################################################################
###################################Water Monitoring Function######################################
##################################################################################################            
##################################################################################################
def WateringProgram():
    
    global WateringInterval
    global WateringFlag
    global WateringDayStamp    
    global WateringLength
    global WateringTimer
    
    
    try:
        
    

        if (WateringDayStamp == 0 and WateringFlag == 0 and WateringTimer == 0): ##THIS WOULD COVER WHEN JUST STARTED AND NEED TO WATER
            GPIO.output(5,0)
            WateringDayStamp = time.localtime().tm_yday
            WateringFlag = 0
            WateringTimer = time.time() + WateringLength
            #Watering Setup
#            print('Watering Setup')
            
        elif (abs(WateringDayStamp - time.localtime().tm_yday) == 0 and WateringFlag == 0 and WateringTimer >= time.time()):
            GPIO.output(5,1)
            WateringFlag = 1 #################
#            print('Watering Cycle Started')
        
        elif (abs(WateringDayStamp - time.localtime().tm_yday) == 0 and WateringFlag == 1 and WateringTimer >= time.time()):
            GPIO.output(5,1)
            WateringFlag = 1
#            print('Continue Watering Cycle')
        
        elif (abs(WateringDayStamp - time.localtime().tm_yday) == 0 and WateringFlag == 1 and WateringTimer < time.time()):
            GPIO.output(5,0)
            WateringFlag = 1 #################
#            print('No watering needed, already watered that day')
            
        elif (abs(WateringDayStamp - time.localtime().tm_yday) == WateringInterval and WateringInterval == 1 and WateringFlag == 1):  ##THIS WOULD COVER 1 DAY INTERVALS WHEN WATERING NEEDED
            GPIO.output(5,0)
            WateringFlag = 0
            WateringDayStamp = time.localtime().tm_yday
            WateringTimer = time.time() + WateringLength
#            print('Watering cycle restarted, setting up watering timer, 1 day interval')
            
        elif (abs(WateringDayStamp - time.localtime().tm_yday) == WateringInterval and WateringFlag == 1):  ##THIS WOULD COVERS >1 DAY INTERVALS WHEN WATERING NEEDED
            GPIO.output(5,0)
            WateringFlag = 0
            WateringDayStamp = time.localtime().tm_yday
            WateringTimer = time.time() + WateringLength            
#            print('Watering needed, setting up watering timer, >1 day intervals')
        
        elif (abs(WateringDayStamp - time.localtime().tm_yday) < WateringInterval and WateringFlag == 1): #THIS WOULD >1 DAY INTERVALS WHEN WATERING NOT NEEDED
            GPIO.output(5,0)
            WateringFlag = 1
#            print('No watering needed, within watering interval, >1 day interval')
        
        else:
            print('broke')
    
    except KeyboardInterrupt:
        print('Quitter! GPIO cleaned up')
        #GPIO.cleanup() #GPIO cleanup here














##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
#####################Define Threading Function For Scheduleer#####################################
##################################################################################################
##################################################################################################








def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()






##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
#####################Setup Ideal Growing Conditions For Environmental Monitoring Loop#############
##################################################################################################
##################################################################################################
        
        
        
        
        
        
        
        
def GrowConditions():
#    ImportNecessaryPackages()
    CycleTypeFunc()
    CropIdentification()
    StandardVsResearch()
    IdealGrowingCond()
    WateringConditions()
    DataCollectionGrowCabinet() #NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW
    
    

##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
#####################GROW CABINET RUN PROGRAM#####################################################
##################################################################################################
##################################################################################################
    
    
    

#def GrowCabinetOperation():
    
    
    ####Need to alter this for scheduler
    
    
    #TempRun = threading.Thread(name = 'TemperatureMonitoring', target = TemperatureMonitoring)
    #EnvRun = threading.Thread(name = 'EnvironmentalMonitoring', target = EnvironmentalMonitoring)
    ##DataLoggerRun = threading.Thread(name = 'DataLogger', target = DataWriteToSet) #NEW NEW NEW NEW
    
    
    #TempRun.start()
    #time.sleep(5)
    #EnvRun.start()
    #time.sleep(5) NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW
    #DataLoggerRun.start()  NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW


##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
#####################Actual Program Run Commands##################################################    










##IMPORT NECESSARY PACKAGES
import RPi.GPIO as GPIO #need to comment out 
import time
from w1thermsensor import W1ThermSensor
import datetime
import threading
import pandas as pd
#import csv
import os.path
import schedule
#maybe put grow cabinet conditions up here so referenced once, try statement allows keyboard interrupt.
#under the current try loop format the grow cabinet code will repeatedly try to initiate so I need to find a better method to kill the threads
#GrowConditions()
#
#try:
#    while True:
#        ##DETERMINE OPTIMAL GROWING CONDITIONS--PRE-PROGRAMMED OR USER DEFINED
#    
#        GrowConditions()
#        ##MONITORY ENVIRONMENTAL CONDITIONS
#        GrowCabinetOperation()
#
#except KeyboardInterrupt:
#    print('Quitter! GPIO cleaned up')
#    GPIO.cleanup() #GPIO cleanup here
#
#        ##DETERMINE OPTIMAL GROWING CONDITIONS--PRE-PROGRAMMED OR USER DEFINED


#########3I think this is currently needed before growconditions() references them to make sure they are global, not certain##########
#WateringInterval = None
#WateringFlag = None
#WateringDayStamp = 0
#WateringLength = None
#WateringTimer = 0

 
GrowConditions()
        ##MONITORY ENVIRONMENTAL CONDITIONS
#GrowCabinetOperation()

#############################conditions for environmental monitoring were placed here to try and stop the on-off issue with EnvironmentalMonitoring() code
##########################################################################################################################################################

global FanOnTime
global HeatOnTime
global FanTimeCheck
global HeatTimeCheck

global SleepTime

global ResearchCycleStartFlag
global DayFlag
global DayTimer
global NightFlag
global NightTimer


global WateringInterval
global WateringFlag
global WateringDayStamp    
global WateringLength
global WateringTimer



PinOut = (17,22,27,5) #Defines output pins
GPIO.setmode(GPIO.BCM) #Defines how GPIO pins should be numbered
GPIO.setup(PinOut, GPIO.OUT) #Defines what role GPIO pins will have


FanOnTime = 0
HeatOnTime = 0
FanTimeCheck = 0
HeatTimeCheck = 0
SleepTime = 2    

DayFlag = 'N/A' #updated 12/17
ResearchCycleStartFlag = 'N/A' #updated 12/17



##########################################################################################################################################################
##########################################################################################################################################################
    
###CODE TO RUN EVIRONMENTLA MONITORING AND DATA LOGGER
schedule.every(1).seconds.do(run_threaded, TemperatureMonitoring)        
schedule.every(2).seconds.do(run_threaded, EnvironmentalMonitoring)
schedule.every(2).seconds.do(run_threaded, WateringProgram)
schedule.every(15).minutes.do(run_threaded, DataWriteToSet)

while True:
    schedule.run_pending()
    time.sleep(1)


