---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Prabhakar Palanivel", "Oracle Corporation"]
sched_url: https://kccncna2023.sched.com/event/1R2tG/insights-and-gotchas-from-the-zero-downtime-migration-of-10000+-cloud-hosted-etcd-key-value-stores-prabhakar-palanivel-oracle-corporation
youtube_search_url: https://www.youtube.com/results?search_query=Insights+and+Gotchas+from+the+Zero-Downtime+Migration+of+10000%2B+Cloud+Hosted+Etcd+Key-Value+Stores+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Insights and Gotchas from the Zero-Downtime Migration of 10000+ Cloud Hosted Etcd Key-Value Stores - Prabhakar Palanivel, Oracle Corporation

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Prabhakar Palanivel, Oracle Corporation
- Schedule: https://kccncna2023.sched.com/event/1R2tG/insights-and-gotchas-from-the-zero-downtime-migration-of-10000+-cloud-hosted-etcd-key-value-stores-prabhakar-palanivel-oracle-corporation
- Busca YouTube: https://www.youtube.com/results?search_query=Insights+and+Gotchas+from+the+Zero-Downtime+Migration+of+10000%2B+Cloud+Hosted+Etcd+Key-Value+Stores+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Insights and Gotchas from the Zero-Downtime Migration of 10000+ Cloud Hosted Etcd Key-Value Stores.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tG/insights-and-gotchas-from-the-zero-downtime-migration-of-10000+-cloud-hosted-etcd-key-value-stores-prabhakar-palanivel-oracle-corporation
- YouTube search: https://www.youtube.com/results?search_query=Insights+and+Gotchas+from+the+Zero-Downtime+Migration+of+10000%2B+Cloud+Hosted+Etcd+Key-Value+Stores+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cvfX-ORpKPQ
- YouTube title: Insights and Gotchas from the Zero-Downtime Migration of 10000+ Cloud Hosted... Prabhakar Palanivel
- Match score: 0.913
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/insights-and-gotchas-from-the-zero-downtime-migration-of-10000-cloud-h/cvfX-ORpKPQ.txt
- Transcript chars: 32290
- Keywords: member, migration, cluster, members, legacy, environment, architecture, control, leader, volumes, basically, gateway, resolution, instance, clusters, corresponding, search, update

### Resumo baseado na transcript

hello everyone thanks for joining um I am prabakar paril I'm a Consulting engineer uh in arle uh Cloud infrastructure so uh what is in it for you right like uh why you have to spend next 30 minutes here so um I would touch upon few internal aspects of it City and um we would share some of the learnings we had over the last 78 years operating uh tens of thousands of it CD clusters and and um as we evolved we re architectured our um HD architecture it communicates so there is no code DNS involved there our bcn DNS gets the query and then it translates it and it communicates locally but what happened in our case was uh when a let's say I'm adding a new member and I am

### Excerpt da transcript

hello everyone thanks for joining um I am prabakar paril I'm a Consulting engineer uh in arle uh Cloud infrastructure so uh what is in it for you right like uh why you have to spend next 30 minutes here so um I would touch upon few internal aspects of it City and um we would share some of the learnings we had over the last 78 years operating uh tens of thousands of it CD clusters and and um as we evolved we re architectured our um HD architecture so we will talk about how we went about re architecting and also migrating the it City deployment from the Legacy architecture to the new architecture and also we'll talk about some of the learnings when we did this uh migration from the Legacy to new architecture just a very brief uh uh introduction so uh like I said I work with OC I and oi has a global infrastructure across uh the globe with multiple regions and in each of these regions uh ok which is our managed kubernetes offering is a day one service and there are um multiple uh internal as well as external applications are onboarded to OK and in fact many of the OCA Services run on top of ok itself so uh with the growth in the adaption we were looking at oper efficiencies and one uh thing we identified was to improve the way the H CD was deployed and operated like you know each OK cluster has a backend it City and hence we need to find a way to operate it better to operate kubernetes better so we went through this journey of re architecting uh and uh at this moment we completed the migration to the new architecture with um zero customer uh reported issues I think um having a um great and uh engineering team really helped but the Equal Credit goes to the it City Sig because of the high bar they maintain with respect to the patch releases and major releases they make because we had uh it City clusters running all the way from it 3.3 to now 3.5x but we could do all those migration with zero customer escalation so I just want to thank the uh it for their focus on the high bar they maintain so start to start with some brief int uh HD internals as you all know uh distribut H CD is a distributed key valy store uh I do hear that some folks run single member it City in production I don't know I don't believe that but I do hear it from some of my friends but it doesn't make sense running a single uh member it CD uh in production yeah it has to be a distributed key value pair and um it uses grpc for both its client as as well as uh peer to-peer communication um and you
