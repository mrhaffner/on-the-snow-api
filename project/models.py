from project import db
from slugify import slugify


class Resort(db.Model):
    __tablename__ = 'resorts'
    __table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True)  #autoincrement
    state = db.Column(db.String)
    
    def serialize_all(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state,
            'summit': self.summit,
            'vertical_drop': self.vertical_drop,
            'base': self.base,
            'trams': self.trams,
            'fast_eights': self.fast_eights,
            'fast_sixes': self.fast_sixes,
            'fast_quads': self.fast_quads,
            'quad': self.quad,
            'triple': self.triple,
            'double': self.double,
            'surface': self.surface,
            'total': self.total,
            'runs': self.runs,
            'terrain_parks': self.terrain_parks,
            'longest_run': self.longest_run,
            'skiable_terrain': self.skiable_terrain,
            'snow_making': self.snow_making,
            'days_open_last_year': self.days_open_last_year,
            'projected_days_open': self.projected_days_open,
            'night_skiing': self.night_skiing,
            'mi_night_skiing': self.mi_night_skiing,
            'mi_pistes': self.mi_pistes,
            'mi_snow_making': self.mi_snow_making,
            'years_open': self.years_open,
            'average_snowfall': self.average_snowfall,
            'url': self.url
        }
    
    def serialize_name(self):
        return {             
            'id': self.id,
            'name': self.name,
            'state_slug': slugify(self.state)
        }