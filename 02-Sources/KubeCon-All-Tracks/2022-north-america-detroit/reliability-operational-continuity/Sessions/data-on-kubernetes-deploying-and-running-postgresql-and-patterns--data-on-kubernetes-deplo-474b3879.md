---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Chris Milsted", "Ondat", "Gabriele Bartolini", "EDB"]
sched_url: https://kccncna2022.sched.com/event/182GB/data-on-kubernetes-deploying-and-running-postgresql-and-patterns-for-databases-in-a-kubernetes-cluster-chris-milsted-ondat-gabriele-bartolini-edb
youtube_search_url: https://www.youtube.com/results?search_query=Data+On+Kubernetes%2C+Deploying+And+Running+PostgreSQL+And+Patterns+For+Databases+In+a+Kubernetes+Cluster.+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Data On Kubernetes, Deploying And Running PostgreSQL And Patterns For Databases In a Kubernetes Cluster. - Chris Milsted, Ondat & Gabriele Bartolini, EDB

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Chris Milsted, Ondat, Gabriele Bartolini, EDB
- Schedule: https://kccncna2022.sched.com/event/182GB/data-on-kubernetes-deploying-and-running-postgresql-and-patterns-for-databases-in-a-kubernetes-cluster-chris-milsted-ondat-gabriele-bartolini-edb
- Busca YouTube: https://www.youtube.com/results?search_query=Data+On+Kubernetes%2C+Deploying+And+Running+PostgreSQL+And+Patterns+For+Databases+In+a+Kubernetes+Cluster.+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Data On Kubernetes, Deploying And Running PostgreSQL And Patterns For Databases In a Kubernetes Cluster..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182GB/data-on-kubernetes-deploying-and-running-postgresql-and-patterns-for-databases-in-a-kubernetes-cluster-chris-milsted-ondat-gabriele-bartolini-edb
- YouTube search: https://www.youtube.com/results?search_query=Data+On+Kubernetes%2C+Deploying+And+Running+PostgreSQL+And+Patterns+For+Databases+In+a+Kubernetes+Cluster.+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=99uSJXkKpeI
- YouTube title: Data On Kubernetes, Deploying And Running PostgreSQL And... - Chris Milsted & Gabriele Bartolini
- Match score: 0.764
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/data-on-kubernetes-deploying-and-running-postgresql-and-patterns-for-d/99uSJXkKpeI.txt
- Transcript chars: 34467
- Keywords: storage, database, native, postgres, running, cluster, primary, replication, recovery, standalone, application, important, instance, actually, backup, everything, databases, source

### Resumo baseado na transcript

welcome everyone my name is Chris Milstead I work for a company who ownedat which is a container storage solution that runs inside kubernetes so turn your kubernetes cluster into kind of a storage array and I'm here presenting with Rover one two three okay good hi I'm Gabriel bartolini as you have my guest I'm From Italy I work for EDB which is one of the major contributors to the pause gear SQL open source project I'm vice president and CTO of cloud native and my primary goal in

### Excerpt da transcript

welcome everyone my name is Chris Milstead I work for a company who ownedat which is a container storage solution that runs inside kubernetes so turn your kubernetes cluster into kind of a storage array and I'm here presenting with Rover one two three okay good hi I'm Gabriel bartolini as you have my guest I'm From Italy I work for EDB which is one of the major contributors to the pause gear SQL open source project I'm vice president and CTO of cloud native and my primary goal in the organization is to enhance the podcast experience in the kubernetes space I I'm an active member of the postgres community and I've been working for PO with possess for over two days two decades I I'm an early adopter of the devops culture and here today I will briefly cover the cloud native PG open source operator while Chris will primarily talk about the storage part between us hopefully you find it interesting so we're going to try and do a bit about kind of the intro set the scene then we're going to do a lot about the postgres patterns and then we're going to try and do a little demo at the end which uh I have recorded it because anyone in Valencia know what the Wi-Fi was like trying to do a live demo was absolutely impossible so we've gone for the backup safe video but it is running on my laptop so if anyone does want to come and see it in real life come and find me either here afterwards or at the booth and we'll go in through it and do it again and as you can see by the picture EDB had a party last night and there might have been some alcohol served and uh yeah we we don't look like that normally in real life so the first part is um The Click is not clicking there we go we're on there so um the first part is um there was a talk previously to this one which was you know data on kubernetes um bring it on so we're not going to try and convince you to put data in kubernetes we're going to assume that you're all given in this room that this is the case but if you are interested and want to know more both of our companies are very active members and proud supporters of the data and kubernetes and they've got these great reports so if you or your boss or your teams or anyone is interested in convincing people to run data in kubernetes please go and download this report there's a QR code in the bottom right hand side and the slides which you can click on that and you'll get access to the report anything else you want to say about that one's gabrielli that's fine no I know that
