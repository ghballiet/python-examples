class Job:
    name = ""
    times = {}
    releases = []
    
    def __init__(self,name):
        self.name = name
        self.times = {
            'sun' : False,
            'mon' : False,
            'tue' : False,
            'wed' : False,
            'thu' : False,
            'fri' : False,
            'sat' : False
        }
    
        
    def add_time(self,time):
        if time.lower().strip() == "weekdays":
            self.times['mon'] = True
            self.times['tue'] = True
            self.times['wed'] = True
            self.times['thu'] = True
            self.times['fri'] = True
        elif time.lower().strip() == "daily":
            for k in self.times.keys():
                self.times[k] = True
        else:
            self.times[time.lower().strip()] = True
    
    def __str__(self):
        output = ""
        output += self.name.strip() + "  "
        if self.times['sun'] == True:
            output += " X   "
        else: 
            output += "     "
        if self.times['mon'] == True:
            output += " X   "
        else: 
            output += "     "
        if self.times['tue'] == True:
            output += " X   "
        else: 
            output += "     "
        if self.times['wed'] == True:
            output += " X   "
        else: 
            output += "     "
        if self.times['thu'] == True:
            output += " X   "
        else: 
            output += "     "
        if self.times['fri'] == True:
            output += " X   "
        else: 
            output += "     "
        if self.times['sat'] == True:
            output += " X   "
        else: 
            output += "     "
        return output
        
    def __unicode__(self):
        return self.name
    

class JobParser:
    jobs = []
    tag = ""
    name = ""
    code = ""
    
    def __init__(self,name):
        self.name = name
    
    
    def __init__(self,name,tag):
        self.name = name
        self.tag = tag
    
        
    def __init__(self,name,tag,code):
        self.name = name
        self.tag = tag
        self.code = code
    
    def add_job(self,job):
        self.jobs.append(job)
    
    def parse(self):
        print "          SUN  MON  TUE  WED  THU  FRI  SAT"
        curr_job = None
        lines = self.code.split("\n")
        for line in lines:
            if line.startswith("/*"):
                continue
            line = line.strip()
            tokens = line.split()
            
            if len(tokens) > 0:
                t = tokens[0]
            
                if t.lower() == "job":
                    name = tokens[1]
                    j = Job(name)
                    curr_job = j
                    if j not in self.jobs:
                        self.add_job(j)
                elif t.lower() == "run":
                    curr_job.add_time(tokens[1])
                elif t.lower() == "endjob":
                    print curr_job
                    curr_job = None
    
    


file = """                    INVOKE SYS4.ESP.PROCLIB(HVLILERP)
                    APPL HVLILERP           /*** HVL DAILY ERROR REPORTS ***/
                    JCLLIB 'ITE.JOBLIB'
                    COPYJCL 'SYS4.ESP.COPYJCL'
                    TAG 'ESC 4'
                    OPTIONS RESTARTSTEP
                    SUBAPPL LERP
                    JOB HVL5LUDD
                      EARLYSUB 00:05
                      LATESUB  01:05
                     RUN DAILY
                     REL HVL#LXED
                    ENDJOB
                    JOB HVL#LXED
                     RUN DAILY
                     REL (HVL#LRPT,HVL#LEDR)
                    ENDJOB
                    JOB HVL#LRPT
                      RUN DAILY
                    ENDJOB
                    JOB HVL#LEDR
                     RUN DAILY
                    ENDJOB
"""

jp = JobParser("HVLCKHD","",file)
jp.parse()