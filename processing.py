# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:13:47 2022

@author: Utente
"""

import time
import json
import numpy as np

class SignalsByNight():
    def __init__(self):
        self.content=json.load(open("apneaLog.json"))
        self.dict=self.content['e']
        self.hr=[]
        self.spo2=[]
        self.snoor=[]
        self.episodes=[]
        self.timestamp=[]
    
    def signals(self):
        hr=[]
        spo2=[]
        snoor=[]
        ts=[]
        for d in self.dict:
            for c in d:
                if c['n']=='heart rate':
                    hr=c['value']
                    ts=c['timestamp']
                    
                    self.hr.append(hr)
                    self.timestamp.append(ts)
                elif c['n']== 'Sp02':
                    spo2=c['value']
                    self.spo2.append(spo2)
                elif c['n']=='snooring':
                    snoor=c['value']
                    self.snoor.append(snoor)
                
        return self.hr, self.spo2, self.snoor, self.timestamp


class Detection():
    def __init__(self,signals):
        self.hr=signals[0]
        self.spo2=signals[1]
        self.snoor=signals[2]
        self.episodes=[]
        self.ts_episodes=[]
    #def test(self):
        #print(self.hr)
        
    def detection(self):
        for i in range(len(self.hr)):
            
            if self.hr[i] <= (73.1):
                if self.spo2[i]< (93.1) or self.snoor[i] > 45:
                    ts=self.ts_episodes[i]
                    self.episodes.append(1)
                    self.ts_episodes.append(ts)
            else:
                self.episodes.append(0)
            
            
        return self.episodes, self.ts_episodes
    
    def statistics(self):
        
        tot_apnea=np.sum(self.episodes)
        
        avr_hr=np.avarage(self.hr)
        std_hr=np.average(self.hr)
        
        avr_spo2=np.avarage(self.spo2)
        std_spo2=np.average(self.spo2)
        
        avr_snoor=np.avarage(self.snoor)
        std_snoor=np.average(self.snoor)
        
        #Writing of a json file with the above stat and ts of 
        #when apnea appeared
        
        
        
            
    

    
      
    
        
    
            
         
        

if __name__ == '__main__':

    sign=SignalsByNight()
    signals=sign.signals()
    test=Detection(signals).detection()