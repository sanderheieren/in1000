class Celle:
    def __init__(self):
        self._status = 'død'
        
    def __str__(self):
        return 'Celle er ' + self._status

    def settDoed(self):
        self._status = 'død'

    def settLevende(self):
        self._status = 'levende'
    
    def erLevende(self):
        return self._status == 'levende'
    
    def hentStatusTegn(self):
        if self.erLevende():
            return 'O'
        return '.'

    