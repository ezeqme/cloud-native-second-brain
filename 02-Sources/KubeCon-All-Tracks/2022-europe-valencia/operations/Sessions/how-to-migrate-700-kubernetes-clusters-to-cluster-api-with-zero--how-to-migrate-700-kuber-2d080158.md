---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Operations"
themes: ["Kubernetes Core"]
speakers: ["Tobias Giese", "Sean Schneeweiss", "Mercedes-Benz Tech Innovation"]
sched_url: https://kccnceu2022.sched.com/event/yttp/how-to-migrate-700-kubernetes-clusters-to-cluster-api-with-zero-downtime-tobias-giese-sean-schneeweiss-mercedes-benz-tech-innovation
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Migrate+700+Kubernetes+Clusters+to+Cluster+API+with+Zero+Downtime+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How to Migrate 700 Kubernetes Clusters to Cluster API with Zero Downtime - Tobias Giese & Sean Schneeweiss, Mercedes-Benz Tech Innovation

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Operations]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Tobias Giese, Sean Schneeweiss, Mercedes-Benz Tech Innovation
- Schedule: https://kccnceu2022.sched.com/event/yttp/how-to-migrate-700-kubernetes-clusters-to-cluster-api-with-zero-downtime-tobias-giese-sean-schneeweiss-mercedes-benz-tech-innovation
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Migrate+700+Kubernetes+Clusters+to+Cluster+API+with+Zero+Downtime+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How to Migrate 700 Kubernetes Clusters to Cluster API with Zero Downtime.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttp/how-to-migrate-700-kubernetes-clusters-to-cluster-api-with-zero-downtime-tobias-giese-sean-schneeweiss-mercedes-benz-tech-innovation
- YouTube search: https://www.youtube.com/results?search_query=How+to+Migrate+700+Kubernetes+Clusters+to+Cluster+API+with+Zero+Downtime+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KzYV-fJ_wH0
- YouTube title: How to Migrate 700 Kubernetes Clusters to Cluster API with Zero D... Tobias Giese & Sean Schneeweiss
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-to-migrate-700-kubernetes-clusters-to-cluster-api-with-zero-downti/KzYV-fJ_wH0.txt
- Transcript chars: 23983
- Keywords: cluster, machine, control, clusters, management, migration, machines, create, resources, workload, infrastructure, migrate, provider, legacy, deployment, worker, resource, thanks

### Resumo baseado na transcript

all right uh thanks for joining this session after runch and I'm really excited a lot of people in there this room I actually uh moderate a couple more session yesterday but some room is not quite po so I really excited about this topic and so uh my name is Daniel o I'm a CNF Ambassador I'm I'm so happy to be here as moderate this session today and thanks for joining once again so we're going to talk a little bit about our next topic is how to

### Excerpt da transcript

all right uh thanks for joining this session after runch and I'm really excited a lot of people in there this room I actually uh moderate a couple more session yesterday but some room is not quite po so I really excited about this topic and so uh my name is Daniel o I'm a CNF Ambassador I'm I'm so happy to be here as moderate this session today and thanks for joining once again so we're going to talk a little bit about our next topic is how to migrate seven 00 kubernetes cruster not 7 not 70 it's a 700 kubernetes cruster to cruster API with a zero downtime so I'm really happy for here and then please welcome our next great speaker Sean and Tobias from Merc B Tech Innovation please welcome the speakers okay nice so hello everyone and Welcome to our talk on how to migrate 700 kubernetes clusters to the cluster life cycle management software called cluster API so today we will present to you how we replaced our Legacy kubernetes Fleet Management with cluster API formerly it was based on terraform and the most important part was Zero downtime and no effort for the cluster users I'm Sean schne a software engineer from Mercedes-Benz Tech Innovation also I'm a maintainer of cluster API provider openstack this is my first Cube con and I'm so happy to meet all of you Hol hi my name is sias giz I am also a software engineer for Mercedes-Benz Tech Innovation I'm also maintainer for cluster API provider open stack and I'm working with kubernetes for 5 years now so this technical presentation targets software and operating engineers and all who is into cluster management it's maybe a bit um bit hard to learn in the beginning but it's definitely worth the effort so keep it on Mercedes-Benz Tech Innovation is a subsidiary of the German car manufacturer Mercedes-Benz it's the uh the headquarter is located in ol and at b c disp tech Innovation we don't build cars we build software and we are formerly known as damel TSS just in case you want to check the G commit history or you already known us as D TSS so yeah our platform team develops and operates a huge Fleet Management and we're operating 900 clusters all over the world in four data centers in uh Atlanta Beijing Frankfurt and stutgart and just a note during the time we have submitted this talk we only had 700 clusters so 200 classes more in half a year that's not too bad I think so the agenda uh we first step in and set the stage just that everybody knows what we are talking about then we will uh talk about the Legacy
