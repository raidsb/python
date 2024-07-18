input_facts = ""
input_fact_phrases = input_facts.split(',')
conclude = "some a are c"
conclude_result = None

if conclude == "some a are c":
    if "all a are b" in input_fact_phrases:
        if "some c are b" in input_fact_phrases:
            conclude_result = False

        if "some b are c" in input_fact_phrases:
            conclude_result = False

    if "all b are a" in input_fact_phrases and "some b are c" in input_fact_phrases:
        conclude_result = True


