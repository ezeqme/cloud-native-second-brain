---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "GitOps Delivery", "Community Governance"]
speakers: ["Jesse Suen", "Akuity", "Alexander Matyushentsev", "Intuit"]
sched_url: https://kccncna2021.sched.com/event/lV89/the-argo-ecosystem-tailoring-your-installation-through-community-add-ons-jesse-suen-akuity-alexander-matyushentsev-intuit
youtube_search_url: https://www.youtube.com/results?search_query=The+Argo+Ecosystem%3A+Tailoring+Your+Installation+Through+Community+Add-ons+CNCF+KubeCon+2021
slides: []
status: parsed
---

# The Argo Ecosystem: Tailoring Your Installation Through Community Add-ons - Jesse Suen, Akuity & Alexander Matyushentsev, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Jesse Suen, Akuity, Alexander Matyushentsev, Intuit
- Schedule: https://kccncna2021.sched.com/event/lV89/the-argo-ecosystem-tailoring-your-installation-through-community-add-ons-jesse-suen-akuity-alexander-matyushentsev-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=The+Argo+Ecosystem%3A+Tailoring+Your+Installation+Through+Community+Add-ons+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre The Argo Ecosystem: Tailoring Your Installation Through Community Add-ons.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV89/the-argo-ecosystem-tailoring-your-installation-through-community-add-ons-jesse-suen-akuity-alexander-matyushentsev-intuit
- YouTube search: https://www.youtube.com/results?search_query=The+Argo+Ecosystem%3A+Tailoring+Your+Installation+Through+Community+Add-ons+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EPtiDNXpS78
- YouTube title: The Argo Ecosystem: Tailoring Your Installation Through Comm... Jesse Suen & Alexander Matyushentsev
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/the-argo-ecosystem-tailoring-your-installation-through-community-add-o/EPtiDNXpS78.txt
- Transcript chars: 28019
- Keywords: argo, application, projects, create, canary, applications, rollout, actually, cluster, notifications, github, already, features, annotations, wanted, basically, extension, pretty

### Resumo baseado na transcript

hi my name is alexander mitroshansev and i'm a principal software engineer at intuit and i'm a long time maintainer of argo so as henrik said i've worked on pretty much all of the projects and my my focus right now is argo cd and my co-speaker is jesse he will talk about himself very soon first few words about company i'm working for so i work for intuit which is a us-based tech fintech company founded in 1983 and we are proud builders of products like turbotax quickbooks and

### Excerpt da transcript

hi my name is alexander mitroshansev and i'm a principal software engineer at intuit and i'm a long time maintainer of argo so as henrik said i've worked on pretty much all of the projects and my my focus right now is argo cd and my co-speaker is jesse he will talk about himself very soon first few words about company i'm working for so i work for intuit which is a us-based tech fintech company founded in 1983 and we are proud builders of products like turbotax quickbooks and mint and so we serve 10 000 million customers from all the segments and into it is a cncf gold member next jc continue uh hi everyone my name is jesse soon and i'm an argo project lead along with alex i'm also co-founder of a company called acuity which we just launched this week and the kvd provides vendor-supported distribution of argo as well as support and services around the argo project so before we get into it it's always useful to start and explain what the argo project is at a high level and argo is a collection of kubernetes native tools and all focused on the area of application delivery and is comprised of four main projects cd rollouts workflow and events and each project is focused on a specific use case and they're all designed to use to be used standalone with loose integrations between the projects so you might be wondering like how did we end up with for like loosely coupled projects and then a collection of ecosystem projects and it all comes down to some design philosophies that we share about the project and so we believe that all each project should stay focused on a specific use case and and solving that use case very well for example argo cd is all about delivering manifest from a git repo to kubernetes clusters and a few years back we had this need to do you know blue green and canary deployments on kubernetes and there was this push to to have that functionally baked into argo cd but the more we thought about it it felt like it was out of scope uh from what argo cd was originally aimed to do and the approach could be considered too opinionated uh it'd maybe make it argo cd2 too complex and so we decided to develop it as a separate project and that became our goal rollouts and we felt like that was a great decision because today we have you know a lot of people who like to use our ocd but they don't they don't need largo rollouts and then we also have users who use rollouts but they don't use argo cd and so you kind of get to pick and to choose the tools that
