from automata.fa.dfa import DFA
from automata.pda.dpda import DPDA
from automata.fa.nfa import NFA

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/dfa")
async def automata(request: Request):
    try:
        info = await request.json()
    except ValueError as e:
        return {"ERR0R:": e.args[0]}
    else:
        # dfa its a quintuple
        states = set(info.get("states", [])) # finite set of states
        input_symbols = set(info.get("input_symbols", [])) # alphabet
        transitions = dict(info.get("transitions", {})) # function of state transitions
        initial_state = info.get("initial_state", "") # initial state
        final_states = set(info.get("final_states", [])) # final state
        input_w = info.get("input_w", "") # input word

        # Check if the DFA is valid
    try:
        if len(states) == 0:
            return { "message": "States cannot be empty" }
        if any(state == "" for state in states):
            return {"message": "Cannot exists empty state in states"}
        if len(input_symbols) == 0:
            return { "message": "Input symbols cannot be empty" }
        if initial_state == "":
            return { "message": "Initial state cannot be empty" }
        if len(final_states) == 0:
            return { "message": "Final states cannot be empty" }
        if len(transitions) == 0:
            return { "message": "Transitions cannot be empty" }
        if input_w == "":
            return { "message": "Input string cannot be empty" }
    except ValueError as e:
        return {"ERR0R:": e.args[0]}
    else:
        # DFA which matches all binary strings ending in an odd number of '1's
        dfa = DFA(
            states=states,
            input_symbols=input_symbols,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )

        if dfa.accepts_input(input_w):
            return { "message": "Accepted" }
        else:
            return { "message": "Rejected" }


#pushdown automata
@app.post("/dpda")
async def pushdown_automata(request: Request):
    try:
        info = await request.json()
    except ValueError as e:
        return {"ERR0R ": e.args}
    else:
        states = set(info.get("states", []))
        input_symbols = set(info.get("input_symbols", []))
        stack_symbols = set(info.get("stack_symbols", []))
        transitions = dict(info.get("transitions", {}))
        initial_state = info.get("initial_state", "")
        initial_stack_symbol = info.get("initial_stack_symbol", "")
        final_states = set(info.get("final_state", []))
        acceptance_mode = info.get("acceptance_mode", "")
        input_w = info.get("input_w", "")

        # regras de negócio
        try:
            if len(states) == 0:
                return { "message": "States cannot be empty" }
            if any(state == "" for state in states):
                return {"message": "Cannot exists empty state in states"}
            if len(input_symbols) == 0:
                return { "message": "Input Symbol cannot be empty" }
            if len(stack_symbols) == 0:
                return { "message": "Stack symbols cant be empty" }
            if len(transitions) == 0:
                return {"message": "Transitions cannot be empty"}
            if initial_state == "":
                return { "message": "Initial state cant be empty" }
            if initial_stack_symbol == "":
                return { "message": "Initial state cant be empty" }
            if final_states == "":
                return { "message": "Final state(s) cant be empty" }
            if acceptance_mode == "":
                return { "message": "Acceptance mode cant be empty! Needs to be defined!" }
        except ValueError as e:
            return { "ERROR": e.args }
        dpda = DPDA(
            states=states,
            stack_symbols=stack_symbols,
            input_symbols=input_symbols,
            initial_stack_symbol=initial_stack_symbol,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )

        if dpda.accepts_input(input_w):
            return {"message": "Accepted"}
        return {"message": "Rejected"}

@app.post("/nfa")
async def nfa_automata(request: Request):
    try:
        info = await request.json()
    except ValueError as e:
        return {"ERR0R: ": e.args[0]}

    else:
        states = set(info.get("states", []))
        input_symbols = set(info.get("input_symbols", []))
        transitions = dict(info.get("transitions", {}))
        initial_state = info.get("initial_state", [])
        final_states = set(info.get("final_states", []))
        input_w = info.get("input_w", "")

        # regras de negócio
        try:
            if len(states) == 0:
                return {"message": "States cannot be empty"}
            if any(state == "" for state in states):
                return {"message": "Cannot exists empty state in states"}
            if len(input_symbols) == 0:
                return {"message": "Input Symbol cannot be empty"}
            if len(transitions) == 0:
                return {"message": "Transitions cannot be empty"}
            if initial_state == "":
                return {"message": "Initial state cant be empty"}
            if len(final_states) == 0 or any(final_state == "" for final_state in final_states):
                return {"message": "Final state(s) cant be empty"}
        except ValueError as e:
            return {"ERR0R: ": e.args}
        else:
            nfa = NFA(
                states=states,
                input_symbols=input_symbols,
                transitions=transitions,
                initial_state=initial_state,
                final_states=final_states
            )

            if nfa.accepts_input(input_w):
                return {"message": "Accepted"}
            return {"message": "Rejected"}

