module.exports = () => ({
    "Type": "AWS::DynamoDB::Table",
    "DeletionPolicy":"Retain",
    "Properties": {
        "TableName": "${file(${self:provider.stage}.yml):TABLA_REGIONES}",
        "AttributeDefinitions": [
            {
                "AttributeName": "codigo_region",
                "AttributeType": "N"
            },
            {
                "AttributeName": "nombre_region_labs",
                "AttributeType": "S"
            }
        ],
        "KeySchema": [
            {
                "AttributeName" : "codigo_region",
                "KeyType" : "HASH"
            }
            
        ],
        "BillingMode": "PAY_PER_REQUEST",
        "GlobalSecondaryIndexes": [
            {
                "IndexName": "nombreLabsIndex",
                "KeySchema": [
                    {
                        "AttributeName" : "nombre_region_labs",
                        "KeyType" : "HASH"
                    }
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                }
            }
        ]
    }
});
