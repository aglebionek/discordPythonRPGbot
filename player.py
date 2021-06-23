import discord
import asyncio
import os

class Player:    
    
    def __init__(self, **kwargs):
        lang = "pl"
        if "lang" in kwargs.keys():
            lang = kwargs["lang"]
        
        if lang == "pl":
            information = ['imię', 'zawód', 'wiek', 'zamieszkały', 'urodzony']
            characteristics = ['siła', 'kondycja', 'budowa', 'zręczność', 'wygląd', 'edukacja', 'inteligencja', 'moc']
        else:
            information = ['name', 'occupation', 'age', 'sex', 'residence', 'birthplace']
            characteristics = ['strength', 'condition', 'bodysize', 'dexterity', 'appearance', 'education', 'intelligence', 'power']
        
        
        for inf in information:
            setattr(self, inf, None)
        
        for char in characteristics:
            setattr(self, char, 0)

        for key, value in kwargs.items():
            key = key.lower()
            if key in information:
                setattr(self, key, value)

        if lang == "pl":
            skills = {'antropologia': 1, 'archeologia': 1, 'broń palna długa': 25, 'broń palna krótka': 20, 'charakteryzacja': 5,
        'elektryka': 10, 'gadanina': 5, 'historia': 5, 'jeździectwo': 5, 'język obcy': 1, 'język ojczysty': self.edukacja,
        'korzystanie z bibliotek': 20, 'księgowość': 5, 'majętność': 0, 'mechanika': 10, 'medycyna': 1, 'mity cthulhu': 0,
        'nasłuchiwanie': 20, 'nauka': 1, 'nawigacja': 10, 'obsługa ciężkiego sprzętu': 1, 'okultyzm': 5, 'perswazja': 10,
        'pierwsza pomoc': 30, 'pilotowanie': 1, 'pływanie': 20, 'prawo': 5, 'prowadzenie samochodu': 20, 'psychoanaliza': 1, 
        'psychologia': 10, 'rzucanie': 20, 'skakanie': 20, 'spostrzegawczość': 25, 'sztuka/rzemosiosło': 5,
        'sztuka przetrwania': 10, 'ślusarstwo': 1, 'tropienie': 10, 'ukrywanie': 20, 'unik': self.zręczność/2, 'urok osobisty': 15,
        'walka wręcz': 25, 'wiedza o naturze': 10, 'wspinaczka': 20, 'wycena': 5, 'zastraszanie': 15, 'zręczne palce': 10}
        else:
             skills = {'accounting': 5, 'anthropology': 1, 'appraise': 5, 'archeology': 1, 'art/craft': 5, 'charm': 15, 'climb': 20,
        'credit rating': 0, 'cthulhu mythos': 0, 'disguise': 5, 'dodge' : self.dexterity/2, 'drive auto': 20, 'elec repair': 10, 
        'fast talks': 5, 'fighting': 25, 'firearms long': 25, 'firearms short': 20, 'first aid': 30, 'history': 5,
        'intimidate': 15, 'jump': 20, 'language other': 1, 'language': self.education, 'law': 5, 'library use': 20, 'listen': 20,
        'locksmith': 1, 'mech repair': 10, 'medicine': 1, 'natural world': 10, 'navigate': 10, 'occult': 5, 'op hv machines': 1,
        'persuade': 10, 'pilot': 1, 'psychology': 10, 'psychoanalysis': 1, 'ride': 5, 'science': 1, 'sleight of hand': 10,
        'spot hidden': 25, 'stealth': 20, 'survival': 10, 'swim': 20, 'throw': 20, 'track': 10}

        for k, v in skills.items():
            setattr(self, k, v)

        '''
        @staticmethod
        def Update():
            if message.author.id not in PlayersClass.players
            if os.path.isfile("./players.pickle"):
                with open('players.pickle', 'rb') as file:
        '''
    async def list(self):
        return (self.__dict__)