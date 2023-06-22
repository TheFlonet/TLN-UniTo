from cky import cky


def read_grammar(path: str):
    try:
        with open(path) as f:
            grammar = []
            for line in f.readlines():
                rule = line.strip()
                head, bodies = rule.split(' ::= ')
                bodies = [b.split(' ') for b in bodies.split(' | ')]
                for body in bodies:
                    grammar.append((head, body))
            return grammar
    except IOError:
        print('Error while parsing the grammar')


class Color:
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def exec_on_phrase(phrase: str, grammar: list[tuple]):
    print(phrase)
    phrase = phrase.lower().split(' ')
    res = cky(phrase, grammar)
    if not res:
        print(Color.RED + 'Invalid sentence' + Color.END)
    print()


if __name__ == '__main__':
    test_sentence = 'Paolo ama Francesca dolcemente'
    english_sentences = ['Book the flight through Houston', 'Does she prefer a morning flight']
    klingon_sentences = [
        'tlhIngan Hol Dajatlh\'a\'', 'puq vIlegh jIH', 'pa\'Daq jIHtaH', 'tlhIngan maH',
        'Heghlu\'meH QaQ jajvam', 'tlhIngan Hol vIjatlhaHbe\'', 'Hab SoSlI\' Quch', 'nuqDaq \'oH Qe\' QaQ\'e\''
    ]

    print(Color.BOLD + 'Esempio su una micro grammatica per l\'italiano' + Color.END)
    exec_on_phrase(test_sentence, read_grammar('grammars/italiano.cnf'))

    print(Color.BOLD + 'Frasi testate sulla grammatica L1 di Jurafsky' + Color.END)
    eng_grammar = read_grammar('grammars/l1_jurafsky.cnf')
    for i in range(2):
        exec_on_phrase(english_sentences[i], eng_grammar)

    print(Color.BOLD + 'Frasi della lingua Klingon' + Color.END)
    klingon_grammar = read_grammar('grammars/klingon.cnf')
    for i in range(8):
        exec_on_phrase(klingon_sentences[i], klingon_grammar)
