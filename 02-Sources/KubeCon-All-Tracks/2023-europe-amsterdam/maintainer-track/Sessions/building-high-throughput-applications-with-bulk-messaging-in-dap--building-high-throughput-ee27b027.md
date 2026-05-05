---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Shubham Sharma", "Microsoft"]
sched_url: https://kccnceu2023.sched.com/event/1HySo/building-high-throughput-applications-with-bulk-messaging-in-dapr-shubham-sharma-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Building+High-Throughput+Applications+with+Bulk+Messaging+in+Dapr+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building High-Throughput Applications with Bulk Messaging in Dapr - Shubham Sharma, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Shubham Sharma, Microsoft
- Schedule: https://kccnceu2023.sched.com/event/1HySo/building-high-throughput-applications-with-bulk-messaging-in-dapr-shubham-sharma-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Building+High-Throughput+Applications+with+Bulk+Messaging+in+Dapr+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building High-Throughput Applications with Bulk Messaging in Dapr.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HySo/building-high-throughput-applications-with-bulk-messaging-in-dapr-shubham-sharma-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Building+High-Throughput+Applications+with+Bulk+Messaging+in+Dapr+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WMBAo-UNg6o
- YouTube title: Building High-Throughput Applications with Bulk Messaging in Dapr - Shubham Sharma, Microsoft
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-high-throughput-applications-with-bulk-messaging-in-dapr/WMBAo-UNg6o.txt
- Transcript chars: 22687
- Keywords: dapper, application, publish, events, subscribe, subscriber, running, messages, replicas, component, simple, published, message, already, multiple, publishing, applications, publisher

### Resumo baseado na transcript

good morning everyone let's get started uh thank you u89 for following me on Twitter already uh hi uh I'm shubham uh I work at Microsoft and I'm a maintainer of Dapper's JavaScript SDK so this morning we'll talk about how you can write High throughput applications using Dapper so we'll start with seeing how some asynchronous messaging patterns work in general and then how you could use Dapper with your Pub sub needs and then we'll look at the newest addition to Dapper's Pub sub block the bulk apis

### Excerpt da transcript

good morning everyone let's get started uh thank you u89 for following me on Twitter already uh hi uh I'm shubham uh I work at Microsoft and I'm a maintainer of Dapper's JavaScript SDK so this morning we'll talk about how you can write High throughput applications using Dapper so we'll start with seeing how some asynchronous messaging patterns work in general and then how you could use Dapper with your Pub sub needs and then we'll look at the newest addition to Dapper's Pub sub block the bulk apis so yeah let's get started okay so this is our normal asynchronous messaging application looks like you you have your publisher you have a few subscribers uh you have a Kafka Pub sub broker in this case so your card can your card can publish events onto Kafka and then um and then Kafka sends those events to the subscribers in this case it's shipping and notification and they can do something with that event process that and so and so uh you could also have an alternate model where you have multiple Publishers so you have multiple Publishers who generate events send it to Kafka and then you have a single subscriber listening for those and you could have MS2 and any combination basically of Publishers and subscribers you could also do something like this where you have the same replica we have multiple replicas of the same subscriber and then each replica kind of helps in load balancing your events so if you have imagine if you have a lot of events right and you want to process them so you could have multiple replicas doing that on your behalf so for for those of you who don't know about Dapper Dapper sits as a sidecar and let's see how you could do a simple operation like publish And subscribe using Dapper so each application has its own diverside car in the scenario and what the cart application needs to do is uh send this request to Dabber so Dapper is a sidecar on the port 3500 it's a well-defined port and all you need to do is do a publish slash Kafka slash order so publishes the operation Kafka is the name of your broker and order is the topic name and then you could send your data and Dapper will then send this data to the pub sub queue it will find where Kafka is it will send the data to that it will listen for data from the pub sub queue as well and then forward those data to the subscribed applications and in this case Dapper can use any components it supports so on the top on the bottom right you have a list of supported components and Dapper supports a l
