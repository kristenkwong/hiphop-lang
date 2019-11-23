## EBNF

```
<HHE> ::= <id>
        | open <filename> as <id>
        | save <id> as <filename>
        | apply <func> to <id>
        | apply-all [<funcs>] to <id>
        | save-macro [<funcs>] as <id>

<filename> ::= "<literal>"

<funcs> ::= <func>
        | <func>, <funcs>

<func> ::= <id> <nums>

<literal> ::= STRING

<nums> ::= 
         | <num> <nums>
```