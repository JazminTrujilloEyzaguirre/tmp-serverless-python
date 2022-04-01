module.exports = () => ({
    "Type": "AWS::DynamoDB::Table",
    "DeletionPolicy":"Retain",
    "Properties": {
        "TableName": "${file(${self:provider.stage}.yml):TABLA_LEADS}",
        "AttributeDefinitions": [
            {
                "AttributeName": "idlead",
                "AttributeType": "S"
            }
        ],
        "KeySchema": [
            {
                "AttributeName": "idlead",
                "KeyType": "HASH"
            }
        ],
        "ProvisionedThroughput": {
            "ReadCapacityUnits": 2,
            "WriteCapacityUnits": 2
        }
    }
});
