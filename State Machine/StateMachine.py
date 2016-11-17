

##===================================================================
## Transitions

class StateTransition(object):
    def __init__(self, toState):
        self.toState = toState

    def execute(self):
        print "Transitoning..."

##===================================================================
## States

class State(object):
    def __init__(self, StateMachine):
        self.StateMachine = StateMachine

    def enter(self):
        pass

    def execute(self):
        pass
        
    def exit(self):
        pass

class StartState(object):
    def __init__(self, StateMachine):
        super(StartState, self).__init__(StateMachine)

    def enter(self):
        ##Call GameState.GUI_Manager to display the Start Menu
        pass

    def execute(self):
        ##Wait until the user makes a playthrough choice
        ##On New Game, call GameState.UserFile_Manager to create a new save file, then set transition to TransitionState
        ##On Load Game, call GameState.UserFile_Manager to load existing save, then set transition to TransitionState
        pass
        
    def exit(self):
        ##Call GameState.GUI_Manager to close the start menu, open the game menu
        pass

class TransitionState(object):
    def __init__(self, StateMachine):
        super(TransitionState, self).__init__(StateMachine)

    def enter(self):
        pass

    def execute(self):
        ##Call GameState.DataFile_Handler to open the sent DataFile name, set transition to ReadState
        pass
        
    def exit(self):
        pass

class ReadState(object):
    def __init__(self, StateMachine):
        super(ReadState, self).__init__(StateMachine)

    def enter(self):
        
        pass

    def execute(self):
        ##Call GameState.DataFile_Handler to parse keyword
        ##Depending on the returned value, set transition to:
            ##On ENC, WaitState
            ##On FIN, TransitionState
            ##On Anything else, ReadState
        pass
        
    def exit(self):
        pass

class WaitState(object):
    def __init__(self, StateMachine):
        super(WaitState, self).__init__(StateMachine)

    def enter(self):
        pass

    def execute(self):
        ##Wait for user choice, print user choice, clear buttons, set line number to appropriate position
        pass
        
    def exit(self):
        pass


##===================================================================
## Finite State Machine

class StateMachine(object):
    def __init__(self, character):
        self.char = character
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None
        self.trans = None

    def addTransition(self, transName, transition):
        self.transitions[transName] = transition

    def addState(self, stateName, state):
        self.states[stateName] = state

    def setState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def toTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    def execute(self):
        if(self.trans):
            self.curState.Exit()
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.curState.Enter()
            self.trans = None
        self.curState.Execute()

##===================================================================
## GameState

Char = type ("Char", (object,), {})

class GameState(Char):
    def __init__(self):
        self.StateMachine = StateMachine(self)

        ## States
        self.StateMachine.AddState("StartState", StartState(self.StateMachine))
        self.StateMachine.AddState("TransitionState", TransitionState(self.StateMachine))
        self.StateMachine.AddState("ReadState", ReadState(self.StateMachine))
        self.StateMachine.AddState("WaitState", WaitState(self.StateMachine))

        ## Transitions
        self.StateMachine.AddTransition("toStartState", StateTransition("StartState"))
        self.StateMachine.AddTransition("toTransitionState", StateTransition("TransitionState"))
        self.StateMachine.AddTransition("toReadState", StateTransition("ReadState"))
        self.StateMachine.AddTransition("toWaitState", StateTransition("WaitState"))

        self.FSM.SetState("Start")

    def Execute(self):
        self.FSM.Execute()

if __name__ == '__main__':
    game = GameState()
    
    game.Execute()

