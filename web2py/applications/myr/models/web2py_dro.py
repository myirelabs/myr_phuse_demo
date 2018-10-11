class Web2pyDigitalResearchObject(object):
    def __init__(self,config={}):
        self.config = config
        self.base_path = config["base_path"]
        self.logger_process = BlockchainLogger(config["blockchain_path_process"])
        self.logger_presentation = BlockchainLogger(config["blockchain_path_presentation"])
        self.logger_data = BlockchainLogger(config["blockchain_path_data"])
    
    def write(self):
        self.calculate_presentation_code_hash()
        self.calculate_process_code_hash()
        self.calculate_data_hash()
        
    def calculate_data_hash(self):
        
        logger = self.logger_data
        
        dirname = self.config["data_dir"]
        filename = self.config["data_path"]
        path = os.path.join(dirname, filename)
        
        contents = open(path,"r").read()
        
        h = hashlib.sha1(contents).hexdigest()
        data = "%s:%s" % (path,h)    
        
        logger.log(data)
        
    
    def calculate_process_code_hash(self):
        base_path = self.base_path
        logger = self.logger_process
        
        for dirname, dirnames, filenames in os.walk(base_path):
            for filename in filenames:
                if ".py" in filename and filename.endswith(".py"):
                    path = os.path.join(dirname, filename)
                    h = hashlib.sha1(open(path,"r").read()).hexdigest()
                    data = "%s:%s" % (path,h)    
                    logger.log(data)

    def calculate_presentation_code_hash(self):
        base_path = self.base_path
        logger = self.logger_presentation

        for dirname, dirnames, filenames in os.walk(base_path):
            for filename in filenames:
                if ".html" in filename and filename.endswith(".html"):
                    path = os.path.join(dirname, filename)
                    h = hashlib.sha1(open(path,"r").read()).hexdigest()    
                    data = "%s:%s" % (path,h)    
                    logger.log(data)
                if ".css" in filename and filename.endswith(".css"):
                    path = os.path.join(dirname, filename)
                    h = hashlib.sha1(open(path,"r").read()).hexdigest()    
                    data = "%s:%s" % (path,h)    
                    logger.log(data)
                if ".js" in filename and filename.endswith(".js"):
                    path = os.path.join(dirname, filename)
                    h = hashlib.sha1(open(path,"r").read()).hexdigest()    
                    data = "%s:%s" % (path,h)    
                    logger.log(data)