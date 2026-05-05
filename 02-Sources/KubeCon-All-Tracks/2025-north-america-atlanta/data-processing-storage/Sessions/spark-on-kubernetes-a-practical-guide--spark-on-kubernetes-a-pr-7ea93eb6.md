---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Damon Cortesi", "Airbnb"]
sched_url: https://kccncna2025.sched.com/event/27Fd6/spark-on-kubernetes-a-practical-guide-damon-cortesi-airbnb
youtube_search_url: https://www.youtube.com/results?search_query=Spark+on+Kubernetes%2C+a+Practical+Guide+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Spark on Kubernetes, a Practical Guide - Damon Cortesi, Airbnb

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Damon Cortesi, Airbnb
- Schedule: https://kccncna2025.sched.com/event/27Fd6/spark-on-kubernetes-a-practical-guide-damon-cortesi-airbnb
- Busca YouTube: https://www.youtube.com/results?search_query=Spark+on+Kubernetes%2C+a+Practical+Guide+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Spark on Kubernetes, a Practical Guide.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fd6/spark-on-kubernetes-a-practical-guide-damon-cortesi-airbnb
- YouTube search: https://www.youtube.com/results?search_query=Spark+on+Kubernetes%2C+a+Practical+Guide+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ejJ6A0sIdbw
- YouTube title: Spark on Kubernetes, a Practical Guide - Damon Cortesi, Airbnb
- Match score: 0.859
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/spark-on-kubernetes-a-practical-guide/ejJ6A0sIdbw.txt
- Transcript chars: 32912
- Keywords: cluster, logs, running, driver, pretty, little, server, shuffle, actually, apache, operator, hadoop, history, support, options, submit, submission, kelliborn

### Resumo baseado na transcript

I'm going to be talking today about uh Airbnb's Spark on Kubernetes journey. I've been a stats nerd since 1996 when I was doing automated data entry into Excel. We have to do a lot of picking and choosing and kind of figuring out what the right instance type is for our workloads and there are options like Carpenter and Kubernetes that are a lot better for that. So, we use internally Carpenter as our autoscaler and that's responded really well in early testing. In theory, if we have shared workloads on the Kubernetes cluster with Spark workloads though, they can be pretty bursty. We use open telemetry internally for our metrics collection and we have a lot of paved pathways internally where uh some of the observability things are more baked in on Kubernetes than our existing solution.

### Excerpt da transcript

Uh my name is Damon Cortezy. I'm going to be talking today about uh Airbnb's Spark on Kubernetes journey. So uh quick bit about me. I'm a staff software at Airbnb. I've been working on data platforms since about 2010. I had a startup back then. We were doing MongoDB. Uh migrated to HBAS. So lots of good fun back then. I've been a stats nerd since 1996 when I was doing automated data entry into Excel. So clearly I choose all the right uh technologies. Uh I'm also an open source contributor. Uh I'm an Apache Libby committer. Uh I opened my first PR on the open telemetry project this year and if you go to my GitHub I got a bunch of fun tools there too like a rustbased S3 greer that does it all in parallel. Uh because turns out I look through a lot of logs on S3. So uh let's get started. So why Spark on Kubernetes, right? Like like let's dig into this a little bit. Um we've had Hadoop for nearly two decades now. It's still being actively developed, right? But things like Java support for example are a little bit lagging.

I think Java 11 runtime support was just introduced in 2022. So why Kubernetes might be obvious to everybody here, but a few specific reasons. One is flexibility. So Spark versions, right? For us to be able to upgrade a Spark version in our existing cluster, uh it's kind of kind of uh challenging, right? Um Hadoop 3 does support running both Docker and run C containers, but Kubernetes is a much more uh mature solution for that. The second one is compute optimization. This kind of goes along with flexibility. So, we've done a lot of work existing or optimizing our existing clusters. Um, but it's not as automated as we'd like from an instance type perspective, right? We have to do a lot of picking and choosing and kind of figuring out what the right instance type is for our workloads and there are options like Carpenter and Kubernetes that are a lot better for that. So, we use internally Carpenter as our autoscaler and that's responded really well in early testing. Finally, we should be able to have more efficient resource utilization.

In theory, if we have shared workloads on the Kubernetes cluster with Spark workloads though, they can be pretty bursty. It's not unusual for us to spike up to, you know, from, you know, five or 10,000 uh running and pending pods up to 30 or 40,000 p running and pending pods. So, uh we'll see if this one actually holds true. Next up is modernization. So like I mentioned Hadoop uh Java runtime support still a lit
