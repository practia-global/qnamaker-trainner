# Sobre el contenido

Esta carpeta contiene scripts provistos por Microsoft para acceder a QnA que no han sido implementados en el qna_module

## Knowledge Base content limits

Overall limits on the content in the knowledge base:

- Length of answer text: 25,000
- Length of question text: 1,000
- Length of metadata key/value text: 100
- Supported characters for metadata name: Alphabets, digits and _
- Supported characters for metadata value: All except : and |
- Length of file name: 200
- Supported file formats: ".tsv", ".pdf", ".txt", ".docx", ".xlsx".
- Maximum number of alternate questions: 100
- Maximum number of question-answer pairs: Depends on the Azure Search tier chosen. A question and answer pair maps to a document on Azure Search index.

## Create Knowledge base call limits:

These represent the limits for each create knowledge base action; that is, clicking Create KB or calling the CreateKnowledgeBase API.

- Maximum number of alternate questions per answer: 100
- Maximum number of URLs: 10
- Maximum number of files: 10

## Update Knowledge base call limits

These represent the limits for each update action; that is, clicking Save and train or calling the UpdateKnowledgeBase API.

- Length of each source name: 300
- Maximum number of alternate questions added or deleted: 100
- Maximum number of metadata fields added or deleted: 10
- Maximum number of URLs that can be refreshed: 5

Fuente: https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/limits