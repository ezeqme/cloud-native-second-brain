---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["Application Development"]
speakers: ["Aman Singh", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27FcB/drasi-a-new-take-on-change-driven-architectures-aman-singh-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Drasi%3A+A+New+Take+on+Change-driven+Architectures+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Drasi: A New Take on Change-driven Architectures - Aman Singh, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United States / Atlanta
- Speakers: Aman Singh, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27FcB/drasi-a-new-take-on-change-driven-architectures-aman-singh-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Drasi%3A+A+New+Take+on+Change-driven+Architectures+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Drasi: A New Take on Change-driven Architectures.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FcB/drasi-a-new-take-on-change-driven-architectures-aman-singh-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Drasi%3A+A+New+Take+on+Change-driven+Architectures+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nbLJ_ICpZhc
- YouTube title: Drasi: A New Take on Change-driven Architectures - Aman Singh, Microsoft
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/drasi-a-new-take-on-change-driven-architectures/nbLJ_ICpZhc.txt
- Transcript chars: 31935
- Keywords: sources, database, vector, postgress, changes, cluster, reviews, simple, result, question, another, write, queries, databases, reaction, application, product, embedding

### Resumo baseado na transcript

My name is Aman Singh and I'm a maintainer of a new and upcoming CNCF project called DRSI. So today we will look at two demos of changed-driven scenarios and we will see how Drai can simplify the architecture for us. Now when the user asks the question, the app would first query the vector store to find the most relevant documents which are then sent along with the user's question to the model and that is what allows the model to give an accurate datadriven answer containing information from both the microservices. Well, the real-time experts in the room might just tell us to use event streaming where we subscribe to the databases change logs using tools like Debzium, publish those changes to a message broker like Kafka and then we can write a stateful stream processing Now once connected, DRSI allows us to query data coming from all these various multiple disparate sources as though it was all part of a single virtual graph. Now notice that the query here does not care about streams, windows, joins, watermarks, none of that.

### Excerpt da transcript

My name is Aman Singh and I'm a maintainer of a new and upcoming CNCF project called DRSI. So today we will look at two demos of changed-driven scenarios and we will see how Drai can simplify the architecture for us. Now with everyone excited about AI, I want to open today's discussion with chat applications. So how do we build a chat application today? Well, we simply wrap the LLM model in our application code and that allows us to ask it questions like what is the largest country and since the model has been trained on large amount of internet data, it is able to give us a factual answer. But what happens when we want to ask it questions about our own data? Say we wanted to build a chat application for an online electronics store where the product spiker was maintaining its information in a Postgress database and the review service uh writes to a separate MySQL database. So how would the model respond to a question about the laptops in the store? Now the base LLM here has a problem. It has no idea about the products in our store since this private data was not part of its training.

So out of the box, the best it can do is give us a generic unhelpful response like this, admitting that it cannot access our internal databases. So how do we bridge this gap? A common pattern in use today is retrieval augmented generation or rag where we first join the data from our sources and generate text documents from that and then feed those documents into an embedding generator which uses another AI model to convert the text's meaning into numerical vectors and finally those vectors are loaded into a vector database like quadrant and that serves as a knowledge base for the chat application. Now when the user asks the question, the app would first query the vector store to find the most relevant documents which are then sent along with the user's question to the model and that is what allows the model to give an accurate datadriven answer containing information from both the microservices. But this brings us to the real challenge. What happens the moment the product price or description gets updated in our Postgress database?

Suddenly the answer from the chat application is wrong. And it's the same story when new reviews get added to the MySQL database. Now, our smart assistant is confidently giving customers bad information, which is arguably worse than giving no information at all. What we need here is a real-time rag system, one that automatically updates the vector
