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
themes: ["Security", "Kubernetes Core"]
speakers: ["Amine Hilaly", "Igor Velichkovich", "AWS"]
sched_url: https://kccncna2023.sched.com/event/1R2uP/safeguarding-clusters-exploring-the-benefits-and-navigating-the-dangers-of-admission-controllers-amine-hilaly-igor-velichkovich-aws
youtube_search_url: https://www.youtube.com/results?search_query=Safeguarding+Clusters%3A+Exploring+the+Benefits+and+Navigating+the+Dangers+of+Admission+Controllers+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Safeguarding Clusters: Exploring the Benefits and Navigating the Dangers of Admission Controllers - Amine Hilaly & Igor Velichkovich, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Amine Hilaly, Igor Velichkovich, AWS
- Schedule: https://kccncna2023.sched.com/event/1R2uP/safeguarding-clusters-exploring-the-benefits-and-navigating-the-dangers-of-admission-controllers-amine-hilaly-igor-velichkovich-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Safeguarding+Clusters%3A+Exploring+the+Benefits+and+Navigating+the+Dangers+of+Admission+Controllers+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Safeguarding Clusters: Exploring the Benefits and Navigating the Dangers of Admission Controllers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uP/safeguarding-clusters-exploring-the-benefits-and-navigating-the-dangers-of-admission-controllers-amine-hilaly-igor-velichkovich-aws
- YouTube search: https://www.youtube.com/results?search_query=Safeguarding+Clusters%3A+Exploring+the+Benefits+and+Navigating+the+Dangers+of+Admission+Controllers+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6kK9otYAYac
- YouTube title: Safeguarding Clusters: Exploring the Benefits and Navigating... - Amine Hilaly & Igor Velichkovich
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/safeguarding-clusters-exploring-the-benefits-and-navigating-the-danger/6kK9otYAYac.txt
- Transcript chars: 28597
- Keywords: admission, cluster, deployment, server, validating, request, target, conditions, policy, policies, expression, language, create, access, namespace, registry, failure, mutating

### Resumo baseado na transcript

all right hello everyone um good afternoon my name's Igor vitkovic I'm uh SD for Amazon eks and we're going to be talking about um what you can do with admission web Hooks and admission controllers and also the dangers of those and I'm joined by my colleague here um my name is Amin I'm also an engineer at the Amazon eks and uh yeah um before we kick it off um I would like to ask you a question so by show of hands uh have ever anyone here

### Excerpt da transcript

all right hello everyone um good afternoon my name's Igor vitkovic I'm uh SD for Amazon eks and we're going to be talking about um what you can do with admission web Hooks and admission controllers and also the dangers of those and I'm joined by my colleague here um my name is Amin I'm also an engineer at the Amazon eks and uh yeah um before we kick it off um I would like to ask you a question so by show of hands uh have ever anyone here like used admission web Works before a little bit uh have you ever broken a cluster or an application running in your in your U cluster using admission web hooks or admission controllers nice I already see three or four oh five that's cool you're in the right talk so today we're going to be talking about exactly those problems and how to mitigate them in today's menu we have a quick intr prodction to uh mutation and validation web hooks so if you never used them before it's completely fine we're going to talk about them and then we're going to switch to the dangers um of using the admission controllers and web hooks uh we will also IG is going to do a demo of uh web Hooks and how to take down your cluster using um mutating web hooks we're going to also talk about new feature that just landed in cues 1.27 1.28 uh called uh match conditions or the common expression language and also known as cell and we also going to finish with a demo about how to use cell on Leverage in your cluster to uh for a better security um of R um so let's State the problem in early uh 20123 we stopped using kgcr iio and we started recommending to use registry case.

iio for multiple reasons um that the community is very aware of on the bottom you can see them uh tweeting about this in in 2020 like saying like hey we should uh switch Registries um and uh try to to spread the message across the community anyways uh the reason why we're talking about this like hey as an administrator I want to enforce this policy in my cluster I want my uh cluster users to start using the new registry however there will be always someone who's going to forget about it so let's say actor let's say Bob or Alice someone who forgot about them twet and they are still writing manifest let's say pods or deployments and they are still using the old registry let's call it a um they are using kgcr IO and what's going to happen they're going to apply that to the API server the API server is going to um persist the information at CD however I want the API server to process the ne
