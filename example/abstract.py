# -*- coding: utf-8 -*-

from PlantUMLHelper.usecase import *

d = UsecaseDiagram()
d.main_actor = MainActor("System", "SYS")
d.actors = [
    Actor("User", ""),
    SubActor("User", "Administrator", ""),
    SubActor("User", "Monitoring Agent", ""),
    SubActor("User", "Manager", ""),
    Actor("Sentry", ""),
    Actor("SNMP Agent", ""),
    Actor("Syslog Agent", ""),
    Actor("REST API Client", ""),
    SubActor("Sentry", "Windows Sentry", ""),
    SubActor("Sentry", "Linux Sentry", ""),
    ]

d.rels = [
    Relationship("User", "monitoring"),
    Relationship("User", "configuration"),
    Relationship("User", "policy management"),
    Relationship("Sentry", "interaction with 3rd-party agent"),
    Relationship("SNMP Agent", "interaction with 3rd-party agent"),
    Relationship("Syslog Agent", "interaction with 3rd-party agent"),
    Relationship("REST API Client", "interaction with 3rd-party agent"),
    ]

print d.generate_output()
