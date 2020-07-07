import logging

from azure.durable_functions import DurableOrchestrationClient
import azure.functions as func


async def main(req: func.HttpRequest, starter: str, message):
    """This function starts up the orchestrator from an HTTP endpoint
    starter: str
        A JSON-formatted string describing the orchestration context
    message:
        An azure functions http output binding, it enables us to establish
        an http response.
    Parameters
    ----------
    req: func.HttpRequest
        An HTTP Request object, it can be used to parse URL
        parameters.
    """


    function_name = req.route_params.get('functionName')
    base = req.params.get('base')
    exp = req.params.get('exp')
    logging.warning(f"Durable fuction triggered with base: " + base + ", exp: " + exp)
    
    logging.info(starter)
    client = DurableOrchestrationClient(starter)
    data = {
        "base": base,
        "exp": exp
    }
    instance_id = await client.start_new(function_name, client_input=data)
    response = client.create_check_status_response(req, instance_id)
    message.set(response)