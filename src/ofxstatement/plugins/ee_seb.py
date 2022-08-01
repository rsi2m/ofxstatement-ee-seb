from typing import Set, List, Iterable, TextIO, Optional

from ofxstatement.plugin import Plugin
from ofxstatement.parser import StatementParser
from ofxstatement.parser import CsvStatementParser
from ofxstatement.statement import Statement, StatementLine


class EstoniaSebPlugin(Plugin):
    def get_parser(self, filename: str) -> "SebParser":
        return SebParser(open(filename, "rt"))


class SebParser(CsvStatementParser):
    def __init__(self, fin: TextIO) -> None:
        super().__init__(fin)

    def parse(self) -> Statement:
        stmt = super().parse()
        """Main entry point for parsers

        super() implementation will call to split_records and parse_record to
        process the file.
        """

        print(stmt)
        
        return stmt

    def split_records(self) -> Iterable[str]:
        """Return iterable object consisting of a line per transaction"""
        return []

    def parse_record(self, line: str) -> StatementLine:
        """Parse given transaction line and return StatementLine object"""
        return StatementLine("sd")
