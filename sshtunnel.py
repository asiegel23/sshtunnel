import subprocess

class sshtunnel():
    def __init__(self, localport, remoteport, remoteuser, remotehost):
        self.localport = localport      
        self.remoteport = remoteport   
        self.remoteuser = remoteuser    
        self.remotehost = remotehost                                                        
    def run(self):
        exit_status = subprocess.call([
            'ssh', '-N',
                   '-L', str(self.localport) + ':' + self.remotehost + ':' +
            str(self.remoteport),
                   self.remoteuser + '@' + self.remotehost ])
        if exit_status != 0:
            return "SSH Tunnel failed"
            
            
