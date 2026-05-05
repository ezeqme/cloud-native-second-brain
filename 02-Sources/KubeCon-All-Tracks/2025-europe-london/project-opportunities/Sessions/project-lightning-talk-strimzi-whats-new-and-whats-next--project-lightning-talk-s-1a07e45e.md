---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["Community Governance"]
speakers: ["Gantigmaa Selenge", "Contributor"]
sched_url: https://kccnceu2025.sched.com/event/1tcwg/project-lightning-talk-strimzi-whats-new-and-whats-next-gantigmaa-selenge-contributor
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Strimzi+%E2%80%93+What%27s+New+and+What%27s+Next+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Strimzi – What's New and What's Next - Gantigmaa Selenge, Contributor

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Gantigmaa Selenge, Contributor
- Schedule: https://kccnceu2025.sched.com/event/1tcwg/project-lightning-talk-strimzi-whats-new-and-whats-next-gantigmaa-selenge-contributor
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Strimzi+%E2%80%93+What%27s+New+and+What%27s+Next+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Strimzi – What's New and What's Next.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwg/project-lightning-talk-strimzi-whats-new-and-whats-next-gantigmaa-selenge-contributor
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Strimzi+%E2%80%93+What%27s+New+and+What%27s+Next+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1jPvEAhkklg
- YouTube title: Project Lightning Talk: Strimzi – What's New and What's Next - Gantigmaa Selenge, Contributor
- Match score: 0.866
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-strimzi-whats-new-and-whats-next/1jPvEAhkklg.txt
- Transcript chars: 3631
- Keywords: clusters, cluster, version, streamzy, stream, zookeeper, release, please, apache, running, various, components, operations, streams, support, provide, source, operator

### Resumo baseado na transcript

It's a CNCF incubating project uh open source under Apache license uh 20. Um it's based built based on Kubernetes operator pattern and provides various operators to run um manage Kafka components also has additional tools to make running CFKA as easy as possible. uh motivation for this to get rid of that uh additional system to maintain and manage and that simplifies the deployment and operations and also improves the scalability and performance. There are other couple of interesting um work uh being cons considered uh which is uh stretching Kafka clusters across multiple Kubernetes clusters and also to provide built-in gateway to uh exposed cast uh Kafka clusters. Um so if you would like to learn more about streamy and hear about interesting use cases and integrations, please join us. So if you're interested to learn more, please come and join our session.

### Excerpt da transcript

Hi everyone. Um, my name is Kantima Silen, but I usually go by Tina. I'm a software engineer at Red Hat and also contributor of StreamZy. So, I'm very excited to be here to talk about StreamZy. So, what is StreamZy? It's a CNCF incubating project uh open source under Apache license uh 20. It's an operator for running Apache Cafka on Kubernetes. Um it's based built based on Kubernetes operator pattern and provides various operators to run um manage Kafka components also has additional tools to make running CFKA as easy as possible. So, StreamZ um um automates the installation of Kafka itself as well as um other components like Kafka connect, mirror maker and HTTP bridge which is provided by StreamZy uh for connecting to your cluster over HTTP and StreamZ handles not just day one operations but also day two operations like upgrades, certificate management, um scaling of clusters and configuration of clusters. also uses another open source project called uh cruise control for balancing data in your cluster and with stream you can also easily monitor your cluster integrates with uh various monitoring tools and also for security it provides various different authentication mechanisms.

Okay. So one of the biggest uh and recent change that was introduced to streams is um removal of zookeeper. So zookeeper was used to store metadata of clusters um but it was removed from in apache cafka 40 release. So it's been replaced by cafka's own implementation based on um raph protocol. So the metadata is stored within cafka itself. uh motivation for this to get rid of that uh additional system to maintain and manage and that simplifies the deployment and operations and also improves the scalability and performance. So stream 045 is the current release and this is the last version to support zookeeper based clusters and this is also the last version which you can um migrate your existing zookeeper based cluster to craft and we plan to provide extended support for this version and the next release will be 046 and with this you can only run a craft cluster so you need to migrate your existing clusters before you can upgrade this upgrade to this version. We're also removing um some deprecated components like uh mirror maker one.

So future plans for streams uh we currently working on improving certificate management um to uh provide better support for tools like search manager and also um trying to integrate self-healing uh future of uh cruise control and we also plan to um re
