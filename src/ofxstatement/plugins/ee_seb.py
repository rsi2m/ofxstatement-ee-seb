from typing import Set, List, Iterable, TextIO, Optional

from ofxstatement.plugin import Plugin
from ofxstatement.parser import StatementParser
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import Statement, StatementLine
import csv


class EstoniaSebPlugin(Plugin):
    def get_parser(self, filename: str) -> "SebParser":
        return SebParser(open(filename, "rt"))


class SebParser(CsvStatementParser):

    # 0 Account
    # 1 Valuta
    # 2 Buchungstext
    # 3 Kontonummer
    # 4 Auftraggeber / Empfänger
    # 5 Konto/IBAN
    # 6 BLZ/BIC
    # 7 Verwendungszweck
    # 8 Betrag in EUR

    mappings = {"payee": 4, "date": 2, "id": 10, "amount": 8, "memo":11}
    date_format = "%d.%m.%Y"

    def __init__(self, fin: TextIO) -> None:
        super().__init__(fin)

    def split_records(self) -> Iterable[str]:
        return csv.reader(self.fin, delimiter=';')

    def parse_record(self, line: str) -> StatementLine:
        if self.cur_record < 2:
            return None

        print(line[8])
        line[8] = line[8] if line[7]=="C" else "-"+line[8]
        
        sl = super(SebParser, self).parse_record(line)
        print(sl.amount)
        return sl
