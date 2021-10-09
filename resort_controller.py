from models import Resort

def get_resort_by_id(id):
    resort = Resort.query.filter_by(id=id).first()
    return Resort.serialize_all(resort)

def get_resort_names_by_state(state):
    print(state)
    resorts = Resort.query.filter_by(state='Colorado').all() #make case insensitive
    return [Resort.serialize_name(resort) for resort in resorts]