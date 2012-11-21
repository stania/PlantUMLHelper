# -*- coding: utf-8 -*-

import StringIO

class UsecaseDiagram(object):
    def __init__(self):
        self.rels = []
        self.actors = []
        self.__main_actor = None
        pass

    @property
    def main_actor(self):
        return self.__main_actor

    @main_actor.setter
    def main_actor(self, actor):
        self.__main_actor = actor

    def generate_output(self):
        output = StringIO.StringIO()
        print >> output, "\n".join(
            ["@startuml", "scale 0.8", "left to right direction", "skinparam defaultFontName 나눔고딕"])
        print >> output, ""
        print >> output, "actor :{0}: as {1}".format(self.main_actor.name, self.main_actor.alias)
        for actor in filter(lambda x: type(x) is not SubActor, self.actors):
            print >> output, "actor :{0}:".format(actor.name, actor.alias)
        for actor in filter(lambda x: type(x) is SubActor, self.actors):
            if actor.alias:
                print >> output, ":{0}: <-up- :{1}: as {2}".format(actor.super_actor_alias, actor.name, actor.alias)
            else:
                print >> output, ":{0}: <-up- :{1}:".format(actor.super_actor_alias, actor.name)
        print >> output, Package("", self.rels).getvalue(self.main_actor.alias)
        print >> output, "@enduml"
        result = output.getvalue()
        output.close()
        return result

class Actor(object):
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias

class MainActor(Actor):
    def __init__(self, name, alias):
        super(MainActor, self).__init__(name, alias)

class SubActor(Actor):
    def __init__(self, super_actor_alias, name, alias):
        super(SubActor, self).__init__(name, alias)
        self.super_actor_alias = super_actor_alias
        
class Relationship(object):
    def __init__(self, actor, usecase):
        self.usecase = usecase
        self.actor = actor

    def getvalue(self, main_actor_alias, last_rel = [None]):
        ret = None
        if last_rel[0] and last_rel[0].usecase is self.usecase:
            ret = ":{actor}: -up- ({usecase})".format( 
                usecase=self.usecase,
                actor=self.actor)
        else:
            ret = ":{main_actor}: -do- ({usecase})\n:{actor}: -up- ({usecase})".format( 
                main_actor=main_actor_alias,
                usecase=self.usecase,
                actor=self.actor)
        last_rel[0] = self
        return ret
        
class Package(Relationship):
    def __init__(self, name, rels = None):
        self.name = name
        self.rels = rels or []

    def getvalue(self, main_actor_alias):
        if all([type(_) is Relationship for _ in self.rels]):
            buf = StringIO.StringIO()
            for rel in reversed(self.rels):
                print >> buf, rel.getvalue(main_actor_alias)
            return buf.getvalue()
        else:
            pkgs = []
            curpkg = None
            for item in self.rels:
                if type(item) is Package:
                    if curpkg:
                        pkgs.append(curpkg)
                        curpkg = None
                    pkgs.append(item)
                else:
                    if not curpkg:
                        curpkg = Package(None, [])
                    curpkg.rels.append(item)
            if curpkg:
                pkgs.append(curpkg)
                curpkg = None

            buf = StringIO.StringIO()

            for item in pkgs:
                if item.name:
                    print >> buf, "package \"{name}\" {{\n{contents}}}\n".format(
                        name=item.name, contents=item.getvalue(main_actor_alias))
                else:
                    print >> buf, item.getvalue(main_actor_alias)

            return buf.getvalue()

def single_package(subactor_name, name):
    return Package(name[:name.find(" ")], [
        Relationship(subactor_name, name)
        ])

