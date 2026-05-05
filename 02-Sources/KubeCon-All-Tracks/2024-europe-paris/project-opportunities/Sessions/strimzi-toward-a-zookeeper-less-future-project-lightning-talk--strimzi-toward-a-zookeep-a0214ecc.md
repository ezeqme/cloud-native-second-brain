---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aNIp/strimzi-toward-a-zookeeper-less-future-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Strimzi%3A+Toward+a+ZooKeeper-less+Future+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Strimzi: Toward a ZooKeeper-less Future | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aNIp/strimzi-toward-a-zookeeper-less-future-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Strimzi%3A+Toward+a+ZooKeeper-less+Future+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Strimzi: Toward a ZooKeeper-less Future | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aNIp/strimzi-toward-a-zookeeper-less-future-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Strimzi%3A+Toward+a+ZooKeeper-less+Future+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_zpjMh8p02Y
- YouTube title: Strimzi: Toward a ZooKeeper-less Future | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/strimzi-toward-a-zookeeper-less-future-project-lightning-talk/_zpjMh8p02Y.txt
- Transcript chars: 6035
- Keywords: zookeeper, apachi, clusters, production, support, limitations, managing, source, projects, changes, controller, basically, streamy, whether, lightning, everyone, called, working

### Resumo baseado na transcript

hello everyone welcome to cucon uh my name is yob Schultz and I'm one of the maintainers of the project called strey and uh in this lightning talk I will talk about what is stmy and about the thing we are working on most uh these days months and that's zookeeper removal from Apachi Kafka uh if you don't know stmy we are a cncf incubating project we actually moved to incubation from sandbox quite recently so so hooray that's a big achievement for us and we are of course

### Excerpt da transcript

hello everyone welcome to cucon uh my name is yob Schultz and I'm one of the maintainers of the project called strey and uh in this lightning talk I will talk about what is stmy and about the thing we are working on most uh these days months and that's zookeeper removal from Apachi Kafka uh if you don't know stmy we are a cncf incubating project we actually moved to incubation from sandbox quite recently so so hooray that's a big achievement for us and we are of course open source project open source Community under Apache License 2.0 and uh we focus on running Apachi kfka on kubernetes in a most easy and kubernetes Native way as possible and for that we provide bunch of operators we have one operator which kind of runs all the different Kafka server components such as the Brokers mirror maker connect but we have also some other operators for managing uh users or topics and we have also some smaller tools and utilities for uh uh for making your life easier when you run kfon kubernetes uh we try to cover all the different things there are to the Kafka application life cycle from the initial deployment and installation operations uh monitoring uh and uh and the things such as security and we of course try to also uh play nicely with all the other Cloud native projects and all the other open source projects and try to integrate them as much as possible instead of Reinventing the wheel and uh the thing we are working on most lately and which I will really focus most right now on is uh in the top left corner where you see the Zookeeper and the CFA par that's where there are some major changes happening and that's where a lot of the work is so if you run CFA before you probably know that for a long time it has been always dependent on zookeeper for managing metadata bootstrapping the Clusters electing the controller node and so on but it's changing and zookeeper is being replaced by something what's called craft which stands for Kafka raft and it's kind of kafka's own take on the raft protocol or algorithm for keeping the quum and this is something that's work in progress since 2019 and it's still going on and that's not because people are lazy or slow but it's because it's really huge effort with a lot of changes both in the Apachi kfka project itself but also a lot of changes for us in in strey which we have to adjust to the motivation for that is uh a to get rid of Zookeeper uh zookeeper does some things really great but it has also some issues uh so uh yeah
