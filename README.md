## EBNF

```
<HHE> ::= apply <func> <args> to <id>
        | open "<filename>" as <id>
        | save <id> as "filename>"
        | <id>
        | <num>

<args> ::= <arg>
         | <arg> <args>
         | 

<arg> ::= NUMBER

<id> ::= STRING 
```