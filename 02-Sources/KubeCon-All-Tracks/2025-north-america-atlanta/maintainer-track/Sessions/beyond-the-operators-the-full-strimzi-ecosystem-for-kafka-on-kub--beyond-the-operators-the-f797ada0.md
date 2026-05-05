---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "Community Governance"]
speakers: ["Paolo Patierno", "IBM", "Michael Morris", "Ericsson Software Technology"]
sched_url: https://kccncna2025.sched.com/event/27NoO/beyond-the-operators-the-full-strimzi-ecosystem-for-kafka-on-kubernetes-paolo-patierno-ibm-michael-morris-ericsson-software-technology
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+the+Operators%3A+The+Full+Strimzi+Ecosystem+for+Kafka+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Beyond the Operators: The Full Strimzi Ecosystem for Kafka on Kubernetes - Paolo Patierno, IBM & Michael Morris, Ericsson Software Technology

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Paolo Patierno, IBM, Michael Morris, Ericsson Software Technology
- Schedule: https://kccncna2025.sched.com/event/27NoO/beyond-the-operators-the-full-strimzi-ecosystem-for-kafka-on-kubernetes-paolo-patierno-ibm-michael-morris-ericsson-software-technology
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+the+Operators%3A+The+Full+Strimzi+Ecosystem+for+Kafka+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Beyond the Operators: The Full Strimzi Ecosystem for Kafka on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NoO/beyond-the-operators-the-full-strimzi-ecosystem-for-kafka-on-kubernetes-paolo-patierno-ibm-michael-morris-ericsson-software-technology
- YouTube search: https://www.youtube.com/results?search_query=Beyond+the+Operators%3A+The+Full+Strimzi+Ecosystem+for+Kafka+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mYt9C0YQxDY
- YouTube title: Beyond the Operators: The Full Strimzi Ecosystem for Kafka on... Paolo Patierno & Michael Morris
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/beyond-the-operators-the-full-strimzi-ecosystem-for-kafka-on-kubernete/mYt9C0YQxDY.txt
- Transcript chars: 28911
- Keywords: cluster, stream, components, client, operator, provides, clients, quotas, streamy, access, bridge, broker, matrix, configuration, connect, server, config, running

### Resumo baseado na transcript

Thank you very much for being here and first before starting with this session uh let's do a little poll I would say so how many people knows about Kafka it seems all the people here and how many people know about stream okay less people about stream so for people who don't know about stream just a stream 101 stream is a CNCF incubating project about running apacha on kubernetes this. So mo mostly working on Kafka and Kubernetes and streamy of course I'm one of the core streams maintainers and I am also CNCF ambassador but yeah one of the most important thing for me is to be fan of formula 1 and moto GP so Ferrari and with me we have Michael. Let's see how we can uh uh complete the solution of our Aapachi Kafka cluster by putting all these components what kind of problems they are uh solving. So what problems you have and what kind of solution you have with these uh stream components. So you are able to deploy your Apache Kafka cluster on Kubernetes by using stream custom resources or your Kafka custom resource where you describe everything about your Kafka cluster.

### Excerpt da transcript

Thank you very much for being here and first before starting with this session uh let's do a little poll I would say so how many people knows about Kafka it seems all the people here and how many people know about stream okay less people about stream so for people who don't know about stream just a stream 101 stream is a CNCF incubating project about running apacha on kubernetes this. So you can use streamy and on so all the operators that stream easy provides for manage your Kafka cluster to deploy your Kafka cluster. So handling the day one operations and also day2 operations like setting up security or um changing configuration or upgrading your Kafka cluster and so on. Now for people who knows about streams already, this session is not going to cover streams itself. So the cluster operator, the topic operator, the user operator, the main core component within stream, but more the the the ecosystem that we have around stream. Streamy is not just these operators, but there are several components within the streamy organization and we will see how all these components can help you in order to kind of complete your solution.

So the solution that you have by running Apache Cafka on Kubernetes. Um okay so the components that sorry u first of all let me uh introduce myself uh I am Paulo I am an uh engineer working at IBM on the data and event streaming processing stuff. So mo mostly working on Kafka and Kubernetes and streamy of course I'm one of the core streams maintainers and I am also CNCF ambassador but yeah one of the most important thing for me is to be fan of formula 1 and moto GP so Ferrari and with me we have Michael. >> Hello. Yeah my name is Michael Morris. I work for Ericson software technology which is a part of Ericson that focuses on contributing to open source projects that are important to us. So as part of that work I contribute to a number of open source projects uh in CNCF and elsewhere and one of those projects is streamy. >> So as you already mentioned um Kafka is not just the operator you can see in this light Azure block the stream operator. So the core component that you have in stream Z but these are all the other components that we are going to show during this session.

Uh let me just thank first of all the contributors because uh a good part of these components are coming from contributors in the community uh even from mentorship for students and then these components grow up and became the the the components that are today. So
