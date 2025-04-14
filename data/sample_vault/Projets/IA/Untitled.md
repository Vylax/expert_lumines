```
email_data = {

        "sender": msg["From"],

        "to": msg.get("To", ""),

        "cc": msg.get("Cc", ""),

        "subject": msg.get("Subject", ""),

        "body": msg.get_body(preferencelist=("plain")).get_content() if msg.get_body() else "",

        "timestamp": msg["Date"],

        "attachments": [part.get_filename() for part in msg.iter_attachments()]

    }
```


company mails priority containing the following columns, "sender", "to", "cc", "subject", "body", "timestamp", "attachments"

company mails priority containing the following columns, "sender", "to", "cc", "subject", "body", "timestamp", "attachments", with 5 priority levels, where body is the length of a normal mail


https://huggingface.co/spaces/infinite-dataset-hub/infinite-dataset-hub?q=company+mails+priority+containing+columns,+"sender",+"to",+"cc",+"subject",+"body",+"timestamp",+"attachments",+where+body+is+the+length+of+a+normal+mail&dataset=InMailTrainingDB&tags=ML-model,+email,+performance+measurement

https://huggingface.co/spaces/infinite-dataset-hub/infinite-dataset-hub?q=company+mails+priority+containing+columns,+"sender",+"to",+"cc",+"subject",+"body",+"timestamp",+"attachments",+where+body+is+the+length+of+a+normal+mail&dataset=HighPriorityEmailDB&tags=high-value+mail,+data+science,+transactional+emails