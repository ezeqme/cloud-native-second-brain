---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Jakub Scholz", "Red Hat", "Yaodong Yang", "Strimzi Kafka Contributor"]
sched_url: https://kccncna2024.sched.com/event/1hoxd/strimzi-data-streaming-on-kubernetes-with-apache-kafka-jakub-scholz-red-hat-yaodong-yang-strimzi-kafka-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Strimzi%3A+Data+Streaming+on+Kubernetes+with+Apache+Kafka+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Strimzi: Data Streaming on Kubernetes with Apache Kafka - Jakub Scholz, Red Hat & Yaodong Yang, Strimzi Kafka Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Jakub Scholz, Red Hat, Yaodong Yang, Strimzi Kafka Contributor
- Schedule: https://kccncna2024.sched.com/event/1hoxd/strimzi-data-streaming-on-kubernetes-with-apache-kafka-jakub-scholz-red-hat-yaodong-yang-strimzi-kafka-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Strimzi%3A+Data+Streaming+on+Kubernetes+with+Apache+Kafka+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Strimzi: Data Streaming on Kubernetes with Apache Kafka.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoxd/strimzi-data-streaming-on-kubernetes-with-apache-kafka-jakub-scholz-red-hat-yaodong-yang-strimzi-kafka-contributor
- YouTube search: https://www.youtube.com/results?search_query=Strimzi%3A+Data+Streaming+on+Kubernetes+with+Apache+Kafka+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=q6WYs8AEEDk
- YouTube title: Strimzi: Data Streaming on Kubernetes with Apache Kafka - Jakub Scholz & Yaodong Yang
- Match score: 0.886
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/strimzi-data-streaming-on-kubernetes-with-apache-kafka/q6WYs8AEEDk.txt
- Transcript chars: 30293
- Keywords: cluster, zookeeper, storage, stream, basically, clusters, feature, operator, already, support, version, resources, brokers, create, around, migration, provide, release

### Resumo baseado na transcript

welcome everyone to our talk about uh strey uh my name is jaob Schultz I'm one of the maintainers of the streamy project and hi I'm yo I'm a software engineer in Apple so mainly we we use streamy and we contribut to stream Z so we are basically contribut stream and use of stream Z and yeah today we will start by quickly explaining what is streamy uh and how it works and then we will look a bit more closely on uh some of the features which we have some demos of how to configure it and how to do the migration and so on so you can use this as a as a source and the next feature to talk about is steered storage and for that I will hand over okay so t storage so as you know that in the past several years the Kafka Community have been working very hard to design and implement this feature in AP Kafka and finally it was released in the kka 3.6 today many of the people are

### Excerpt da transcript

welcome everyone to our talk about uh strey uh my name is jaob Schultz I'm one of the maintainers of the streamy project and hi I'm yo I'm a software engineer in Apple so mainly we we use streamy and we contribut to stream Z so we are basically contribut stream and use of stream Z and yeah today we will start by quickly explaining what is streamy uh and how it works and then we will look a bit more closely on uh some of the features which we have been working on on some of the latest changes and updates and then uh give you a bit uh view into the future what we might be working on next and uh yeah we definitely appreciate that so many of you are here because uh uh we know that Friday afternoon it's not the best time and everyone is already maybe a bit tired but thanks for being here so if you don't know what streams is then streams is incubating cncf project which focus on running Apachi kfka on kubernetes uh to do that we use the operator pattern so we provide different operators for running all the Apachi kfka server components but uh also to manage things such as users topics or Kafka connect connectors and then we have some other let's say smaller components which should help you run Kon berties we have an HTTP Bridge use the HTTP protocol to talk with uh with uh Kafka we have for example some config providers which uh make it easier to for example load data from Secrets or config Maps when configuring your Kafka applications and uh and tools like that to kind of make your life as easy as possible when running Kafka on on Cube uh I hope all of you know at least a little bit about Kafka so it's the uh leading Distributing message log and data streaming platform it's something you can use as a as a basis to kind of build all various things from Integrations of microservices to even driven architectures uh event sourcing uh but you can also use it for these kind of more uh simple tasks such as uh shifting for example metrics or logs between different systems and locations and and stuff like that so that's all what Kafka can do uh it has also great ecosystem of different connectors clients and so on and uh uh Kafka itself is not really part of strey it's a separate project uh which was originally founded by LinkedIn uh and it's part of aachi software foundation and strey basically provides the orchestration on top of uh kubernetes uh what we try to do in strs is this kind of kubernetes native Kafka experience where the operator pattern basically provides y
