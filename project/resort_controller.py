from project.models import Resort

def get_resort_by_id(id):
    resort = Resort.query.filter_by(id=id).first()
    return Resort.serialize_all(resort)

def get_resort_names_by_state(state):
    resorts = Resort.query.filter_by(state=state).all()
    return [Resort.serialize_name(resort) for resort in resorts]

def get_all_resort_names():
    resorts = Resort.query.all()
    return [Resort.serialize_name(resort) for resort in resorts]