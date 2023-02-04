import pandas as pd

class Loadtimezone:
    
    def __init__(self):
        self.save : bool=False
        self.code : str='America/Newyork'
        self.load_data(save=self.save)
            
    def load_data(self, save=False):                
        timezone = pd.read_html("https://www.healthstream.com/hlchelp/Administrator/Classes/HLC_Time_Zone_Abbreviations.htm",header=0)
        self.timezone = timezone[0]
        if save: timezone.to_csv('timezone.csv',index=False)

    def code2Time(self,code):
        return self.timezone[self.timezone["Abbreviation"]==code]
    