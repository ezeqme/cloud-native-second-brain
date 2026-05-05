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
sched_url: https://kccnceu2024.sched.com/event/1aQhP/k8gb-reliable-global-service-load-balancing-without-vendor-lock-in-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=K8gb%3A+Reliable+Global+Service+Load+Balancing+without+vendor+lock-in+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# K8gb: Reliable Global Service Load Balancing without vendor lock-in | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQhP/k8gb-reliable-global-service-load-balancing-without-vendor-lock-in-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=K8gb%3A+Reliable+Global+Service+Load+Balancing+without+vendor+lock-in+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre K8gb: Reliable Global Service Load Balancing without vendor lock-in | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQhP/k8gb-reliable-global-service-load-balancing-without-vendor-lock-in-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=K8gb%3A+Reliable+Global+Service+Load+Balancing+without+vendor+lock-in+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MsQ0E7SYNPo
- YouTube title: K8gb: Reliable Global Service Load Balancing without vendor lock-in | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/k8gb-reliable-global-service-load-balancing-without-vendor-lock-in-pro/MsQ0E7SYNPo.txt
- Transcript chars: 5954
- Keywords: global, cluster, application, scenario, environment, status, balancing, traffic, basically, clusters, region, strategy, ingress, management, multiple, regions, external, standard

### Resumo baseado na transcript

uh hi everybody uh I'm Yuri I'm creator of uh kubernetes Global balancer project that I want to talk about today and uh what is uh uh KGB uh it is open source project that is uh targeted to solve uh interesting challenge of global traffic management uh so it basically uh makes your applications uh globally available and resilient in a situation when you dealing with a multicluster uh scenario when your kubernetes clusters are deployed in a geographically dispersed manner so it can be multiple data centers multiple

### Excerpt da transcript

uh hi everybody uh I'm Yuri I'm creator of uh kubernetes Global balancer project that I want to talk about today and uh what is uh uh KGB uh it is open source project that is uh targeted to solve uh interesting challenge of global traffic management uh so it basically uh makes your applications uh globally available and resilient in a situation when you dealing with a multicluster uh scenario when your kubernetes clusters are deployed in a geographically dispersed manner so it can be multiple data centers multiple regions so highly distributed uh environment uh the main uh differentiators of the project of the kgp project is that it's kubernetes native so it's exposes a gbcd to control quite challenging uh Global traffic management configuration uh there is no single point of failure because there is no need for management cluster so you deploy KGB next to your workloads uh we are using uh DNS protocols that is Bal tested it's running the uh internet and whole setup is distributed by Design we supporting multiple load balanc load balancing strategies like failover run robing and Jo proximity uh the whole solution is designed to uh solve high impact Regional failur and why it is GS SOB Global Serv SL balancing solution it's also has a unique prop property of figuring out what is actually happening on your cluster down to the PO status poort SC check granularity so roughly how it works uh we have uh a canonical example of KGB setup we have two clusters deployed in two different regions region a region B and it it can be different data centers it can be uh different Cloud regions like AWS us AWS Europe or any cloud provider and even hybrid mode whatever environment you need to Target uh KGB is getting installed next to the workloads so to to your workload clusters and together with the main orchestration KGB controller it also uh ships within itself two important components it's external DNS and core DNS that is dedicated cor DNS deployment not related to The Standard kubernetes one what external DNS integration is doing it automatically configures the Z ation in your environment DNS provider so it can be routed to three Azure public DNS and someon prep Solutions cloudware anything after the Zone delegation is configured uh the DNS uh request from the client is going to be automatically forwarded to the core DNS instances that are controlled by a KGB and the core DNS instances are going to response with dynamically crafted uh DNS responses according to to uh
