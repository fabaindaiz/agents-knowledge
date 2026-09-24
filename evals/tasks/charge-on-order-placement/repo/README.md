# billing

Orders and payments. Every outbound call to the payment provider goes through
`billing.transport.RetryingTransport`, which retries a call up to three times when it times out.
