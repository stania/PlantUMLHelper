# -*- coding: utf-8 -*-

from PlantUMLHelper.usecase import *

d = UsecaseDiagram()
d.main_actor = MainActor("SYSTEM", "SYS")
d.actors = [
    Actor("User", ""),
    SubActor("User", "Administrator", ""),
    SubActor("User", "Monitoring Agent", ""),
    SubActor("User", "Manager", ""),
    ]

d.rels = [
    Package("1.1. Case 1", [
        Relationship("User", r"1.1.1. Subcase 1"),
        Relationship("User", r"1.1.2. Subcase 2")
    ]),
    Package("1.2. Case 2", [
        single_package("User", "1.2.1. Subcase 1"),
        single_package("User", "1.2.2. Subcase 2"),
        Package(r"1.2.3. Subcase 3", [
            Relationship("User", r"case 1.2.3.1 "),
            Relationship("User", r"case 1.2.3.2 "),
            Relationship("User", r"case 1.2.3.3 "),
            Relationship("User", r"case 1.2.3.4 "),
        ]),
    ]),
    Package(r"1.3. Case 3", [
        Package("1.3.1. Subcase 1", [
            Relationship("User", r"case 1.3.1.1"),
            Relationship("User", r"case 1.3.1.2"),
            Relationship("User", r"case 1.3.1.3"),
            Relationship("User", r"case 1.3.1.4"),
            Relationship("User", r"case 1.3.1.5"),
            Relationship("User", r"case 1.3.1.6"),
        ]),
        single_package("User", r"1.3.2. Subcase 2"),
        single_package("User", r"1.3.3. Subcase 3"),
        Package("1.3.4. Subcase 4", [
            Relationship("User", r"case 1.3.4.1."),
            Relationship("User", r"case 1.3.4.2."),
            Relationship("User", r"case 1.3.4.3."),
        ]),
        single_package("User", r"1.3.5. Subcase 5"),
    ]),
    Package(r"1.4. ", [
        Relationship("User", r"Subcase 1"),
    ]),
    Package(r"1.5. ", [
        Relationship("User", r"Subcase 1"),
        Relationship("User", r"Subcase 2"),
        Relationship("User", r"Subcase 3"),
    ]),
    ]

print d.generate_output()
