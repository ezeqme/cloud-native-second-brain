---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security"]
speakers: ["Sujith Katakam", "Karen Tu", "Robinhood Markets", "Inc."]
sched_url: https://kccncna2023.sched.com/event/1R2rw/k8s-authnz-at-robinhood-learning-from-reductions-migrations-and-designing-automation-sujith-katakam-karen-tu-robinhood-markets-inc
youtube_search_url: https://www.youtube.com/results?search_query=K8s+Auth%7BN%2CZ%7D+at+Robinhood+-+Learning+from+Reductions%2C+Migrations+and+Designing+Automation+CNCF+KubeCon+2023
slides: []
status: parsed
---

# K8s Auth{N,Z} at Robinhood - Learning from Reductions, Migrations and Designing Automation - Sujith Katakam & Karen Tu, Robinhood Markets, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United States / Chicago
- Speakers: Sujith Katakam, Karen Tu, Robinhood Markets, Inc.
- Schedule: https://kccncna2023.sched.com/event/1R2rw/k8s-authnz-at-robinhood-learning-from-reductions-migrations-and-designing-automation-sujith-katakam-karen-tu-robinhood-markets-inc
- Busca YouTube: https://www.youtube.com/results?search_query=K8s+Auth%7BN%2CZ%7D+at+Robinhood+-+Learning+from+Reductions%2C+Migrations+and+Designing+Automation+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre K8s Auth{N,Z} at Robinhood - Learning from Reductions, Migrations and Designing Automation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rw/k8s-authnz-at-robinhood-learning-from-reductions-migrations-and-designing-automation-sujith-katakam-karen-tu-robinhood-markets-inc
- YouTube search: https://www.youtube.com/results?search_query=K8s+Auth%7BN%2CZ%7D+at+Robinhood+-+Learning+from+Reductions%2C+Migrations+and+Designing+Automation+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aBUGtu-venk
- YouTube title: K8s Auth{N,Z} at Robinhood - Learning from Reductions, Migrations and D... Sujith Katakam & Karen Tu
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/k8s-auth-n-z-at-robinhood-learning-from-reductions-migrations-and-desi/aBUGtu-venk.txt
- Transcript chars: 33515
- Keywords: access, groups, google, cluster, actually, permissions, client, wanted, server, request, question, resources, application, infrastructure, policy, bindings, started, company

### Resumo baseado na transcript

okay um we'll go ahead and get started now since it's 4:30 um hello I'm Karen and this is sui we're part of the orchestration team at Robin Hood um where we manage our kubernetes clusters and today what we'll be talking about is going through the Journey of how um Robin Hood's strategy for kubernetes um authorization and authentication has evolved so to give you a little bit of context um Robin Hood decide as a company to actually start using kubernetes at the end of 2018 and the

### Excerpt da transcript

okay um we'll go ahead and get started now since it's 4:30 um hello I'm Karen and this is sui we're part of the orchestration team at Robin Hood um where we manage our kubernetes clusters and today what we'll be talking about is going through the Journey of how um Robin Hood's strategy for kubernetes um authorization and authentication has evolved so to give you a little bit of context um Robin Hood decide as a company to actually start using kubernetes at the end of 2018 and the designed decision was to have um our own self-managed kues clusters on top of AWS and that's still what we are using today and we went with a multi-tenant model so each application gets its own namespace and every application has a corresponding team that owns it and a team might own multiple Nam spaces if they have multiple applic appliations so um yeah in case you can't see it the top is the kubernetes resources and um the two boxes inside are the name spaces and here at the bottom um I have Google Groups because at that point in time um that was something that already existed in the company um each team had a corresponding Google group and this Google group was used for things like um emailing and also using Google Calendars so we decided to Leverage The already um existing Google Groups and use that to um get access to the kubernetes Clusters and Associated name spaces so because we wanted to have each team to have access to the Nay spaces they own we created a cluster rule for this um namespace admin and that included things that a regular application team might need like managing their pods and we also created a rule binding in every single Nam space to bind to that cluster rule and use the Google Groups but um this covers application teams but you might be wondering um what about infrastructure teams that might have needs to access resources across several namespaces or even to manage cluster wide resources and for that we used a cluster rule called admin rule which is very similar to the built-in cluster admin cluster rule which gives um permissions to do literally anything in the cluster via the wild card version and resources and the Google group on the bottom right is the infrastructure team and they are the ones that have access to this so um this was our initial design and that worked fine when Robin Hood was a small startup with very few Engineers but as the company grew this um initial design was no longer going to work and the one of the primary reasons for that is
