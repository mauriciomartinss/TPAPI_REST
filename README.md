## Trabalho prático da disciplina "Teoria da computacao"

### O que foi feito

- Implementacao de uma api rest usando FastApi
- Foi gerado uma imagem docker
- Link para o repositório do [DockerHub](https://hub.docker.com/repository/docker/mauriciomartinss/api-teoria-computacao/general)

### Testes HTTP

1. DFA - which matches all binary strings ending in an odd number of '1's (POST http://127.0.0.1:8000/dfa)
```json
{
    "states": ["q0", "q1", "q2"],
    "input_symbols": ["0", "1"],
    "transitions": {
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q0", "1": "q2"},
        "q2": {"0": "q2", "1": "q1"}
    },
    "initial_state": "q0",
    "final_states": ["q1"],
    "input_w": "01"
}
```

2. DPDA which which matches zero or more 'a's, followed by the same number of 'b's (accepting by final state) (POST http://127.0.0.1:8000/dpda)
```json
{
	"states": [ "q0", "q1", "q2", "q3" ],
	"input_symbols": [ "a", "b" ],
	"stack_symbols": [ "0", "1" ],
	"transitions": {
	    	 "q0": {
			 "a": {
				 "0": [ "q1", [ "1", "0" ] ]
			 }
	    	 },
		 "q1": {
			 "a": {
				 "1": [ "q1", [ "1", "1" ] ]
			 },
			 "b": {
				 "1": [ "q2", "" ]
	      		}
		 },
		 "q2": {
			 "b": {
				 "1": [ "q2", "" ]
			 },
			 "": { "0": [ "q3", [ "0" ] ]
			 }
		 }
	},
	"initial_state": "q0",
	"initial_stack_symbol": "0",
	"final_states": [ "q3" ],
	"acceptance_mode": "both",
	"input_w": "ab"
}
```

3. NFA which matches strings beginning with 'a', ending with 'a', and containing no consecutive 'b's (POST http://127.0.0.1:8000/nfa)

```json
{
	"states": ["q0", "q1", "q2"],
	"input_symbols": ["b", "a"],
	"transitions": {
		"q0": {
			"a": ["q1"]
		},
		"q1": {
			"a": ["q1"],
			"b": ["q2"]
		},
		"q2": {
			"": ["q0"]
		}
	},
	"initial_state": "q0",
	"final_states": ["q1"],
	"input_w": "aba"
}
```

