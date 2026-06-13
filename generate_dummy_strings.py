import os
from app import app
from models import db, GlobalOpportunity

with app.app_context():
    countries = db.session.query(GlobalOpportunity.country).distinct().all()
    categories = db.session.query(GlobalOpportunity.category).distinct().all()
    
    with open('dummy_strings.py', 'w', encoding='utf-8') as f:
        f.write("def dummy():\n")
        f.write("    _('Global')\n")
        f.write("    _('All Countries')\n")
        for (c,) in countries:
            if c: 
                # Escape quotes
                c_esc = c.replace("'", "\\'")
                f.write(f"    _('{c_esc}')\n")
        for (c,) in categories:
            if c: 
                c_esc = c.replace("'", "\\'")
                f.write(f"    _('{c_esc}')\n")
    print("Generated dummy_strings.py with dynamic content!")
