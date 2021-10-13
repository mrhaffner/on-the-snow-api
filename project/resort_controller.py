from project.models import Resort

def get_resort_by_id(id):
    resort = Resort.query.filter_by(id=id).first()
    return Resort.serialize_all(resort)

def get_resort_names_by_state(state):
    resorts = Resort.query.filter_by(state=state).all()
    resortList = [Resort.serialize_name(resort) for resort in resorts]
    resortList.sort(key=lambda resort: resort['id'])
    return resortList

def get_all_resort_names():
    resorts = Resort.query.all()
    resortList = [Resort.serialize_name(resort) for resort in resorts]
    resortList.sort(key=lambda resort: resort['id'])
    return resortList

def get_state_list():
    query = Resort.query.with_entities(Resort.state).distinct()
    return [state.state for state in query.all()]