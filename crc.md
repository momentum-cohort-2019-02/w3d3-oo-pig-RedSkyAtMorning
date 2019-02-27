# Designing Objects for Pig Jig
Define all necessary classes, including responsibilties and collaborators

## Die
Attributes
    sides: 6
Responsibilities
    Return cast results to *gameMaster* when asked
    (gets rolled by *player*)

## DieDecision
Attributes
    roll or no roll of *die*
Responsibilities
    a decision from *player* to *GameMaster*

## Player
Attributes
    name: player or computer
    accumulated_score: initialized at 0
    strategy: 1 or 2 
Responsbilities
        decision to roll *die*
        evaluate *die* with *strategy*

### Hmm, Strategy Statements
1 - ask for user inititation (y to roll again) for *die decision*
2 - if score 20, hold, else *die decision*


## GameMaster 
Attributes
    person_score 
    computer_score
    holding_game
Responsbilities
    determines who goes first, *player* or *computer* with *die*
    asks for *decision* from *player*
    administers pig penalty, such that *score* is set = 0
    keeps scoreboard of *score* of each *player*
    compares *scores*
    determine winner *player*









