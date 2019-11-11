## EBNF

<HHE> ::= apply <func> <HHE> to <IMG>
        | open {<filename>} as <id>
        | <id>
        | <num>

<id> ::= STRING 