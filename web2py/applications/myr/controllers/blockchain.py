
config = {
          "base_path":request.folder,
          "blockchain_path_data": os.path.join(request.folder,"private","myr.blockchain.data"),
          "blockchain_path_process": os.path.join(request.folder,"private","myr.blockchain.process"),
          "blockchain_path_presentation": os.path.join(request.folder,"private","myr.blockchain.presentation"),
          "data_dir":os.path.join(request.folder,"databases"),
          "data_path":os.path.join(request.folder,"databases","storage.sqlite")
          }

dro = Web2pyDigitalResearchObject(config)


def index():
    return dict(config=config)

def verify():
    fields = [Field("blockchain_file","upload")]
    form = SQLFORM.factory(*fields)
    if form.process().accepted:
        
        filename = form.vars.blockchain_file
        path = os.path.join(request.folder,"uploads",filename)
        
        if filename.endswith("data"):
            logger = dro.logger_data
            logger.verify(path)
        if filename.endswith("process"):
            logger = dro.logger_process
            logger.verify(path)
        if filename.endswith("presentation"):
            logger = dro.logger_presentation
            logger.verify(path)
        
    return dict(form=form)

def view():
    # highly unsafe
    path_type = request.args(0)
    path = config[path_type]
    return open(path,"r").read()

def create_study():
    form = SQLFORM(db.study_publication)
    
    if form.process().accepted:
        dro.write()
    
    return dict(form=form)

