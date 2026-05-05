---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["Kubernetes Core"]
speakers: ["Adam Janikowski", "Jörg Schad", "ArangoDB"]
sched_url: https://kccnceu2022.sched.com/event/ytpo/transparent-live-migration-of-services-between-kubernetes-cluster-adam-janikowski-jorg-schad-arangodb
youtube_search_url: https://www.youtube.com/results?search_query=Transparent+Live+Migration+of+Services+Between+Kubernetes+Cluster+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Transparent Live Migration of Services Between Kubernetes Cluster - Adam Janikowski & Jörg Schad, ArangoDB

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Adam Janikowski, Jörg Schad, ArangoDB
- Schedule: https://kccnceu2022.sched.com/event/ytpo/transparent-live-migration-of-services-between-kubernetes-cluster-adam-janikowski-jorg-schad-arangodb
- Busca YouTube: https://www.youtube.com/results?search_query=Transparent+Live+Migration+of+Services+Between+Kubernetes+Cluster+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Transparent Live Migration of Services Between Kubernetes Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpo/transparent-live-migration-of-services-between-kubernetes-cluster-adam-janikowski-jorg-schad-arangodb
- YouTube search: https://www.youtube.com/results?search_query=Transparent+Live+Migration+of+Services+Between+Kubernetes+Cluster+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l-2yy-wtyBQ
- YouTube title: Transparent Live Migration of Services Between Kubernetes Cluster - Adam Janikowski & Jörg Schad
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/transparent-live-migration-of-services-between-kubernetes-cluster/l-2yy-wtyBQ.txt
- Transcript chars: 25182
- Keywords: cluster, database, second, clusters, actually, balancer, migration, customer, migrate, scenario, center, regions, operator, upgrade, providers, managed, provide, course

### Resumo baseado na transcript

welcome to kubecon again and uh also to everyone here and also people remote very excited to have in-person events anymore i really missed kubecon i must say over the last years uh welcome to our talk about transparent live migration of services between kubernetes cluster across multi-cloud as you can already figure out we tried to squeeze as many buzzwords in there as possible but what is it really about so it's about moving stateful services so in our case that's a distributed database between different kubernetes clusters between

### Excerpt da transcript

welcome to kubecon again and uh also to everyone here and also people remote very excited to have in-person events anymore i really missed kubecon i must say over the last years uh welcome to our talk about transparent live migration of services between kubernetes cluster across multi-cloud as you can already figure out we tried to squeeze as many buzzwords in there as possible but what is it really about so it's about moving stateful services so in our case that's a distributed database between different kubernetes clusters between different regions and even between different cloud providers this is a quite a challenge for us because it should be transparent for the user so when we do that we want our database users to actually not at least not lose the availability of the cluster they might have a small performance degradation but from an operational perspective this is super useful as you'll see for upgrading et cetera managing a general managed service for databases we are spoiled by choice we had a number of options we evaluated uh all of them they require cooperation of multiple tools from kubernetes over our kubernetes operator networking layer and also the database needs to be aware so we'll talk a little bit about that and also try to give like general advice for different setups and then uh we'll try the challenge for everything a live demo here on stage let's all hope this goes well we this is my colleague adam here hello my name is adam i joined the communities of my adventure with the kubernetes itself from the version 1.1 from this point on time i worked as the devops but i found that development is a little bit more interesting for me and from two and a half years i'm developing the operator which is used for the anglodb from this point of time we went to the a lot but i will pass it okay no i actually took the opposite choice so i'm a little further away from development right now which is very sad but uh cto currently at iran could be very happy to combine like my big two passions cloud nativeness so it was early on with this hype like back at mesosphere uh building up also like community so it's really great to see kubecon also growing that much and then yeah the other passion database systems uh also across different career stages and now yeah i all get that like within one role pretty cool why are we here as a database company talking about at a yeah kubecon here if we look at databases in 2022 we actually even if we look at the landsca
