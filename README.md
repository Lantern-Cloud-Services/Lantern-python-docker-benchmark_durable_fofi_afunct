# Lantern-python-docker-benchmark_durable_fofi_afunct

A Python implementation of an Azure fan out/in durable function that takes a base integer and an exponential integer as query params.  The orchestrator function then instantiates parallel action functions to perform the base value to the power the every integer from 2 to the exponential integer and sums the results of each execution, evaluating execution time required.  For example

http://127.0.0.1:7071/api/orchestrators/DurableOrchestration?base=3&exp=4

would perform an action function to produce the value of 

<code>3^2 = 9</code>

<code>3^3 = 27</code>

<code>3^4 = 81</code>

resulting in a final sum of 

<code>117</code>

and a total time of ~.00035

With output similar to 

```
{
    "name": "DurableOrchestration",
    "instanceId": "95f2717703324304b461cc91c7d865cb",
    "runtimeStatus": "Completed",
    "input": "{\"base\": \"3\", \"exp\": \"4\"}",
    "customStatus": null,
    "output": "With the input values base: 3, exp: 4 we calculated a total result of 117 in 0.000354766845703125 seconds using FOFI.",
    "createdTime": "2020-07-07T21:02:03Z",
    "lastUpdatedTime": "2020-07-07T21:02:04Z"
}
```
