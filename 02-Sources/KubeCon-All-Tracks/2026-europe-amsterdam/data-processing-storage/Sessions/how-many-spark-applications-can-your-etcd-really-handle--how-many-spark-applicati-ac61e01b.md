---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["AI ML", "Storage Data"]
speakers: ["João Soares", "João Azevedo", "Feedzai"]
sched_url: https://kccnceu2026.sched.com/event/2CW7u/how-many-spark-applications-can-your-etcd-really-handle-joao-soares-joao-azevedo-feedzai
youtube_search_url: https://www.youtube.com/results?search_query=How+Many+Spark+Applications+Can+Your+Etcd+Really+Handle%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# How Many Spark Applications Can Your Etcd Really Handle? - João Soares & João Azevedo, Feedzai

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: João Soares, João Azevedo, Feedzai
- Schedule: https://kccnceu2026.sched.com/event/2CW7u/how-many-spark-applications-can-your-etcd-really-handle-joao-soares-joao-azevedo-feedzai
- Busca YouTube: https://www.youtube.com/results?search_query=How+Many+Spark+Applications+Can+Your+Etcd+Really+Handle%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre How Many Spark Applications Can Your Etcd Really Handle?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7u/how-many-spark-applications-can-your-etcd-really-handle-joao-soares-joao-azevedo-feedzai
- YouTube search: https://www.youtube.com/results?search_query=How+Many+Spark+Applications+Can+Your+Etcd+Really+Handle%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jmz8c3oEmPY
- YouTube title: How Many Spark Applications Can Your Etcd Really Handle? - João Soares & João Azevedo, Feedzai
- Match score: 0.849
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/how-many-spark-applications-can-your-etcd-really-handle/jmz8c3oEmPY.txt
- Transcript chars: 22371
- Keywords: actually, objects, object, server, storage, create, applications, cluster, already, clusters, submission, resource, resources, scheduling, requests, around, events, concept

### Resumo baseado na transcript

We basically manage most of the data infrastructure as a service in a Kubernetes ecosystem. I work as a platform engineering across multiple domains mainly compute and network. We had to uh page teams to actually help with simple operations like checking the logs of a spark submission or even more complex stuff like a session of a a job that has already executed in history server for example. So, we are basically moving towards Kubernetes consolidation with a single operational model and trying to adopt a more cloudnative approach to our infrastructure that is more costefficient as well. And although it looks like moving our services to Kubernetes will make our lives easier, we will show you throughout this talk that we faced a couple of challenges that we hope would serve as learning lessons for for everyone. Well, Spark as a service was born in Kubernetes with three main requirements.

### Excerpt da transcript

So hello everyone. Well, I know this is the last day of CubeCon. Everyone should be tired, but we hope this is a fun one. We'll be presenting how many Spark applications cand really handle. So I'm Jean Asveu. I started my career doing database research back in the university. I now work at the data reliability team in FISA. We basically manage most of the data infrastructure as a service in a Kubernetes ecosystem. >> So I'm Jean Swage. I work as a platform engineering across multiple domains mainly compute and network. Uh I also come from a research background on high performance and distributed systems and work as an assistant professor at the University of Quimmer. So our use case at FISA one of our products is a real-time uh fraud detection platform for banks and payment processors. uh during the last year in numbers we process around 90 billion of events which totaled uh eight 83 trillion dollars in payments. So fresh data is essential for accurate decisions. Why do we use spark? So this is the backbone for our batch processing.

Feature engineering and model training. Delaying execution of Spark applications can result in degraded transaction scoring and possibly undetected fraud. Regarding scale, we have over 150 production yarn clusters isolated per client and use case. 4,000 Spark applications are launched each day, which totals three per minute across several regions. This is a growing number. Since Spark as a service on our platform, we've enabled a plethora of new integrations. >> Well, as you can see, our previous setup was not the best. Uh we had lack of resource efficiency. Basically, we had to manage independent clusters per client and use case. We didn't have a multi-tenency concept. And with all these independent clusters, we had sparse configuration over where everywhere. And it added operational burden in terms of managing all this uh configuration and also coordinating all these upgrades. But most importantly, we had to involve SRRES in day-to-day operations. We had to uh page teams to actually help with simple operations like checking the logs of a spark submission or even more complex stuff like a session of a a job that has already executed in history server for example.

Well, to give you some context, in FISA, we are undergoing a strategic shift. So, we are basically moving towards Kubernetes consolidation with a single operational model and trying to adopt a more cloudnative approach to our infrastructure that is more costefficien
