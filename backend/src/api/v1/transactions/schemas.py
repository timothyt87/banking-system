from pydantic import BaseModel, Field, StrictInt, StrictFloat, validator, ValidationError


class TransferFund(BaseModel):
    sender_account_number: str = Field(default="1234567890",
                                       title="Sender Account Number",
                                       description="The Sender Account Number",
                                       min_length=10,
                                       max_length=10)
    recipient_account_number: str = Field(default="1234567890",
                                          title="Recipient Account Number",
                                          description="The Recipient Account Number",
                                          min_length=10,
                                          max_length=10
                                          )
    amount: float = Field(default=1.0,
                          title="Amount",
                          description="The Amount to transfer",
                          ge=1)
