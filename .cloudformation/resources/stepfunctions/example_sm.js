module.exports = () => (
    {
        "CatchAllFallback": {
            "Type": "Task",
            "Resource": "${self:custom.ARN_PREFIX}-catchFallback",
            "End": true
        },
        "Payload": {
            "Type": "Task",
            "Resource": "${self:custom.ARN_PREFIX}-payload",
            "Next": "Exceptions",
            "Catch": [{
                "ErrorEquals": ["States.ALL"],
                "Next": "CatchAllFallback"
            }]
        },
        "Exceptions": {
            "Type": "Task",
            "Resource": "${self:custom.ARN_PREFIX}-exceptions",
            "Retry": [{
                "ErrorEquals": ["States.ALL"],
                "IntervalSeconds": 1,
                "MaxAttempts": 2,
            }],
            "Catch": [
                {
                    "ErrorEquals": ["States.ALL"],
                    "Next": "CatchAllFallback"
                }
            ],
            "End": true
        }
    }
)
