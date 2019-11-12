## EBNF

```
<HHE> ::= <img>
        | open <filename> as <id>
        | save <id> as <filename>

<img> ::= <id>
		| apply <func> to <img>

<filename> ::= "<literal>"

<func> ::= <id> <nums>

<literal> ::= STRING

<nums> ::= 
         | <num> <nums>
```