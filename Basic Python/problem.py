class DFAAccessControl:
    def __init__(self):
        # Define transitions: state -> {symbol: next_state}
        self.transitions = {
            'q0': {'CS': 'Lobby_0', 'AO': 'Cafeteria_0', 'BC': 'AdminOffice_0'},
            'Lobby_0': {'PE': 'Lobby_1'},
            'Lobby_1': {'FR': 'Lobby_2'},
            'Lobby_2': {'VR': 'Lobby_Accept'},
            'Laboratory_0': {'FP': 'Laboratory_1'},
            'Laboratory_1': {'BC': 'Laboratory_2'},
            'Laboratory_2': {'PE': 'Laboratory_Accept'},
            'ServerRoom_0': {'FP': 'ServerRoom_1'},
            'ServerRoom_1': {'BC': 'ServerRoom_2'},
            'ServerRoom_2': {'AO': 'ServerRoom_Accept'},
            'ExecutiveLounge_0': {'FR': 'ExecutiveLounge_1'},
            'ExecutiveLounge_1': {'PE': 'ExecutiveLounge_2'},
            'ExecutiveLounge_2': {'VR': 'ExecutiveLounge_Accept'},
            'ResearchWing_0': {'RS': 'ResearchWing_1'},
            'ResearchWing_1': {'FP': 'ResearchWing_2'},
            'ResearchWing_2': {'BC': 'ResearchWing_Accept'},
            'Auditorium_0': {'PE': 'Auditorium_1'},
            'Auditorium_1': {'PE': 'Auditorium_2'},
            'Auditorium_2': {'FR': 'Auditorium_Accept'},
            'Cafeteria_0': {'VR': 'Cafeteria_1'},
            'Cafeteria_1': {'FR': 'Cafeteria_2'},
            'Cafeteria_2': {'PE': 'Cafeteria_Accept'},
            'AdminOffice_0': {'BC': 'AdminOffice_1'},
            'AdminOffice_1': {'RS': 'AdminOffice_2'},
            'AdminOffice_2': {'FP': 'AdminOffice_Accept'}
        }
        self.accepting_states = {
            'Lobby_Accept', 'Laboratory_Accept', 'ServerRoom_Accept',
            'ExecutiveLounge_Accept', 'ResearchWing_Accept',
            'Auditorium_Accept', 'Cafeteria_Accept', 'AdminOffice_Accept'
        }
        self.start_state = 'q0'

    def process(self, sequence):
        state = self.start_state
        for symbol in sequence:
            if state not in self.transitions or symbol not in self.transitions[state]:
                return "Access Denied"
            state = self.transitions[state][symbol]
        return "Access Granted" if state in self.accepting_states else "Access Denied"


# Example usage
if __name__ == "__main__":  # Fixed the __name__ check
    dfa = DFAAccessControl()
    tests = [
        (['CS', 'PE', 'FR', 'VR'], "Lobby"),
        (['CS', 'FP', 'PE'], "Laboratory - wrong"),
        (['CS', 'FP', 'BC'], "ServerRoom - partial"),
        (['CS', 'FR', 'PE', 'VR', 'EXTRA'], "ExecutiveLounge with extra"),
        (['BC', 'RS', 'INVALID'], "AdminOffice with invalid")
    ]

    for seq, desc in tests:
        print(f"Test {desc}: {dfa.process(seq)}")
