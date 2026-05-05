---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Alerting", "Kubernetes", "Scalability Reliability", "Visualization Dashboards"]
speakers: ["Juraj Michálek", "Pradeep Lalwani"]
source_url: https://promcon.io/2024-berlin/talks/applying-gitops-principles-for-central-alert-management/
youtube_url: https://www.youtube.com/watch?v=NxdYJKOasEM
youtube_search_url: https://www.youtube.com/results?search_query=Applying+GitOps+principles+for+central+alert+management+PromCon+2024
video_match_score: 1.024
status: video-found
---

# Applying GitOps principles for central alert management

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: Juraj Michálek, Pradeep Lalwani
- Página oficial: https://promcon.io/2024-berlin/talks/applying-gitops-principles-for-central-alert-management/
- YouTube: https://www.youtube.com/watch?v=NxdYJKOasEM

## Resumo

In this talk we will explore how we can use git to store and review alerts for Prometheus and compatible backends such as Mimir, Thanos, Cortex. Further we will use folder structure to control to which regions / environments and tenants the alerts and recording rules get deployed to. We will also use Promtool, Promruval and pipeline tool of your choice to: Run unit tests for the alerts Validate the alerts queries (such as minimal range_interval in queries, syntax of the queries, querying only allowed tenants, etc) Ensure alerts follow company policies, i.e.

## Abstract oficial

In this talk we will explore how we can use git to store and review alerts for Prometheus and compatible backends such as Mimir, Thanos, Cortex.

Further we will use folder structure to control to which regions / environments and tenants the alerts and recording rules get deployed to.

We will also use Promtool, Promruval and pipeline tool of your choice to:


Run unit tests for the alerts
Validate the alerts queries (such as minimal range_interval in queries, syntax of the queries, querying only allowed tenants, etc)
Ensure alerts follow company policies, i.e. have some specific labels present 
Use either git-sync (https://github.com/kubernetes/git-sync) or argocd to deliver these alerts to your backend of choice.


At the end we will take a look at how we can use the same pattern for provisioning dashboards in Grafana.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/applying-gitops-principles-for-central-alert-management/
- YouTube: https://www.youtube.com/watch?v=NxdYJKOasEM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NxdYJKOasEM
- YouTube title: PromCon 2024 - Applying GitOps principles for central alert management
- Match score: 1.024
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/applying-gitops-principles-for-central-alert-management/NxdYJKOasEM.txt
- Transcript chars: 22325
- Keywords: basically, alerts, actually, mentioned, mimir, validation, labels, around, already, grafana, pipeline, elastic, heavily, dashboard, number, observability, important, repository

### Resumo baseado na transcript

[Music] all right uh welcome everybody thanks for attending uh the topic we are going to discuss uh is the kops principles for applying for the alerting management uh before starting it just a small introduction uh my name is pradep uh working in swisser as a uh site reliability engineer mainly maintaining uh observability platforms I come from the background of uh elastic stack uh very heavily used um some of you I already heard the name of influx so I think uh people know ttac it's uh the

### Excerpt da transcript

[Music] all right uh welcome everybody thanks for attending uh the topic we are going to discuss uh is the kops principles for applying for the alerting management uh before starting it just a small introduction uh my name is pradep uh working in swisser as a uh site reliability engineer mainly maintaining uh observability platforms I come from the background of uh elastic stack uh very heavily used um some of you I already heard the name of influx so I think uh people know ttac it's uh the influx uh not the chronograph part I love uh grafana before chronograph so uh and then now uh moving or shifting towards the um Loki grafana U Tempo and MIM uh stack and uh my colleague would you like to hi um my name is y mik I also worked at swis uh and I'm sorry with focus on observability um in my free time but also during work I contribute to alel and um looks good to meac and um I'm also active in the alal promeets working group and um now I'm also um in U LFC LFX mentorship project on the on the Arthur uh David and ARA uh implementing um remote right to which was already mentioned before in the remot red exporter of The alel Collector and I also recently became a grafana champion can't beat that thank you so before going to the problem statement um here's the quick look um at our uh landcape or the architecture as you can see we use mostly all the components um from F mimir to low key um for lcks um and tempo for traces um all the visualization happens at the grafana end um all these sources comes and connects there uh how we uh take the metrics traces and logs from the users uh is basically um as you can see on the left hand side you have the customers um cities clusters even though some customers don't have communes clusters so they have their services um they can send their metrics and traces on HTTP or grpc uh we have uh this hotel collector at our end uh pretty basic standard basically nothing much in there uh use aler manager heavily um and uh on the right hand side you see there is something which is not native grafana ecosystem is elastic basically we use elastic stack heavily for our logging and why we use that we will come in the next slide uh we have our in-house uh system of event management it's uh very tightly coupled with uh our standards in terms of like uh alerting correlations uh with the data what we have uh it's very smart system which basically correlates merge the alerts and generates an event which is more meaningful avoiding noises and thi
