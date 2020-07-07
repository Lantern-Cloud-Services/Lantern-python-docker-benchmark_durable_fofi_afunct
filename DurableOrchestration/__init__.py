import logging
import time

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    start_time = time.time()

    params = context.get_input()
    base = int(params["base"])
    exp = int(params["exp"])

    logging.warning(f"Orchestrator Triggered with params - base: " + base.__str__() + ", exp: " + exp.__str__())
    results = []
    for x in range(2, exp+1):        
        data = {
            "base": base,
            "exp": x
        }
        r = yield context.call_activity("DurableActivity", data)
        results.append(r)
    
    # this summation could also be done via an additional activity function
    total = 0
    for val in results:
        total += val
    
    end_time = time.time()
    total_time = end_time-start_time
    final_result = f"With the input values base: {base}, exp: {exp} we calculated a total result of {total} in {total_time} seconds"

    return final_result


main = df.Orchestrator.create(orchestrator_function)