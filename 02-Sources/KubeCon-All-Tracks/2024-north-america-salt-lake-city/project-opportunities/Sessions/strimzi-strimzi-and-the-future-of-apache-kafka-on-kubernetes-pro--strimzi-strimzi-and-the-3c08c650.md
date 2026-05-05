---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Storage Data", "Kubernetes Core"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8P/strimzi-strimzi-and-the-future-of-apache-kafka-on-kubernetes-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Strimzi%3A+Strimzi+and+the+Future+of+Apache+Kafka+on+Kubernetes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Strimzi: Strimzi and the Future of Apache Kafka on Kubernetes | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8P/strimzi-strimzi-and-the-future-of-apache-kafka-on-kubernetes-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Strimzi%3A+Strimzi+and+the+Future+of+Apache+Kafka+on+Kubernetes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Strimzi: Strimzi and the Future of Apache Kafka on Kubernetes | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8P/strimzi-strimzi-and-the-future-of-apache-kafka-on-kubernetes-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Strimzi%3A+Strimzi+and+the+Future+of+Apache+Kafka+on+Kubernetes+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=v7lvSuF4bLo
- YouTube title: Strimzi: Strimzi and the Future of Apache Kafka on Kubernetes | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/strimzi-strimzi-and-the-future-of-apache-kafka-on-kubernetes-project-l/v7lvSuF4bLo.txt
- Transcript chars: 4570
- Keywords: zookeeper, support, features, release, apachi, operators, removal, finally, version, strimzi, lightning, everyone, running, operator, managing, handle, course, native

### Resumo baseado na transcript

okay great uh welcome to cubec con everyone uh and to the lightning talk about uh the strey project uh streams is a incubating project and it focus on running Apachi Kafka on uh on kubernetes we do that using the operator pattern so we have operators for running all the different Apachi Kafka server components but also some additional things such as operators for managing users for managing topics or Kafka connect connectors for example and uh we have some other tooling to make it as easy as possible

### Excerpt da transcript

okay great uh welcome to cubec con everyone uh and to the lightning talk about uh the strey project uh streams is a incubating project and it focus on running Apachi Kafka on uh on kubernetes we do that using the operator pattern so we have operators for running all the different Apachi Kafka server components but also some additional things such as operators for managing users for managing topics or Kafka connect connectors for example and uh we have some other tooling to make it as easy as possible to run Kafka on on kubernetes such as confli providers or an HTTP Bridge we try to cover the whole uh application life cycle so uh we handle the installation with all the different uh methods which are used such as uh Helm or operator Hub uh we also handle all the kind of day two day three and so on operations such as upgrades reconfigurations uh and stuff like that we of course Support also monitoring and uh we have support for security as well and in all these things we kind of try to integrate with other Cloud native projects so that you don't uh need to start using something new but that you can stick with the tools which you are hopefully even using in your own cloud native landscape what makes triy maybe a bit different from some of the other cncf projects is that we quite heavily depend on the Apachi KFA which is not part of strey and it has its own road map its own features which are being implemented and uh for the last years one of those really main features Kafka was working on Was the removal of the Zookeeper dependency which is replaced with something called craft which is kafka's own take on the raft uh algorithm and it kind of replaced the Zookeeper completely and it's been going really for several years and in strey we basically have to adopt things like this as well and adjust to them so really a lot of the work we have been doing in the last uh months and years was around this zookeeper removal and the good thing is uh or maybe bad we will see is that it's coming to an end and finally in early 2025 with the Kafka 4.0 release zookeeper will be completely gone and that means important milestone for strumsy as well so the next stry release z45 will be the last strey version with support for zookeeper so uh yeah that's where you can still use the Zookeeper based clusters but the Zookeeper based clusters won't be kind of left away to rot away but there is a migration process to the new craft mode and you have to do the migration latest with this t
