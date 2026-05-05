---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Jakub Scholz", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7oP/elastic-data-streaming-autoscaling-apache-kafka-jakub-scholz-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Elastic+Data+Streaming%3A+Autoscaling+Apache+Kafka+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Elastic Data Streaming: Autoscaling Apache Kafka - Jakub Scholz, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Jakub Scholz, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7oP/elastic-data-streaming-autoscaling-apache-kafka-jakub-scholz-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Elastic+Data+Streaming%3A+Autoscaling+Apache+Kafka+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Elastic Data Streaming: Autoscaling Apache Kafka.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oP/elastic-data-streaming-autoscaling-apache-kafka-jakub-scholz-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Elastic+Data+Streaming%3A+Autoscaling+Apache+Kafka+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pj6eLTC2tv8
- YouTube title: Elastic Data Streaming: Autoscaling Apache Kafka - Jakub Scholz, Red Hat
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/elastic-data-streaming-autoscaling-apache-kafka/pj6eLTC2tv8.txt
- Transcript chars: 27587
- Keywords: cluster, storage, scaling, brokers, actually, happens, basically, rebalance, around, broker, important, replicas, pretty, rebalancing, minutes, resource, horizontal, autoscaling

### Resumo baseado na transcript

okay so welcome to my talk about uh Autos scaling up atafa my name is yob Schultz I work as an engineer at redhead and I'm also a maintainer of the stry project and uh occasionally I'm also Apachi Kafka contributor if you don't know what strumsy then stry is a cncf incubating project which focus on running Apachi count kubernetes so we provide uh operators for running all the different server components of uh of apachi Kafka but we also have operators for managing things such as users topics

### Excerpt da transcript

okay so welcome to my talk about uh Autos scaling up atafa my name is yob Schultz I work as an engineer at redhead and I'm also a maintainer of the stry project and uh occasionally I'm also Apachi Kafka contributor if you don't know what strumsy then stry is a cncf incubating project which focus on running Apachi count kubernetes so we provide uh operators for running all the different server components of uh of apachi Kafka but we also have operators for managing things such as users topics connectors and we have some other smaller tools to make it easier to use uh Kafka on on Cube and uh yeah maybe on the beginning uh we can touch on why Autos scaling Apachi Kafka Brokers might be interesting why it might matter well gafka is quite often a pretty big workload which is taking quite a lot of resources so yeah if we manage to autoscale it in some effective and efficient way maybe we can save some costs maybe we can save some energy be a bit more green uh or something like that so so that's why we uh looked into it and uh maybe bit untraditionally let's start a talk with uh the first part of a of a demo so here in my kubernetes cluster I have already a Kafka cluster deployed so what we can see here is that uh right now I have here three Brokers 10 11 and 12 uh remember that uh for later uh I'm not using zookeeper anymore I'm using this craft thing which is new in Kafka so I have these three controllers uh as well to manage the quarum and so on and then I have these additional tools which streams the use cruise control is for cluster rebalancing it's a it's a tool from LinkedIn then uh this entity operator that's what I mentioned for managing users and uh and topics and this scafa exporter is just for some additional metrics and then uh yeah this is the main stream the operator which is actually running this uh this cluster and uh so what I'm going to do right now on the beginning is uh I'm going to deploy my load so just create some kubernetes jobs which will create bunch of pots and uh yeah they will start uh producing a load of messages and consuming the load of messages and uh yeah hopefully later when we get back to the demo we should see that some autoscaling happened and uh yeah if not then uh yeah something didn't work so in the meantime while it's hopefully AOS scaling we can get back to the to the slide uh and uh we can talk a bit more about the difference between scalability and elasticity because uh quite often when you mention Kafka then for a lo
